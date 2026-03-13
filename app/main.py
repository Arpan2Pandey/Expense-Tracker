from fastapi import FastAPI

from .database import engine, Base
from .routes.expense_routes import router
from .models import expense


app = FastAPI()


# Create database tables
Base.metadata.create_all(bind=engine)


# Register routes
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Expense Tracker API running"}