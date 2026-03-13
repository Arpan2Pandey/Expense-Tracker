from pydantic import BaseModel

class ExpenseCreate(BaseModel):

    title       : str
    amount      : float
    category    : str
    description : str | None = None