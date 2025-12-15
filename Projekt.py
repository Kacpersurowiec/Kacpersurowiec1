import cv2
import numpy as np
import requests
import os
import time
import uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()
os.makedirs("results", exist_ok=True)


def process(img, name):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    img = cv2.resize(img,
                     (0, 0), fx=0.8, fy=0.8)
    boxes, _ = (hog.detectMultiScale
                (img, winStride=(8, 8), padding=(8, 8), scale=1.05))
    for (x, y, w, h) in boxes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    path = f"results/{int(time.time())}_{name}.jpg"
    cv2.imwrite(path, img)
    return {"count": len(boxes), "path": path}


@app.get("/local")
def local(path: str):
    return process(cv2.imread(path), "local")


@app.get("/url")
def url(url: str):
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                        verify=False).content
    arr = np.frombuffer(resp, np.uint8)
    return process(cv2.imdecode(arr, cv2.IMREAD_COLOR), "url")


@app.post("/upload")
async def upload(file: UploadFile):
    data = await file.read()
    arr = np.frombuffer(data, np.uint8)
    return process(cv2.imdecode(arr, cv2.IMREAD_COLOR), file.filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
