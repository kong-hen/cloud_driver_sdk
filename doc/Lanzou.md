# 蓝奏云 Python 库使用文档

## 1. 配置与初始化

首先，准备 `config.yaml` 配置文件，内容示例：

```yaml
lanzou:
  username: "你的用户名"
  password: "你的密码"
```

在代码中读取配置并初始化蓝奏云会话：

```python
import yaml
from Lanzou import LanzouSession

# 读取配置文件
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
lanzou_conf = config["lanzou"]

# 创建蓝奏云基础实例
session = LanzouSession()

# 登录获取cookie
status, result = session.login(lanzou_conf["username"], lanzou_conf["password"])
```

---

## 2. 文件管理

### 2.1 创建文件管理实例

```python
from Lanzou import LanzouFileManager
file_manager = LanzouFileManager(session)
```

### 2.2 重命名文件

```python
status, result = file_manager.rename_file("文件ID", "新文件名.png")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "重命名成功",
#     "text": None,
#     "dat": None
# }
# False {
#     "zt": 0,
#     "info": "会员已过期，无法使用",
#     "text": None,
#     "dat": None
# }
```

### 2.3 删除文件

```python
status, result = file_manager.delete_file("文件ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "已删除",
#     "text": None,
#     "dat": None
# }
```

### 2.4 上传文件

```python
status, result = file_manager.upload_file("本地文件路径", "上传文件名.txt", "目标文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "上传成功",
#     "text": [
#         {
#             "icon": "txt",
#             "id": "246766304",
#             "f_id": "iYYAN31w12je",
#             "name_all": "上传测试.txt",
#             "name": "上传测试.txt",
#             "size": "18.0 B",
#             "time": "0 秒前",
#             "downs": "0",
#             "onof": "0",
#             "is_newd": "https://wwa.lanzouq.com"
#         }
#     ]
# }
```

### 2.5 移动文件

```python
status, result = file_manager.move_file("文件ID", "目标文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "移动成功",
#     "text": None,
#     "dat": None
# }
```

### 2.6 设置文件密码

```python
status, result = file_manager.set_file_pwd("文件ID", "密码", "1")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "设置成功",
#     "text": None,
#     "dat": None
# }
```

---

## 3. 文件夹管理

### 3.1 创建文件夹管理实例

```python
from Lanzou import LanzouFolderManager
folder_manager = LanzouFolderManager(session)
```

### 3.2 创建文件夹

```python
status, result = folder_manager.create_folder("文件夹名称", "父文件夹ID", "文件夹描述")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "创建成功",
#     "text": "12296591",
#     "dat": None
# }
```

### 3.3 删除文件夹

```python
status, result = folder_manager.delete_folder("文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "删除成功",
#     "text": None,
#     "dat": None
# }
```

### 3.4 获取文件夹信息

```python
status, result = folder_manager.get_folder_info("文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": {
#         "name": "测试2",
#         "des": "测试文件夹2",
#         "pwd": "1vo0",
#         "onof": "1",
#         "taoc": "",
#         "is_newd": "https://wwa.lanzouq.com",
#         "new_url": "https://wwa.lanzouq.com/b0rafeg1e"
#     },
#     "text": None,
#     "dat": None
# }
```

### 3.5 修改文件夹信息

```python
status, result = folder_manager.set_folder_info("文件夹ID", "新名称", "新描述")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "成功修改",
#     "text": None,
#     "dat": None
# }
```

### 3.6 修改文件夹密码

```python
status, result = folder_manager.set_folder_pwd("文件夹ID", "密码", "1")
# 返回示例：
# True {
#     "zt": 1,
#     "info": "修改成功",
#     "text": None,
#     "dat": None
# }
```

### 3.7 获取文件夹列表

```python
status, result = folder_manager.get_folder_list("父文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": [
#         {
#             "name": "测试",
#             "folder_des": "[测试文件夹]",
#             "folderid": 12295088,
#             "now": 1
#         }
#     ],
#     "text": [
#         {
#             "onof": "1",
#             "folderlock": "0",
#             "is_lock": "0",
#             "is_copyright": "0",
#             "name": "修改测试2",
#             "fol_id": "12295254",
#             "folder_des": "[修改测试文件夹2...]"
#         }
#     ],
#     "dat": null
# }
```

### 3.8 获取文件列表

```python
status, result = folder_manager.get_file_list("文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": 1,
#     "text": [
#         {
#             "icon": "jpg",
#             "id": "246767298",
#             "name_all": "EB9DA95273BC463B238A14588B7E6E8C.jpg",
#             "name": "EB9DA95273BC463B238A14588B7E6E8C.jpg",
#             "size": "342.3 K",
#             "time": "24 分钟前",
#             "downs": "0",
#             "onof": "0",
#             "is_lock": "0",
#             "filelock": "0",
#             "is_copyright": 0,
#             "is_bakdownload": 0,
#             "bakdownload": "0",
#             "is_des": 0,
#             "is_ico": 0
#         }
#     ],
#     "dat": null
# }
```

---

## 4. 分享链接管理

### 4.1 创建分享管理实例

```python
from Lanzou import LanzouShareManager
share_manager = LanzouShareManager(session)
```

### 4.2 获取文件分享链接

```python
status, result = share_manager.get_file_link("文件ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": {
#         "pwd": "bofq",
#         "onof": "1",
#         "f_id": "it02C31w1u5i",
#         "taoc": "",
#         "is_newd": "https://wnwgongzuoshi.lanzouq.com"
#     },
#     "text": None,
#     "dat": None
# }
```

### 4.3 获取文件夹分享链接

```python
status, result = share_manager.get_folder_link("文件夹ID")
# 返回示例：
# True {
#     "zt": 1,
#     "info": {
#         "pwd": "bofq",
#         "onof": "1",
#         "f_id": "it02C31w1u5i",
#         "taoc": "",
#         "is_newd": "https://wnwgongzuoshi.lanzouq.com"
#     },
#     "text": None,
#     "dat": None
# }
```

---

## 5. 他人分享链接下载

### 5.1 创建下载管理实例

```python
from Lanzou import LanzouDownManager
lanzouDown = LanzouDownManager()
```

### 5.2 获取文件夹参数

```python
status = lanzouDown.get_folder_params("分享链接URL")
```

### 5.3 获取文件及文件夹列表

```python
status, result = lanzouDown.get_file_list(url="分享链接URL", page=1)
```

### 5.4 获取文件信息（包含下载链接）

```python
status, result = lanzouDown.get_file_info("文件分享链接", pwd="密码", final=True)
# 返回示例：
# True {
#     "title": "文件名称.apk",
#     "size": "57.0 M",
#     "author": "KongHen02",
#     "desc": "测试描述",
#     "url": "https://developer-oss.lanrar.com/file/...",
#     "down": ""
# }
```

### 5.5 通过下载链接获取下载直链

```python
status, result = lanzouDown.get_final_url("下载链接")
```

---

## 6. 打印输出

所有接口返回均为 `(status, result)`，可直接打印：

```python
import json
print(status, json.dumps(result, indent=4))
```

---

## 7. 其他说明

- 各接口返回状态 `status` 为布尔值，`True` 表示成功，`False` 表示失败
- 返回结果中的 `zt` 字段：1 表示成功，0 表示失败
- `info` 字段包含操作结果的详细信息
- `text` 字段通常包含文件或文件夹的详细信息
- 分享链接管理需要用户登录后才能使用
- 他人分享链接下载不需要登录即可使用

如需更详细的参数说明或扩展用法，请参考源码或补充提问。