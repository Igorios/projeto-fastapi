
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

@router.get("", response_model=List[ContasPagarReceberResponse], status_code=200)
def listar_contas(db: Session = Depends(get_db)):
    contas = db.query(ContaPagarReceber).all()
    return contas

@router.get("/{id}", response_model=ContasPagarReceberResponse, status_code=200)
def exibir_conta(id: int, db: Session = Depends(get_db)):
    conta = db.query(ContaPagarReceber).get(id)
    return conta

    
@router.post("", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta_request: ContasPagarReceberResquest, db: Session = Depends(get_db)):

    conta = ContaPagarReceber(
        **conta_request.dict()
    ) 

    db.add(conta)
    db.commit()
    db.refresh(conta)

    return conta


@router.put("/{id}", response_model=ContasPagarReceberResponse, status_code=200)
def atualizar_conta(id: int, conta_a_pagar_receber_request: ContasPagarReceberResquest, db: Session = Depends(get_db)):

    conta = db.query(ContaPagarReceber).get(id)

    for campo, valor in conta_a_pagar_receber_request.dict().items():
        setattr(conta, campo, valor)

    db.commit()
    db.refresh(conta)
    return conta


@router.delete("/{id}", status_code=204)
def deletar_conta(id: int, db: Session = Depends(get_db)):
    conta = db.query(ContaPagarReceber).get(id)
    db.delete(conta)
    db.commit()
    return None

