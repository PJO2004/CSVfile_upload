# program start
```
1. [POST] CSV Click
2. [Try it out] Click
3. file select
4. Execute
```
주의사항
- file을 저장 할 때 excel file이 아닌 CSV file형태로 변환한 후 excute를 해야합니다.
- file을 upload할 때 excute를 두번 해주셔야 정상적으로 db에 데이터가 들어갈 수 있습니다.
- 같은 파일 이름으로는 중복이 뜰 수가 있습니다.

추가 사항
- 기존에 column명이 한글로 되어있을경우 테이블이 생성이 되지 않았던 문제점을 자동으로 영어로 번역해주는 방식으로 해결하였습니다.

# DB 확인 하는법
```
1. DB.bat을 실행
2. psql -U postgres 작성 후 실행 [DB접속]
- all table확인 : \dt
- 각 table의 값 확인 : select * from (table이름);
  -> table이름은 업로드한 파일 이름대로 저장이 됩니다.
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
