import yaml
from Quark import QuarkSession,  QuarkFileManager, QuarkFolderManager, QuarkShareManager, QuarkUploadManager, QuarkTaskManager, QuarkSaveManager, QuarkDownManager

# 读取配置文件
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
quark_conf = config["quark"]

# 创建夸克基础实例
QuarkSession = QuarkSession(cookie=quark_conf["cookie"])

# 检查cookie是否有效
status, result = QuarkSession.get_user_info()




# 创建文件管理实例
quark_file = QuarkFileManager(session=QuarkSession)

# 获取文件夹内列表测试
status, result = quark_file.get_lists(pdir_fid="752c1bcfd6e74778bbb7ebb163fb47a2", page=2, size=10, sort_by="file_name", sort_order="asc")

# 移动文件/文件夹示例
status, result = quark_file.move_file(src_fids=["aeef85aa805242aebd51f1552fa2e331", "77c2aae227214f158c9e7fe97973444d"], dst_pdir_fid="9281aec492a74b4195d6108f7f34aacd")
# 返回任务ID，需要通过任务ID查询任务状态
# 返回示例：
"""
True {
   "task_id": "4308d28d0bb84903aa50ee5ae1ca49b0",
   "finish": true
}
"""

# 重命名文件/文件夹示例
status, result = quark_file.rename_file("aeef85aa805242aebd51f1552fa2e331", new_name="test.png")
# 返回示例：
"""
True {}
"""

# 删除文件/文件夹示例
status, result = quark_file.remove_file(fids=["57eb0bedbdd74296a5d0bd5917ab6cd5", "4bea66049fa04fcd98a274d88e8d7505"])
# 返回任务ID，需要通过任务ID查询任务状态
# 返回示例：
"""
True {
    "task_id": "d6ad8de7ec4a486d8ba66d5ffe2a4199",
    "finish": false
}
"""




# 创建文件夹管理实例
quark_folder = QuarkFolderManager(session=QuarkSession)

# 创建文件夹测试
status, result = quark_folder.create_folder(folder_name="创建测试", pdir_fid="57e02c0c94d84ee7b02dfc186441c6f6")
# 返回示例：
"""
True {
    "finish": true,
    "fid": "ec191dd55629408eb736e374aa1e58aa"
}
"""




# 创建转存分享的文件实例
quark_save = QuarkSaveManager(session=QuarkSession)

# 获取分享文件保存列表
status, result = quark_save.get_share_info(text="我用夸克网盘分享了「python」，点击链接即可保存。打开「夸克APP」，无需下载在线播放视频，畅享原画5倍速，支持电视投屏。\n链接：https://pan.quark.cn/s/f5e20b6bb6e3\n提取码：Z2pt")
# 返回示例：
"""
True {
    "pwd_id": "f5e20b6bb6e3",
    "passcode": "Z2pt"
}
"""

# 获取分享链接的stoken
status, result = quark_save.get_share_stoken(pwd_id="f5e20b6bb6e3", passcode="Z2pt")
# 返回示例：
"""
True {
    "subscribed": false,
    "stoken": "LNqcLxBVVzCEWESkw60yvrFZpg0k7vzkR/Gagsn0DZs=",
    "share_type": 0,
    "author": {
        "member_type": "SUPER_VIP",
        "avatar_url": "http://image.quark.cn/o/uop/1Ht08/;;0,uop/g/uop/avatar/14a87ba9bda90a2059941c5ec1743857.jpg;3,160",
        "nick_name": "z*"
    },
    "url_type": 2,
    "expired_type": 1,
    "expired_at": 4102416000000,
    "title": "测试"
}
"""

# 下面测试使用的链接是：https://pan.quark.cn/s/2747b1acf7fe
# 获取分享链接的根目录文件列表
status, result = quark_save.get_share_list(pwd_id="2747b1acf7fe", stoken="uJ9zxm8Vbf++Lj+Nfg7ZkLECgoNt7Ab1euBIno2vfPI=", pdir_fid="0", page=1, size=10, sort_by="file_name", sort_order="asc")
# 获取分享链接的指定文件夹文件列表
status, result = quark_save.get_share_list(pwd_id="2747b1acf7fe", stoken="uJ9zxm8Vbf++Lj+Nfg7ZkLECgoNt7Ab1euBIno2vfPI=", pdir_fid="57e02c0c94d84ee7b02dfc186441c6f6", page=1, size=10, sort_by="file_name", sort_order="asc")

