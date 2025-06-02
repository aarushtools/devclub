from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoItem(BaseModel):
    id: int
    name: str

todos = [
    {"id": 1, "name": "Buy milk"},
    {"id": 2, "name": "Read book"}
]

@app.get("/todos")
def get_todos():
    return todos

@app.post("/add_todo")
def add_todo(item: TodoItem):
    todos.append({"id": item.id, "name": item.name })

@app.post("/remove_todo")
def remove_todo(item: TodoItem):
    for index, value in enumerate(todos):
        if value["id"] == item.id and value["name"] == item.name:
            del todos[index]


@app.get("/")
def index():
    return FileResponse("static/index.html")
