from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse 
from routes.books import router as books_router


app = FastAPI()

app.include_router(books_router)

@app.get("/")
async def root():
    return RedirectResponse(url="/books")
    

