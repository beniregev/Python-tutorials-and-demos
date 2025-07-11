from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
   return { "Hello": "World" }

@app.get("/items")
def get_all():
   return items

@app.get("/items/{item_id}")
def get_by_id(item_id: int) -> str:
   item = items[item_id]
   return item

@app.post('/items')
def create_item(item : str):
   items.append(item)
   return item