# 转存全部文件到文件夹中
status, result = quark_save.save_share_file(pwd_id="2747b1acf7fe", stoken="uJ9zxm8Vbf++Lj+Nfg7ZkLECgoNt7Ab1euBIno2vfPI=", to_pdir_fid="57e02c0c94d84ee7b02dfc186441c6f6", pdir_save_all=True)
# 全部转存返回示例：
# 返回任务ID，需要通过任务ID查询任务状态
"""
True {
    "task_id": "4a7b54a5bdd64c79bfd06bd5185809e2"
}
"""
# 转存指定文件到文件夹中
status, result = quark_save.save_share_file(pwd_id="2747b1acf7fe", stoken="uJ9zxm8Vbf++Lj+Nfg7ZkLECgoNt7Ab1euBIno2vfPI=", to_pdir_fid="57e02c0c94d84ee7b02dfc186441c6f6", fid_list=["d8d25f7e7a6e47a9ba6d855af48a3070", "ac9e2a6f0c794891bd41baa2e7f3ddca"], share_token_list=["252093c1c193f9abbf4a3fd78c86bd1b", "362a155115479790d5faffdc9b5d4330"], pdir_save_all=False)
# 返回示例：
# 返回任务ID，需要通过任务ID查询任务状态
"""
True {
    "task_id": "cfe75f0fe4474e3f85fc3835c247185c",
    "task_sync": true,
    "task_resp": {
        "status": 200,
        "code": 0,
        "message": "ok",
        "timestamp": 1753398869,
        "data": {
            "task_id": "cfe75f0fe4474e3f85fc3835c247185c",
            "event_id": "97y0l2-26ced21fa481c2",
            "task_type": 17,
            "task_title": "分享-转存",
            "status": 1,
            "created_at": 1753398868850,
            "finished_at": 1753398868921,
            "share": {
                "meaning_link": true
            },
            "save_as": {
                "search_exit": false,
                "save_as_select_top_fids": [],
                "remain_capacity": 5466032511467,
                "to_pdir_fid": "57e02c0c94d84ee7b02dfc186441c6f6",
                "save_as_sum_num": 2,
                "is_pack": "0",
                "save_as_top_fids": [
                    "947d1879daff4928b90f6e2f767cbb04",
                    "650df7cdb5c241c9b4e82d0afe798aa3"
                ],
                "to_pdir_name": "测试",
                "min_save_file_size": 5522358
            }
        },
        "metadata": {}
    }
}
"""




# 创建分享链接实例
quark_share = QuarkShareManager(session=QuarkSession)

# 创建分享
status, result = quark_share.create_share(fid_list=["bbc1c492216942c6a213137542bf1e54", "5c1c23dce22041669fc72c1f43e91762", "947d1879daff4928b90f6e2f767cbb04"], title="分享测试", expired_type=1, url_type=1)
# 返回示例：
# 返回任务ID，需要通过任务ID查询任务状态
"""
True {
    "task_id": "2b6a31c873dc4a1ba72c6825d5199351",
    "task_sync": false
}
"""

# 获取分享链接密码等信息
status, result = quark_share.get_share_info(share_id="44a3ef11640247a68b8bbb6eb2e5f9fe")
# 返回示例：
"""
True {
    "title": "测试2",
    "sub_title": "我用网盘给你分享文件，赶快查收吧。",
    "share_type": 0,
    "pwd_id": "9cc971d49c5a",
    "share_url": "https://pan.quark.cn/s/9cc971d49c5a",
    "url_type": 1,
    "expired_type": 1,
    "file_num": 3,
    "expired_at": 4102416000000,
    "first_file": {
        省略...
    },
    "path_info": "/测试",
    "partial_violation": false,
    "size": 5627896,
    "first_layer_file_categories": [
        0,
        4,
        3
    ],
    "download_pvlimited": false
}
"""
# 参数说明
"""
share_url: 分享链接URL
"""





# 创建任务信息实例
quark_task = QuarkTaskManager(session=QuarkSession)

