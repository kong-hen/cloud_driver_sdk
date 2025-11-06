import base64
from .session import Yun139Session
from typing import List, Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    SHARE,
)


class Yun139ShareManager:
    def __init__(self, session: Yun139Session):
        self.session = session

    def create_share(
        self,
        title: str,
        url_type: int = 0,
        fid_list: List[str] = [],
        fld_list: List[str] = [],
        expired_time: int = 0,
    ) -> Tuple[bool, Any]:
        """
        创建分享任务
        :param title: 分享标题
        :param url_type: 分享类型 (0: 无密码；1: 有密码)
        :param fid_list: 要分享的文件ID列表
        :param fld_list: 要分享的文件夹ID列表
        :param expired_time: 过期时间 (0: 永久；其他：天数)
        :return: (status, 响应数据/错误原因)
        """
        try:
            token = self.session.Token
            # 解码Base64授权信息
            decode_bytes = base64.b64decode(token)
            decode_str = decode_bytes.decode('utf-8')
            # 分割授权信息
            splits = decode_str.split(":")
            if len(splits) < 3:
                return False, {
                    "msg": "Token无效"
                }
        except:
            return False, {
                "msg": "解析Token失败"
            }
        
        data = {
            "getOutLinkReq": {
                "subLinkType": 0,
                "encrypt": url_type,
                "coIDLst": fid_list,
                "caIDLst": fld_list,
                "pubType": 1,
                "dedicatedName": title,
                "periodUnit":1,
                "viewerLst":[],
                "extInfo": {
                    "isWatermark": 0,
                    "shareChannel": "3001"
                },
                "commonAccountInfo": {
                    "account": splits[1],
                    "accountType": 1
                }
            }
        }

        if expired_time > 0:
            data["getOutLinkReq"]["period"] = expired_time
        
        return self.session.request(url=SHARE, method="POST", data=data)
