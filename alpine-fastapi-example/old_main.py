from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = [
    {"id": 1, "name": "Buy milk"},
    {"id": 2, "name": "Read book"}
]
