from fastapi import FastAPI
from pydantic import BaseModel
# request body를 정의를 할때 Pydantic과 함께 사용


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# post 방식으로 만들어서 누군가가 전달해주면 받는 post)

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# FastAPI는 자동적으로 함수의 파라미터에서 path로 부터 받은 것은 path 파라미터로 인식을 하고, Pydantic 모델로 선언된것은 request body로 인식함

# $ curl -X 'PUT' \
#   'http://localhost:8080/items/123' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "sunny",
#   "description": "412",
#   "price": 105.5,
#   "tax": 22
# }'

# put은 쉽게 생각하면 수정이라고 생각하면 되겠다. 
# {"item_id":123,"name":"sunny","description":"412","price":105.5,"tax":22.0} 이런식으로 받아진다