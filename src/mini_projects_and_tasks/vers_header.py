from fastapi import FastAPI,APIRouter,HTTPException,Header,Depends

app = FastAPI()
note_router = APIRouter(prefix="/api/notes")

def get_apy_version(version : str = Header(None)):
    if version == "1":
        return "v1"
    elif version == "2":
        return "v2"
    raise HTTPException(status_code=400, detail="Invalid or missing API version")

@note_router.get("/",tags=["Notes"])
async def endpoint1(version : str = Depends(get_apy_version)):
    if version == "v1":
        return "Notes in v1: Note 1, Note 2"
    elif version == "v2":
        return  "Notes in v2: Note 1 (draft), Note 2 (published)"

@note_router.get("/{note_id}",tags=["Notes"])
async def endpoint2(note_id : int,version : str = Depends(get_apy_version)):
    if note_id  != int(note_id) or note_id < 0:
        raise HTTPException(status_code=400, detail="Invalid note ID")
    if version == "v1":
        return f"Note {note_id} in v1"
    elif version == "v2":
        return f"Note {note_id} in v2 with status: draft"
    
@note_router.get("/count",tags=["Notes"])
async def endpoint3(version : str = Depends(get_apy_version)):
    if version == "v1":
        raise HTTPException(status_code=400,detail='Invalid or missing API version')
    elif version == "v2":
        return "Total notes in v2: 2"

app.include_router(note_router)