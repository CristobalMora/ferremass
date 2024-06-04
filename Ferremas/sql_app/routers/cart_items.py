from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter()

@router.get("/", response_model=list[schemas.CartItem])
def read_cart_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    cart_items = crud.get_cart_items(db, user_id=current_user.id, skip=skip, limit=limit)
    return cart_items

@router.post("/", response_model=schemas.CartItem)
def create_cart_item(cart_item: schemas.CartItemCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.create_cart_item(db=db, cart_item=cart_item, user_id=current_user.id)

@router.put("/{cart_item_id}", response_model=schemas.CartItem)
def update_cart_item(cart_item_id: int, cart_item: schemas.CartItemBase, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    updated_cart_item = crud.update_cart_item(db, cart_item_id=cart_item_id, cart_item=cart_item)
    if updated_cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return updated_cart_item

@router.delete("/{cart_item_id}", response_model=schemas.CartItem)
def delete_cart_item(cart_item_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    deleted_cart_item = crud.delete_cart_item(db, cart_item_id=cart_item_id)
    if deleted_cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return deleted_cart_item