# 获取任务状态
status, result = quark_task.get_task_status(task_id="2b6a31c873dc4a1ba72c6825d5199351", retry_index=0)
# 返回示例：
"""
True {
    "task_id": "2b6a31c873dc4a1ba72c6825d5199351",
    "event_id": "9781bj-26ced90ef0b87f",
    "task_type": 8,
    "task_title": "分享",
    "status": 2,
    "created_at": 1753399777772,
    "finished_at": 1753399777913,
    "share_id": "44a3ef11640247a68b8bbb6eb2e5f9fe",
    "share": {
        "meaning_link": true
    },
    "save_as": {
        "save_as_select_top_fids": [],
        "is_pack": "0",
        "save_as_top_fids": []
    },
    "creation_snapshot": {
        "success_count": 3,
        "failed_count": 0
    }
}
"""
# 关键参数说明：
"""
status为0则还未分享完成
status为2则分享成功
share_id为分享链接ID，调用QuarkShareManager下的get_share_info获取分享链接密码等信息
"""




# 创建文件上传实例
quark_upload = QuarkUploadManager(session=QuarkSession)

# 定义上传进度函数
def progress(percent):
    print(f"上传进度: {percent}%")

# 上传文件
status, result = quark_upload.upload_file(file_path="111.zip", file_name="上传测试.zip", pdir_fid="9281aec492a74b4195d6108f7f34aacd", progress_callback=progress)
# 返回示例：
# 云端存在相同文件(hash验证)
"""
True {
    "finish": true,
    "obj_key": "35cd2b39f96c4be494a34a07dc1d35b0",
    "fid": "c3ab5896b5d04771aa3e452cdfacfb59",
    "pdir_fid": "bbc1c492216942c6a213137542bf1e54",
    "preview_url": "https://img-view-c-zb.drive.quark.cn/WGboOrgU/6489421911/20d977a9bae843b48ea5cfc86620f85a6882e1f9/6882e1f9d4b7199c98304a3ea63a28d325fdab7a/preview?auth_key=1753419131-88959-10800-97a5bb66bf498ab2263920d2f22d05cd&sp=100&token=5-d26f972c2be627802ccffd87cd0c8b3e-2-3-3096-35cd2b39f96c4be494a34a07dc1d35b0-0-0-0-0-1753408331290-3453d250d538b23a78922a792b404674&ud=16-2-5-N-N-N-11-N-1-N-0-N-N-N-N",
    "format_type": "application/zip",
    "size": 91094454,
    "path_fid_map": {}
}
"""
# 云端不存在相同文件
"""
True {
    "task_id": "393cae1e2ed243ca80d4b074052e4063",
    "finish": true,
    "obj_key": "35cd2b39f96c4be494a34a07dc1d35b0",
    "fid": "33daf04d688747eb9b0fcd8391b95961",
    "pdir_fid": "9281aec492a74b4195d6108f7f34aacd",
    "file_name": "上传测试.zip",
    "md5": "a464cbe4c078a73b6367542a4fb5efe9",
    "sha1": "7f51816e0a715c624f0caeed21afed28c008ca50",
    "preview_url": "https://img-view-c-zb.drive.quark.cn/WGboOrgU/6489421911/20d977a9bae843b48ea5cfc86620f85a6882e1f9/6882e1f9d4b7199c98304a3ea63a28d325fdab7a/preview?auth_key=1753418826-88959-10800-a24030259746bc3ec0cd5b8bbeef3e04&sp=100&token=5-d26f972c2be627802ccffd87cd0c8b3e-2-3-3096-35cd2b39f96c4be494a34a07dc1d35b0-0-0-0-0-1753408026273-0b57d9600b834b6c17bb2fc9dbad6614&ud=16-2-6-N-N-N-11-N-1-N-0-N-N-N-N",
    "format_type": "application/x-zip-compressed",
    "size": 91094454,
    "file_struct": {
        "platform_source": "pc"
    }
}
"""
# 关键参数说明：
"""
finish: 是否完成上传
fid: 文件ID
"""




# 创建文件下载实例
quark_down = QuarkDownManager(session=QuarkSession)

# 获取下载链接
fid_list = ["078d0433bd65406e83c43538a36f8ba8"]
status, result = quark_down.get_download_url(fid_list=fid_list)
# 返回示例：
"""
True {
    "file": {
        "fid": "078d0433bd65406e83c43538a36f8ba8",
        "file_name": "爱德华的小说 - 蒋蒋、朱贺.flac",
        "size": 28384894,
        "format_type": "audio/x-flac",
        "download_url": "https://dl-pc-zb-cf.pds.quark.cn/..."
    },
    "cookie": "cookie字符串"
}
"""





# 打印输出
print(status, result)
