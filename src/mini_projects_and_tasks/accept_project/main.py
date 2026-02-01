from fastapi import FastAPI,HTTPException,Request,Response
from fastapi.responses import JSONResponse
import re
from api_versions.products.v1_models import ProductV1
from api_versions.products.v2_models import ProductV2

app = FastAPI()

def get_api_version_from_accept(accept_header : str | None):
    if not accept_header:
        return None
    match = re.search(r'application/vnd\.mycompany\.v(\d+)\+json',accept_header)
    if match:
        return match.group(1)
    return None

@app.get("/products/")
async def get_products(request : Request) -> Response:
    accept_header = request.headers.get("accept")
    requested_version = get_api_version_from_accept(accept_header)
    if not requested_version:
        raise HTTPException(status_code=406,detail="Not Acceptable. Please specify a supported API version in the Accept header (e.g., Accept: application/vnd.mycompany.v1+json).")
    if requested_version == "1":
        products_data_v1 = [
            ProductV1(id=1, name="Laptop Basic", price=1200.0),
            ProductV1(id=2, name="Mouse Wireless", price=25.0)
        ]
        return JSONResponse(
            content=[p.model_dump() for p in products_data_v1],
            media_type="application/vnd.mycompany.v1+json"
        )
    elif requested_version == "2":
        products_data_v2 = [
            ProductV2(product_id="LPT001", product_name="Super Laptop Pro", current_price=1800.0,currency="USD", description="High-performance laptop for professionals."),
            ProductV2(product_id="MOU005", product_name="Ergo Mouse Elite", current_price=45.0,currency="EUR", description="Ergonomic mouse with customizable buttons.")
        ]
        return JSONResponse(
            content=[p.model_dump() for p in products_data_v2],
            media_type="application/vnd.mycompany.v2+json"
        )
    else:
        raise HTTPException(status_code=400, detail=f"API Version {requested_version} is not supported for this resource.")
    

@app.get("/")
async def root():
    return {
        "message": "Welcome to Content Negotiation Versioning Example! Check /docs for details."}