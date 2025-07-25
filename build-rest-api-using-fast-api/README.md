# REST API in Python using FastAPI Demo App

This is a demonstration application for creating and running a REST API in Python using FastAPI.

## Tech Stack

- Python v3.13.2
- FastAPI (latest as for 2025-07-07)
- uvicorn (latest as for 2025-07-07)
- VS Code

## SETUP

### PREREQUISITES

You need to have Python installed on your machine. There are many guide videos and documentation on how to do that on different operating systems.

Simply type "download and install Python on Windows 11" (replace "Windows 11" with your operating system) and follow the instructions.

### INSTALLING `FastAPI` AND `uvicorn`

Open an PowerShell or command-line terminal and install `FastAPI` and `uvicorn` using the following commands:

```powershell title="PowerShell"
pip install fastapi
pip install uvicorn
pip install pydantic
```

OR in a single command: `pip install fastapi uvicorn pydantic`.

## CREATE THE APPLICATION

Create a folder for the application, for example, _build-rest-api-using-fast-api_.

Inside the folder create a file `main.py` or any other name for your application.

In the file `main.py` paste the following code:

```python title="Python"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
   return { "Hello": "World" }
```

Go back to the terminal can run your application using the command 

```powershell
python -m uvicorn main:app --reload
```

- `python` to run your Python program, without it your system will look for `uvicorn` in the `PATH` environment variable.
- `uvicorn` a Python package that allow you to run a Python program as a server.
- `main` your file name `main.py`, if you are using another name then write the filename without the `.py` extension.
- `app` the variable name of your application inside the `main.py` file (line 3 in the example code).

If you get an error running the application it's possible that you either don't have Python installed, you didn't setup the PATH environment variable, or something similar.

Resolve your issue and continue.

## TEST YOUR APPLICATION RUNNING

Open a browser and navigate to `localhost:8000` or `127.0.0.1:8000`. You should get and see something similar to the following:

```json title="JSON"
{
  "Hello": "World"
}
```

## CREATING ROUTES

This demo app will be for a TO-DO list. In the file `main.py` I add:

1. An array `items` which will be a global array.
2. A POST endpoint To add TO-DO task to the list, with path `/items` and the function with the following signature: `create_item(item : str)`. The `item` parameter is a query parameter.

Use the following command in the terminal to make the post request:

```PowerShell title="PowerShell"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items?item=apple"
```

Note that you need to add the parameter as a query-parameter (?) and to add the parameter name ("item") and the value separated by an equal (=) sign.

You should receive `"apple"` as a response.

Then we can add another item using the same cURL command with a little modification:

```powershell title="PowerShell"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items?item=orange"
```

Add a GET endpoint to retrieve all the items, with path `/items` and a function with the following signature: `get_all()`. Don't worry that you have the same path as the POST request, its perfectly legal as long as they have something different, such as Path (URL) parameters, HTTP method, etc.

Run again the 2 cURL commands to add "apple" and "orange" to the `items` array (since we added code the server/app was reloaded and all data reset). Then run the following cURL command to get the items list:

````powershell title="PowerShell"
curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items"
```.

You should get a response `["apple", "orange"]` if you called "apple" first and then "orange".

Add an endpoint to retrieve a specific item by id (the index of the item in the `items` array), and a function with the following signature: `get_by_id(item_id: int) -> str`. This signature means the function name is "get_by_id", it receives a parameters `item_id` of type integer and returns a string.

To test the endpoints we need to again add the items "apple" and "orange", the send the GET BY ID request to get the specific item use the following command:

```powershell title="PowerShell"
curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items/0"
curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items/1"
curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items/777"
````

**IMPORTANT:** Remember that in the array the first item has the index (id) 0, the 2nd item id is 1, etc. To send the GET request.

We will get "apple" for the first API GET request call and "orange" for the second.
for the third API GET request we will get "Internal Server Error".

When a user receives such an error it's not good, UX wise.

Next we will raise errors properly.

## RAISING ERRORS

There's a universal standard for [HTTP Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status). Each group, or range, or status codes has a purpose and a specific general reason that we can use and everyone will understand, e.g., client error (4xx), redirect (3xx), success (2xx), etc.

In our case, we called a GET request with an id `777` which doesn't exists in the array. This is a client error in the 4xx family of status codes. We will open the page in the link and navigate the [4. Client error responses (400 – 499)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#client_error_responses), and scroll until we see "404 Note Found", this code is what we want to return in this case, to signal to the user that an item with the given id was not in the array.

We will go to the `main.py` program and add `HTTPException` to import it from `fastapi`, the updated code will look as follow:

```python title="Python"
from fastapi import FastAPI, HTTPException
```

And then down in the handler function `get_by_id(item_id: int) -> str` we will add a condition to check if the id exists and return it, or raise status code 404 with a suitable message:

