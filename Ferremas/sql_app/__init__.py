from .database import Base, engine
from .models import User, Item, CartItem

Base.metadata.create_all(bind=engine)
