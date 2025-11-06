from .session import Yun139Session
from typing import Tuple, Any, Optional, Callable
import hashlib
import os
import requests
from .API import (
    DRIVE_DOMAIN,
    FILE_CREATE,
    FILE_COMPLETE,
)


class Yun139UploadManager:
    def __init__(self, session: Yun139Session):
        self.session = session
    
    def create_upload(
      self,
      file_name: str,
      file_path: str,
      parent_folder_id: str = "/",
    ) -> str:
        """
        创建文件上传任务
        :param file_name: 文件名
        :param file_path: 文件路径
        :param parent_folder_id: 父文件夹ID，默认根目录
        :return: 分片上传信息
        """
        # 获取文件大小
        try:
            file_size = os.path.getsize(file_path)
        except Exception as e:
            return False, f"获取文件大小失败: {str(e)}"
        
        # 将20MB转换为字节
        chunk_size_bytes = 20 * 1024 * 1024
        # 计算分块块数
        num_chunks = (file_size + chunk_size_bytes - 1) // chunk_size_bytes

        # 循环获取分块信息
        partList = []
        for i in range(num_chunks):
            start = i * chunk_size_bytes
            end = min(start + chunk_size_bytes, file_size)
            chunk_size = end - start
            partList.append({
                "parallelHashCtx": {"partOffset": start},
                "partNumber": i + 1,
                "partSize": chunk_size
            })
        
        # 计算文件的SHA256
        try:
          with open(file_path, "rb") as f:
              file_hash = hashlib.sha256()
              while chunk := f.read(8192):
                  file_hash.update(chunk)
          content_hash = file_hash.hexdigest()
        except Exception as e:
            return False, f"计算文件哈希失败: {str(e)}"

        url = DRIVE_DOMAIN + FILE_CREATE
        data = {
            "parentFileId": parent_folder_id,
            "name": file_name,
            "type": "file",
            "size": file_size,
            "fileRenameMode": "auto_rename",
            "contentHash": content_hash,
            "contentHashAlgorithm": "SHA256",
            "contentType": "application/oct-stream",
            "parallelUpload": False,
            "partInfos": partList
        }

        status, resp = self.session.request(url=url, method="POST", data=data)
        if not status:
            return False, resp
        else:
            resp["content_hash"] = content_hash
            return True, resp

    def upload_chunk(
        self,
        file_path: str,
        upload_url: str,
        part_number: int,
    ) -> bool:
        """
        上传文件分片
        :param file_path: 文件路径
        :param upload_url: 上传URL
        :param part_number: 分片编号
        :return: 是否上传成功
        """
        headers = {
          "Accept": "*/*",
          "Connection": "keep-alive",
          "Origin": "https://yun.139.com",
          "Referer": "https://yun.139.com/",
          "Content-Type": "application/oct-stream",
        }

        # 读取分片数据
        try:
            chunk_size_bytes = 20 * 1024 * 1024
            with open(file_path, "rb") as f:
                f.seek((part_number - 1) * chunk_size_bytes)
                chunk_data = f.read(chunk_size_bytes)
        except Exception as e:
            return False, f"读取分片数据失败: {str(e)}"
        
        response = requests.put(upload_url, headers=headers, data=chunk_data)
        if response.status_code == 200:
            return True, f"上传分片{part_number}成功"
        else:
            return False, f"上传分片{part_number}失败: {response.status_code} {response.text}"

    def upload_complete(
        self,
        upload_id: str,
        fid: str,
        content_hash: str,
    ) -> bool:
        """
        完成文件上传
        :param upload_id: 上传ID
        :param file_id: 文件ID
        :param content_hash: 文件内容哈希
        :return: 是否完成成功
        """
        url = DRIVE_DOMAIN + FILE_COMPLETE
        data = {
          "fileId": fid,
          "uploadId": upload_id,
          "contentHash": content_hash,
          "contentHashAlgorithm":"SHA256"
        }
        
        return self.session.request(url=url, method="POST", data=data)

    def upload_file(
        self,
        file_name: str,
        file_path: str,
        pdir_fid: str = "/",
        progress_callback: Optional[Callable[[int], None]] = None,
    ) -> Tuple[bool, Any]:
        """
        上传文件
        :param file_name: 文件名
        :param file_path: 文件路径
        :param pdir_fid: 父文件夹ID，默认为"/"（根目录）
        :param progress_callback: 进度回调函数
        :return: 上传结果
        """
        # 创建上传任务
        create_status, create_info = self.create_upload(file_name=file_name, file_path=file_path, parent_folder_id=pdir_fid)
        if not create_status:
            return False, create_info

        # 检查是否秒传成功
        if create_info.get("rapidUpload"):
            return True, create_info
        
        # 获取上传信息
        content_hash = create_info.get("content_hash")
        fileId = create_info.get("fileId")
        uploadId = create_info.get("uploadId")
        if not content_hash or not fileId or not uploadId:
            return False, create_info
        
        # 解析上传分片信息
        partList = create_info.get("partInfos")
        if not partList:
            return False, create_info
        
        # 循环上传分片
        for part in partList:
            part_number = part.get("partNumber", 1)
            upload_url = part.get("uploadUrl")
            upload_status, upload_msg = self.upload_chunk(file_path, upload_url, part_number)
            if not upload_status:
                break

            # 输出上传进度
            if progress_callback:
                progress_callback(min(100, int(part_number / len(partList) * 100)))
        
        # 如果某个分片上传失败
        if not upload_status:
            return False, upload_msg
        
        # 完成上传
        return self.upload_complete(upload_id=uploadId, fid=fileId, content_hash=content_hash)
