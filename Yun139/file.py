from .session import Yun139Session
from typing import List, Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    FILE_MOVE,
    FILE_RENAME,
    FILE_DELETE,
)


class Yun139FileManager:
    def __init__(self, session: Yun139Session):
        self.session = session

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

        url = DRIVE_DOMAIN + FILE_MOVE
        data = {
          "fileIds": src_fids,
          "toParentFileId": dst_pdir_fid
        }

        return self.session.request(url=url, method="POST", data=data)

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

        url = DRIVE_DOMAIN + FILE_RENAME
        data = {
          "fileId": fid,
          "name": new_name,
          "description":""
        }
        
        return self.session.request(url=url, method="POST", data=data)

    def remove_file(
        self,
        fids: List[str],
    ) -> Tuple[bool, Any]:
        """
        删除文件/文件夹
        :param fids: 文件/文件夹ID列表
        :return: (status, 响应数据/错误原因)
        """

        url = DRIVE_DOMAIN + FILE_DELETE
        data = {
          "fileIds": fids,
        }
        
        return self.session.request(url=url, method="POST", data=data)
