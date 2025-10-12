from .session import LanzouSession
from typing import Tuple, Any
from .API import DRIVE_DOMAIN

class LanzouShareManager:
    def __init__(self, session: LanzouSession):
        self.session = session

    def get_file_link(
        self,
        file_id: str
    ) -> Tuple[bool, Any]:
        """
        获取文件分享链接
        :param file_id: 文件ID
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 22,
            "file_id": file_id,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def get_folder_link(
        self,
        folder_id: str
    ) -> Tuple[bool, Any]:
        """
        获取文件夹分享链接
        :param folder_id: 文件夹ID
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 18,
            "folder_id": folder_id,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data