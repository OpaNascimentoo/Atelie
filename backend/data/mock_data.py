PEDIDOS_INICIAIS = [
    {"id": 1, "cliente": "Ana Carolina Silva", "servico": "Ajuste de Vestido", "peca": "Vestido Social", "data": "18 Mai 2025", "horario": "09:00", "status": "Em Produção"},
    {"id": 2, "cliente": "Bruno Mendes", "servico": "Barra de Calça", "peca": "Calça Jeans", "data": "18 Mai 2025", "horario": "10:30", "status": "Agendado"},
    {"id": 3, "cliente": "Carla Ferreira", "servico": "Customização", "peca": "Jaqueta", "data": "18 Mai 2025", "horario": "11:00", "status": "Pronto para Prova"},
    {"id": 4, "cliente": "Daniel Souza", "servico": "Conserto", "peca": "Terno", "data": "19 Mai 2025", "horario": "14:00", "status": "Entregue"},
    {"id": 5, "cliente": "Fernanda Lima", "servico": "Ajuste de Vestido", "peca": "Vestido de Festa", "data": "20 Mai 2025", "horario": "10:00", "status": "Agendado"},
    {"id": 6, "cliente": "Gustavo Ramos", "servico": "Barra de Calça", "peca": "Calça Social", "data": "20 Mai 2025", "horario": "11:30", "status": "Em Produção"},
    {"id": 7, "cliente": "Helena Martins", "servico": "Modelagem", "peca": "Blusa sob Medida", "data": "15 Mai 2025", "horario": "09:30", "status": "Entregue"},
    {"id": 8, "cliente": "Igor Peixoto", "servico": "Customização", "peca": "Camiseta", "data": "14 Mai 2025", "horario": "14:00", "status": "Entregue"},
]

CLIENTES_INICIAIS = [
    {"id": 1, "nome": "Ana Carolina Silva", "telefone": "(11) 99988-1122", "email": "ana.silva@email.com", "endereco": "Rua das Flores, 123 - São Paulo/SP", "pedidos": 4, "ultimo_atendimento": "20/10/2026", "status": "Ativa"},
    {"id": 2, "nome": "Gustavo Ramos", "telefone": "(11) 98877-1100", "email": "gustavo.ramos@email.com", "endereco": "Av. Paulista, 510 - São Paulo/SP", "pedidos": 2, "ultimo_atendimento": "18/10/2026", "status": "Em produção"},
    {"id": 3, "nome": "Bruno Mendes", "telefone": "(11) 98441-2233", "email": "bruno.mendes@email.com", "endereco": "Rua do Comércio, 88 - São Paulo/SP", "pedidos": 3, "ultimo_atendimento": "21/10/2026", "status": "Ativa"},
    {"id": 4, "nome": "Fernanda Lima", "telefone": "(21) 98860-1001", "email": "fernanda.lima@email.com", "endereco": "Rua do Porto, 45 - Rio de Janeiro/RJ", "pedidos": 2, "ultimo_atendimento": "19/10/2026", "status": "Em avaliação"},
    {"id": 5, "nome": "Juliana Oliveira", "telefone": "(31) 98122-3344", "email": "juliana.oliveira@email.com", "endereco": "Av. Minas, 30 - Belo Horizonte/MG", "pedidos": 1, "ultimo_atendimento": "16/10/2026", "status": "Ativa"},
    {"id": 6, "nome": "Mariana Souza", "telefone": "(41) 98555-2100", "email": "mariana.souza@email.com", "endereco": "Rua da Lapa, 77 - Curitiba/PR", "pedidos": 3, "ultimo_atendimento": "22/10/2026", "status": "Ativa"},
    {"id": 7, "nome": "Rafael Martins", "telefone": "(51) 98770-4411", "email": "rafael.martins@email.com", "endereco": "Av. Beira Rio, 12 - Porto Alegre/RS", "pedidos": 2, "ultimo_atendimento": "17/10/2026", "status": "Em produção"},
    {"id": 8, "nome": "Camila Ferreira", "telefone": "(62) 99990-1234", "email": "camila.ferreira@email.com", "endereco": "Rua Nova, 94 - Goiânia/GO", "pedidos": 1, "ultimo_atendimento": "15/10/2026", "status": "Ativa"},
]

