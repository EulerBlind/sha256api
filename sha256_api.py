from fastapi import FastAPI, Request
import hashlib
from pydantic import BaseModel

app = FastAPI()


class Sha256Item(BaseModel):
    raw_string: str


class Sha256Response(BaseModel):
    sha256: str


@app.post("/sha256", response_model=Sha256Response)
async def get_sha256_value(body: Sha256Item):
    """
    :param body: json 类型
    :return:
    """
    content = body.raw_string
    m_sha256 = hashlib.sha256()
    m_sha256.update(bytes(content, "utf8"))
    resp = Sha256Response(sha256=m_sha256.hexdigest())
    return resp


@app.get("/sha256")
async def get_sha256_value(request: Request):
    """
    :param request: 单请求体类型
    :return:
    """
    content = await request.body()
    m_sha256 = hashlib.sha256()
    m_sha256.update(content)
    return m_sha256.hexdigest()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
