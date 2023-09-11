from fastapi import FastAPI, HTTPException
import json
from typing import Union

app = FastAPI()

# Load data from the JSON file
with open("data.json") as f:
    data = json.load(f)

@app.get("/")
def read_root():
    return {"Welcome to Moshe's Book API"}

@app.get("/authors/{author_id}")
def find_author(author_id: int):
    if author_id < 0 or author_id >= len(data["authors"]):
        raise HTTPException(status_code=404, detail="Author not found")
    
    author = data["authors"][author_id]
    return author

@app.get("/books/{book_name}")
def find_book(book_name: str):
    for author in data["authors"]:
        if book_name in author["books"]:
            return author
    raise HTTPException(status_code=404, detail="Book not found")

