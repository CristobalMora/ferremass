from fastapi import FastAPI
from sql_app.routers import users, items, auth as auth_router, cart_items, pay_service

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(auth_router.router, tags=["auth"])
app.include_router(cart_items.router, prefix="/cart-items", tags=["cart-items"])
app.include_router(pay_service.router, prefix="/pay-service", tags=["pay-service"])
