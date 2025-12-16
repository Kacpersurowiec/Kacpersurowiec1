import cv2
import numpy as np
import requests
import uvicorn
from fastapi import FastAPI, UploadFile

GREEN = (0, 255, 0)
THICKNESS = 2
SCALE = 1.1

app = FastAPI()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def bytes_to_image(content: bytes):
    arr = np.frombuffer(content, np.uint8)
    return cv2.imdecode(arr, cv2.IMREAD_COLOR)


def detect_and_save(img, suffix: str):
    boxes, _ = hog.detectMultiScale(img, scale=SCALE)
    for (x, y, w, h) in boxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, THICKNESS)

    filename = f"wynik_{suffix}.jpg"
    cv2.imwrite(filename, img)
    return {"count": len(boxes), "file": filename}


@app.get("/local")
def local(path: str):
    img = cv2.imread(path)
    return detect_and_save(img, "local")


@app.get("/url")
def url(target_url: str):
    resp = requests.get(
        target_url,
        headers={"User-Agent": "Mozilla/5.0"},
        verify=False
    )
    img = bytes_to_image(resp.content)
    return detect_and_save(img, "url")


@app.post("/upload")
async def upload(file: UploadFile):
    content = await file.read()
    img = bytes_to_image(content)
    return detect_and_save(img, "upload")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
