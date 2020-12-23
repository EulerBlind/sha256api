# 运行方式
```
uvicorn sha256_api:app --workers=4 --port=8000 --host=0.0.0.0
```

# 提供两个API
1、`GET /sha256`直接返回请求体的sha256值

2、`POST /sha256` 在json请求体中传入raw_string参数，返回的json请求体中sha256字段即sha256值

# 调试界面
`http://elvisiky.com:8033/docs`

# 部署方式
```docker-compose up -d --build```