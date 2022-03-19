# Start Frame Work
import os

# 글자 깨짐 방지
os.system("chcp 65001")

# window environment
os.system("cd docker && docker-compose up -d")

# module download
os.system("pip install -r requirements.txt")
os.system("WEB.lnk")
os.system("uvicorn server:application --reload")