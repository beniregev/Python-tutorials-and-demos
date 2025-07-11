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

