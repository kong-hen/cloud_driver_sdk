from threading import stack_size
import requests
from http.cookies import SimpleCookie
from typing import Dict, Tuple, Optional, Any
from .API import (
    PAN_DOMAIN,
    USER_INFO,
)


class QuarkSession:

    cookies: Dict[str, str]

    def __init__(self, cookie: str):
        self.cookies = self.parse_cookie(cookie)
        self.config = {
            "referer": "https://pan.quark.cn",
            "origin": "https://pan.quark.cn",
            "pr": "ucpro",
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        }

    def parse_cookie(
        self,
        cookie: str,
    ) -> Dict[str, str]:
        """
        解析cookie字符串为字典
        :param cookie_str: cookie字符串
        :return: cookie字典
        """
        cookies = SimpleCookie()
        cookies.load(cookie)
        return {k: v.value for k, v in cookies.items()}

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
        headers = {
            "Cookie": "; ".join([f"{k}={v}" for k, v in self.cookies.items()]),
            "Accept": "application/json, text/plain, */*",
            "Referer": self.config["referer"],
            "User-Agent": self.config["ua"],
            "Origin": self.config["origin"],
            "Priority": "u=1, i",
        }
        params = {"pr": self.config["pr"], "fr": "pc"}
        if query_params:
            params.update(query_params)
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                headers["Content-Type"] = "application/json"
                response = requests.post(url, headers=headers, params=params, json=data)
            else:
                return False, f"不支持的HTTP方法: {method}"
            response.raise_for_status()
            json_resp = response.json()
            # 更新cookie
            if "__puus" in response.cookies:
                self.cookies['__puus'] = response.cookies['__puus']
            return True, json_resp
        except requests.exceptions.RequestException as e:
            return False, str(e)
        except Exception as e:
            return False, str(e)

    def get_user_info(self) -> Tuple[bool, str]:
        """
        获取用户信息
        返回 (True, 用户信息) 或 (False, 错误信息)
        """
        url = PAN_DOMAIN + USER_INFO
        params = {"fr": "pc", "platform": "pc"}
        status, resp = self.request(url, "GET", query_params=params)
        if not status:
            return False, resp
        if resp.get("success") is True and resp.get("code") == "OK":
            return True, resp.get("data", {})
        else:
            return False, resp
