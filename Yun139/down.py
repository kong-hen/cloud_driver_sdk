from .session import Yun139Session
from typing import Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    FILE_DOWNLOAD
)


class Yun139DownManager:
    def __init__(self, session: Yun139Session):
        self.session = session

    def get_download_url(
        self,
        fid: str,
    ) -> Tuple[bool, Any]:
        """
        下载文件
        :param fid: 要下载的文件ID
        :return: (status, 响应数据/错误原因)
        """

        url = DRIVE_DOMAIN + FILE_DOWNLOAD
        data = {
          "fileId": fid,
        }
        
        return self.session.request(url=url, method="POST", data=data)