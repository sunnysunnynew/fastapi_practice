# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # http://localhost:8080/items/?q=123/ items?q=123을 했을떄 왼쪽처럼 해서 dict items  밖에 q:123이 생김



# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # http://localhost:8080/items/?q=24214142142142141414141414141414141414444444444444444444444444444444444444444444444444444444444444444444444444444412313123131 q가 50자가 넘어가면 cfx : max_length = 50이라는 말이 나옴



from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# http://localhost:8080/items/?q=24214142142142141414141414141414141414444444444444444444444444444444444444444444444444444444444444444444444444444412313123131 
# 이떄는 message가 추가 됩니다. 

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results