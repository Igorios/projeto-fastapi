
from decimal import Decimal
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/contas_a_pagar_e_receber")

class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str

class ContasPagarReceberResquest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str

@router.get("", response_model=List[ContasPagarReceberResponse])
def listarContas():
    return [
        ContasPagarReceberResponse(
            id=1,
            descricao="contas a pagar teste",
            tipo="Pagar",
            valor=2000.00
        ),
        ContasPagarReceberResponse(
            id=2,
            descricao="contas a pagar teste",
            tipo="Receber",
            valor=3000.00
        ),
    ]
    
    
@router.post("", response_model=ContasPagarReceberResquest, status_code=201)
def criar_conta(conta: ContasPagarReceberResquest):
    return ContasPagarReceberResquest(
            id=3,
            descricao=conta.descricao,
            tipo=conta.tipo,
            valor=conta.valor
        )