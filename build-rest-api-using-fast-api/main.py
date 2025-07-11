from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
   return { "Hello": "World" }

@app.get("/items")
def get_all():
   return items

@app.post('/items')
def create_item(item : str):
   items.append(item)
   return item
