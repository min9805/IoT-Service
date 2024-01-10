from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from app.config.database import create_tables
from app.domain.answer import answer_router
from app.domain.device import device_router
from app.domain.question import question_router
from app.domain.user import user_router


app = FastAPI()

origins = [
    "*",
    "http://127.0.0.1:5173",  # Svelte
    "http://localhost:3000",  # React
    "http://localhost:8000",  # React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.include_router(device_router.router)
app.mount("/assets", StaticFiles(directory="app/frontend/dist/assets"))

create_tables()

#@app.get("/")
#def index():
#    return FileResponse("app/frontend/dist/index.html")
