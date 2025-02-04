from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is a test project for learning FastAPI and PyTest!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": a * b}

@app.get("/divide")
def divide_numbers(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}