import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

if not firebase_admin._apps:
    cred = credentials.Certificate("pizzabestellapp-c93b5-firebase-adminsdk-fbsvc-c6c715fabd.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("public/index.html")

app.mount("/", StaticFiles(directory="public"), name="static")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_delay=0.5,
        reload_includes=["*.py"],
        reload_excludes=["public/*"],
        log_level="debug",
        reload_dirs=["."],
    )