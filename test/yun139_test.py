import json
from Yun139 import Yun139Session, Yun139FileManager, Yun139FolderManager, Yun139ShareManager, Yun139UploadManager, Yun139TaskManager, Yun139DownManager

# 创建移动云盘基础实例
token = "cGM6MTc3MzkwNjc2MjQ6bGN1R1dsWkJ8MXxSQ1N8MTc2NTAzOTQ3MDI4M3xhQ0NxM0VOWFczYl8yRUFLU1Z4RVZPX2NPNzdrS1VDZk0uanlSdU1qMG51YlNoMjBtSWpzbW5NNjd6QUV5VWNMRjlqZzZvX2o1cDg2WjNELkZxSlpyd0ZIZjQ5VkZObF9LQ1dwT2NMMTJwNzd1RWljd212YW9nTW5HQnJ3NFI2S0tqRGxIVUtYTUdOb2pXNk5KR0cyZFNzaUxXV1FReWE5YkxhcmMuMDJpMEEt"
Yun139Session = Yun139Session(token=token)

# 刷新token
status, result = Yun139Session.refresh_token()

# 说明：
# 1. 刷新token后，实例会自动更新token
# 2. token有效期小于15天才可以刷新




# 创建文件管理实例
yun139_file = Yun139FileManager(session=Yun139Session)


# 移动文件
status, result = yun139_file.move_file(
    src_fids=["FjyKEUGVXXmeU1zaXq1xO1JzHSVgVV0zn", "FqHFCWKxM1AKQwA80SQJF4buUj1DcTMaC", "Fr6papebvD1_xZSKZETlP4LxPl62W7x3f"],
    dst_pdir_fid="FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
)
# 响应示例
"""
True {'taskId': '1813463306615229568'}
"""
# 说明
# 获取任务ID后，可通过查询任务状态接口查询任务执行结果。


# 重命名文件/文件夹
status, result = yun139_file.rename_file(
    fid="FjyKEUGVXXmeU1zaXq1xO1JzHSVgVV0zn",
    new_name="2.png",
)
# 响应示例
"""
True {
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "fileId": "FjyKEUGVXXmeU1zaXq1xO1JzHSVgVV0zn",
        "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
        "name": "2.png",
        "description": "",
        "type": "file",
        "fileExtension": "png",
        "category": "image",
        "createdAt": "2025-11-06T18:55:47.463+08:00",
        "updatedAt": "2025-11-07T02:31:40.812+08:00",
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": false,
        "size": 124409,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": [
            {
                "style": "Small",
                "url": "https://ykj-eos-wx2-01.eos-wuxi-3.cmecloud.cn/9090eac76d6a483cbfeec335c5247c30086?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27xN1zgYFRctrTz1JQmGbGBgbfIkdQh1Z3.jpg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251106T183140Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=Y60FITYLOX7N6UJWBOEE%2F20251106%2Fdefault%2Fs3%2Faws4_request&t=3&u=1151300927707421677&ot=personal&oi=1151300927707421677&f=FjyKEUGVXXmeU1zaXq1xO1JzHSVgVV0zn&ext=eyJ1dCI6MX0%3D&X-Amz-Signature=3ab4c1f3f878cd489a68af8259156408c488dee3b37e3a4494cd8935f288ff2e"
            }
        ],
        "punishMode": null,
        "contentHash": "a64b0c5e352363f56db46f05e995aeb9a3b40eebbc9eb2393fca1aa1768d6361",
        "contentHashAlgorithm": "sha256",
        "revisionId": "1813235766453649536.1813235766453649537",
        "mediaMetaInfo": {
            "width": 1200,
            "height": 1200,
            "takenAt": null,
            "duration": null
        },
        "addressDetail": {
            "addressline": null,
            "country": null,
            "province": null,
            "city": null,
            "district": null,
            "township": null
        },
        "systemDir": null,
        "metadataAuditInfo": {
            "auditStatus": 1,
            "auditLevel": 10,
            "auditResult": 1
        },
        "contentAuditInfo": {
            "auditStatus": 0,
            "auditLevel": null,
            "auditResult": null
        }
    }
}
"""


# 删除文件
status, result = yun139_file.remove_file(
    fids=["FqHFCWKxM1AKQwA80SQJF4buUj1DcTMaC"],
)
# 响应示例
"""
True {
  "taskId": "1813468597285129984",
  "batchFileResults": null
}
"""




# 创建文件夹管理实例
yun139_folder = Yun139FolderManager(session=Yun139Session)

