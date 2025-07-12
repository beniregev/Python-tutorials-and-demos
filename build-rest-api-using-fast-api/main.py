from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

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
   print(f"item id is {item_id}")
   if item_id < len(items):
      return items[item_id]
   else:
      raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/id/{item_id}")
def get_by_id(item_id: int) -> str:
   print(f"item id is {item_id}")
   if item_id < len(items):
      return items[item_id]
   else:
      return JSONResponse(
         status_code=404, 
         content={
            "status": 404,
            "detail": "Item not fount"
         }
      )

@app.post('/items')
def create_item(item : str):
   items.append(item)
   return item
