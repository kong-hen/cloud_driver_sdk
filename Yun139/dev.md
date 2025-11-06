# 文件

## 文件列表

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/list' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 15:55:44,HhCGdYBLRyopmmBV,45F6EC3CC94941A344CFE2291C100221' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"pageInfo":{"pageSize":100,"pageCursor":null},"orderBy":"updated_at","orderDirection":"DESC","parentFileId":"FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz","imageThumbnailStyleList":["Small","Large"]}'

### 响应
{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "items": [
            {
                "fileId": "Fn46Cmd1r_WIfRHuhSRdLuIxrT5Gta-_i",
                "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
                "name": "新建文件夹",
                "description": "",
                "type": "folder",
                "fileExtension": "",
                "category": "folder",
                "createdAt": "2025-11-06T15:54:10.867+08:00",
                "updatedAt": "2025-11-06T15:54:10.867+08:00",
                "trashedAt": null,
                "localCreatedAt": null,
                "localUpdatedAt": null,
                "starredAt": null,
                "starred": false,
                "size": null,
                "thumbnailUrls": null,
                "punishMode": null,
                "contentHash": null,
                "contentHashAlgorithm": null,
                "systemDir": false,
                "revisionId": null,
                "mediaMetaInfo": null,
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
            },
            {
                "fileId": "FpBhf7j8A0pN17SY8zvhF5rf9kuZPAMAT",
                "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
                "name": "newsid.zip",
                "description": null,
                "type": "file",
                "fileExtension": "zip",
                "category": "zip",
                "createdAt": "2025-11-06T15:55:41.768+08:00",
                "updatedAt": "2025-11-06T15:55:44.059+08:00",
                "trashedAt": null,
                "localCreatedAt": null,
                "localUpdatedAt": null,
                "starredAt": null,
                "starred": false,
                "size": 39514,
                "thumbnailUrls": null,
                "punishMode": null,
                "contentHash": "076c29a2215f54c854e591a8fcb095bcecc7e23f68cdcc2403fab671d6e93eba",
                "contentHashAlgorithm": "sha256",
                "systemDir": false,
                "revisionId": "1813145123341500544.1813145123341500545",
                "mediaMetaInfo": null,
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
}




## 新建文件夹

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/create' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 15:54:10,P6AKUdgBM4rRome8,68857760043FBA8A5C1E00C069ED2D83' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"parentFileId":"FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz","name":"新建文件夹","description":"","type":"folder","fileRenameMode":"force_rename"}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
        "fileId": "Fn46Cmd1r_WIfRHuhSRdLuIxrT5Gta-_i",
        "type": "folder",
        "fileName": "新建文件夹",
        "rapidUpload": false,
        "uploadId": null,
        "partInfos": null,
        "exist": null,
        "formInfo": null
    }
}


## 重命名文件夹/文件

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/update' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 15:57:36,gAvZrmlMIlJZEOX5,20BE879B1D6819EF4F1C3219845727B6' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"fileId":"Fn46Cmd1r_WIfRHuhSRdLuIxrT5Gta-_i","name":"重命名","description":""}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "fileId": "Fn46Cmd1r_WIfRHuhSRdLuIxrT5Gta-_i",
        "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
        "name": "重命名",
        "description": "",
        "type": "folder",
        "fileExtension": "",
        "category": "folder",
        "createdAt": "2025-11-06T15:54:10.867+08:00",
        "updatedAt": "2025-11-06T15:57:37.002+08:00",
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": false,
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


## 删除文件夹/文件

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/recyclebin/batchTrash' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 15:58:52,5Ajo7QTLMurPizj8,4071A0544A621153A6AEDB86B91CC2C2' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"fileIds":["FlmDqpdDUq11LgrAEG81F5IWFJ62g1Lnd"]}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "taskId": "1813146724206741248",
        "batchFileResults": null
    }
}


## 移动文件夹/文件

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/batchMove' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 16:02:36,7Qty9h2MwiBrdbQx,EA0D08D0BCF869A6856F57146FAC22CA' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"fileIds":["Fn46Cmd1r_WIfRHuhSRdLuIxrT5Gta-_i","FpBhf7j8A0pN17SY8zvhF5rf9kuZPAMAT"],"toParentFileId":"FqnVwsXnHDGOVKV2Gu1RNbLmQvbkJxx7j"}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "taskId": "1813148603548534144"
    }
}


