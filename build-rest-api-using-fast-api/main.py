from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
   text: str
   is_done: bool = False


items = []

@app.get("/")
def root():
   return { "Hello": "World" }

@app.get("/items")
def get_all():
   return items

# http://localhost:8000/items/{item_id}
@app.get("/items/{item_id}")
def get_by_id(item_id: int) -> str:
   print(f"item id is {item_id}")
   if item_id < len(items):
      return items[item_id]
   else:
      raise HTTPException(status_code=404, detail="Item not found")

# http://localhost:8000/items/id/{item_id}
@app.get("/items/id/{item_id}", response_model=Item)
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
      
# return up-to LIMIT number of items (10 items by default)
# http://localhost:8000/list-items
@app.get("/list-items", response_model=list[Item])
def list_items(limit: int = 10):
   return items[0:limit]
   
# http://localhost:8000/items/query?item=item_name
@app.post('/items/query')
def create_item(item: str):
   items.append(item)
   return item

# http://localhost:8000/items/string/{item-name}
@app.post('/items/string/{item_name}')
def create_item(item_name: str):
   items.append(item_name)
   return item_name

# http://localhost:8000/items/model
@app.post('/items/model')
def create_item(item: Item):
   items.append(item)
   return item

# http://localhost:8000/items/list-model
@app.post('/items/list-model')
def create_items(list_items: List[Item]):   # Notice the "List[Item]"
   items.extend(list_items) # list1.extend(list2) ==> Add the items of list2 into list1
   return list_items
