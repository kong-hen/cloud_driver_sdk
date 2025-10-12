import requests
import re
from urllib.parse import urlparse
from typing import Tuple, Dict, Any, Optional
import random


class LanzouDownManager:
    """
    独立的网页爬虫类，用于爬取蓝奏云页面并提取参数，以及模拟请求获取文件列表。
    """

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, Any]] = None,
        data: Any = None,
    ) -> Tuple[bool, Any]:
        """
        内部通用请求方法。
        :param method: 'GET' 或 'POST'
        :param url: 请求地址
        :param headers: 请求头
        :param data: POST数据
        :return: (status, 响应内容/错误信息)
        """
        if headers is None:
            headers = {}
        headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            }
        )
        try:
            if method.upper() == "GET":
                resp = requests.get(url, headers=headers)
            elif method.upper() == "POST":
                resp = requests.post(url, data=data, headers=headers)
            else:
                return False, f"不支持的HTTP方法: {method}"
            resp.raise_for_status()
            return True, resp
        except Exception as e:
            return False, f"请求失败: {str(e)}"

    def get_final_url(
        self,
        url: str,
    ) -> Tuple[bool, str]:
        """
        获取最终下载链接
        :param url: 下载链接
        :return: 最终下载链接
        """
        # 生成随机IP
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "CLIENT-IP": ip,
            "X-FORWARDED-FOR": ip,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
        }

        try:
            resp = requests.get(url, headers=headers, allow_redirects=True)
            return True, resp.url
        except Exception as e:
            return False, f"获取下载直链失败: {str(e)}"

    def is_lanzou(
        self,
        url: str,
    ) -> Tuple[bool, str]:
        """
        判断是否是蓝奏云链接并获取链接地址
        :param url: 链接
        :return: (status, 链接地址)
        """
        is_lan = ".lanzou" in url.lower()
        try:
            parsed = urlparse(url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            return is_lan, base_url
        except Exception:
            return False, ""

    def get_folder_params(
        self,
        url: str,
    ) -> Tuple[bool, Any]:
        """
        获取文件夹参数
        :param url: 目标页面链接
        :return: (status, {参数字典/错误信息})
        """
        status, resp = self.request("GET", url)
        if not status:
            return False, resp

        html = resp.text

        # 检查是否有密码输入框
        pwd_input = re.search(r'<input[^>]+type="text"[^>]+id="pwd"[^>]*>', html)
        has_pwd = pwd_input is not None

        # 提取JS参数
        js_block = re.search(
            r"<script[^>]*>.*?var [^;]+;.*?function more\(\).*?</script>", html, re.S
        )

        if not js_block:
            return False, "未找到必要的JS代码块"

        js_code = js_block.group(0)

        # 提取变量
        def extract_var(name):
            m = re.search(
                rf"var\s+{re.escape(name)}\s*=\s*['\"]?([^'\";]+)['\"]?;", js_code
            )
            return m.group(1) if m else None

        # 使用更安全的提取方式
        lx_match = re.search(r"'lx':'(\d+)'", js_code)
        uid_match = re.search(r"'uid':'(\d+)'", js_code)
        fid_match = re.search(r"'fid':(\d+)", js_code)
        rep_match = re.search(r"'rep':(\d+)", js_code)
        t_name_match = re.search(r"'t':([a-zA-Z0-9_\$]+)", js_code)
        k_name_match = re.search(r"'k':([a-zA-Z0-9_\$]+)", js_code)
        up_match = re.search(r"'up':(\d+)", js_code)
        ls_match = re.search(r"'ls':(\d+)", js_code)

        lx = lx_match.group(1) if lx_match else "2"
        uid = uid_match.group(1) if uid_match else None
        fid = fid_match.group(1) if fid_match else None
        rep = rep_match.group(1) if rep_match else "0"
        t = extract_var(t_name_match.group(1)) if t_name_match else None
        k = extract_var(k_name_match.group(1)) if k_name_match else None
        up = up_match.group(1) if up_match else "1"
        ls = ls_match.group(1) if ls_match else "1"

        if not all([uid, fid, t, k]):
            return False, "获取必要的参数失败"

        params = {
            "pwd": has_pwd,
            "lx": lx,
            "uid": uid,
            "fid": fid,
            "rep": rep,
            "t": t,
            "k": k,
            "up": up,
            "ls": ls,
        }
        return True, params

    def get_folder_list(
        self,
        url: str,
        pwd: Optional[str] = None,
    ) -> Tuple[bool, Any]:
        """
        获取文件夹中文件夹列表
        """
        lan_status, lan_data = self.is_lanzou(url)
        if not lan_status:
            return False, "不是蓝奏云链接"

        html_status, html_resp = self.get_folder_params(url)
        if not html_status:
            return False, html_resp

        if html_resp.get("pwd", True) and not pwd:
            return False, "需要密码但未提供"
        else:
            return True, html_resp
        

    def get_file_list(
        self,
        url: str,
        pwd: Optional[str] = None,
        page: int = 1,
    ) -> Tuple[bool, Any]:
        """
        获取文件列表
        :param url: 蓝奏云链接
        :param pwd: 密码（可选）
        :param page: 页码
        :return: (status, 响应json/错误信息)
        """
        lan_status, lan_data = self.is_lanzou(url)
        if not lan_status:
            return False, "不是蓝奏云链接"

        html_status, html_resp = self.get_folder_params(url)
        if not html_status:
            return False, html_resp

        if html_resp.get("pwd", True) and not pwd:
            return False, "需要密码但未提供"

        # 构建请求参数
        request_params = html_resp.copy()
        request_params["pwd"] = pwd
        request_params["pg"] = page

        headers = {
            "Accept": "application/json, text/javascript, */*",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        list_url = f"{lan_data}/filemoreajax.php?file={html_resp['fid']}"
        status, resp = self.request(
            "POST", list_url, headers=headers, data=request_params
        )

        if not status:
            return False, resp

        try:
            data = resp.json()
            if data.get("zt") == 1:
                return True, data
            else:
                return False, data
        except Exception as e:
            return False, f"解析响应失败: {str(e)}"

    def get_no_pwd_param(
        self,
        url: str,
        html: str,
        final: bool = False,
    ) -> Tuple[bool, Any]:
        """
        获取无密码参数
        :param url: 源页面链接
        :param html: 页面html
        :param final: 是否获取最终下载链接
        :return: (status, {参数字典/错误信息})
        """
        # 文件名（从<title>标签获取，去除-蓝奏云后缀）
        title_tag = re.search(r"<title>(.*?)</title>", html, re.I)
        title = title_tag.group(1).strip() if title_tag else ""
        if title:
            title = re.sub(r"[-－]\s*蓝奏云$", "", title).strip()

        # 获取文件大小
        size_match = re.search(r'<span class="p7">文件大小：</span>([^<]+)<br>', html)
        size = size_match.group(1).strip() if size_match else ""

        # 获取分享用户
        author_match = re.search(
            r'<span class="p7">分享用户：</span><font>([^<]+)</font><br>', html
        )
        author = author_match.group(1).strip() if author_match else ""

        # 获取文件描述
        desc_match = re.search(r'<span class="p7">文件描述：</span><br>([^<]*)<', html)
        desc = desc_match.group(1).strip() if desc_match else ""

        # 获取下载iframe的url
        iframe_match = re.search(r'<iframe[^>]+class="ifr2"[^>]+src="([^"]+)"', html)
        iframe_url = ""

        if iframe_match:
            src = iframe_match.group(1)
            # 获取主域名
            parsed = urlparse(url)
            base_url = (
                f"{parsed.scheme}://{parsed.netloc}"
                if parsed.scheme and parsed.netloc
                else "https://wwa.lanzoui.com"
            )
            iframe_url = base_url + src if not src.startswith("http") else src

        if not iframe_url:
            return False, "未找到下载iframe"

        # 获取iframe内容
        iframe_status, iframe_resp = self.request("GET", iframe_url)
        if not iframe_status:
            return False, iframe_resp

        iframe_html = iframe_resp.text

        # 获取iframe内容中的参数
        ajax_url_matches = list(
            re.finditer(r"url\s*:\s*['\"]([^'\"]+)['\"]", iframe_html)
        )
        if len(ajax_url_matches) < 2:
            return False, "获取请求接口失败"

        ajax_url = ajax_url_matches[1].group(1)

        # 提取各个参数
        ajaxdata_match = re.search(
            r"var\s+ajaxdata\s*=\s*['\"]([^'\"]+)['\"];", iframe_html
        )
        wp_sign_match = re.search(
            r"var\s+wp_sign\s*=\s*['\"]([^'\"]+)['\"];", iframe_html
        )

        ajaxdata = ajaxdata_match.group(1) if ajaxdata_match else None
        wp_sign = wp_sign_match.group(1) if wp_sign_match else None

        if not ajaxdata or not wp_sign:
            return False, "获取参数失败"

        # 组装参数
        ajax_params = {
            "action": "downprocess",
            "websignkey": ajaxdata,
            "signs": ajaxdata,
            "sign": wp_sign,
            "websign": "",
            "kd": "1",
            "ves": "1",
        }

        # 发送请求获取下载链接
        get_down_url = f"https://wwa.lanzouq.com{ajax_url}"
        headers = {"referer": iframe_url}

        ajax_status, ajax_resp = self.request(
            "POST", get_down_url, headers=headers, data=ajax_params
        )

        if not ajax_status:
            return False, ajax_resp

        try:
            ajax_data = ajax_resp.json()
            if ajax_data.get("zt") == 1:
                # 构建最终下载链接
                down_url = f"{ajax_data.get('dom', '')}/file/{ajax_data.get('url', '')}"
                if final:
                    final_status, final_data = self.get_final_url(down_url)
                    if not final_status:
                        return False, final_data

                result = {
                    "title": title,
                    "size": size,
                    "author": author,
                    "desc": desc,
                    "url": down_url,
                    "down": final_data if final else "",
                }
                return True, result
            else:
                return False, ajax_data
        except Exception as e:
            return False, f"解析下载链接失败: {str(e)}"

    def get_pwd_param(
        self,
        url: str,
        html: str,
        pwd: str,
        final: bool = False,
    ) -> Tuple[bool, Any]:
        """
        获取密码参数
        :param url: 源页面链接
        :param html: 页面html
        :param pwd: 密码
        :param final: 是否获取最终下载链接
        :return: (status, {参数字典/错误信息})
        """
        # 获取文件大小
        size_match = re.search(r'<div class="n_filesize">大小：([^<]+)</div>', html)
        size = size_match.group(1).strip() if size_match else ""

        # 获取文件描述
        desc_match = re.search(r'<div class="n_box_des">([^<]*)</div>', html)
        desc = desc_match.group(1).strip() if desc_match else ""

        # 获取作者信息
        author_match = re.search(
            r'<div class="passwddiv-user">获取<span>([^<]*)</span>的文件</div>', html
        )
        author = author_match.group(1).strip() if author_match else ""

        # 提取JS块，获取action、sign、kd
        js_block = re.search(
            r"<script[^>]*>.*?data\s*:\s*\{[^}]+\}.*?</script>", html, re.S
        )

        action = sign = kd = down_url = None

        if js_block:
            js_code = js_block.group(0)
            # kd变量
            kd_var = re.search(r"var\s+kdns\s*=\s*([0-9]+);", js_code)
            kd = kd_var.group(1) if kd_var else None

            # 获取请求接口
            down_url_match = re.search(r"url\s*:\s*['\"]([^'\"]+)['\"]", js_code)
            down_url = down_url_match.group(1) if down_url_match else None

            # data对象
            data_obj_list = list(re.finditer(r"data\s*:\s*\{([^}]+)\}", js_code))
            if len(data_obj_list) > 3:
                data_str = data_obj_list[2].group(1)
                action_match = re.search(r"'action':'([^']+)'", data_str)
                sign_match = re.search(r"'sign':'([^']+)'", data_str)
                action = action_match.group(1) if action_match else None
                sign = sign_match.group(1) if sign_match else None

        if not all([down_url, action, sign, kd]):
            return False, "获取参数失败"

        # 请求获取文件下载链接
        get_down_url = f"https://wwa.lanzouq.com{down_url}"
        headers = {"referer": url}

        down_status, down_resp = self.request(
            "POST",
            get_down_url,
            data={"action": action, "sign": sign, "kd": kd, "p": pwd},
            headers=headers,
        )

        if not down_status:
            return False, down_resp

        try:
            down_data = down_resp.json()
            if down_data.get("zt") != 1:
                return False, down_data.get("inf", "密码错误或文件不存在")

            # 获取最终下载链接
            down_url = f"{down_data.get('dom', '')}/file/{down_data.get('url', '')}"
            if final:
                final_status, final_data = self.get_final_url(down_url)
                print(final_status, final_data)
                if not final_status:
                    return False, final_data

            # 总结文件信息
            file_info = {
                "title": down_data.get("inf", ""),
                "size": size,
                "author": author,
                "desc": desc,
                "url": down_url,
                "down": final_data if final else "",
            }
            return True, file_info
        except Exception as e:
            return False, f"解析下载直链失败: {str(e)}"

    def get_file_info(
        self,
        url: str,
        pwd: Optional[str] = None,
        final: bool = False,
    ) -> Tuple[bool, Any]:
        """
        获取文件参数
        :param url: 目标页面链接
        :param pwd: 密码（可选）
        :param final: 是否获取最终下载链接（开启会严重增加请求时间）
        :return: (status, {参数字典/错误信息})
        """
        status, resp = self.request("GET", url)
        if not status:
            return False, resp

        html = resp.text

        # 判断是否取消分享
        if re.search(r"文件取消分享了", html):
            return False, "文件取消分享了"

        # 判断是否有密码输入框
        pwd_input = re.search(r'<input[^>]+type="text"[^>]+id="pwd"[^>]*>', html)
        has_pwd = pwd_input is not None

        if not has_pwd:
            return self.get_no_pwd_param(url, html, final)
        elif has_pwd and pwd:
            return self.get_pwd_param(url, html, pwd, final)
        else:
            return False, "请输入密码"