## 下载文件

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/getDownloadUrl' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 16:22:45,ZMHGQxpGEaweVFgF,7E9232548F384EB977DBC8CDA568A6F8' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"fileId":"FqRfdx22osqO-tU0ZvV1Nb7ryEM8dqKAj"}'

#### 请求参数说明

- fileId：文件ID

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "fileId": "FqRfdx22osqO-tU0ZvV1Nb7ryEM8dqKAj",
        "errCode": null,
        "message": null,
        "url": "https://b22-obs-ykj-01.obs.cidc-rp-2006.joint.cmecloud.cn/835819d8d344400396abdce1a824fb08086?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27%25E4%25B8%25AD%25E5%259B%25BD%25E7%25A7%25BB%25E5%258A%25A8%25E4%25BA%2591%25E7%259B%2598%25E4%25BA%25A7%25E5%2593%2581%25E6%2589%258B%25E5%2586%258C.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251106T082244Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AH4RWOMWLEL7ROYSF2S5%2F20251106%2Fcidc-rp-2006%2Fs3%2Faws4_request&t=2&u=1151300927707421677&ot=personal&oi=1151300927707421677&f=FqRfdx22osqO-tU0ZvV1Nb7ryEM8dqKAj&ext=eyJ1dCI6MX0%3D&X-Amz-Signature=5c96030dd1a00a2b81527c3f2363941961066ef4036c2aa5680b41d19e83885b",
        "expiration": "2025-11-06T16:37:44.872+08:00",
        "size": 32029905,
        "cdnUrl": "https://yun.mcloud.139.com:443/cdnv1/20241023/FqF8bFyjxCaPMGZCsjbNHSLngJhZUcQMj.pdf?sign=c9e2e786a75d72f25660b25cdf81fbab&t=1762418264",
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
}


# 任务

## 查询任务状态

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/task/get' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 16:02:37,3Nec1X7ct9SBEz4d,0070ECAF6D19CBC11D68007A1573977F' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"taskId":"1813148603548534144"}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "taskInfo": {
            "taskId": "1813148603548534144",
            "status": "Succeed",
            "progress": 100,
            "createdAt": "2025-11-06T16:02:36.000+08:00",
            "startedAt": "2025-11-06T16:02:36.000+08:00",
            "finishedAt": "2025-11-06T16:02:37.000+08:00",
            "code": null,
            "message": null,
            "taskType": 2
        },
        "batchFileResults": [
            {
                "srcFile": {
                    "fileId": "Fn46Cmd1r_WIfRHuhSRdLuIxrT5Gta-_i",
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
            },
            {
                "srcFile": {
                    "fileId": "FpBhf7j8A0pN17SY8zvhF5rf9kuZPAMAT",
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
            }
        ],
        "extraData": "{\"totalProcess\":0,\"consumedProcess\":2}"
    }
}


# 分享

## 分享文件

### 请求

