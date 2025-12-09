import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

if not firebase_admin._apps:
    cred = credentials.Certificate("pizza-app-dd667-firebase-adminsdk-fbsvc-84ec5cecdb.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("public/index.html")

@app.get("/api/restaurants")
async def zeig_restaurants():
    docs = db.collection("restaurants").stream()

    restaurants = []
    
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        restaurants.append(item)

    return {"restaurants": restaurants}

@app.get("/api/restaurants/{restaurant_id}/speisekarte")
async def zeig_restaurants_speisekarte(restaurant_id):
    docs = db.collection("restaurants").document(restaurant_id).collection("speisekarte").stream()

    speisekarte = []
    
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        speisekarte.append(item)

    return {"speisekarte": speisekarte}

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