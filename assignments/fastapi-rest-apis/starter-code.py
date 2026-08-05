"""Starter code para a assignment Building REST APIs with FastAPI."""

from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Building REST APIs with FastAPI")


class ItemInput(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    done: bool = False


class Item(ItemInput):
    id: int


# Armazenamento em memoria para fins educacionais.
items: Dict[int, Item] = {}
next_id = 1


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to your FastAPI assignment API!"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/items", status_code=201)
def create_item(payload: ItemInput) -> Item:
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item


@app.get("/items")
def list_items() -> list[Item]:
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, payload: ItemInput) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **payload.model_dump())
    items[item_id] = updated
    return updated


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
