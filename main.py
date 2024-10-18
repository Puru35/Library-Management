from fastapi import FastAPI
from pydantic import BaseModel
from typing import List #, Optional

app = FastAPI()

class Book(BaseModel):
    title: str
    id: int
    author: str
    description: str | None = None # description: Optional[str] = None

books = []

@app.get("/books/")
def initial():
    """
    Initial homepage message
    """
    return {"message": "Welcome to the Bookstore!"}

@app.post("/books/add/", response_model=Book)
def add_book(book: Book):
    """
    Add a new book to the bookstore
    """
    books.append(book)
    return books

@app.get("books/all/", response_model=List[Book])
def get_books():
    """
    Get all books in the bookstore
    """
    return books

@app.get("/books/{book_id}/", response_model=Book)
def get_book(book_id: int):
    """
    Get a book by its ID
    """
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found!"}

@app.put("/books/{book_id}/", response_model=Book)
def update_book(book_id: int, book: Book):
    """
    Update a book by its ID, given another book object
    """
    for index, item in enumerate(books):
        if item.id == book_id:
            books[index] = book
            return book
    return {"error": "Book not found!"}

@app.delete("/books/{book_id}/")
def delete_book(book_id: int):
    """
    Delete a book by its ID
    """
    global books
    books = [book for book in books if book.id != book_id]
    return {"message": "Book deleted successfully!"}

# Run the app

# uvicorn main:app --reload

# to view the developer docs for this app, visit http://127.0.0.1:8000/docs or http://http://127.0.0.1:8000/redoc