
from decimal import Decimal
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from contas_a_pagar_e_receber.models.contas_a_pagar_e_receber_model import ContaPagarReceber
from shared.dependencies import get_db


router = APIRouter(prefix="/contas_a_pagar_e_receber")

class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str

    class Config:
        orm_mode = True

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
    
    
@router.post("", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta_request: ContasPagarReceberResquest, db: Session = Depends(get_db)):

    conta = ContaPagarReceber(
        **conta_request.dict()
    ) 

    db.add(conta)
    db.commit()
    db.refresh(conta)

    return conta