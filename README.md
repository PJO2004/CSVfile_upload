# program start
```
1. [POST] CSV Click
2. [Try it out] Click
3. file select
4. Execute
```
주의사항
- file을 저장 할 때 excel file이 아닌 CSV file형태로 변환한 후 excute를 해야합니다.



# dementia analyze
```
data : data, tablename

db_
-> db : database, table modelling

__init__
-> fastAPI
```


## start
```commandline
docekr-compose up -d
```

## WEB server
```commandline
uvicorn server:application --reload
```

## Python
- python v3.10 : 
<a class="button" href="https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe" style="user-select: auto;">Download Python 3.10.2</a>

## pycharm
- https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows

## Docker Install
- WSL2 : 
  - dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
  - dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
  - https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
  - wsl --set-default-version 2
- docker install : 
<a href="https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&amp;utm_medium=webreferral&amp;utm_campaign=dd-smartbutton&amp;utm_location=header" class="btn btn-primary">Download for Windows</a>