# 创建文件夹测试
status, result = yun139_folder.create_folder(folder_name="创建文件夹测试", pdir_fid="/")
# 返回示例
"""
True {
    "parentFileId": "/",
    "fileId": "Fqkd1QUxDEyTTkHUC5mdPNrmiuEk8QwGk",
    "type": "folder",
    "fileName": "创建文件夹测试",
    "rapidUpload": False,
    "uploadId": None,
    "partInfos": None,
    "exist": None,
    "formInfo": None
}
"""


# 获取文件列表
# 第一页
status, result = yun139_folder.get_lists(pdir_fid="FkohtRUgT4bh_lXm9OFhHBIFtoE04E_M4", size=50, cursor=None, sort_by="file_name", sort_order="asc")
# 第二页
status, result = yun139_folder.get_lists(pdir_fid="FkohtRUgT4bh_lXm9OFhHBIFtoE04E_M4", size=50, cursor="0|[57-0-0,12-0-1][JzlYdEZEWk8zMEZ0UjlaRjdIM0ZxLUc3MFpWMzBaZEhfYWUxVU1laUhicHlXYnRWLSc=,J0ZpcUlmVDFyNUlGRHc4MHhSenkxRzVwbEgwa2NxLVRMUSc=]", sort_by="file_name", sort_order="asc")
# 參數説明
# cursor：首页为None，还有文件的话会返回nextPageCursor
# 返回示例
"""
True {
    "items": [
        {
            "fileId": "Fiy3GykVcP9lxL8gNU1VJupjIC8I1XC1Z",
            "parentFileId": "Fn_WtHq4W6j7l6Vvh1zZI1YwQYBbeFvi-",
            "name": "跳转浏览器打开.jpg",
            "description": null,
            "type": "file",
            "fileExtension": "jpg",
            "category": "image",
            "createdAt": "2025-11-06T16:27:40.404+08:00",
            "updatedAt": "2025-11-06T16:27:43.078+08:00",
            "trashedAt": null,
            "localCreatedAt": null,
            "localUpdatedAt": null,
            "starredAt": null,
            "starred": false,
            "size": 134390,
            "thumbnailUrls": [
                {
                    "style": "Large",
                    "url": "https://ykj-eos-wx2-01.eos-wuxi-3.cmecloud.cn/201834f508ee42578f0bbafe25ea5a5a086?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%271VlGsvKlhZNw1kUyowMy9NJiDVMZ5NKT.jpg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251106T181634Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=Y60FITYLOX7N6UJWBOEE%2F20251106%2Fdefault%2Fs3%2Faws4_request&t=3&u=1151300927707421677&ot=personal&oi=1151300927707421677&f=Fiy3GykVcP9lxL8gNU1VJupjIC8I1XC1Z&ext=eyJ1dCI6MX0%3D&X-Amz-Signature=430c618d8dce1cbfcb193088b78a8e1d3f900ecbcc8bb12b6f8f517d82d73eba"
                },
                {
                    "style": "Small",
                    "url": "https://ykj-eos-wx2-01.eos-wuxi-3.cmecloud.cn/174a3830341144058ca6d506a9b7db41086?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27whS7upwNBr9T7IsUiTDrEhSr5JXcPCIB.jpg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251106T181634Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=Y60FITYLOX7N6UJWBOEE%2F20251106%2Fdefault%2Fs3%2Faws4_request&t=3&u=1151300927707421677&ot=personal&oi=1151300927707421677&f=Fiy3GykVcP9lxL8gNU1VJupjIC8I1XC1Z&ext=eyJ1dCI6MX0%3D&X-Amz-Signature=75b7b0bc6954c11bca7e7f30081046c0b769af6605aadb5f6cfc45f7af691914"
                }
            ],
            "punishMode": null,
            "contentHash": "433acbfad8c7bfd00f7a845c958749cb1163c871f3a10bb357b0e06a91ffaf33",
            "contentHashAlgorithm": "sha256",
            "systemDir": false,
            "revisionId": "1813161216340709504.1813161216340709505",
            "mediaMetaInfo": {
                "width": 1080,
                "height": 2154,
                "takenAt": "2023-11-14T22:19:19.000+08:00",
                "duration": null
            },
            "metadataAuditInfo": {
                "auditStatus": 1,
                "auditLevel": 10,
                "auditResult": 1
            },
            "contentAuditInfo": {
                "auditStatus": 0,
                "auditLevel": null,
                "auditResult": null
            },
            "userTags": null,
            "addressDetail": {
                "addressline": null,
                "country": null,
                "province": null,
                "city": null,
                "district": null,
                "township": null
            }
        }
    ],
    "nextPageCursor": null
}
"""




