# Quark 网盘 Python 库使用文档

## 1. 配置与初始化

首先，准备 `config.yaml` 配置文件，内容示例：

```yaml
quark:
  cookie: "你的cookie"
```

在代码中读取配置并初始化 Quark 会话：

```python
import yaml
from Quark import QuarkSession

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

quark_conf = config["quark"]
QuarkSession = QuarkSession(cookie=quark_conf["cookie"])
```

## 2. 检查 Cookie 是否有效

```python
status, result = QuarkSession.get_user_info()
```

---

## 3. 文件管理

### 3.1 创建文件管理实例

```python
from Quark import QuarkFileManager
quark_file = QuarkFileManager(session=QuarkSession)
```

### 3.2 获取文件夹内列表

```python
status, result = quark_file.get_lists(
    pdir_fid="文件夹ID",
    page=1,
    size=10,
    sort_by="file_name",
    sort_order="asc"
)
```

### 3.3 移动文件/文件夹

```python
status, result = quark_file.move_file(
    src_fids=["文件ID1", "文件ID2"],
    dst_pdir_fid="目标文件夹ID"
)
# 返回示例
# True {"task_id": "...", "finish": true}
```

### 3.4 重命名文件/文件夹

```python
status, result = quark_file.rename_file("文件ID", new_name="新文件名.png")
# 返回示例
# True {}
```

### 3.5 删除文件/文件夹

```python
status, result = quark_file.remove_file(fids=["文件ID1", "文件ID2"])
# 返回示例
# True {"task_id": "...", "finish": false}
```

---

## 4. 文件夹管理

### 4.1 创建文件夹管理实例

```python
from Quark import QuarkFolderManager
quark_folder = QuarkFolderManager(session=QuarkSession)
```

### 4.2 创建文件夹

```python
status, result = quark_folder.create_folder(
    folder_name="创建测试",
    pdir_fid="父文件夹ID"
)
# 返回示例
# True {"finish": true, "fid": "..."}
```

---

## 5. 分享转存

### 5.1 创建转存实例

```python
from Quark import QuarkSaveManager
quark_save = QuarkSaveManager(session=QuarkSession)
```

### 5.2 获取分享信息

```python
status, result = quark_save.get_share_info(text="分享文本")
# 返回示例
# True {"pwd_id": "...", "passcode": "..."}
```

### 5.3 获取分享链接 stoken

```python
status, result = quark_save.get_share_stoken(pwd_id="...", passcode="...")
# 返回示例
# True {"stoken": "...", ...}
```

### 5.4 获取分享链接文件列表

```python
status, result = quark_save.get_share_list(
    pwd_id="...",
    stoken="...",
    pdir_fid="0",  # 根目录
    page=1,
    size=10,
    sort_by="file_name",
    sort_order="asc"
)
```

### 5.5 转存全部/部分文件到网盘

**全部转存：**

```python
status, result = quark_save.save_share_file(
    pwd_id="...",
    stoken="...",
    to_pdir_fid="目标文件夹ID",
    pdir_save_all=True
)
# 返回示例
# True {"task_id": "..."}
```

**部分转存：**

```python
status, result = quark_save.save_share_file(
    pwd_id="...",
    stoken="...",
    to_pdir_fid="目标文件夹ID",
    fid_list=["文件ID1", "文件ID2"],
    share_token_list=["token1", "token2"],
    pdir_save_all=False
)
# 返回示例
# True {"task_id": "...", ...}
```

---

## 6. 分享链接管理

### 6.1 创建分享链接实例

```python
from Quark import QuarkShareManager
quark_share = QuarkShareManager(session=QuarkSession)
```

### 6.2 创建分享链接

```python
status, result = quark_share.create_share(
    fid_list=["文件ID1", "文件ID2", "文件ID3"],
    title="分享标题",
    expired_type=1,  # 1=永久，2=7天等
    url_type=1       # 1=公开，2=私密等
)
# 返回示例
# True {
#     "task_id": "2b6a31c873dc4a1ba72c6825d5199351",
#     "task_sync": false
# }
```

- **fid_list**：要分享的文件/文件夹ID列表
- **title**：分享标题
- **expired_type**：过期类型（如1为永久，2为7天等）
- **url_type**：链接类型（如1为公开，2为私密等）

> 创建分享后会返回 `task_id`，可用任务管理接口查询进度，分享成功后可通过 `get_share_info` 获取分享链接等详细信息。

### 6.3 获取分享链接信息

```python
status, result = quark_share.get_share_info(share_id="分享ID")
# 返回示例
# True {"title": "...", "share_url": "...", ...}
```

---

## 7. 任务管理

### 7.1 创建任务管理实例

```python
from Quark import QuarkTaskManager
quark_task = QuarkTaskManager(session=QuarkSession)
```

### 7.2 获取任务状态

```python
status, result = quark_task.get_task_status(task_id="任务ID", retry_index=0)
# status=0 未完成，status=2 成功
# share_id 可用于获取分享链接信息
```

---

## 8. 文件上传

### 8.1 创建上传实例

```python
from Quark import QuarkUploadManager
quark_upload = QuarkUploadManager(session=QuarkSession)
```

### 8.2 上传文件

```python
def progress(percent):
    print(f"上传进度: {percent}%")

status, result = quark_upload.upload_file(
    file_path="本地文件路径",
    file_name="上传文件名.zip",
    pdir_fid="目标文件夹ID",
    progress_callback=progress
)
# 返回示例（云端存在同文件）：
# True {"finish": true, "fid": "...", ...}
# 返回示例（云端不存在同文件）：
# True {"task_id": "...", "finish": true, "fid": "...", ...}
```

---

## 9. 下载文件
### 9.1 创建下载实例

```python
from Quark import QuarkDownManager
quark_down = QuarkDownManager(session=QuarkSession)
```

### 9.2 获取下载链接
```python
fid_list = ["078d0433bd65406e83c43538a36f8ba8"]
status, result = quark_down.get_download_url(fid_list=fid_list)
# 返回示例：
# 说明：下载文件需要携带cookie
# True {
#     "file": {
#         "fid": "078d0433bd65406e83c43538a36f8ba8",
#         "file_name": "爱德华的小说 - 蒋蒋、朱贺.flac",
#         "size": 28384894,
#         "format_type": "audio/x-flac",
#         "download_url": "https://dl-pc-zb-cf.pds.quark.cn/..."
#     },
#     "cookie": "cookie字符串"
# }
```

---

## 10. 打印输出

所有接口返回均为 `(status, result)`，可直接打印：

```python
import json
print(status, json.dumps(result, indent=4))
```

---

## 11. 其他说明

- 各接口参数请参考注释及返回示例。
- 任务型操作（如移动、删除、转存、分享等）返回 `task_id` 后，可用任务管理接口查询进度。
- 分享相关操作需先获取 `pwd_id`、`stoken` 等参数。

---

如需更详细的参数说明或扩展用法，请参考源码或补充提问。 
