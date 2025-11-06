import base64
import hashlib
from urllib.parse import quote
from typing import List, Dict, Any, Optional, Tuple
import requests
import string
import secrets
import time
import json
import xml.etree.ElementTree as ET
from .API import REFRESH_TOKEN


class Yun139Session:

    Token: str

    def __init__(self, token: str):
        if token.startswith("Basic "):
            self.Token = token[6:]
        else:
            self.Token = token

    def cal_sign(self, body: str, ts: str, rand_str: str, ) -> str:
        # URL编码
        body = quote(body, safe='')
        # 分割字符串并排序
        chars: List[str] = list[str](body)
        chars.sort()
        body = ''.join(chars)
        # Base64编码
        body = base64.b64encode(body.encode('utf-8')).decode('utf-8')
        # 计算MD5
        body_md5 = hashlib.md5(body.encode('utf-8')).hexdigest()
        ts_rand_md5 = hashlib.md5(f"{ts}:{rand_str}".encode('utf-8')).hexdigest()
        # 组合并再次计算MD5，然后转为大写
        combined = body_md5 + ts_rand_md5
        result = hashlib.md5(combined.encode('utf-8')).hexdigest().upper()
        return result

    def request(
        self,
        url: str,
        method: str,
        data: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> Tuple[bool, Any]:
        """
        通用请求方法，url 必须为完整路径。
        :param url: 完整请求地址
        :param method: 请求方法
        :param data: POST数据
        :param query_params: 查询参数
        """
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        alphabet = string.ascii_letters + string.digits
        randomStr = ''.join(secrets.choice(alphabet) for _ in range(16))
        sign = self.cal_sign(json.dumps(data), ts, randomStr)

        headers = {
            "Accept":               "application/json, text/plain, */*",
            "Authorization":        "Basic " + self.Token,
            "Caller":               "web",
            "Cms-Device":           "default",
            "Mcloud-Channel":       "1000101",
            "Mcloud-Client":        "10701",
            "Mcloud-Route":         "001",
            "Mcloud-Sign":          f"{ts},{randomStr},{sign}",
            "Mcloud-Version":       "7.14.0",
            "x-DeviceInfo":         "||9|7.14.0|chrome|120.0.0.0|||windows 10||zh-CN|||",
            "x-huawei-channelSrc":  "10000034",
            "x-inner-ntwk":         "2",
            "x-m4c-caller":         "PC",
            "x-m4c-src":            "10002",
            "x-SvcType":            "1",
            "X-Yun-Api-Version":    "v1",
            "X-Yun-App-Channel":    "10000034",
            "X-Yun-Channel-Source": "10000034",
            "X-Yun-Client-Info":    "||9|7.14.0|chrome|120.0.0.0|||windows 10||zh-CN|||dW5kZWZpbmVk||",
            "X-Yun-Module-Type":    "100",
            "X-Yun-Svc-Type":       "1",
        }
        
        if query_params:
            params = {}
            params.update(query_params)
        else:
            params = None
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                headers["Content-Type"] = "application/json;charset=UTF-8"
                response = requests.post(url, headers=headers, json=data)
            else:
                return False, f"不支持的HTTP方法: {method}"
            response.raise_for_status()
            json_resp = response.json()
            if json_resp.get("success") == True:
                return True, json_resp.get("data")
            else:
                return False, json_resp
        except requests.exceptions.RequestException as e:
            return False, str(e)
        except Exception as e:
            return False, str(e)

    def refresh_token(self) -> str:
        """
        刷新139云盘的访问令牌
        :return: 新的Base64编码的授权信息
        """
        try:
            token = self.Token

            # 解码Base64授权信息
            decode_bytes = base64.b64decode(token)
            decode_str = decode_bytes.decode('utf-8')
            
            # 分割授权信息
            splits = decode_str.split(":")
            if len(splits) < 3:
                return False, {
                    "msg": "Token无效"
                }
            
            # 解析令牌信息
            strs = splits[2].split("|")
            if len(strs) < 4:
                return False, {
                    "msg": "Token无效"
                }
            
            # 检查令牌有效期
            expiration = int(strs[3])
            expiration -= int(time.time() * 1000)  # 转换为毫秒
            
            # 如果有效期大于15天，无需刷新
            if expiration > 1000 * 60 * 60 * 24 * 15:
                return True, {
                    "msg": "令牌有效期大于15天，无需刷新",
                    "token": token
                }
            
            # 如果令牌已过期
            if expiration < 0:
                return False, {
                    "msg": "Token已经过期"
                }
            
            # 发送刷新令牌请求
            req_body = f"<root><token>{splits[2]}</token><account>{splits[1]}</account><clienttype>656</clienttype></root>"
            
            headers = {
                "Content-Type": "application/xml"
            }
            
            response = requests.post(REFRESH_TOKEN, data=req_body, headers=headers)
            response.raise_for_status()
            
            # 解析XML响应
            root = ET.fromstring(response.text)
            return_code = root.findtext("return")
            desc = root.findtext("desc")
            auth = root.findtext("token")
            
            if return_code != "0":
                return False, {
                    "msg": f"Token刷新失败: {desc}"
                }
            
            # 构建新的授权信息
            new_auth = f"{splits[0]}:{splits[1]}:{auth}"
            new_token = base64.b64encode(new_auth.encode('utf-8')).decode('utf-8')
            self.Token = new_token
            return True, {
                "msg": "Token刷新成功",
                "token": new_token
            }

        except Exception as e:
            return False, {
                "msg": f"Token刷新失败: {str(e)}"
            }
