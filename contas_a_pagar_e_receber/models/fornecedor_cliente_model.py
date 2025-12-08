
from sqlalchemy import Column, Integer, Numeric, String
from shared.database import Base
from sqlalchemy.orm import relationship


class FornecedorCliente(Base):
    __tablename__ = "fornecedor_cliente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255))

    contas = relationship("ContaPagarReceber", back_populates="fornecedor")

