import cv2
import numpy as np
import requests
import uuid
import uvicorn
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()
jobs = {}


def detect(jid, source, is_url):
    try:
        print(f"Przetwarzanie ID: {jid}...")  # Log w konsoli
        if is_url:
            headers = {'User-Agent': 'Mozilla/5.0'}
            resp = requests.get(source, headers=headers, verify=False, timeout=10)

            if resp.status_code != 200:
                raise Exception(f"Strona zwróciła kod błędu: {resp.status_code}")

            arr = np.frombuffer(resp.content, np.uint8)
            img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

            if img is None:
                raise Exception("Pobrano dane, ale to nie jest poprawne zdjęcie.")
        else:
            img = cv2.imread(source)
            if img is None:
                raise Exception("Nie znaleziono pliku na dysku lub jest uszkodzony.")

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
        boxes, _ = hog.detectMultiScale(img, winStride=(8, 8), padding=(8, 8), scale=1.05)

        jobs[jid] = {"status": "done", "count": len(boxes), "msg": "Sukces"}
        print(f"Sukces ID: {jid}, liczba: {len(boxes)}")

    except Exception as e:
        error_msg = str(e)
        print(f"BŁĄD ID: {jid} -> {error_msg}")
        jobs[jid] = {"status": "error", "msg": error_msg}


@app.get("/local")
def local_file(path: str, bg: BackgroundTasks):
    jid = str(uuid.uuid4())
    jobs[jid] = {"status": "pending"}
    bg.add_task(detect, jid, path, False)
    return {"id": jid}


@app.get("/url")
def web_file(url: str, bg: BackgroundTasks):
    jid = str(uuid.uuid4())
    jobs[jid] = {"status": "pending"}
    bg.add_task(detect, jid, url, True)
    return {"id": jid}


@app.get("/status/{jid}")
def check_status(jid: str):
    return jobs.get(jid, {"status": "not found"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)