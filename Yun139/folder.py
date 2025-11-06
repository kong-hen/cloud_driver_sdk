from .session import Yun139Session
from typing import Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    FILE_LIST,
    FOLDER_CREATE,
)


class Yun139FolderManager:
    def __init__(self, session: Yun139Session):
        self.session = session

    def get_lists(
        self, 
        pdir_fid: str = "/",
        size: int = 50,
        cursor: str = None,
        sort_by: str = "file_name",
        sort_order: str = "asc",
    ) -> Tuple[bool, Any]:
        """
        获取文件夹列表
        :param pdir_fid: 父目录ID，默认0（根目录）
        :return: (status, 响应数据/错误原因)
        :param size: 每页数量
        :param cursor: 分页游标（上一页获取结果中的nextPageCursor），首页为None
        :param sort_by: 排序字段，"file_name" 或 "updated_at"，默认"file_name"
        :param sort_order: 排序方式，"asc" 或 "desc"，默认"asc"
        """
        if sort_by not in ("file_name", "updated_at"):
            return False, "sort_by 只能为 'file_name' 或 'updated_at'"
        if sort_by == "file_name":
            sort_by = "name"
        if sort_order not in ("asc", "desc"):
            return False, "sort_order 只能为 'asc' 或 'desc'"
        
        url = DRIVE_DOMAIN + FILE_LIST
        data = {
            "pageInfo": {
                "pageSize": size,
                "pageCursor": cursor,
            },
            "orderBy": sort_by,
            "orderDirection": sort_order.upper(),
            "parentFileId": pdir_fid,
            "imageThumbnailStyleList": ["Small", "Large"],
        }

        return self.session.request(url=url, method="POST", data=data)

    def create_folder(
        self,
        folder_name: str,
        pdir_fid: str = "/",
    ) -> Tuple[bool, Any]:
        """
        创建文件夹
        :param folder_name: 文件夹名称
        :param pdir_fid: 父目录ID，默认"/"（根目录）
        :return: (status, 响应数据/错误原因)
        """
        
        url = DRIVE_DOMAIN + FOLDER_CREATE
        data = {
            "parentFileId": pdir_fid,
            "name": folder_name,
            "description":"",
            "type":"folder",
            "fileRenameMode":"force_rename"
        }
        
        return self.session.request(url=url, method="POST", data=data)
