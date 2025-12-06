import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


