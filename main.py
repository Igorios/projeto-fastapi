
from fastapi import FastAPI
import uvicorn
from shared.exceptions_handler import not_found_exception_handle

from contas_a_pagar_e_receber import contas_a_pagar_e_receber_router

from shared.database import engine, Base
from contas_a_pagar_e_receber.models.contas_a_pagar_e_receber_model import ContaPagarReceber
from shared.exceptions import NotFound

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/ping")
def ping():
    return "pong"

app.include_router(contas_a_pagar_e_receber_router.router)
app.add_exception_handler(NotFound, not_found_exception_handle)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)