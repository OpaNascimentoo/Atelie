from backend.app import create_app


def test_app_creates_and_exposes_health_and_pedidos():
    app = create_app()
    client = app.test_client()

    health = client.get('/api/health')
    assert health.status_code == 200
    assert health.json['status'] == 'ok'

    pedidos = client.get('/api/pedidos')
    assert pedidos.status_code == 200
    assert isinstance(pedidos.json, list)
    assert len(pedidos.json) > 0


def test_crud_endpoints_for_clientes_produtos_encomendas_and_doacoes():
    app = create_app()
    client = app.test_client()

    novo_cliente = client.post('/api/clientes', json={
        'nome': 'Cliente Teste CRUD',
        'telefone': '(11) 98888-7777',
        'email': 'teste.crud@email.com',
        'endereco': 'Rua de Teste, 99',
        'status': 'Ativa',
    })
    assert novo_cliente.status_code == 201
    cliente_id = novo_cliente.json['id']

    atualizado = client.put(f'/api/clientes/{cliente_id}', json={'status': 'Em avaliação'})
    assert atualizado.status_code == 200
    assert atualizado.json['status'] == 'Em avaliação'

    novo_produto = client.post('/api/produtos', json={
        'nome': 'Produto Teste CRUD',
        'categoria': 'Vestidos',
        'preco': 45.5,
        'disponibilidade': 'Disponível',
        'imagem': '/imagens/Vitrine/Vestido_aurora.jpeg',
        'material': 'Algodão',
        'reaproveitado': False,
    })
    assert novo_produto.status_code == 201
    produto_id = novo_produto.json['id']

    produto_edit = client.put(f'/api/produtos/{produto_id}', json={'disponibilidade': 'Reservado'})
    assert produto_edit.status_code == 200
    assert produto_edit.json['disponibilidade'] == 'Reservado'

    nova_encomenda = client.post('/api/encomendas', json={
        'cliente': 'Cliente Teste CRUD',
        'produto': 'Produto Teste CRUD',
        'quantidade': 2,
        'valor_unitario': 45.5,
        'valor_total': 91.0,
        'status': 'Recebida',
        'observacao': 'Teste CRUD',
    })
    assert nova_encomenda.status_code == 201
    encomenda_id = nova_encomenda.json['id']

    encomenda_update = client.put(f'/api/encomendas/{encomenda_id}', json={'status': 'Confirmada'})
    assert encomenda_update.status_code == 200
    assert encomenda_update.json['status'] == 'Confirmada'

    nova_doacao = client.post('/api/doacoes', json={
        'nome': 'Doador Teste CRUD',
        'tipo_peca': 'Camisa',
        'descricao': 'Peça de teste',
        'estado_peca': 'Bom',
        'status': 'Recebida',
        'imagem': '/imagens/dashboards/Camiseta.jpeg',
    })
    assert nova_doacao.status_code == 201
    doacao_id = nova_doacao.json['id']

    doacao_update = client.put(f'/api/doacoes/{doacao_id}', json={'status': 'Em avaliação'})
    assert doacao_update.status_code == 200
    assert doacao_update.json['status'] == 'Em avaliação'

    assert client.delete(f'/api/doacoes/{doacao_id}').status_code == 200
    assert client.delete(f'/api/encomendas/{encomenda_id}').status_code == 200
    assert client.delete(f'/api/produtos/{produto_id}').status_code == 200
    assert client.delete(f'/api/clientes/{cliente_id}').status_code == 200
