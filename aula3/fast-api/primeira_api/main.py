from typing import Union, Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

'''Criar um db falso e endpoints de produtos e quantidade de produtos no estoque'''

db_estoque = []


class Item(BaseModel):
    id: int
    produto: str
    quantidade_estoque: int


@app.post("/estoque")
def add_item_estoque(item: Item):
    db_estoque.append(item)
    return item


@app.get("/estoque")
def listar_estoque():
    cont = 0
    for i in range(0, len(db_estoque)):
        cont += db_estoque[i].quantidade_estoque
    return db_estoque, cont

# class Item(BaseModel):
#     id: int
#     descricao: str
#     valor: float


# @app.post("/")
# def read_root(user_agent: Optional[str] = Header(None)):
#     return {"user_agent": user_agent}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/item")
# def add_item(novo_item: Item):
#     return novo_item
