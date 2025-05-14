from fastapi import FastAPI

app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 2):
#     return fake_items_db[skip : skip + limit]

# skip이 늘어나면 보이는 게 작아짐 여기선 3개니까 limit은 최대 3이 넘어가도 3개씩 나옴 


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# http://localhost:8080/items/라면?q="5600원" 이런식으로 가능하다

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# # http://localhost:8080/items/%EB%9D%BC%EB%A9%B4?short=true 일떄는 item만 나오고 false때는 description이 같이나온다. 아무것도 안넣고 q만 넣으면 item, q, description이 같이나온다

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# http://localhost:8080/users/123?q=123/items/123= q와 short는 모두 irems에 붙여야한다.
# http://localhost:8080/users/123/items/123?q=123&short=True 이렇게 쓰면 items, users, q만 나온다. short는 true 이기 떄문에


from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy 이런식으로 쓰면 잘나온다
