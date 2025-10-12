from .session import LanzouSession
from typing import Tuple, Any, Optional
import os
import mimetypes
from .API import DRIVE_DOMAIN, UPLOAD_DOMAIN

class LanzouFileManager:
    def __init__(self, session: LanzouSession):
        self.session = session

    def rename_file(
        self,
        file_id: str,
        file_name: str,
    ) -> Tuple[bool, Any]:
        """
        重命名文件（需要会员）
        :param file_id: 文件ID
        :param file_name: 新文件名
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 46,
            "file_id": file_id,
            "file_name": file_name,
            "type": 2,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def set_file_desc(
        self,
        file_id: str,
        desc: str,
    ) -> Tuple[bool, Any]:
        """
        设置文件描述
        :param file_id: 文件ID
        :param file_desc: 文件描述
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 11,
            "file_id": file_id,
            "desc": desc,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        print("修改描述：", resp_data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def delete_file(
        self,
        file_id: str
    ) -> Tuple[bool, Any]:
        """
        删除文件
        :param file_id: 文件ID
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 6,
            "file_id": file_id,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def move_file(
        self,
        file_id: str,
        folder_id: str = "-1"
    ) -> Tuple[bool, Any]:
        """
        移动文件
        :param file_id: 文件ID
        :param folder_id: 目标文件夹ID，默认-1为根目录
        :return: (status, 响应数据/错误原因) 
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 20,
            "file_id": file_id,
            "folder_id": folder_id,
        }
        status, resp_data = self.session.request(url, method="POST", data=data)
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def set_file_pwd(
        self,
        file_id: str,
        file_pwd: str,
        onof: str = "1",
    ) -> Tuple[bool, Any]:
        """
        设置文件密码
        :param file_id: 文件ID
        :param file_pwd: 文件密码
        :param onof: 是否开启文件密码，1为开启，0为关闭
        :return: (status, 响应数据/错误原因)
        """
        url = DRIVE_DOMAIN + "?u=" + self.session.uid
        data = {
            "task": 23,
            "file_id": file_id,
            "shows": onof,
            "shownames": file_pwd,
        }
        status, resp_data = self.session.request(url, method="POST", data=data) 
        if status and resp_data.get("zt") == 1:
            return True, resp_data
        else:
            return False, resp_data

    def upload_file(
        self,
        file_name: str,
        file_path: str,
        folder_id: str = "-1"
    ) -> Tuple[bool, Any]:
        """
        上传文件，文件需小于100MB。
        :param file_path: 待上传文件路径
        :param file_name: 文件名（可选）
        :param folder_id: 父文件夹id，默认-1为根目录
        :return: (status, 响应数据/错误信息)
        """
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return False, "文件不存在"
        
        file_size = os.path.getsize(file_path)
        if file_size >= 100 * 1024 * 1024:
            return False, "文件不能大于100MB"
        
        if not file_name:
            file_name = os.path.basename(file_path)
        
        file_mime = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        
        # 准备上传数据
        data = {
            "task": "1",
            "vie": "2",
            "ve": "2",
            "id": "WU_FILE_0",
            "name": file_name,
            "type": file_mime,
            "size": str(file_size),
            "folder_id_bb_n": folder_id,
        }
        
        # 使用 files 参数而不是 data 来上传文件
        try:
            with open(file_path, "rb") as file_obj:
                files = {"upload_file": (file_name, file_obj, file_mime)}
                status, resp_data = self.session.request(
                    UPLOAD_DOMAIN, 
                    method="POST", 
                    data=data,
                    files=files
                )
                
                if status and resp_data.get("zt") == 1:
                    return True, resp_data
                else:
                    return False, resp_data
        except Exception as e:
            return False, f"文件上传异常: {str(e)}"

