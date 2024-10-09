import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select, SQLModel
from db import get_session
from models.pigs import Pig
from models.wolves import Wolf
from models.houses import House

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Little Pigs, Little Pigs, Let Me In!"}

def create_generic(model):
    def create(item: model, session: Session = Depends(get_session)):
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    return create

def read_generic(model):
    def read(item_id: int, session: Session = Depends(get_session)):
        return session.get(model, item_id)
    return read

def update_generic(model):
    def update(item_id: int, item: model, session: Session = Depends(get_session)):
        db_item = session.get(model, item_id)
        if db_item:
            item_data = item.model_dump(exclude_unset=True)
            for key, value in item_data.items():
                setattr(db_item, key, value)
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item
        return {"error": f"{model.__name__} with id {item_id} not found"}
    return update

def delete_generic(model):
    def delete(item_id: int, session: Session = Depends(get_session)):
        item = session.get(model, item_id)
        if item:
            session.delete(item)
            session.commit()
        return {"ok": True}
    return delete

# Pig CRUD
app.post("/pigs/")(create_generic(Pig))
app.get("/pigs/{item_id}")(read_generic(Pig))
app.put("/pigs/{item_id}")(update_generic(Pig))
app.delete("/pigs/{item_id}")(delete_generic(Pig))

# Wolf CRUD
app.post("/wolves/")(create_generic(Wolf))
app.get("/wolves/{item_id}")(read_generic(Wolf))
app.put("/wolves/{item_id}")(update_generic(Wolf))
app.delete("/wolves/{item_id}")(delete_generic(Wolf))

# House CRUD
app.post("/houses/")(create_generic(House))
app.get("/houses/{item_id}")(read_generic(House))
app.put("/houses/{item_id}")(update_generic(House))
app.delete("/houses/{item_id}")(delete_generic(House))