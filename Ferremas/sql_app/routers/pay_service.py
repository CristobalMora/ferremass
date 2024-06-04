from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..auth import get_current_user
from ..webpay_client import create_transaction, commit_transaction

router = APIRouter()

@router.post("/initiate", response_model=dict)
def initiate_payment(amount: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    buy_order = f"{current_user.id}-{amount}"
    session_id = f"{current_user.id}-{amount}"
    return_url = "http://localhost:8000/pay-service/return"  # URL de retorno en modo de pruebas

    response = create_transaction(amount, session_id, buy_order, return_url)
    if not response:
        raise HTTPException(status_code=400, detail="Payment initiation failed")

    return {
        "token": response['token'],
        "url": response['url']
    }

@router.post("/return", response_model=dict)
async def commit_payment(request: Request, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    form = await request.form()
    token = form.get('token_ws')
    if not token:
        raise HTTPException(status_code=400, detail="No token provided")

    response = commit_transaction(token)
    if not response:
        raise HTTPException(status_code=400, detail="Payment confirmation failed")

    return {
        "status": response.status,
        "amount": response.amount,
        "buy_order": response.buy_order,
        "transaction_date": response.transaction_date
    }
