import cv2
import numpy as np
import requests
import uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def run(img, suffix):
    boxes, _ = hog.detectMultiScale(img, scale=1.1)
    for (x, y, w, h) in boxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    filename = f"wynik_{suffix}.jpg"
    cv2.imwrite(filename, img)
    return {"count": len(boxes), "file": filename}


@app.get("/local")
def local(path: str):
    return run(cv2.imread(path), "local")


@app.get("/url")
def url(url: str):
    resp = requests.get(
        url,
        headers={'User-Agent': 'Mozilla/5.0'},
        verify=False
    )
    arr = np.frombuffer(resp.content, np.uint8)
    return run(cv2.imdecode(arr, cv2.IMREAD_COLOR), "url")


@app.post("/upload")
async def upload(file: UploadFile):
    content = await file.read()
    arr = np.frombuffer(content, np.uint8)
    return run(cv2.imdecode(arr, cv2.IMREAD_COLOR), "upload")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
