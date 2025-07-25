from .session import QuarkSession
from typing import List, Tuple, Any
from .API import (
    SHARE,
    TASK,
    SHARE_PASSWORD,
    DRIVE_DOMAIN,
)


class QuarkShareManager:
    def __init__(self, session: QuarkSession):
        self.session = session

    def create_share(
        self,
        fid_list: List[str],
        title: str,
        expired_type: int = 1,
        url_type: int = 1,
    ) -> Tuple[bool, Any]:
        """
        创建分享任务
        :param fid_list: 要分享的文件/文件夹ID列表
        :param title: 分享标题
        :param expired_type: 过期类型 (1: 永久；2：1天；3：7天；4：30天)
        :param url_type: URL类型 (1: 无密码；2：有密码)
        :return: (status, 响应数据/错误原因)
        """
        if expired_type < 1 or expired_type > 4:
            expired_type = 1
        if url_type not in (1, 2):
            url_type = 1
        data = {
            "fid_list": fid_list,
            "title": title,
            "url_type": url_type,
            "expired_type": expired_type,
        }
        url = DRIVE_DOMAIN + SHARE
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp

    def get_share_info(
        self,
        share_id: str,
    ) -> Tuple[bool, Any]:
        """
        获取分享链接信息
        :param share_id: 分享ID
        :return: (status, 响应数据/错误原因)
        """
        data = {"share_id": share_id}
        url = DRIVE_DOMAIN + SHARE_PASSWORD
        status, resp = self.session.request(url, "POST", data)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp
