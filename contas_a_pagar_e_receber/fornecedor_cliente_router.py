
from fastapi import HTTPException
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from shared.exceptions import NotFound
from contas_a_pagar_e_receber.models.fornecedor_cliente_model import FornecedorCliente

router = APIRouter(prefix="/fornecedor_cliente",)

class FornecedorClienteResponse(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True


class FornecedorClienteRequest(BaseModel):
    nome: str = Field(min_length=1, max_length=255)



@router.get("", response_model=List[FornecedorClienteResponse])
def todos_fornecedor_clientes(db: Session = Depends(get_db)):
    fornecedores = db.query(FornecedorCliente).all()
    return fornecedores


@router.get("/{id}", response_model=FornecedorClienteResponse)
def exibir_fornecedor(id: int, db: Session = Depends(get_db)):
    fornecedor = db.query(FornecedorCliente).get(id)

    if fornecedor is None:
        raise NotFound("Fornecedor cliente")
    return  fornecedor


@router.post("", response_model=FornecedorClienteResponse, status_code=201)
def criar_fornecedor(fornecedor_request: FornecedorClienteRequest, db: Session = Depends(get_db)):

    fornecedor = FornecedorCliente(
        **fornecedor_request.dict()
    )

    db.add(fornecedor)
    db.commit()
    db.refresh(fornecedor)

    return  fornecedor






