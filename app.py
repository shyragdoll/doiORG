import httpx

from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


client = httpx.Client(
    follow_redirects=True, timeout=10, verify=False,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
)

@app.get("/")
def doiORG(doi:str, head:int=0):
    header = None
    resp = client.head(f"https://doi.org/{doi}")
    if head == 1:
        header = dict(resp.headers)
    return {"url": str(resp.url), "code": resp.status_code, "header": header}


