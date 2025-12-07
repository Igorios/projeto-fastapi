from fastapi import Request
from fastapi.responses import JSONResponse

async def not_found_exception_handle(request: Request, exception):
    return JSONResponse(
        status_code=404,
        content={"message": f"Opps! {exception.name} não encontrado"},
    )