# fastAPI + DB 연동
from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()


@app.post("/csv")
async def upload_file(file: UploadFile = File(...)):
    upload_directory = "./app/data/"

    contents = await file.read()
    with open(os.path.join(upload_directory, "data.csv"), "wb") as fp:
        fp.write(contents)

    with open(os.path.join(upload_directory, "filename.txt"), "w") as fp:
        fp.write(file.filename.split(".")[0])

    os.system("python ./app/db_.py")

    return {"filename": file.filename}

