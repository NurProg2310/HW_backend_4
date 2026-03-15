from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from models.book import Book

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/books", response_class=HTMLResponse)
async def books_list(request: Request, page: int = 1):
    per_page = 10
    books = Book.get_all()

    total_books = len(books)
    total_pages = (total_books + per_page - 1) // per_page

    if page < 1:
        page = 1
    if total_pages > 0 and page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page
    books_on_page = books[start:end]

    return templates.TemplateResponse(
        "books/list.html",
        {
            "request": request,
            "books": books_on_page,
            "page": page,
            "total_pages": total_pages,
        }
    )


@router.get("/books/new", response_class=HTMLResponse)
async def new_book_form(request: Request):
    return templates.TemplateResponse(
        "books/new.html",
        {"request": request}
    )


@router.post("/books")
async def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    total_pages: int = Form(...),
    genre: str = Form(...)
):
    book = Book(
        id=Book.next_id(),
        title=title,
        author=author,
        year=year,
        total_pages=total_pages,
        genre=genre
    )
    book.save()

    return RedirectResponse(url="/books", status_code=303)


@router.get("/books/{book_id}", response_class=HTMLResponse)
async def book_detail(request: Request, book_id: int):
    book = Book.get_by_id(book_id)

    if not book:
        return PlainTextResponse("Not Found", status_code=404)

    return templates.TemplateResponse(
        "books/detail.html",
        {
            "request": request,
            "book": book
        }
    )