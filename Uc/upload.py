from .session import UcSession
from typing import Tuple, Any, Dict, List, Optional, Callable
import time
import mimetypes
import hashlib
import base64
import json
import os
from datetime import datetime, timezone
import requests
from .API import (
    DRIVE_DOMAIN,
    FILE_UPLOAD_PRE,
    FILE_UPDATE_HASH,
    FILE_UPLOAD_AUTH,
    FILE_UPLOAD_FINISH,
)


class UcUploadManager:
    def __init__(self, session: UcSession):
        self.session = session

    def up_pre(
        self,
        file_name: str,
        mimetype: str,
        size: int,
        parent_id: str,
    ) -> Tuple[bool, Any]:
        """
        预上传请求
        :param file_name: 文件名
        :param mimetype: MIME类型
        :param size: 文件大小
        :param parent_id: 父目录ID
        :return: (status, 预上传响应/错误原因)
        """
        now = int(time.time() * 1000)
        data = {
            "ccp_hash_update": True,
            "dir_name": "",
            "file_name": file_name,
            "format_type": mimetype,
            "l_created_at": now,
            "l_updated_at": now,
            "pdir_fid": parent_id,
            "size": size,
        }
        url = DRIVE_DOMAIN + FILE_UPLOAD_PRE
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp
        return False, resp

    def up_hash(
        self,
        md5_hash: str,
        sha1_hash: str,
        task_id: str,
    ) -> Tuple[bool, Any]:
        """
        提交文件哈希验证
        :param md5_hash: MD5哈希值
        :param sha1_hash: SHA1哈希值
        :param task_id: 上传任务ID
        :return: (status, finish字段/错误原因)
        """
        data = {"md5": md5_hash, "sha1": sha1_hash, "task_id": task_id}
        url = DRIVE_DOMAIN + FILE_UPDATE_HASH
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            finish = resp.get("data", {}).get("finish", False)
            return True, resp.get("data", {})
        return False, resp

    def up_part(
        self,
        pre: Dict[str, Any],
        mime_type: str,
        part_number: int,
        chunk_data: bytes,
    ) -> Tuple[bool, Any]:
        """
        上传文件分片
        :param pre: 预上传响应数据
        :param mime_type: MIME类型
        :param part_number: 分片编号
        :param chunk_data: 分片数据
        :return: (status, ETag/错误原因)
        """
        now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        auth_meta = f"PUT\n\n{mime_type}\n{now}\nx-oss-date:{now}\nx-oss-user-agent:aliyun-sdk-js/6.6.1 Chrome 98.0.4758.80 on Windows 10 64-bit\n/{pre['data']['bucket']}/{pre['data']['obj_key']}?partNumber={part_number}&uploadId={pre['data']['upload_id']}"
        auth_data = {
            "auth_info": pre["data"]["auth_info"],
            "auth_meta": auth_meta,
            "task_id": pre["data"]["task_id"],
        }
        url = DRIVE_DOMAIN + FILE_UPLOAD_AUTH
        status, auth_resp = self.session.request(url, "POST", auth_data)
        if not status:
            return False, auth_resp
        if auth_resp.get("code") == 0 and auth_resp.get("status") == 200:
            upload_url = f"https://{pre['data']['bucket']}.{pre['data']['upload_url'][7:]}/{pre['data']['obj_key']}"
            headers = {
                "Authorization": auth_resp["data"]["auth_key"],
                "Content-Type": mime_type,
                "Referer": "https://pan.quark.cn/",
                "x-oss-date": now,
                "x-oss-user-agent": "aliyun-sdk-js/6.6.1 Chrome 98.0.4758.80 on Windows 10 64-bit",
            }
            params = {"partNumber": str(part_number), "uploadId": pre["data"]["upload_id"]}
            try:
                response = requests.put(
                    upload_url, headers=headers, params=params, data=chunk_data, timeout=30
                )
                response.raise_for_status()
                return True, response.headers.get("ETag")
            except requests.exceptions.RequestException as e:
                return False, str(e)
        return False, auth_resp

    def up_commit(
        self,
        pre: Dict[str, Any],
        etags: List[str],
    ) -> Tuple[bool, Any]:
        """
        提交分片上传完成
        :param pre: 预上传响应数据
        :param etags: 所有分片的ETag列表
        :return: (status, None/错误原因)
        """
        now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        xml_parts = []
        for i, etag in enumerate(etags, 1):
            xml_parts.append(
                f"<Part><PartNumber>{i}</PartNumber><ETag>{etag}</ETag></Part>"
            )
        xml_body = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<CompleteMultipartUpload>\n{"".join(xml_parts)}\n</CompleteMultipartUpload>"""
        md5 = hashlib.md5()
        md5.update(xml_body.encode("utf-8"))
        content_md5 = base64.b64encode(md5.digest()).decode("utf-8")
        callback_json = json.dumps(pre["data"]["callback"])
        callback_b64 = base64.b64encode(callback_json.encode("utf-8")).decode("utf-8")
        auth_meta = f"POST\n{content_md5}\napplication/xml\n{now}\nx-oss-callback:{callback_b64}\nx-oss-date:{now}\nx-oss-user-agent:aliyun-sdk-js/6.6.1 Chrome 98.0.4758.80 on Windows 10 64-bit\n/{pre['data']['bucket']}/{pre['data']['obj_key']}?uploadId={pre['data']['upload_id']}"
        auth_data = {
            "auth_info": pre["data"]["auth_info"],
            "auth_meta": auth_meta,
            "task_id": pre["data"]["task_id"],
        }
        url = DRIVE_DOMAIN + FILE_UPLOAD_AUTH
        status, auth_resp = self.session.request(url, "POST", auth_data)
        if not status:
            return False, auth_resp
        if auth_resp.get("code") == 0 and auth_resp.get("status") == 200:
            upload_url = f"https://{pre['data']['bucket']}.{pre['data']['upload_url'][7:]}/{pre['data']['obj_key']}"
            headers = {
                "Authorization": auth_resp["data"]["auth_key"],
                "Content-MD5": content_md5,
                "Content-Type": "application/xml",
                "Referer": "https://pan.quark.cn/",
                "x-oss-callback": callback_b64,
                "x-oss-date": now,
                "x-oss-user-agent": "aliyun-sdk-js/6.6.1 Chrome 98.0.4758.80 on Windows 10 64-bit",
            }
            params = {"uploadId": pre["data"]["upload_id"]}
            try:
                response = requests.post(
                    upload_url, headers=headers, params=params, data=xml_body, timeout=30
                )
                response.raise_for_status()
                return True, response.json()
            except requests.exceptions.RequestException as e:
                return False, str(e)
        return False, auth_resp

    def up_finish(
        self,
        pre: Dict[str, Any],
    ) -> Tuple[bool, Any]:
        """
        完成上传流程
        :param pre: 预上传响应数据
        :return: (status, None/错误原因)
        """
        data = {"obj_key": pre["data"]["obj_key"], "task_id": pre["data"]["task_id"]}
        url = DRIVE_DOMAIN + FILE_UPLOAD_FINISH
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp

    def upload_file(
        self,
        file_name: str,
        file_path: str,
        pdir_fid: str = "0",
        progress_callback: Optional[Callable[[int], None]] = None,
    ) -> Tuple[bool, Any]:
        """
        完整的文件上传流程
        :param file_name: 文件名
        :param file_path: 文件路径
        :param pdir_fid: 父目录ID，默认为0（根目录）
        :param progress_callback: 进度回调函数，参数为当前进度百分比（0-100）
        :return: (status, 文件ID/错误原因)
        """
        mime_type, _ = mimetypes.guess_type(file_name)
        if not mime_type:
            mime_type = "application/octet-stream"
        try:
            file_size = os.path.getsize(file_path)
        except Exception as e:
            return False, f"无法获取文件大小: {str(e)}"
        md5_hash = hashlib.md5()
        sha1_hash = hashlib.sha1()
        try:
            with open(file_path, "rb") as f:
                while True:
                    chunk = f.read(8192)
                    if not chunk:
                        break
                    md5_hash.update(chunk)
                    sha1_hash.update(chunk)
        except Exception as e:
            return False, f"读取文件计算哈希失败: {str(e)}"
        md5_hex = md5_hash.hexdigest()
        sha1_hex = sha1_hash.hexdigest()
        status, pre_resp = self.up_pre(file_name, mime_type, file_size, pdir_fid)
        if not status:
            return False, f"预上传失败: {pre_resp}"
        status, up_hash_result = self.up_hash(
            md5_hex, sha1_hex, pre_resp.get("data", {}).get("task_id", "")
        )
        if not status:
            return False, f"哈希验证失败: {up_hash_result}"
        if up_hash_result.get("finish") is True:
            return True, up_hash_result
        part_size = pre_resp.get("metadata", {}).get("part_size", 0)
        etags: List[str] = []
        part_number = 1
        uploaded = 0
        try:
            with open(file_path, "rb") as f:
                while True:
                    chunk = f.read(part_size)
                    if not chunk:
                        break
                    status, etag = self.up_part(pre_resp, mime_type, part_number, chunk)
                    if not status:
                        return False, f"分片{part_number}上传失败: {etag}"
                    etags.append(etag)
                    part_number += 1
                    uploaded += len(chunk)
                    if progress_callback:
                        progress = min(100, int(uploaded / file_size * 100))
                        progress_callback(progress)
        except Exception as e:
            return False, f"读取文件分片上传失败: {str(e)}"
        status, commit_resp = self.up_commit(pre_resp, etags)
        if not status:
            return False, f"提交上传失败: {commit_resp}"
        status, finish_resp = self.up_finish(pre_resp)
        if not status:
            return False, f"完成上传失败: {finish_resp}"
        return True, finish_resp