# 创建分享链接实例
yun139_share = Yun139ShareManager(session=Yun139Session)


# 创建分享链接
status, result = yun139_share.create_share(
    title="分享7天测试",
    url_type=0,
    fid_list=["FjyKEUGVXXmeU1zaXq1xO1JzHSVgVV0zn"],
    fld_list=["FqnVwsXnHDGOVKV2Gu1RNbLmQvbkJxx7j"],
    expired_time=7,
)
# 响应示例
"""
True {
  "result": {
    "resultCode": "0",
    "resultDesc": ""
  },
  "getOutLinkRes": {
    "getOutLinkResSet": [
      {
        "objID": "aab3b2f8d00e491da36b466052d94a5a",
        "passwd": "q9su",
        "linkID": "2qidFfUiQDtnx",
        "linkUrl": "https://yun.139.com/shareweb/#/w/i/2qidFfUiQDtnx",
        "linkUrlMin": null
      }
    ]
  }
}
"""




# 创建任务管理实例
yun139_task = Yun139TaskManager(session=Yun139Session)


# 查询任务状态
status, result = yun139_task.get_task_status(
    task_id="1813463306615229568",
)
# 响应示例
"""
True {
  "taskInfo": {
    "taskId": "1813463306615229568",
    "status": "Succeed",
    "progress": 100,
    "createdAt": "2025-11-07T02:27:52.000+08:00",
    "startedAt": "2025-11-07T02:27:52.000+08:00",
    "finishedAt": "2025-11-07T02:27:52.000+08:00",
    "code": null,
    "message": null,
    "taskType": 2
  },
  "batchFileResults": [
    {
      "srcFile": {
        "fileId": "FjyKEUGVXXmeU1zaXq1xO1JzHSVgVV0zn",
        "parentFileId": null,
        "name": null,
        "description": null,
        "type": "file",
        "fileExtension": null,
        "category": null,
        "createdAt": null,
        "updatedAt": null,
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": null,
        "size": null,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": null,
        "contentHashAlgorithm": null,
        "revisionId": null,
        "mediaMetaInfo": null,
        "addressDetail": null,
        "systemDir": null,
        "metadataAuditInfo": null,
        "contentAuditInfo": null
      },
      "rstFile": {
        "fileId": null,
        "parentFileId": null,
        "name": null,
        "description": null,
        "type": "file",
        "fileExtension": null,
        "category": null,
        "createdAt": null,
        "updatedAt": null,
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": null,
        "size": null,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": null,
        "contentHashAlgorithm": null,
        "revisionId": null,
        "mediaMetaInfo": null,
        "addressDetail": null,
        "systemDir": null,
        "metadataAuditInfo": null,
        "contentAuditInfo": null
      },
      "errCode": "0000",
      "message": "请求成功"
    },
    {
      "srcFile": {
        "fileId": "FqHFCWKxM1AKQwA80SQJF4buUj1DcTMaC",
        "parentFileId": null,
        "name": null,
        "description": null,
        "type": "file",
        "fileExtension": null,
        "category": null,
        "createdAt": null,
        "updatedAt": null,
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": null,
        "size": null,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": null,
        "contentHashAlgorithm": null,
        "revisionId": null,
        "mediaMetaInfo": null,
        "addressDetail": null,
        "systemDir": null,
        "metadataAuditInfo": null,
        "contentAuditInfo": null
      },
      "rstFile": {
        "fileId": null,
        "parentFileId": null,
        "name": null,
        "description": null,
        "type": "file",
        "fileExtension": null,
        "category": null,
        "createdAt": null,
        "updatedAt": null,
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": null,
        "size": null,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": null,
        "contentHashAlgorithm": null,
        "revisionId": null,
        "mediaMetaInfo": null,
        "addressDetail": null,
        "systemDir": null,
        "metadataAuditInfo": null,
        "contentAuditInfo": null
      },
      "errCode": "0000",
      "message": "请求成功"
    },
    {
      "srcFile": {
        "fileId": "Fr6papebvD1_xZSKZETlP4LxPl62W7x3f",
        "parentFileId": null,
        "name": null,
        "description": null,
        "type": "folder",
        "fileExtension": null,
        "category": null,
        "createdAt": null,
        "updatedAt": null,
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": null,
        "size": null,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": null,
        "contentHashAlgorithm": null,
        "revisionId": null,
        "mediaMetaInfo": null,
        "addressDetail": null,
        "systemDir": null,
        "metadataAuditInfo": null,
        "contentAuditInfo": null
      },
      "rstFile": {
        "fileId": null,
        "parentFileId": null,
        "name": null,
        "description": null,
        "type": "folder",
        "fileExtension": null,
        "category": null,
        "createdAt": null,
        "updatedAt": null,
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": null,
        "size": null,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": null,
        "contentHashAlgorithm": null,
        "revisionId": null,
        "mediaMetaInfo": null,
        "addressDetail": null,
        "systemDir": null,
        "metadataAuditInfo": null,
        "contentAuditInfo": null
      },
      "errCode": "0000",
      "message": "请求成功"
    }
  ],
  "extraData": {
    "totalProcess": 0,
    "consumedProcess": 3
  }
}
"""




