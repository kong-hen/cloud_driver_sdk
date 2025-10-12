from .session import LanzouSession
from typing import Tuple, Any
from .API import DRIVE_DOMAIN

class LanzouFolderManager:
    def __init__(self, session: LanzouSession):
        self.session = session

    def create_folder(
        self,
        folder_name: str,
        parent_id: str = "-1",
        folder_description: str = ""
    ) -> Tuple[bool, Any]:
        """
        创建文件夹
        :param folder_name: 文件夹名称
        :param parent_id: 父目录ID，默认-1（根目录）
        :param folder_description: 文件夹描述
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 2,
            "parent_id": parent_id,
            "folder_name": folder_name,
            "folder_description": folder_description or folder_name,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data
        """
        重命名文件夹
        :param folder_id: 文件夹ID
        :param folder_name: 新文件夹名称
        :param folder_description: 新描述
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 4,
            "folder_id": folder_id,
            "folder_name": folder_name,
            "folder_description": folder_description or folder_name,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def delete_folder(
        self,
        folder_id: str
    ) -> Tuple[bool, Any]:
        """
        删除文件夹
        :param folder_id: 文件夹ID
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 3,
            "folder_id": folder_id,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data
    
    def get_folder_info(
        self,
        folder_id: str
    ) -> Tuple[bool, Any]:
        """
        获取文件夹信息
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

    def set_folder_info(
        self,
        folder_id: str,
        folder_name: str,
        folder_description: str = ""
    ) -> Tuple[bool, Any]:
        """
        设置文件夹信息
        :param folder_id: 文件夹ID
        :param folder_name: 文件夹名称
        :param folder_description: 文件夹描述
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 4,
            "folder_id": folder_id,
            "folder_name": folder_name,
            "folder_description": folder_description,
        }
        status, resp_data = self.session.request(url, method="POST", data=data) 
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def set_folder_pwd(
        self,
        folder_id: str,
        folder_pwd: str,
        onof: str = "1",
    ) -> Tuple[bool, Any]:
        """
        设置文件夹密码
        :param folder_id: 文件夹ID
        :param onof: 是否开启文件夹密码，1为开启，0为关闭
        :param folder_pwd: 文件夹密码
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 16,
            "folder_id": folder_id,
            "shows": onof,
            "shownames": folder_pwd,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def get_folder_list(
        self,
        folder_id: str = "-1"
    ) -> Tuple[bool, Any]:
        """
        获取文件夹内文件夹列表，一次性返回全部
        :param folder_id: 文件夹ID，默认-1（根目录）
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 27,
            "folder_id": folder_id,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data
    
    def get_file_list(
        self,
        folder_id: str = "-1",
        page: int = 1,
    ) -> Tuple[bool, Any]:
        """
        获取文件夹内文件列表
        :param folder_id: 文件夹ID，默认-1（根目录）
        :param page: 页码，默认1（每页18条）
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid 
        data = {
            "task": 5,
            "folder_id": folder_id,
            "pg": page,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data