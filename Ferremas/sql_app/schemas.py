from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    title: str
    description: str
    category: str
    price: float

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    quantity: int

class CartItemCreate(CartItemBase):
    item_id: int

class CartItem(CartItemBase):
    id: int
    user_id: int
    item_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
