from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class SubscriptionCreate(BaseModel):
    user_id: int
    plan: str

class SubscriptionOut(BaseModel):
    id: int
    user_id: int
    plan: str
    active: bool

    class Config:
        from_attributes = True