PRODUTOS_INICIAIS = [
    {"id": 1, "nome": "Vestido Aurora", "descricao": "Vestido confeccionado artesanalmente com caimento elegante e acabamento refinado.", "categoria": "Vestidos", "preco": 189.90, "disponibilidade": "Disponível", "imagem": "/imagens/Vitrine/Vestido_aurora.jpeg", "material": "Seda e cetim", "reaproveitado": False},
    {"id": 2, "nome": "Saia Bella", "descricao": "Saia midi com modelagem moderna e acabamento delicado para uso casual e eventos.", "categoria": "Saias", "preco": 119.90, "disponibilidade": "Disponível", "imagem": "/imagens/Vitrine/Saia_Bella.jpeg", "material": "Linho com detalhe em renda", "reaproveitado": False},
    {"id": 3, "nome": "Vestido Florença", "descricao": "Versão sofisticada para ocasiões especiais, com corte em linha e bordado discreto.", "categoria": "Vestidos", "preco": 229.90, "disponibilidade": "Reservado", "imagem": "/imagens/Vitrine/Vestido_Florença.jpeg", "material": "Cetim e microfibra", "reaproveitado": False},
    {"id": 4, "nome": "Camisa Serena", "descricao": "Camisa leve com caimento clean, ideal para composições minimalistas e formais.", "categoria": "Camisas", "preco": 99.90, "disponibilidade": "Disponível", "imagem": "/imagens/Vitrine/CamisaSerena.jpeg", "material": "Algodão premium", "reaproveitado": False},
    {"id": 5, "nome": "Bolsa Recria", "descricao": "Acessório feito com tecido reaproveitado, com identidade única e acabamento artesanal.", "categoria": "Acessórios", "preco": 89.90, "disponibilidade": "Disponível", "imagem": "/imagens/Vitrine/Bolsa%20Recria.jpeg", "material": "Tecido reaproveitado", "reaproveitado": True},
    {"id": 6, "nome": "Vestido Recomeço", "descricao": "Peça criada a partir de tecidos reaproveitados e transformados em uma nova proposta estilosa.", "categoria": "Vestidos", "preco": 199.90, "disponibilidade": "Disponível", "imagem": "/imagens/Vitrine/VestidoRecomeço.jpeg", "material": "Tecido reaproveitado", "reaproveitado": True},
    {"id": 7, "nome": "Blusa Atelier", "descricao": "Blusa com corte exclusivo, inspirada no universo da costura artesanal e de alta qualidade.", "categoria": "Blusas", "preco": 149.90, "disponibilidade": "Reservado", "imagem": "/imagens/Vitrine/BlusaAtelier.jpeg", "material": "Malha estruturada", "reaproveitado": False},
    {"id": 8, "nome": "Conjunto Lume", "descricao": "Conjunto elegante para eventos especiais com acabamentos detalhados e conforto.", "categoria": "Conjuntos", "preco": 279.90, "disponibilidade": "Disponível", "imagem": "/imagens/Vitrine/ConjuntoLume.jpeg", "material": "Linho e algodão", "reaproveitado": False},
]