curl 'https://yun.139.com/orchestration/personalCloud-rebuild/outlink/v1.0/getOutLink' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'CMS-DEVICE: default' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -b 'isUserDomainError=false; a_k=7GPCm4UY35hqmWh6; skey=rmU9gju1g9XD5RcSNvpWxOVvwoL0qf1RoNKqcwAvNgAbfO6dsp37IYt47gyCcJS3Mmf2m2Uqw4CdiWlsNmDYSdwF0fXyTdX309KsSXPjZDy8Yr+NY3U9FC5299PACLIvoz2WSf305wvV9yQBjxG9fmdDRUDSE8ESeQAoUQuV3dM=; platform=2; cutover_status=1; ud_id=1151300927707421677; nation_code=+86; ORCHES-I-ACCOUNT-SIMPLIFY=177****7624; ORCHES-I-ACCOUNT-ENCRYPT=MTc3MzkwNjc2MjQ=; token=0cbOm9+s2y/F03dDWpz3tZxBaT0M9esivsZaRGrjvYyWxsCdQtwOrA5xj9RUnP4jBKY+zzqY983ZAXZFThyuD/xq1oYWWh7q+RbehfEUHb1brxyOSAGOP/bVtN4Grl5luNBH1/JW+waFKJqgUnF4UF2q/kb99XUb/gnHbMbnXfsvyqk4QQdIo/YgVPGBntQX7FhAH4xuv4ta8znYgX7t755bxW82gTolgIRGgUmWclB7lDT0cB0/Evg9+hsdVCr+DExsLy0alhYA5qiKcJmSug==; auth_token=XfzYiLkv|1|RCS|1764835180892|YWPaTPSLiDyTc6OEycS4fSI0f9RQz8h2E8CJpwfm15burWfaTo8ABfn2PNIYBCXkDsSsoOcxqCC5Laz.XJj9wUPs9LAnIP179R1bWfLVNDwUN.PSCqUP60n8gMYLMYBjjWAaqFSdnnS9gW_UhbNCmInEsXIcg6S.YxnISz1r_Ww-; hecaiyundata2021jssdkcross=%7B%22distinct_id%22%3A%2219a4de059b2b9a-01adafcb2f44564-26061b51-2073600-19a4de059b3f01%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%2C%22phn%22%3A%22MTc3MzkwNjc2MjQ%3D%22%7D%2C%22%24device_id%22%3A%2219a4de059b2b9a-01adafcb2f44564-26061b51-2073600-19a4de059b3f01%22%7D; userInfo={"extMsg":{"provCode":"371"},"newUser":true}; authorization=Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct; hecaiyun_stay_url=https%3A%2F%2Fyun.139.com%2Fw%2F%23%2Findex; hecaiyun_stay_time=1762415161926; WT_FPC=id=2e30b67505fc36491de1762243140226:lv=1762415731584:ss=1762415162310' \
  -H 'INNER-HCY-ROUTER-HTTPS: 1' \
  -H 'Origin: https://yun.139.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://yun.139.com/w/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'X-Deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'X-Tingyun: c=B|MbVbeLGiVew;x=0e7833329ef645c2;u=base64#MTc3MzkwNjc2MjR8bnVsbA' \
  -H 'caller: web' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 16:09:48,bL6OxIJsdOhBZESE,0BAE345608BD5A9AB1A373E8E6DA68BB' \
  -H 'mcloud-skey: rmU9gju1g9XD5RcSNvpWxOVvwoL0qf1RoNKqcwAvNgAbfO6dsp37IYt47gyCcJS3Mmf2m2Uqw4CdiWlsNmDYSdwF0fXyTdX309KsSXPjZDy8Yr+NY3U9FC5299PACLIvoz2WSf305wvV9yQBjxG9fmdDRUDSE8ESeQAoUQuV3dM=' \
  -H 'mcloud-version: 7.16.2' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'x-SvcType: 1' \
  -H 'x-huawei-channelSrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"getOutLinkReq":{"subLinkType":0,"encrypt":1,"coIDLst":["FilwKFmpPNBOWV3CFfmpJMZm5xx4aTyaT"],"caIDLst":["FizlrtrFYb395jq34Px1NApjcpr7BWH3_","Fli0qzf4OjgiKyrJcsNVI3IXI58WODpyI"],"pubType":1,"dedicatedName":"\"影视飓风_清晰度不如4年前，视频变糊是你的错觉吗_20241102_165724\"等3个文件","period":7,"periodUnit":1,"viewerLst":[],"extInfo":{"isWatermark":0,"shareChannel":"3001"},"commonAccountInfo":{"account":"17739067624","accountType":1}}}'

#### 请求参数说明

- coIDLst：文件ID列表
- caIDLst：文件夹ID列表
- dedicatedName：分享名称
- period：分享有效期，单位：天（不传输此参数为永久）


### 响应

{
    "success": true,
    "code": "0",
    "message": "OK",
    "data": {
        "result": {
            "resultCode": "0",
            "resultDesc": ""
        },
        "getOutLinkRes": {
            "getOutLinkResSet": [
                {
                    "objID": "45bd99f2bdb344c4a2dae29288539d55",
                    "passwd": "sth4",
                    "linkID": "2qidENShBsZob",
                    "linkUrl": "https://yun.139.com/shareweb/#/w/i/2qidENShBsZob",
                    "linkUrlMin": null
                }
            ]
        }
    }
}


#### 响应参数说明

- url：下载链接


# Token

## 刷新Token

### 请求

curl 'https://aas.caiyun.feixin.10086.cn/tellin/authTokenRefresh.do' \
  -H 'Accept: */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/xml' \
  -H 'Origin: chrome-extension://pkgccpejnmalmdinmhkkfafefagiiiad' \
  -H 'Pragma: no-cache' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: none' \
  -H 'Sec-Fetch-Storage-Access: active' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '<root><token>XfzYiLkv|1|RCS|1764835180892|YWPaTPSLiDyTc6OEycS4fSI0f9RQz8h2E8CJpwfm15burWfaTo8ABfn2PNIYBCXkDsSsoOcxqCC5Laz.XJj9wUPs9LAnIP179R1bWfLVNDwUN.PSCqUP60n8gMYLMYcjJWAAqFSdnnS9gW_UhbNCmInEsXIcg6S.YxnISz1r_Ww-</token><account>17739067624</account><clienttype>656</clienttype></root>'