```python title="Python"
@app.get("/items/{item_id}")
def get_by_id(item_id: int) -> str:
   if item_id < len(items):
      return items[item_id]
   else:
      raise HTTPException(status_code=404, detail="Item not found")
```

Now, let's go back to our terminal, the program was reloaded thus we need to insert our items again, and then call the GET request with the id of `777` and check the response from the server. We should get a response similar to the following:

```json title="JSON"
{ "detail": "Item not found" }
```

We can also determine the response content and populate it with the data we want, let's do a simple example.

- We will import `JSONResponse` from `fastapi.responses`.
- We will duplication the handler function `get_by_id(item_id: int) -> str`.
  - Change the path to `'/items/id/{item_id}'`.
  - Change the code to return `JSONResponse` and the desired content.

```python title="Python"
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
```

Then test the returned error by executing the following cURL command:

```powershell title="PowerShell"
curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items/id/777"
```

Python will navigate the the correct function name, by the URL path although there are 2 functions with the same name and signature in the file. We should get a response as the following JSON object:

```json title="JSON"
{ "status": 404, "detail": "Item not fount" }
```

## REQUEST AND PATH PARAMETERS

We will create another function handler with the signature `list_items(limit: int = 10)` and path `"/list-items"`:

```python
@app.get("/list-items")
def list_items(limit: int = 10):

   return items[0:limit]
```

Run the program again, this time create more than 10 items:

```powershell
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=apple"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=orange"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=banana"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=peach"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=date"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=grape"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items?item=watermelon"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=melon"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=grapefruit"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=pineapple"
curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items/query?item=coconut"
```

Check the full list of items, the array should be 11 items:) `curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items"`.

Run the following command in PowerShell the get 10 items (without the coconut) as the default limit value is 10:

```powershell
curl.exe -X GET "http://localhost:8000/list-items"
```

Run the following command to get the first 3 items:

```powershell
curl.exe -X GET "http://localhost:8000/list-items?limit=3"
```

## MORE COMPLEX DATA-STRUCTURE -- USING PYDANTIC `BaseModel`

If we want to build a TO-DO list application then the `item` and `items` must be a more complex data structure than just a string. Luckily, FastAPI also supports py models which allow us to structure our data and also provide additional validation. This makes testing, documentation, and code completion a lot easier.

First let's import the `BaseModel` from `pydantic` at the top of the file.

```python
from pydantic import BaseModel
```

We will define the `Item` class in the "main.py" file right after the `app = FastAPI()`:

```python
class Item(BaseModel):
   text: str = None
   is_done: bool = False
```

Now, we will update the application to use the `Item` module. For example in the POST request endpoint, instead of receiving `def create_item(item: str)` we can change it to `def create_item(item: Item)`, and in the GET request endpoint instead of returning a string we can return the `Item` model:

We will also add a POST endpoint to add multiple items to the `items` list using the `pydantic` model and a `JSONArray` in the POST request payload.

```python
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

# http://localhost:8000/items/{item_id}
@app.get("/items/{item_id}")
def get_by_id(item_id: int) -> str:
   print(f"item id is {item_id}")
   if item_id < len(items):
      return items[item_id]
   else:
      raise HTTPException(status_code=404, detail="Item not found")
```

If we try to use the same cURL request to create the a new item, it will not going to work because we specified the item as a query parameter, and when we use a modeled object like `Item` as part of the argument, it's going to expect that to be in the JSON payload of the request. 

To make it work we need to send the `Item` data as a JSON payload instead of specifying a query parameter. We add the `Item` data with the `-d` switch and remove the query parameter. The cURL command will look as follow:

```powershell
curl.exe -X POST -H "Content-Type: application/json" -d '{"text": "apple"}' "http://localhost:8000/items"
```

OR

```powershell
curl.exe -X POST --url http://localhost:8000/items -H 'Content-Type: application/json' --data '{"text":"Orange"}'
```

## RESPONSE MODELS / MODEL THE RESPONSE

We will use the same `pydantic` model and add a new argument `response_model` to the decorator.

- To return a single Item class just put the class you want to return in the response, e.g.,  `response_model=Item`.
- To return a list of classes just put `list[class-name]`, e.g., `response_model=list[Item]`.

```python
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
```

## INTERACTIVE DOCUMENTATION

FastAPI supports Swagger (OpenAPI 3.0) documentation standard. When using FastAPI, add `/docs#` to your application URL base and you will be able to see it. For example, for the `main.py` file the URL to the Swagger-UI page will be `http://localhost:8000/docs#`.

In the Swagger-UI page you can click "Try it Out" on every request and test it.

**Note:** If you add `/redoc` instead of `/docs#` you will get another set of documentation. It looks the same as Swagger-UI. Choose which ever one you prefer.

## FASTAPI VS. FLASK

- FastAPI is Async by default you can get much more concurrent requests right out of the box.
- FastAPI is easier to use.
- FastAPI is new, but gaining popularity quickly.
- Flask has higher adoption (more people/developers use it), it's an Open Source project with community support.