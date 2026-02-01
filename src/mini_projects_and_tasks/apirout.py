from fastapi import FastAPI,Request,Response
from fastapi.routing import APIRoute,APIRouter

class CustomHeaderRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()  
        async def custom_route_handler(request : Request) -> Response:
            response : Response = await original_route_handler(request)
            response.headers["X_Custom_Header"] = "Hello from Cusstom Route!"
            return response
        return custom_route_handler

class CustomRouter(APIRouter):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,route_class=CustomHeaderRoute,**kwargs)

app = FastAPI()
custom_router = CustomRouter()

@custom_router.get("/items")
async def read_item_with_custom_header():
    return {"message": "Reading items with custom header via CustomRouter."}

app.include_router(custom_router)

@app.get("/users")
async def read_users():
    return {"message": "Reading users (no custom header)."}
