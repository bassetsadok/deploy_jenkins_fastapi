from fastapi import FastAPI

from schema import Item

app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/")
def read_root():
    return {"Hello": "World"}
