from .session import UcSession
from typing import List, Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    FILE_SORT,
    FILE_MOVE,
    FILE_RENAME,
    FILE_DELETE,
)


class UcFileManager:
    def __init__(
        self,
        session: UcSession,
    ):
        self.session = session

    def get_lists(
        self,
        pdir_fid: str = "0",
        page: int = 1,
        size: int = 50,
        sort_by: str = "file_name",
        sort_order: str = "asc",
    ) -> Tuple[bool, Any]:
        """
        获取文件列表
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
            "pdir_fid": pdir_fid,
            "_page": page,
            "_size": size,
            "_fetch_total": 1,
            "_fetch_sub_dirs": 0,
            "_sort": sort,
            "uc_param_str": "",
        }
        url = DRIVE_DOMAIN + FILE_SORT
        status, resp = self.session.request(url, "GET", query_params=query_params)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp

    def move_file(
        self,
        src_fids: List[str],
        dst_pdir_fid: str,
    ) -> Tuple[bool, Any]:
        """
        移动文件/文件夹
        :param src_fids: 源文件/文件夹ID列表
        :param dst_pdir_fid: 目标文件夹ID
        :return: (status, 响应数据/错误原因)
        """
        data = {
            "action_type": 1,
            "exclude_fids": [],
            "filelist": src_fids,
            "to_pdir_fid": dst_pdir_fid,
        }
        url = DRIVE_DOMAIN + FILE_MOVE
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp

    def rename_file(
        self,
        fid: str,
        new_name: str,
    ) -> Tuple[bool, Any]:
        """
        重命名文件/文件夹
        :param fid: 文件/文件夹ID
        :param new_name: 新名称
        :return: (status, 响应数据/错误原因)
        """
        data = {
            "fid": fid,
            "file_name": new_name,
        }
        url = DRIVE_DOMAIN + FILE_RENAME
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp
        return False, resp

    def remove_file(
        self,
        fids: List[str],
    ) -> Tuple[bool, Any]:
        """
        删除文件/文件夹
        :param fids: 文件/文件夹ID列表
        :return: (status, 响应数据/错误原因)
        """
        data = {
            "action_type": 1,
            "exclude_fids": [],
            "filelist": fids,
        }
        url = DRIVE_DOMAIN + FILE_DELETE
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp
