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

```powershell
pip install fastapi
pip install uvicorn
```

## CREATE THE APPLICATION

Create a folder for the application, for example, _build-rest-api-using-fast-api_.

Inside the folder create a file `main.py` or any other name for your application.

In the file `main.py` paste the following code:

``` py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
   return { "Hello": "World" }

```

Go back to the terminal can run your application using the command `python -m uvicorn main:app --reload`.

- `python` to run your Python program, without it your system will look for `uvicorn` in the `PATH` environment variable.
- `uvicorn` a Python package that allow you to run a Python program as a server.
- `main` your file name `main.py`, if you are using another name then write the filename without the `.py` extension.
- `app` the variable name of your application inside the `main.py` file (line 3 in the example code).

If you get an error running the application it's possible that you either don't have Python installed, you didn't setup the PATH environment variable, or something similar.

Resolve your issue and continue.

## TEST YOUR APPLICATION RUNNING

Open a browser and navigate to `localhost:8000` or `127.0.0.1:8000`. You should get and see something similar to the following:

```json
{
  "Hello": "World"
}
```

## CREATING ROUTES

This demo app will be for a TO-DO list. In the file `main.py` I add:

1. An array `items` which will be a global array.
2. A POST endpoint To add TO-DO task to the list, with path `/items` and the function with the following signature: `create_item(item : str)`. The `item` parameter is a query parameter.

Use the following command in the terminal to make the post request `curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items?item=apple"`. Note that you need to add the parameter as a query-parameter (?) and to add the parameter name ("item") and the value separated by an equal (=) sign.

You should receive `"apple"` as a response.

Then we can add another item using the same cURL command with a little modification: `curl.exe -X POST -H "Content-Type: application/json" "http://localhost:8000/items?item=orange"`.

Add a GET endpoint to retrieve all the items, with path `/items` and a function with the following signature: `get_all()`. Don't worry that you have the same path as the POST request, its perfectly legal as long as they have something different, such as Path (URL) parameters, HTTP method, etc.

Run again the 2 cURL commands to add "apple" and "orange" to the `items` array (since we added code the server/app was reloaded and all data reset). Then run the following cURL command to get the items list: `curl.exe -X GET -H "Content-Type: application/json" "http://localhost:8000/items"`. You should get a response `["apple", "orange"]` if you called "apple" first and then "orange".
