from fastapi import FastAPI, Depends, Path
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException

# Import local modules
from . import models
from .schemas import UserCreate, UserOut, SubscriptionCreate, SubscriptionOut
from .database import engine, SessionLocal

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app instance
app = FastAPI(title="Subscription Service")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------
# User Endpoints
# ----------------------
@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ----------------------
# Subscription Endpoints
# ----------------------
@app.post("/subscriptions", response_model=SubscriptionOut)
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    #check if user exists first
    user = db.query(models.User).filter(models.User.id == subscription.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if user already has an active subscription with the same plan
    existing = db.query(models.Subscription).filter(
        models.Subscription.user_id == subscription.user_id,
        models.Subscription.plan == subscription.plan,
        models.Subscription.active == True
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="User already has an active subscription for this plan")

    # Create new subscription
    db_subscription = models.Subscription(
        user_id=subscription.user_id,
        plan=subscription.plan
    )
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


@app.get("/users/{user_id}/subscriptions", response_model=List[SubscriptionOut])
def get_user_subscriptions(user_id: int, db: Session = Depends(get_db)):
    # Step 1: Verify the user exists
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Step 2: Query all subscriptions for this user
    subscriptions = db.query(models.Subscription).filter(models.Subscription.user_id == user_id).all()

    # Step 3: Return the list of subscriptions
    return subscriptions

@app.patch("/subscriptions/{subscription_id}", response_model=SubscriptionOut)
def update_subscription(
    subscription_id: int = Path(..., description="ID of the subscription to update"),
    active: bool = True,  # Default to True; can set False to cancel
    db: Session = Depends(get_db)
):
    # Step 1: Find the subscription and error if not
    subscription = db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    # Step 2: Update the active status
    subscription.active = active
    db.commit()
    db.refresh(subscription)

    # Step 3: Return updated subscription
    return subscription