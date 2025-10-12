# 统一管理所有API域名和路径常量

# 域名常量
PAN_DOMAIN = "https://drive.uc.cn"  # 主要用于登录状态检查
DRIVE_DOMAIN = "https://pc-api.uc.cn"  # 主要用于大部分API请求

# 用户信息
USER_INFO = "/account/info"

# 文件上传
FILE_UPLOAD_PRE = "/1/clouddrive/file/upload/pre"
FILE_UPDATE_HASH = "/1/clouddrive/file/update/hash"
FILE_UPLOAD_AUTH = "/1/clouddrive/file/upload/auth"
FILE_UPLOAD_FINISH = "/1/clouddrive/file/upload/finish"

# 文件列表
FILE_SORT = "/1/clouddrive/file/sort"

# 文件操作
FILE_MOVE = "/1/clouddrive/file/move"
FILE_RENAME = "/1/clouddrive/file/rename"
FILE_DELETE = "/1/clouddrive/file/delete"
CREATE_FOLDER = "/1/clouddrive/file"

# 内容分享
SHARE = "/1/clouddrive/share"
SHARE_PASSWORD = "/1/clouddrive/share/password"

# 任务状态
TASK = "/1/clouddrive/task"