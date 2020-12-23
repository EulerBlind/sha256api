from fastapi import FastAPI, Request
import hashlib

app = FastAPI()


@app.get("/sha256")
async def get_sha256_value(request: Request):
    content = await request.body()
    m_sha256 = hashlib.sha256()
    m_sha256.update(content)
    return m_sha256.hexdigest()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app,work=4)
