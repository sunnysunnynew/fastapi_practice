from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 데이터 모델
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# PATCH 용도: 일부 필드만 들어올 수 있게
class UpdateItem(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

# 임시 저장소 (메모리 기반)
fake_db = {}

# GET: 아이템 조회
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fake_db.get(item_id)
    if item:
        return item
    return {"error": "Item not found"}

# POST: 아이템 생성
@app.post("/items/")
def create_item(item_id: int, item: Item):
    fake_db[item_id] = item
    return {"message": "Item created", "item": item}

# PUT: 아이템 수정 (전체)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        return {"error": "Item not found"}
    fake_db[item_id] = item
    return {"message": "Item updated", "item": item}
# patch : 아이템 일부 수정
@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, item: UpdateItem):
    stored_item = fake_db.get(item_id)
    if not stored_item:
        return {"error": "Item not found"}

    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item.copy(update=update_data)
    fake_db[item_id] = updated_item
    return {"message": "Item updated", "item": updated_item}

# DELETE: 아이템 삭제
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"message": f"Item {item_id} deleted"}
    return {"error": "Item not found"}
