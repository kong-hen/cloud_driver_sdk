import yaml
from Lanzou import LanzouSession
from Lanzou import LanzouSession, LanzouFileManager, LanzouFolderManager, LanzouShareManager, LanzouDownManager

# 读取配置文件
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
lanzou_conf = config["lanzou"]

# 创建蓝奏云基础实例
session = LanzouSession()

# 登录获取cookie
status, result = session.login(lanzou_conf["username"], lanzou_conf["password"])



# 创建文件管理实例
file_manager = LanzouFileManager(session)

# 重命名文件
status, result = file_manager.rename_file("12295254", "9999.png")
# 返回示例：
"""
False {
    "zt": 0,
    "info": "会员已过期，无法使用",
    "text": None,
    "dat": None
}
"""

# 删除文件
status, result = file_manager.delete_file("246738845")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "已删除",
    "text": None,
    "dat": None
}
"""

# 上传文件
status, result = file_manager.upload_file("上传测试.txt", "test.txt", "12295088")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "上传成功",
    "text": [
        {
            "icon": "txt",
            "id": "246766304",
            "f_id": "iYYAN31w12je",
            "name_all": "上传测试.txt",
            "name": "上传测试.txt",
            "size": "18.0 B",
            "time": "0 秒前",
            "downs": "0",
            "onof": "0",
            "is_newd": "https://wwa.lanzouq.com"
        }
    ]
}
"""

# 移动文件
status, result = file_manager.move_file("246766304", "12295088") 
# 返回示例：
"""
True {
    "zt": 1,
    "info": "移动成功",
    "text": None,
    "dat": None
}
"""

# 设置文件密码
status, result = file_manager.set_file_pwd("246766304", "123456", "1")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "设置成功",
    "text": None,
    "dat": None
}
"""




# 创建文件夹管理实例
folder_manager = LanzouFolderManager(session)

# 创建文件夹
status, result = folder_manager.create_folder("测试2", "12295088", "测试文件夹2")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "创建成功",
    "text": "12296591",
    "dat": None
}
"""

# 删除文件夹
status, result = folder_manager.delete_folder("12296591")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "删除成功",
    "text": None,
    "dat": None
}
"""

# 获取文件夹信息
status, result = folder_manager.get_folder_info("12295254")
# 返回示例：
"""
True {
    "zt": 1,
    "info": {
        "name": "测试2",
        "des": "测试文件夹2",
        "pwd": "1vo0",
        "onof": "1",
        "taoc": "",
        "is_newd": "https://wwa.lanzouq.com",
        "new_url": "https://wwa.lanzouq.com/b0rafeg1e"
    },
    "text": None,
    "dat": None
}
"""

# 修改文件夹信息
status, result = folder_manager.set_folder_info("12295254", "测试2", "测试文件夹2")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "成功修改",
    "text": None,
    "dat": None
}
"""

# 修改文件夹密码
status, result = folder_manager.set_folder_pwd("12295254", "1vo0", "1")
# 返回示例：
"""
True {
    "zt": 1,
    "info": "修改成功",
    "text": None,
    "dat": None
}
"""

# 获取文件夹列表
status, result = folder_manager.get_folder_list("12295088")
# 返回示例：
"""
True {
    "zt": 1,
    "info": [
        {
            "name": "测试",
            "folder_des": "[测试文件夹]",
            "folderid": 12295088,
            "now": 1
        }
    ],
    "text": [
        {
            "onof": "1",
            "folderlock": "0",
            "is_lock": "0",
            "is_copyright": "0",
            "name": "修改测试2",
            "fol_id": "12295254",
            "folder_des": "[修改测试文件夹2...]"
        },
        省略...
    ],
    "dat": null
}
"""