# 创建文件上传实例
yun139_upload = Yun139UploadManager(session=Yun139Session)


# 定义上传进度函数
def progress(percent):
    print(f"上传进度: {percent}%")

# 上传文件
status, result = yun139_upload.upload_file(
    file_name="cc.zip",
    file_path="cc.zip",
    pdir_fid="FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
    progress_callback=progress,
)
# 响应示例
"""
上传进度: 100%
True {
  "fileId": "Fvwh5Wdjb6pl8BXzvEgpGhazttFGo2_gZ",
  "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
  "name": "cc.zip",
  "description": null,
  "type": "file",
  "fileExtension": "zip",
  "category": "zip",
  "createdAt": "2025-11-07T03:58:36.440+08:00",
  "updatedAt": "2025-11-07T03:58:37.561+08:00",
  "trashedAt": null,
  "localCreatedAt": null,
  "localUpdatedAt": null,
  "starredAt": null,
  "starred": false,
  "size": 115764,
  "userTags": null,
  "pathInfo": null,
  "labels": null,
  "thumbnailUrls": null,
  "punishMode": null,
  "contentHash": "c3c33c570389e7c62d0903a7a9c847d31f4baa5e778c32de45c1b60f13b05aa3",
  "contentHashAlgorithm": "sha256",
  "revisionId": "1813508974977261312.1813508974977261313",
  "mediaMetaInfo": null,
  "addressDetail": {
    "addressline": null,
    "country": null,
    "province": null,
    "city": null,
    "district": null,
    "township": null
  },
  "systemDir": null,
  "metadataAuditInfo": {
    "auditStatus": 0,
    "auditLevel": null,
    "auditResult": null
  },
  "contentAuditInfo": {
    "auditStatus": 0,
    "auditLevel": null,
    "auditResult": null
  }
}
"""




# 创建文件下载示例
yun139_download = Yun139DownManager(session=Yun139Session)


# 获取文件下载链接
status, result = yun139_download.get_download_url(
    fid="FqRfdx22osqO-tU0ZvV1Nb7ryEM8dqKAj",
)
# 响应示例
"""
True {
  "fileId": "FqRfdx22osqO-tU0ZvV1Nb7ryEM8dqKAj",
  "errCode": null,
  "message": null,
  "url": "https://b22-obs-ykj-01.obs.cidc-rp-2006.joint.cmecloud.cn/835819d8d344400396abdce1a824fb08086?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27%25E4%25B8%25AD%25E5%259B%25BD%25E7%25A7%25BB%25E5%258A%25A8%25E4%25BA%2591%25E7%259B%2598%25E4%25BA%25A7%25E5%2593%2581%25E6%2589%258B%25E5%2586%258C.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251106T190513Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AH4RWOMWLEL7ROYSF2S5%2F20251106%2Fcidc-rp-2006%2Fs3%2Faws4_request&t=2&u=1151300927707421677&ot=personal&oi=1151300927707421677&f=FqRfdx22osqO-tU0ZvV1Nb7ryEM8dqKAj&ext=eyJ1dCI6MX0%3D&X-Amz-Signature=dec21f63a1b115588509f133520ed2037d8af0a8adc8143934edec994b626909",
  "expiration": "2025-11-07T03:20:13.396+08:00",
  "size": 32029905,
  "cdnUrl": "https://yun.mcloud.139.com:443/cdnv1/20241023/FqF8bFyjxCaPMGZCsjbNHSLngJhZUcQMj.pdf?sign=246307c360737ab11f9e114b9bc829aa&t=1762456813",
  "cdnSwitch": false,
  "metadataAuditInfo": {
    "auditStatus": 0,
    "auditLevel": null,
    "auditResult": null
  },
  "contentAuditInfo": {
    "auditStatus": 1,
    "auditLevel": 30,
    "auditResult": 1
  }
}
"""




# 打印输出
print(status, json.dumps(result, ensure_ascii=False, indent=2))