### 响应

<root>
<return>4006</return>
<desc>The token does not exist or has expired.</desc>
</root>


# 上传文件

## 创建上传

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/create' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 23:29:14,Kz440zYDiGNVgzrv,DCA9FBA6DDAFEBD310303A4DEDF56CEB' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"parentFileId":"FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz","name":"WNW.zip","type":"file","size":1462024231,"fileRenameMode":"auto_rename","contentHash":"48cc813d632400906ba86e843d9feabf58a2756081c95292cb34bc72d6fd1169","contentHashAlgorithm":"SHA256","contentType":"application/oct-stream","parallelUpload":false,"partInfos":[{"parallelHashCtx":{"partOffset":0},"partNumber":1,"partSize":20971520},{"parallelHashCtx":{"partOffset":20971520},"partNumber":2,"partSize":20971520},{"parallelHashCtx":{"partOffset":41943040},"partNumber":3,"partSize":20971520},{"parallelHashCtx":{"partOffset":62914560},"partNumber":4,"partSize":20971520},{"parallelHashCtx":{"partOffset":83886080},"partNumber":5,"partSize":20971520},{"parallelHashCtx":{"partOffset":104857600},"partNumber":6,"partSize":20971520},{"parallelHashCtx":{"partOffset":125829120},"partNumber":7,"partSize":20971520},{"parallelHashCtx":{"partOffset":146800640},"partNumber":8,"partSize":20971520},{"parallelHashCtx":{"partOffset":167772160},"partNumber":9,"partSize":20971520},{"parallelHashCtx":{"partOffset":188743680},"partNumber":10,"partSize":20971520},{"parallelHashCtx":{"partOffset":209715200},"partNumber":11,"partSize":20971520},{"parallelHashCtx":{"partOffset":230686720},"partNumber":12,"partSize":20971520},{"parallelHashCtx":{"partOffset":251658240},"partNumber":13,"partSize":20971520},{"parallelHashCtx":{"partOffset":272629760},"partNumber":14,"partSize":20971520},{"parallelHashCtx":{"partOffset":293601280},"partNumber":15,"partSize":20971520},{"parallelHashCtx":{"partOffset":314572800},"partNumber":16,"partSize":20971520},{"parallelHashCtx":{"partOffset":335544320},"partNumber":17,"partSize":20971520},{"parallelHashCtx":{"partOffset":356515840},"partNumber":18,"partSize":20971520},{"parallelHashCtx":{"partOffset":377487360},"partNumber":19,"partSize":20971520},{"parallelHashCtx":{"partOffset":398458880},"partNumber":20,"partSize":20971520},{"parallelHashCtx":{"partOffset":419430400},"partNumber":21,"partSize":20971520},{"parallelHashCtx":{"partOffset":440401920},"partNumber":22,"partSize":20971520},{"parallelHashCtx":{"partOffset":461373440},"partNumber":23,"partSize":20971520},{"parallelHashCtx":{"partOffset":482344960},"partNumber":24,"partSize":20971520},{"parallelHashCtx":{"partOffset":503316480},"partNumber":25,"partSize":20971520},{"parallelHashCtx":{"partOffset":524288000},"partNumber":26,"partSize":20971520},{"parallelHashCtx":{"partOffset":545259520},"partNumber":27,"partSize":20971520},{"parallelHashCtx":{"partOffset":566231040},"partNumber":28,"partSize":20971520},{"parallelHashCtx":{"partOffset":587202560},"partNumber":29,"partSize":20971520},{"parallelHashCtx":{"partOffset":608174080},"partNumber":30,"partSize":20971520},{"parallelHashCtx":{"partOffset":629145600},"partNumber":31,"partSize":20971520},{"parallelHashCtx":{"partOffset":650117120},"partNumber":32,"partSize":20971520},{"parallelHashCtx":{"partOffset":671088640},"partNumber":33,"partSize":20971520},{"parallelHashCtx":{"partOffset":692060160},"partNumber":34,"partSize":20971520},{"parallelHashCtx":{"partOffset":713031680},"partNumber":35,"partSize":20971520},{"parallelHashCtx":{"partOffset":734003200},"partNumber":36,"partSize":20971520},{"parallelHashCtx":{"partOffset":754974720},"partNumber":37,"partSize":20971520},{"parallelHashCtx":{"partOffset":775946240},"partNumber":38,"partSize":20971520},{"parallelHashCtx":{"partOffset":796917760},"partNumber":39,"partSize":20971520},{"parallelHashCtx":{"partOffset":817889280},"partNumber":40,"partSize":20971520},{"parallelHashCtx":{"partOffset":838860800},"partNumber":41,"partSize":20971520},{"parallelHashCtx":{"partOffset":859832320},"partNumber":42,"partSize":20971520},{"parallelHashCtx":{"partOffset":880803840},"partNumber":43,"partSize":20971520},{"parallelHashCtx":{"partOffset":901775360},"partNumber":44,"partSize":20971520},{"parallelHashCtx":{"partOffset":922746880},"partNumber":45,"partSize":20971520},{"parallelHashCtx":{"partOffset":943718400},"partNumber":46,"partSize":20971520},{"parallelHashCtx":{"partOffset":964689920},"partNumber":47,"partSize":20971520},{"parallelHashCtx":{"partOffset":985661440},"partNumber":48,"partSize":20971520},{"parallelHashCtx":{"partOffset":1006632960},"partNumber":49,"partSize":20971520},{"parallelHashCtx":{"partOffset":1027604480},"partNumber":50,"partSize":20971520},{"parallelHashCtx":{"partOffset":1048576000},"partNumber":51,"partSize":20971520},{"parallelHashCtx":{"partOffset":1069547520},"partNumber":52,"partSize":20971520},{"parallelHashCtx":{"partOffset":1090519040},"partNumber":53,"partSize":20971520},{"parallelHashCtx":{"partOffset":1111490560},"partNumber":54,"partSize":20971520},{"parallelHashCtx":{"partOffset":1132462080},"partNumber":55,"partSize":20971520},{"parallelHashCtx":{"partOffset":1153433600},"partNumber":56,"partSize":20971520},{"parallelHashCtx":{"partOffset":1174405120},"partNumber":57,"partSize":20971520},{"parallelHashCtx":{"partOffset":1195376640},"partNumber":58,"partSize":20971520},{"parallelHashCtx":{"partOffset":1216348160},"partNumber":59,"partSize":20971520},{"parallelHashCtx":{"partOffset":1237319680},"partNumber":60,"partSize":20971520},{"parallelHashCtx":{"partOffset":1258291200},"partNumber":61,"partSize":20971520},{"parallelHashCtx":{"partOffset":1279262720},"partNumber":62,"partSize":20971520},{"parallelHashCtx":{"partOffset":1300234240},"partNumber":63,"partSize":20971520},{"parallelHashCtx":{"partOffset":1321205760},"partNumber":64,"partSize":20971520},{"parallelHashCtx":{"partOffset":1342177280},"partNumber":65,"partSize":20971520},{"parallelHashCtx":{"partOffset":1363148800},"partNumber":66,"partSize":20971520},{"parallelHashCtx":{"partOffset":1384120320},"partNumber":67,"partSize":20971520},{"parallelHashCtx":{"partOffset":1405091840},"partNumber":68,"partSize":20971520},{"parallelHashCtx":{"partOffset":1426063360},"partNumber":69,"partSize":20971520},{"parallelHashCtx":{"partOffset":1447034880},"partNumber":70,"partSize":14989351}]}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "parentFileId": "FkohtRUgT4bh_lXm9OFhHBIFtoE04E_M4",
        "fileId": "Ftcm3qeH649fisZJhHY1MkKYseqGR-vFX",
        "type": "file",
        "fileName": "零零七IDC代理授权证书.pdf",
        "rapidUpload": false,
        "uploadId": "2~TdjInd62v7HM_ddOqkePkrVAAkVrYB8",
        "partInfos": [
            {
                "partNumber": 1,
                "partSize": null,
                "uploadUrl": "https://ykj-eos-wx2-01.eos-wuxi-3.cmecloud.cn/83aff2dd1de74f379989d85c5475f12d086?partNumber=1&uploadId=2~TdjInd62v7HM_ddOqkePkrVAAkVrYB8&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251106T151951Z&X-Amz-SignedHeaders=content-length%3Bhost&X-Amz-Expires=7200&X-Amz-Credential=Y60FITYLOX7N6UJWBOEE%2F20251106%2Fdefault%2Fs3%2Faws4_request&t=1&u=1151300927707421677&ot=personal&oi=1151300927707421677&f=Ftcm3qeH649fisZJhHY1MkKYseqGR-vFX&ext=eyJ1dCI6MX0%3D&X-Amz-Signature=fb5215456e377a7bcb2ca15254aa86cfa43aa0abd44c7d9a48a2ba579838d66f",
                "cdnUploadUrl": null,
                "etag": null,
                "parallelHashCtx": {
                    "h": null,
                    "partOffset": null
                }
            }
        ],
        "exist": null,
        "formInfo": null
    }
}

