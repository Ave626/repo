from fastapi import FastAPI,APIRouter,HTTPException

app = FastAPI()
root_router1 = APIRouter()
root_router2 = APIRouter()

v1_router = APIRouter(prefix="/v1")

@v1_router.get("/tasks",tags=["v1 Tasks"])
async def _end():
    return "Tasks in v1: Task 1, Task 2"

@v1_router.get("/tasks/{task_id}", tags=["v1 Tasks"])
async def _end2(task_id : int):
    if task_id != int(task_id) or task_id <= 0:
        raise HTTPException(status_code=400,detail="Invalid task ID")
    return f"Task {task_id} in v1"

v2_router = APIRouter(prefix="/v2")

@v2_router.get("/tasks", tags=["v2 Tasks"])
async def _end():
    return "Tasks in v2: Task 1 (open), Task 2 (closed)"

@v2_router.get("/tasks/{task_id}", tags=["v2 Tasks"])
async def _end2(task_id : int):
    if task_id != int(task_id) or task_id <= 0:
        raise HTTPException(status_code=400,detail="Invalid task ID")
    return f"Task {task_id} in v2 with status: open"

@v2_router.get("/tasks/count", tags=["v2 Tasks"])
async def _end3():
    return "Total tasks in v2: 2"

root_router1.include_router(v1_router)
root_router2.include_router(v2_router)

app.include_router(root_router1,prefix="/api")
app.include_router(root_router2,prefix="/api")