# 获取文件列表
status, result = folder_manager.get_file_list("12295088")
# 返回示例：
"""
True {
    "zt": 1,
    "info": 1,
    "text": [
        {
            "icon": "jpg",
            "id": "246767298",
            "name_all": "EB9DA95273BC463B238A14588B7E6E8C.jpg",
            "name": "EB9DA95273BC463B238A14588B7E6E8C.jpg",
            "size": "342.3 K",
            "time": "24 分钟前",
            "downs": "0",
            "onof": "0",
            "is_lock": "0",
            "filelock": "0",
            "is_copyright": 0,
            "is_bakdownload": 0,
            "bakdownload": "0",
            "is_des": 0,
            "is_ico": 0
        },
        省略...
    ],
    "dat": null
}
"""




# 创建分享管理实例
share_manager = LanzouShareManager(session)

# 获取文件分享链接
status, result = share_manager.get_file_link("246767298")
# 返回示例：
"""
True {
    "zt": 1,
    "info": {
        "pwd": "bofq",
        "onof": "1",
        "f_id": "it02C31w1u5i",
        "taoc": "",
        "is_newd": "https://wnwgongzuoshi.lanzouq.com"
    },
    "text": None,
    "dat": None
}
"""

# 获取文件夹分享链接
status, result = share_manager.get_folder_link("12295088")
# 返回示例：
"""
True {
    "zt": 1,
    "info": {
        "pwd": "bofq",
        "onof": "1",
        "f_id": "it02C31w1u5i",
        "taoc": "",
        "is_newd": "https://wnwgongzuoshi.lanzouq.com"
    },
    "text": None,
    "dat": None
}
"""






# 他人分享的链接
创建下载链接管理实例
lanzouDown = LanzouDownManager()

# 获取文件夹参数
status = lanzouDown.get_folder_params("https://wnwgongzuoshi.lanzouq.com/b0rafebfi")

# 获取文件及文件夹列表
status, result = lanzouDown.get_file_list(url="https://zhiyinruanjian.lanzouu.com/b00jduzw6h", page=1)

# 获取文件信息(包含下载链接)
status, result = lanzouDown.get_file_info("https://wnwgongzuoshi.lanzouq.com/iXPIk05lhp0j", pwd="WNWgzs", final=True)
# 返回示例：
"""
True {
    "title": "文件名称.apk",
    "size": "57.0 M",
    "author": "KongHen02",
    "desc": "测试描述",
    "url": "https://developer-oss.lanrar.com/file/...",
    "down": ""
}
"""

# 通过下载链接获取下载直链
status, result = lanzouDown.get_final_url("https://developer-oss.lanrar.com/file/?AGYCPA8+UGFUXQszBDFRPQE+AjoDuAW9V/EB4F2AA7cH4QDKDtMAsgbZB9pR7QWDVr9UtAfoCoICWlFvB2lQZAA5Am0PfFBlVHILNgR2UTYBMgJrAzkFWFc5AWNdPAM1BzYAYg5qAGAGZQdnUTwFIlZqVCIHZQo9AjxRbwdqUGAAMgJsD2NQIlRyCy0EbVFiAWsCNQNuBShXYAEyXS4DMAc+AHgOMABlBjUHNVFgBTxWPVRmB2gKawI2UTUHbVBlAGQCbA9qUGZUZgs5BGVRYgFsAmEDaQViV2YBMF02AzEHMABnDn0ANQYgBzpRIwVxVn9UNAcqCmECYVFqB2pQZgA3AmAPZ1A8VDELewQkUTkBNgJiAzoFOldhATBdNAMxBzMAbg5kAGQGZAdjUSsFKlYqVDcHNAp/AjhRZgdsUGQAMwJhD2tQMVQ0C2oEYlF2AS4CdwMrBTpXYQExXTQDMQc/AGcOYABnBmYHZFEjBXFWZVQhB2UKOQIyUWIHdVBgADMCew9jUDZUMgtzBGJRYgFjAikDegVjVz8BcF1vA10HZAA8Dm4AZAZ+B3dRcQV9VnxUNAcHCn0CZFFqB2s=")




print(status, result)