## 上传完成

### 请求

curl 'https://personal-kd-njs.yun.139.com/hcy/file/complete' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'authorization: Basic cGM6MTc3MzkwNjc2MjQ6WGZ6WWlMa3Z8MXxSQ1N8MTc2NDgzNTE4MDg5MnxZV1BhVFBTTGlEeVRjNk9FeWNTNGZTSTBmOVJRejhoMkU4Q0pwd2ZtMTVidXJXZmFUbzhBQmZuMlBOSVlCQ1hrRHNTc29PY3hxQ0M1TGF6LlhKajl3VVBzOUxBbklQMTc5UjFiV2ZMVk5Ed1VOLlBTQ3FVUDYwbjhnTVlMTVlCampXQWFxRlNkbm5TOWdXX1VoYk5DbUluRXNYSWNnNlMuWXhuSVN6MXJfV3ct' \
  -H 'cache-control: no-cache' \
  -H 'caller: web' \
  -H 'cms-device: default' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'inner-hcy-router-https: 1' \
  -H 'mcloud-channel: 1000101' \
  -H 'mcloud-client: 10701' \
  -H 'mcloud-route: 001' \
  -H 'mcloud-sign: 2025-11-06 23:50:14,Sy43NPSZE5fHa1az,0FA748C171A390FC8944C644318CA487' \
  -H 'mcloud-version: 7.16.2' \
  -H 'origin: https://yun.139.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://yun.139.com/' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'x-deviceinfo: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||' \
  -H 'x-huawei-channelsrc: 10000034' \
  -H 'x-inner-ntwk: 2' \
  -H 'x-m4c-caller: PC' \
  -H 'x-m4c-src: 10002' \
  -H 'x-svctype: 1' \
  -H 'x-yun-api-version: v1' \
  -H 'x-yun-app-channel: 10000034' \
  -H 'x-yun-channel-source: 10000034' \
  -H 'x-yun-client-info: ||9|7.16.2|chrome|142.0.0.0|086e19a997667ccba1c10fe591ed418e||windows 10||zh-CN|||dW5kZWZpbmVk||' \
  -H 'x-yun-module-type: 100' \
  -H 'x-yun-svc-type: 1' \
  --data-raw '{"fileId":"Fg5NI34Rq-6JxaJMb6AND8ZB2hdf0auki","uploadId":"2~6zmqdi9IorEgdyteAC4rBxtM7Cg0nmU","contentHash":"bbfe5c6f2541bc2741c01aeb761330fbd962f072b32218fda31faf5204217b44","contentHashAlgorithm":"SHA256"}'

### 响应

{
    "success": true,
    "code": "0000",
    "message": "请求成功",
    "data": {
        "fileId": "Fg5NI34Rq-6JxaJMb6AND8ZB2hdf0auki",
        "parentFileId": "FrtDI1Whq8nNnxiot-7FEOr01Bd0YauDz",
        "name": "广电飞号卡.png",
        "description": null,
        "type": "file",
        "fileExtension": "png",
        "category": "image",
        "createdAt": "2025-11-06T23:50:11.555+08:00",
        "updatedAt": "2025-11-06T23:50:14.586+08:00",
        "trashedAt": null,
        "localCreatedAt": null,
        "localUpdatedAt": null,
        "starredAt": null,
        "starred": false,
        "size": 204977,
        "userTags": null,
        "pathInfo": null,
        "labels": null,
        "thumbnailUrls": null,
        "punishMode": null,
        "contentHash": "bbfe5c6f2541bc2741c01aeb761330fbd962f072b32218fda31faf5204217b44",
        "contentHashAlgorithm": "sha256",
        "revisionId": "1813383943513209216.1813383943513209217",
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
}