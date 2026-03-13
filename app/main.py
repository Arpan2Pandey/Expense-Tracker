import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .database import engine, Base
from .routes.expense_routes import router
from .models import expense

app = FastAPI()

# ─── CORS ──────────────────────────────────────────────────────
# Allows browser to talk to FastAPI without being blocked
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── DATABASE ──────────────────────────────────────────────────
# Creates tables in PostgreSQL if they don't exist yet
Base.metadata.create_all(bind=engine)

# ─── ROUTES ────────────────────────────────────────────────────
# All /expenses routes come from expense_routes.py
app.include_router(router)

# ─── SERVE FRONTEND ────────────────────────────────────────────
# BASE_DIR = the folder where main.py lives (i.e. app/)
# We go one level up (..) to find the frontend/ folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/ui", StaticFiles(directory=os.path.join(BASE_DIR, "..", "frontend"), html=True), name="frontend")

@app.get("/")
def home():
    return {"message": "Expense Tracker API running"}