# 서버 실행
from app import app
import uvicorn

application = app

if __name__ == "__main__":
    uvicorn.run("server:application", host="127.0.0.1", port="8000", log_level="info")
