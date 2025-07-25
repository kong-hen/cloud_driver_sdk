from .session import QuarkSession
from typing import Tuple, Any
import random
import time
import re
from .API import (
    DRIVE_DOMAIN,
    DRIVE_H_DOMAIN,
    SHARE_SHAREPAGE_TOKEN,
    SHARE_SHAREPAGE_DETAIL,
    SHARE_SHAREPAGE_SAVE,
)


class QuarkSaveManager:
    def __init__(self, session: QuarkSession):
        self.session = session

    def get_share_info(
        self,
        text: str,
    ) -> Tuple[bool, Any]:
        """
        从文本中提取分享ID、目录ID和提取码
        :param text: 包含分享链接和/或提取码的文本
        :return: (status, 响应数据/错误原因)
        """
        # 提取pwd_id和pdir_fid
        match = re.search(r"/s/(\w+)(#/list/share.*/(\w+))?", text)
        if not match:
            return False, "链接格式错误"
        pwd_id = match.group(1)
        # 提取提取码
        match_code = re.search(r"提取码[:：](\S+\d{1,4}\S*)", text)
        if not match_code:
            passcode = ""
        else:
            passcode = match_code.group(1)
        return True, {"pwd_id": pwd_id, "passcode": passcode}

    def get_share_stoken(
        self,
        pwd_id: str,
        passcode: str = "",
    ) -> Tuple[bool, Any]:
        """
        获取分享stoken
        :param pwd_id: 分享链接ID
        :param passcode: 提取码，默认空
        :return: (status, 响应数据/错误原因)
        """
        query_params = {
            "pr": "ucpro",
            "fr": "pc",
            "uc_param_str": "",
            "__dt": random.randint(100, 999),
            "__t": int(time.time() * 1000),
        }
        data = {
            "pwd_id": pwd_id,
            "passcode": passcode,
            "support_visit_limit_private_share": True,
        }
        url = DRIVE_H_DOMAIN + SHARE_SHAREPAGE_TOKEN
        status, resp = self.session.request(
            url, "POST", data=data, query_params=query_params
        )
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp

    def get_share_list(
        self,
        pwd_id: str,
        stoken: str,
        pdir_fid: str = "0",
        page: int = 1,
        size: int = 50,
        sort_by: str = "file_name",
        sort_order: str = "asc",
    ) -> Tuple[bool, Any]:
        """
        获取分享列表
        :param pwd_id: 分享链接ID
        :param stoken: 分享stoken
        :param pdir_fid: 目录ID，默认0（根目录）
        :param page: 页码
        :param size: 每页数量
        :param sort_by: 排序字段，"file_name" 或 "updated_at"，默认"file_name"
        :param sort_order: 排序方式，"asc" 或 "desc"，默认"asc"
        :return: (status, 响应数据/错误原因)
        """

        if sort_by not in ("file_name", "updated_at"):
            return False, "sort_by 只能为 'file_name' 或 'updated_at'"
        sort = f"file_type:asc,{sort_by}:{sort_order}"

        query_params = {
            "pr": "ucpro",
            "fr": "pc",
            "uc_param_str": "",
            "pwd_id": pwd_id,
            "stoken": stoken,
            "pdir_fid": pdir_fid,
            "force": 0,
            "_page": page,
            "_size": size,
            "_fetch_banner": 1,
            "_fetch_share": 1,
            "_fetch_total": 1,
            "_sort": sort,
            "__dt": random.randint(100, 999),
            "__t": int(time.time() * 1000),
        }
        url = DRIVE_H_DOMAIN + SHARE_SHAREPAGE_DETAIL
        status, resp = self.session.request(url, "GET", query_params=query_params)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp

    def save_share_file(
        self,
        pwd_id: str,
        stoken: str,
        fid_list: list[str] = [],
        share_token_list: list[str] = [],
        to_pdir_fid: str = "0",
        pdir_save_all: bool = True,
    ) -> Tuple[bool, Any]:
        """
        转存指定文件
        :param pwd_id: 分享链接ID
        :param stoken: 分享stoken
        :param fid_list: 要转存的文件fid列表，全部保存则为空列表
        :param share_token_list: 与fid_list对应的share_fid_token列表，全部保存则为空列表
        :param to_pdir_fid: 目标父目录fid，默认为0（根目录）
        :param pdir_save_all: 是否全部保存，默认True
        :return: (status, 响应数据/错误原因)
        """

        query_params = {
            "pr": "ucpro",
            "fr": "pc",
            "uc_param_str": "",
            "__dt": random.randint(100, 999),
            "__t": int(time.time() * 1000),
        }
        data = {
            "fid_list": fid_list,
            "share_token_list": share_token_list,
            "to_pdir_fid": to_pdir_fid,
            "pwd_id": pwd_id,
            "stoken": stoken,
            "pdir_fid": "0",
            "pdir_save_all": pdir_save_all,
            "exclude_fids": [],
            "scene": "link",
        }
        url = DRIVE_DOMAIN + SHARE_SHAREPAGE_SAVE
        status, resp = self.session.request(
            url, "POST", data=data, query_params=query_params
        )
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp
