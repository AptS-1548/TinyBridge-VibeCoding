from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import links
from app.database.database import create_tables

app = FastAPI(
    title="TinyBridge API",
    description="短链接服务API",
    version="1.0.0"
)

# CORS设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # 前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 启动时创建数据库表
@app.on_event("startup")
async def startup():
    create_tables()

# 包含API路由
app.include_router(links.router, prefix="/api")

# 短链跳转路由
app.include_router(links.redirect_router)

@app.get("/")
async def root():
    return {"message": "TinyBridge API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)