from .session import UcSession
from typing import List, Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    FILE_DOWNLOAD
)


class UcDownManager:
    def __init__(self, session: UcSession):
        self.session = session

    def get_download_url(
        self,
        fid_list: List[str],
    ) -> Tuple[bool, Any]:
        """
        下载文件
        :param fid_list: 要下载的文件ID列表，下载文件最大为50MB
        :return: (status, 响应数据/错误原因)
        """
        data = {
          "fids": fid_list,
        }
        url = DRIVE_DOMAIN + FILE_DOWNLOAD + "?pr=UCBrowser&fr=pc"
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            file = resp.get("data", [])[0]
            info = {
                  "fid": file.get("fid"),
                  "file_name": file.get("file_name"),
                  "size": file.get("size"),
                  "format_type": file.get("format_type"),
                  "download_url": file.get("download_url"),
                }
            down_info = {
              "file": info,
              "cookie": "; ".join([f"{key}={value}" for key, value in self.session.cookies.items()]),
            }
            return True, down_info
        return False, resp


