import requests
from typing import Dict, Tuple, Optional, Any
from .API import DRIVE_DOMAIN, LOGIN_DOMAIN

class LanzouSession:
    cookies: Dict[str, str] = {}
    uid: str = ""

    def __init__(
        self,
    ):
        self.config = {
            "referer": "https://pc.woozooo.com",
            "origin": "https://pc.woozooo.com",
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }

    def login(self, user: str, pwd: str) -> Tuple[bool, Any]:
        """
        登录蓝奏云，自动获取 phpdisk_info 和 uid
        :param user: 用户名
        :param pwd: 密码
        :return: (status, 响应数据/错误原因)
        """
        data = {
            "task": "3",
            "uid": user,
            "pwd": pwd,
        }
        status, resp = self.request(LOGIN_DOMAIN, method="POST", data=data)
        if not status:
            return False, resp
        try:
            self.uid = str(resp.get("id"))
            return True, resp
        except Exception:
            return False, resp

    def request(
        self,
        url: str,
        method: str = "POST",
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Any]:
        """
        通用请求方法，适配Lanzou网盘API。
        :param url: 完整请求地址
        :param method: 请求方法
        :param data: POST数据
        :param files: 上传文件用
        """
        headers = {
            "Cookie": "; ".join([f"{k}={v}" for k, v in self.cookies.items()]),
            "Origin": self.config["origin"],
            "Referer": self.config["referer"],
            "User-Agent": self.config["ua"],
        }
        
        # 如果有文件上传，不设置Content-Type，让requests自动设置
        if not files:
            headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
            
        try:
            if method.upper() == "POST":
                response = requests.post(url, headers=headers, data=data, files=files)
            elif method.upper() == "GET":
                response = requests.get(url, headers=headers, params=data)
            else:
                return False, f"不支持的HTTP方法: {method}"
                
            if "phpdisk_info" in response.cookies:
                self.cookies = {k: v for k, v in response.cookies.items()}
            response.raise_for_status()
            return True, response.json()
        except requests.exceptions.RequestException as e:
            return False, str(e)
        except Exception as e:
            return False, str(e)

    def test(self):
        return self.cookies, self.uid