ENCOMENDAS_INICIAIS = [
    {"id": 1, "numero": "#0001", "cliente": "Ana Carolina Silva", "produto": "Vestido Aurora", "quantidade": 1, "valor": 189.90, "data": "20/10/2026", "status": "Em produção", "observacao": "Detalhes em renda e ajuste para evento especial.", "imagem": "/imagens/Vitrine/Vestido_aurora.jpeg"},
    {"id": 2, "numero": "#0002", "cliente": "Bruno Mendes", "produto": "Camisa Serena", "quantidade": 2, "valor": 199.80, "data": "21/10/2026", "status": "Confirmada", "observacao": "Pedido para presente e uso corporativo.", "imagem": "/imagens/Vitrine/CamisaSerena.jpeg"},
    {"id": 3, "numero": "#0003", "cliente": "Mariana Souza", "produto": "Conjunto Lume", "quantidade": 1, "valor": 279.90, "data": "22/10/2026", "status": "Recebida", "observacao": "Cliente solicitou ajustes na barra.", "imagem": "/imagens/Vitrine/ConjuntoLume.jpeg"},
    {"id": 4, "numero": "#0004", "cliente": "Fernanda Lima", "produto": "Vestido Florença", "quantidade": 1, "valor": 229.90, "data": "18/10/2026", "status": "Em análise", "observacao": "Medidas revisadas com a cliente.", "imagem": "/imagens/Vitrine/Vestido_Florença.jpeg"},
    {"id": 5, "numero": "#0005", "cliente": "Rafael Martins", "produto": "Saia Bella", "quantidade": 1, "valor": 119.90, "data": "17/10/2026", "status": "Pronta", "observacao": "Entrega agendada para quinta-feira.", "imagem": "/imagens/Vitrine/Saia_Bella.jpeg"},
    {"id": 6, "numero": "#0006", "cliente": "Camila Ferreira", "produto": "Bolsa Recria", "quantidade": 1, "valor": 89.90, "data": "15/10/2026", "status": "Entregue", "observacao": "Pagamento confirmado e entrega concluída.", "imagem": "/imagens/Vitrine/Bolsa%20Recria.jpeg"},
    {"id": 7, "numero": "#0007", "cliente": "Gustavo Ramos", "produto": "Vestido Recomeço", "quantidade": 1, "valor": 199.90, "data": "19/10/2026", "status": "Confirmada", "observacao": "Material de reaproveitamento aprovado.", "imagem": "/imagens/Vitrine/VestidoRecomeço.jpeg"},
    {"id": 8, "numero": "#0008", "cliente": "Juliana Oliveira", "produto": "Blusa Atelier", "quantidade": 1, "valor": 149.90, "data": "16/10/2026", "status": "Cancelada", "observacao": "Cliente solicitou cancelamento após revisão.", "imagem": "/imagens/Vitrine/BlusaAtelier.jpeg"},
]

DOACOES_INICIAIS = [
    {"id": 1, "nome": "Mariana Souza", "tipo_peca": "Vestido feminino", "descricao": "Vestido em bom estado, com tecido resistente e pouca deformação.", "estado_peca": "Bom", "data_doacao": "12/10/2026", "status": "Recebida", "observacao": "Peça reservada para reaproveitamento em nova modelagem.", "imagem": "/assets/doacoes/doacao-01.svg"},
    {"id": 2, "nome": "Rafael Martins", "tipo_peca": "Camisa social", "descricao": "Camisa masculina em algodão, com corte bem conservado.", "estado_peca": "Bom", "data_doacao": "15/10/2026", "status": "Em avaliação", "observacao": "Tecido será avaliado para confecção de peça personalizada.", "imagem": "/assets/doacoes/doacao-02.svg"},
    {"id": 3, "nome": "Camila Ferreira", "tipo_peca": "Calça jeans", "descricao": "Calça em denim com desgaste leve e boa estrutura.", "estado_peca": "Regular", "data_doacao": "18/10/2026", "status": "Recebida", "observacao": "Pode ser reaproveitada para modelagem de saia ou bolsa.", "imagem": "/assets/doacoes/doacao-03.svg"},
    {"id": 4, "nome": "Ana Carolina Silva", "tipo_peca": "Blusa feminina", "descricao": "Blusa em tecido leve, boa para reaproveitamento em estampa e modelagem.", "estado_peca": "Bom", "data_doacao": "20/10/2026", "status": "Selecionada", "observacao": "Aguardando corte para reaproveitamento do material.", "imagem": "/assets/doacoes/doacao-04.svg"},
    {"id": 5, "nome": "Gustavo Ramos", "tipo_peca": "Saia midi", "descricao": "Saia em algodão com caimento leve e bem conservada.", "estado_peca": "Excelente", "data_doacao": "17/10/2026", "status": "Em reaproveitamento", "observacao": "Material foi separado para nova produção de peça funcional.", "imagem": "/assets/doacoes/doacao-05.svg"},
    {"id": 6, "nome": "Bruno Mendes", "tipo_peca": "Casaco leve", "descricao": "Casaco de manga longa, em tecido estruturado e com bom estado geral.", "estado_peca": "Bom", "data_doacao": "21/10/2026", "status": "Recebida", "observacao": "Avaliação de corte e uso do material para nova criação.", "imagem": "/assets/doacoes/doacao-06.svg"},
]
