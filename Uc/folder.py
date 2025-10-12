from .session import UcSession
from typing import Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    CREATE_FOLDER,
)


class UcFolderManager:
    def __init__(self, session: UcSession):
        self.session = session

    def create_folder(
        self,
        folder_name: str,
        pdir_fid: str = "0",
    ) -> Tuple[bool, Any]:
        """
        创建文件夹
        :param folder_name: 文件夹名称
        :param pdir_fid: 父目录ID，默认0（根目录）
        :return: (status, 响应数据/错误原因)
        """
        data = {
            "pdir_fid": pdir_fid,
            "file_name": folder_name,
            "dir_path": "",
            "dir_init_lock": False,
        }
        url = DRIVE_DOMAIN + CREATE_FOLDER
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp
        return False, resp
