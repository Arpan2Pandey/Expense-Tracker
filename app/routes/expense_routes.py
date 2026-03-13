from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import SessionLocal
from ..models.expense import Expense
from ..schemas.expense_schema import ExpenseCreate

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/expenses")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):

    new_expense = Expense(
        title       = expense.title,
        amount      = expense.amount,
        category    = expense.category,
        description = expense.description
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):

    expenses = db.query(Expense).all()

    return expenses


@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):

    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        return {"error": "Expense not found"}

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}


@router.get("/expenses/total")
def get_total_expense(db: Session = Depends(get_db)):

    total = db.query(func.sum(Expense.amount)).scalar()

    if total is None:
        total = 0

    return {"total_spent": total}