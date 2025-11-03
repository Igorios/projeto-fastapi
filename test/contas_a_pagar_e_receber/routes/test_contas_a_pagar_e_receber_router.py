from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get("/contas_a_pagar_e_receber")
    assert response.status_code == 200

    assert response.json() == [
        {'id': 1, 'descricao': 'contas a pagar teste', 'valor': '2000.0', 'tipo': 'Pagar'}, 
        {'id': 2, 'descricao': 'contas a pagar teste', 'valor': '3000.0', 'tipo': 'Receber'}
    ]


def test_deve_criar_conta_a_pagar_e_receber():
    nova_conta = {
        "descricao": "TESTE",
        "valor": 235.5,
        "tipo": "PAGAR"
    }
    
    response = client.post("/contas_a_pagar_e_receber", json=nova_conta)
    assert response.status_code == 201
    assert response.json()
