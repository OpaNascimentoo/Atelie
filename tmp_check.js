
// ── DATA ──────────────────────────────────────────────────────────────────
const PEDIDOS = [
  { id:'1',  cliente:'Ana Carolina Silva', servico:'Ajuste de Vestido', peca:'Vestido Social',  data:'18 Mai 2025', horario:'09:00', status:'Em Produção',       imagem:'/imagens/dashboards/Vestido_Social.jpeg' },
  { id:'2',  cliente:'Bruno Mendes',       servico:'Barra de Calça',    peca:'Calça Jeans',     data:'18 Mai 2025', horario:'10:30', status:'Agendado',           imagem:'/imagens/dashboards/Calca_Jeans.jpeg' },
  { id:'3',  cliente:'Carla Ferreira',     servico:'Customização',      peca:'Jaqueta',         data:'18 Mai 2025', horario:'11:00', status:'Pronto para Prova',  imagem:'/imagens/dashboards/Jaqueta.jpeg' },
  { id:'4',  cliente:'Daniel Souza',       servico:'Conserto',          peca:'Terno',           data:'19 Mai 2025', horario:'14:00', status:'Entregue',           imagem:'/imagens/dashboards/Terno.jpeg' },
  { id:'5',  cliente:'Fernanda Lima',      servico:'Ajuste de Vestido', peca:'Vestido de Festa',data:'20 Mai 2025', horario:'10:00', status:'Agendado',           imagem:'/imagens/dashboards/Vestido_de_festa.jpeg' },
  { id:'6',  cliente:'Gustavo Ramos',      servico:'Barra de Calça',    peca:'Calça Social',    data:'20 Mai 2025', horario:'11:30', status:'Em Produção',       imagem:'/imagens/dashboards/Calca_social.jpeg' },
  { id:'7',  cliente:'Helena Martins',     servico:'Modelagem',         peca:'Blusa sob Medida',data:'15 Mai 2025', horario:'09:30', status:'Entregue',           imagem:'/imagens/dashboards/Blusa_sob_Medida.jpeg' },
  { id:'8',  cliente:'Igor Peixoto',       servico:'Customização',      peca:'Camiseta',        data:'14 Mai 2025', horario:'14:00', status:'Entregue',           imagem:'/imagens/dashboards/Camiseta.jpeg' },
];

const SVC_ICON = {
  'Ajuste de Vestido': 'ic-scissors',
  'Barra de Calça':    'ic-ruler',
  'Customização':      'ic-star',
  'Conserto':          'ic-wrench',
  'Modelagem':         'ic-spool',
  'Costura':           'ic-needle',
};

const ST = {
  'Em Produção':       { bg:'var(--status-prod-bg)',  text:'var(--status-prod-text)',  dot:'var(--status-prod-dot)',  bar:'var(--status-prod-bar)'  },
  'Agendado':          { bg:'var(--status-ag-bg)',    text:'var(--status-ag-text)',    dot:'var(--status-ag-dot)',    bar:'var(--status-ag-bar)'    },
  'Pronto para Prova': { bg:'var(--status-prova-bg)', text:'var(--status-prova-text)', dot:'var(--status-prova-dot)', bar:'var(--status-prova-bar)' },
  'Entregue':          { bg:'var(--status-ent-bg)',   text:'var(--status-ent-text)',   dot:'var(--status-ent-dot)',   bar:'var(--status-ent-bar)'   },
};

// ── HELPERS ───────────────────────────────────────────────────────────────
const ic = (id, cls='') =>
  `<svg class="${cls}" aria-hidden="true"><use href="#${id}"/></svg>`;

let currentScreen = 'login';
function showScreen(name) {
  const prev = document.getElementById('screen-' + currentScreen);
  const next = document.getElementById('screen-' + name);
  if (!prev || !next || name === currentScreen) return;
  prev.classList.replace('visible', name === 'main' ? 'hidden-left' : 'hidden-right');
  next.classList.remove('hidden-left', 'hidden-right');
  next.classList.add('visible');
  currentScreen = name;
}

let query = '';
let currentView = 'dashboard';
const cnt = s => PEDIDOS.filter(p => p.status === s).length;

async function fetchJson(url) {
  const response = await fetch(url, { headers: { 'Accept': 'application/json' } });
  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(errorBody.error || 'Erro ao carregar os dados.');
  }
  return response.json();
}

function setDashboardMode(isDashboard) {
  const stats = document.querySelector('.stats-row');
  const search = document.querySelector('.search-row');
  if (stats) stats.style.display = isDashboard ? 'grid' : 'none';
  if (search) search.style.display = isDashboard ? 'flex' : 'none';
}

const ENTITY_DEFS = {
  pedidos: {
    label: 'Pedido',
    endpoint: '/api/pedidos',
    fields: [
      { name: 'cliente', label: 'Cliente', type: 'text', required: true },
      { name: 'servico', label: 'Serviço', type: 'text', required: true },
      { name: 'peca', label: 'Peça', type: 'text', required: true },
      { name: 'data', label: 'Data', type: 'text', placeholder: '25 Mai 2025' },
      { name: 'horario', label: 'Horário', type: 'text', placeholder: '15:00' },
      { name: 'status', label: 'Status', type: 'select', options: ['Agendado', 'Em Produção', 'Pronto para Prova', 'Entregue'] }
    ]
  },
  clientes: {
    label: 'Cliente',
    endpoint: '/api/clientes',
    fields: [
      { name: 'nome', label: 'Nome', type: 'text', required: true },
      { name: 'telefone', label: 'Telefone', type: 'text', required: true },
      { name: 'email', label: 'E-mail', type: 'email', required: true },
      { name: 'endereco', label: 'Endereço', type: 'text' },
      { name: 'status', label: 'Status', type: 'select', options: ['Ativa', 'Em produção', 'Em avaliação'] },
      { name: 'ultimo_atendimento', label: 'Último atendimento', type: 'text' }
    ]
  },
  vitrine: {
    label: 'Peça',
    endpoint: '/api/produtos',
    fields: [
      { name: 'nome', label: 'Nome', type: 'text', required: true },
      { name: 'categoria', label: 'Categoria', type: 'text', required: true },
      { name: 'preco', label: 'Preço', type: 'number', required: true },
      { name: 'disponibilidade', label: 'Disponibilidade', type: 'select', options: ['Disponível', 'Reservado', 'Indisponível'] },
      { name: 'imagem', label: 'Imagem', type: 'text', placeholder: '/imagens/Vitrine/Nome_arquivo.jpeg' },
      { name: 'material', label: 'Material', type: 'text' },
      { name: 'descricao', label: 'Descrição', type: 'textarea' }
    ]
  },
  encomendas: {
    label: 'Encomenda',
    endpoint: '/api/encomendas',
    fields: [
      { name: 'cliente', label: 'Cliente', type: 'text', required: true },
      { name: 'produto', label: 'Produto', type: 'text', required: true },
      { name: 'quantidade', label: 'Quantidade', type: 'number', required: true },
      { name: 'valor_unitario', label: 'Valor unitário', type: 'number' },
      { name: 'status', label: 'Status', type: 'select', options: ['Recebida', 'Em análise', 'Confirmada', 'Em produção', 'Pronta', 'Entregue', 'Cancelada'] },
      { name: 'observacoes', label: 'Observações', type: 'textarea' },
      { name: 'imagem', label: 'Imagem', type: 'text', placeholder: '/imagens/Vitrine/arquivo.jpeg' }
    ]
  },
  doacoes: {
    label: 'Doação',
    endpoint: '/api/doacoes',
    fields: [
      { name: 'nome', label: 'Doador', type: 'text', required: true },
      { name: 'tipo_peca', label: 'Tipo da peça', type: 'text', required: true },
      { name: 'descricao', label: 'Descrição', type: 'textarea', required: true },
      { name: 'estado_peca', label: 'Estado', type: 'select', options: ['Bom', 'Regular', 'Excelente'] },
      { name: 'status', label: 'Status', type: 'select', options: ['Recebida', 'Em avaliação', 'Selecionada', 'Em reaproveitamento', 'Reaproveitada', 'Recusada'] },
      { name: 'imagem', label: 'Imagem', type: 'text', placeholder: '/assets/doacoes/doacao-01.svg' }
    ]
  }
};

function escapeHtml(value) {
  return String(value ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function renderGenericCards(title, items, emptyText, formatter, actionType = null) {
  const actionBar = actionType
    ? `<div class="section-action-bar"><button class="primary-btn" type="button" data-action="new" data-type="${actionType}">+ Novo ${ENTITY_DEFS[actionType].label}</button></div>`
    : '';

  if (!items || items.length === 0) {
    document.getElementById('list-wrap').innerHTML = `
      <div class="empty-state">
        ${ic('ic-search')}
        <div class="empty-title">${emptyText}</div>
        <div class="empty-sub">Aguardando novos dados para a área.</div>
      </div>
      ${actionBar}`;
    return;
  }

  document.getElementById('list-wrap').innerHTML = `
    <div class="sec-hdr">
      <div class="sec-rule"></div>
      <span class="sec-title">${title}</span>
      <span class="sec-badge" style="background:var(--status-ag-bg);color:var(--status-ag-text)">${items.length}</span>
      <div class="sec-rule"></div>
    </div>
    ${items.map(item => formatter(item)).join('')}
    ${actionBar}
  `;
}

async function renderView(viewName) {
  currentView = viewName;
  document.querySelectorAll('.nav-tab').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.view === viewName);
  });

  if (viewName === 'dashboard') {
    setDashboardMode(true);
    renderList();
    return;
  }

  setDashboardMode(false);

  try {
    let data = [];
    if (viewName === 'clientes') {
      data = await fetchJson('/api/clientes');
      renderGenericCards('Clientes', data, 'Nenhum cliente cadastrado', (cliente) => `
        <div class="order-card">
          <div class="card-ribbon" style="background:var(--status-ag-bar)"></div>
          <div class="card-body">
            <div class="card-top">
              <img class="mini-photo" src="/assets/produtos/produto-0${(cliente.id % 8) + 1}.svg" alt="Cliente ${cliente.nome}">
              <div class="card-meta">
                <div class="card-client">${cliente.nome}</div>
                <div class="card-service">${cliente.email}</div>
                <div class="card-peca">${ic('ic-tag')} ${cliente.telefone}</div>
              </div>
              <div class="status-pill" style="background:var(--status-ag-bg);border-color:var(--status-ag-dot)22">
                <div class="status-pip" style="background:var(--status-ag-dot)"></div>
                <span class="status-txt" style="color:var(--status-ag-text)">${cliente.status || 'Ativa'}</span>
              </div>
            </div>
            <div class="card-divider"></div>
            <div class="card-foot">
              <div class="c-meta">${ic('ic-cal')}<span>${cliente.ultimo_atendimento || 'Sem registro'}</span></div>
              <div class="c-meta">${ic('ic-person')}<span>${cliente.pedidos || 0} pedidos</span></div>
            </div>
            <div class="card-actions">
              <button class="mini-action" type="button" data-action="edit" data-type="clientes" data-id="${cliente.id}">Editar</button>
              <button class="mini-action danger" type="button" data-action="delete" data-type="clientes" data-id="${cliente.id}">Excluir</button>
            </div>
          </div>
        </div>
      `, 'clientes');
      return;
    }

    if (viewName === 'vitrine') {
      data = await fetchJson('/api/produtos');
      renderGenericCards('Vitrine', data, 'Nenhuma peça em vitrine', (produto) => `
        <div class="order-card">
          <div class="card-ribbon" style="background:var(--status-ent-bar)"></div>
          <div class="card-body">
            <div class="card-top">
              <img class="mini-photo" src="${produto.imagem || '/assets/produtos/produto-01.svg'}" alt="${produto.nome}">
              <div class="card-meta">
                <div class="card-client">${produto.nome}</div>
                <div class="card-service">${produto.categoria}</div>
                <div class="card-peca">${ic('ic-tag')} ${produto.disponibilidade}</div>
              </div>
              <div class="status-pill" style="background:var(--status-ent-bg);border-color:var(--status-ent-dot)22">
                <div class="status-pip" style="background:var(--status-ent-dot)"></div>
                <span class="status-txt" style="color:var(--status-ent-text)">R$ ${Number(produto.preco).toFixed(2)}</span>
              </div>
            </div>
            <div class="card-divider"></div>
            <div class="card-foot">
              <div class="c-meta">${ic('ic-clock')}<span>${produto.descricao}</span></div>
              <button class="details-btn" data-view="produto" data-id="${produto.id}">Ver ${ic('ic-chev')}</button>
            </div>
            <div class="card-actions">
              <button class="mini-action" type="button" data-action="edit" data-type="vitrine" data-id="${produto.id}">Editar</button>
              <button class="mini-action danger" type="button" data-action="delete" data-type="vitrine" data-id="${produto.id}">Excluir</button>
            </div>
          </div>
        </div>
      `, 'vitrine');
      return;
    }

    if (viewName === 'encomendas') {
      data = await fetchJson('/api/encomendas');
      renderGenericCards('Encomendas', data, 'Nenhuma encomenda registrada', (encomenda) => `
        <div class="order-card">
          <div class="card-ribbon" style="background:var(--status-prova-bar)"></div>
          <div class="card-body">
            <div class="card-top">
              <img class="mini-photo" src="${encomenda.imagem || '/imagens/Vitrine/Vestido_aurora.jpeg'}" alt="${encomenda.produto}">
              <div class="card-meta">
                <div class="card-client">${encomenda.numero || '#' + encomenda.id}</div>
                <div class="card-service">${encomenda.cliente} · ${encomenda.produto}</div>
                <div class="card-peca">${ic('ic-tag')} ${encomenda.quantidade} peça(s)</div>
              </div>
              <div class="status-pill" style="background:var(--status-prova-bg);border-color:var(--status-prova-dot)22">
                <div class="status-pip" style="background:var(--status-prova-dot)"></div>
                <span class="status-txt" style="color:var(--status-prova-text)">${encomenda.status}</span>
              </div>
            </div>
            <div class="card-divider"></div>
            <div class="card-foot">
              <div class="c-meta">${ic('ic-cal')}<span>${encomenda.data}</span></div>
              <div class="c-meta">${ic('ic-clock')}<span>R$ ${Number(encomenda.valor || encomenda.valor_total || 0).toFixed(2)}</span></div>
            </div>
            <div class="card-actions">
              <button class="mini-action" type="button" data-action="edit" data-type="encomendas" data-id="${encomenda.id}">Editar</button>
              <button class="mini-action danger" type="button" data-action="delete" data-type="encomendas" data-id="${encomenda.id}">Excluir</button>
            </div>
          </div>
        </div>
      `, 'encomendas');
      return;
    }

    if (viewName === 'doacoes') {
      data = await fetchJson('/api/doacoes');
      renderGenericCards('Doações', data, 'Nenhuma doação cadastrada', (doacao) => `
        <div class="order-card">
          <div class="card-ribbon" style="background:var(--status-prod-bar)"></div>
          <div class="card-body">
            <div class="card-top">
              <img class="mini-photo" src="${doacao.imagem || '/assets/doacoes/doacao-01.svg'}" alt="Doação ${doacao.nome}">
              <div class="card-meta">
                <div class="card-client">${doacao.nome}</div>
                <div class="card-service">${doacao.tipo_peca}</div>
                <div class="card-peca">${ic('ic-tag')} ${doacao.estado_peca}</div>
              </div>
              <div class="status-pill" style="background:var(--status-prod-bg);border-color:var(--status-prod-dot)22">
                <div class="status-pip" style="background:var(--status-prod-dot)"></div>
                <span class="status-txt" style="color:var(--status-prod-text)">${doacao.status || 'Recebida'}</span>
              </div>
            </div>
            <div class="card-divider"></div>
            <div class="card-foot">
              <div class="c-meta">${ic('ic-cal')}<span>${doacao.data_doacao}</span></div>
            </div>
            <div class="card-actions">
              <button class="mini-action" type="button" data-action="edit" data-type="doacoes" data-id="${doacao.id}">Editar</button>
              <button class="mini-action danger" type="button" data-action="delete" data-type="doacoes" data-id="${doacao.id}">Excluir</button>
            </div>
          </div>
        </div>
      `, 'doacoes');
    }
  } catch (error) {
    document.getElementById('list-wrap').innerHTML = `
      <div class="empty-state">
        ${ic('ic-search')}
        <div class="empty-title">Não foi possível carregar esta área</div>
        <div class="empty-sub">${error.message}</div>
      </div>`;
  }
}

function openProductModalFromApi(productId) {
  fetchJson(`/api/produtos/${productId}`).then((produto) => {
    const material = produto.material || 'Material premium';
    const reaproveitado = produto.reaproveitado ? 'Sim' : 'Não';
    const message = `
      <div class="modal-handle"></div>
      <div style="display:flex;justify-content:center;margin-bottom:16px;"><img src="${produto.imagem || '/assets/produtos/produto-01.svg'}" alt="${produto.nome}" style="width:100%;max-width:240px;height:170px;object-fit:cover;border-radius:16px;border:1px solid var(--cream3);background:var(--cream2);"></div>
      <div class="modal-title">${produto.nome}</div>
      <div class="modal-service">${produto.categoria} · ${produto.disponibilidade}</div>
      <div class="modal-divider"></div>
      <div class="modal-row"><span class="modal-lbl">Descrição</span><span class="modal-val">${produto.descricao}</span></div>
      <div class="modal-row"><span class="modal-lbl">Preço</span><span class="modal-val">R$ ${Number(produto.preco).toFixed(2)}</span></div>
      <div class="modal-row"><span class="modal-lbl">Disponibilidade</span><span class="modal-val">${produto.disponibilidade}</span></div>
      <div class="modal-row"><span class="modal-lbl">Material</span><span class="modal-val">${material}</span></div>
      <div class="modal-row"><span class="modal-lbl">Reaproveitado</span><span class="modal-val">${reaproveitado}</span></div>
      <button class="modal-close" onclick="closeModal()">Encomendar</button>
    `;
    document.getElementById('modal-inner').innerHTML = message;
    document.getElementById('modal-ov').classList.add('open');
  }).catch((error) => {
    alert(error.message);
  });
}

function openEntityForm(type, item = null) {
  const def = ENTITY_DEFS[type];
  if (!def) return;

  const isEdit = !!item;
  const fieldsMarkup = def.fields.map((field) => {
    const value = item && item[field.name] !== undefined ? item[field.name] : '';
    const id = `field-${type}-${field.name}`;

    if (field.type === 'select') {
      const options = field.options.map((option) => {
        const selected = String(value || '') === String(option) ? 'selected' : '';
        return `<option value="${escapeHtml(option)}" ${selected}>${escapeHtml(option)}</option>`;
      }).join('');
      return `
        <div class="entity-field">
          <label for="${id}">${field.label}</label>
          <select id="${id}" name="${field.name}">${options}</select>
        </div>`;
    }

    const textarea = field.type === 'textarea';
    const inputType = field.type === 'number' ? 'number' : field.type === 'email' ? 'email' : 'text';
    const inputValue = escapeHtml(value);
    const extra = field.placeholder ? `placeholder="${escapeHtml(field.placeholder)}"` : '';
    const required = field.required ? 'required' : '';

    if (textarea) {
      return `
        <div class="entity-field">
          <label for="${id}">${field.label}</label>
          <textarea id="${id}" name="${field.name}" ${required}>${inputValue}</textarea>
        </div>`;
    }

    return `
      <div class="entity-field">
        <label for="${id}">${field.label}</label>
        <input id="${id}" name="${field.name}" type="${inputType}" value="${inputValue}" ${required} ${extra} />
      </div>`;
  }).join('');

  document.getElementById('modal-inner').innerHTML = `
    <div class="modal-handle"></div>
    <div class="modal-title">${isEdit ? 'Editar' : 'Novo'} ${def.label}</div>
    <div class="modal-service">${isEdit ? 'Atualize os dados da entidade.' : 'Cadastre uma nova informação no sistema.'}</div>
    <form class="entity-form" id="entity-form" data-type="${type}" data-id="${item && item.id ? item.id : ''}">
      <div class="field-grid">${fieldsMarkup}</div>
      <div class="form-actions">
        <button type="button" class="secondary-btn" onclick="closeModal()">Cancelar</button>
        <button type="submit" class="primary-btn">${isEdit ? 'Salvar' : 'Cadastrar'}</button>
      </div>
    </form>
  `;
  document.getElementById('modal-ov').classList.add('open');
}

async function submitEntityForm(event) {
  event.preventDefault();
  const form = event.target.closest('#entity-form');
  if (!form) return;

  const type = form.dataset.type;
  const def = ENTITY_DEFS[type];
  if (!def) return;

  const payload = {};
  const formData = new FormData(form);
  formData.forEach((value, key) => {
    if (key === 'preco' || key === 'valor_unitario' || key === 'valor_total' || key === 'quantidade' || key === 'pedidos') {
      payload[key] = Number(value) || 0;
    } else if (key === 'reaproveitado') {
      payload[key] = value === 'true';
    } else {
      payload[key] = value;
    }
  });

  const isEdit = !!form.dataset.id;
  const url = `${def.endpoint}${isEdit ? `/${form.dataset.id}` : ''}`;
  const response = await fetch(url, {
    method: isEdit ? 'PUT' : 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.error || 'Não foi possível salvar o registro.');
  }

  closeModal();
  if (currentView === 'dashboard') {
    renderList();
    return;
  }

  renderView(currentView);
}

async function deleteEntity(type, id) {
  const def = ENTITY_DEFS[type];
  if (!def) return;

  if (!confirm(`Deseja realmente excluir este ${def.label.toLowerCase()}?`)) return;

  const response = await fetch(`${def.endpoint}/${id}`, { method: 'DELETE' });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    alert(data.error || 'Não foi possível excluir o registro.');
    return;
  }

  if (currentView === 'dashboard') {
    renderList();
    return;
  }
  renderView(currentView);
}

// ── CARD ──────────────────────────────────────────────────────────────────
function card(p) {
  const s  = ST[p.status] || ST['Agendado'];
  const ic_svc = SVC_ICON[p.servico] || 'ic-scissors';
  return `
  <div class="order-card">
    <div class="card-ribbon" style="background:${s.bar}"></div>
    <div class="card-body">
      <div class="card-top">
        <img class="mini-photo" src="${p.imagem || '/imagens/dashboards/Vestido_Social.jpeg'}" alt="${p.peca}" />
        <div class="card-meta">
          <div class="card-client">${p.cliente}</div>
          <div class="card-service">${p.servico}</div>
          <div class="card-peca">${ic('ic-tag')} ${p.peca}</div>
        </div>
        <div class="status-pill" style="background:${s.bg};border-color:${s.dot}22">
          <div class="status-pip" style="background:${s.dot}"></div>
          <span class="status-txt" style="color:${s.text}">${p.status}</span>
        </div>
      </div>
      <div class="card-divider"></div>
      <div class="card-foot">
        <div class="c-meta">${ic('ic-cal')}<span>${p.data}</span></div>
        <div class="c-meta">${ic('ic-clock')}<span>${p.horario}</span></div>
        <button class="details-btn" data-id="${p.id}">Ver ${ic('ic-chev')}</button>
      </div>
    </div>
  </div>`;
}

function secHdr(label, count, badgeBg, badgeColor) {
  return `
  <div class="sec-hdr">
    <div class="sec-rule"></div>
    <span class="sec-title">${label}</span>
    <span class="sec-badge" style="background:${badgeBg};color:${badgeColor}">${count}</span>
    <div class="sec-rule"></div>
  </div>`;
}

async function renderList() {
  let data = [...PEDIDOS];
  try {
    data = await fetchJson('/api/pedidos');
  } catch (error) {
    console.warn('Dashboard sem sincronização com a API:', error.message);
  }

  const q = query.toLowerCase();
  const filtered = q
    ? data.filter(p => (p.cliente || '').toLowerCase().includes(q) || (p.servico || '').toLowerCase().includes(q) || (p.peca || '').toLowerCase().includes(q))
    : data;

  document.getElementById('cnt-prod').textContent = filtered.filter(p => p.status === 'Em Produção').length;
  document.getElementById('cnt-ag').textContent = filtered.filter(p => p.status === 'Agendado').length;
  document.getElementById('cnt-prova').textContent = filtered.filter(p => p.status === 'Pronto para Prova').length;
  document.getElementById('cnt-ent').textContent = filtered.filter(p => p.status === 'Entregue').length;

  const groups = [
    { label:'Em <em>Produção</em>',       key:'Em Produção',       bb:'var(--status-prod-bg)',  bc:'var(--status-prod-text)'  },
    { label:'<em>Agendados</em>',          key:'Agendado',          bb:'var(--status-ag-bg)',    bc:'var(--status-ag-text)'    },
    { label:'Pronto para <em>Prova</em>',  key:'Pronto para Prova', bb:'var(--status-prova-bg)', bc:'var(--status-prova-text)' },
    { label:'<em>Entregues</em>',          key:'Entregue',          bb:'var(--status-ent-bg)',   bc:'var(--status-ent-text)'   },
  ];

  let html = '';
  groups.forEach(g => {
    const items = filtered.filter(p => p.status === g.key);
    if (items.length === 0) return;
    html += secHdr(g.label, items.length, g.bb, g.bc);
    items.forEach(p => html += card(p));
  });

  if (!html) html = `
    <div class="empty-state">
      ${ic('ic-search')}
      <div class="empty-title">Nenhum pedido encontrado</div>
      <div class="empty-sub">Tente outro nome, serviço ou peça.</div>
    </div>`;

  document.getElementById('list-wrap').innerHTML = html;
}

// ── MODAL ─────────────────────────────────────────────────────────────────
function openModal(id) {
  const p = PEDIDOS.find(x => x.id === id); if (!p) return;
  const s = ST[p.status] || ST['Agendado'];
  document.getElementById('modal-inner').innerHTML = `
    <div class="modal-handle"></div>
    <div class="modal-title">${p.cliente}</div>
    <div class="modal-service">${p.servico} · ${p.peca}</div>
    <div class="modal-divider"></div>
    <div class="modal-row"><span class="modal-lbl">Data</span><span class="modal-val">${p.data}</span></div>
    <div class="modal-row"><span class="modal-lbl">Horário</span><span class="modal-val">${p.horario}</span></div>
    <div class="modal-row">
      <span class="modal-lbl">Status</span>
      <span class="modal-val" style="color:${s.text}">${p.status}</span>
    </div>
    <div class="modal-row"><span class="modal-lbl">Peça</span><span class="modal-val">${p.peca}</span></div>
    <button class="modal-close" onclick="closeModal()">Fechar</button>
  `;
  document.getElementById('modal-ov').classList.add('open');
}
function closeModal() { document.getElementById('modal-ov').classList.remove('open'); }

// ── BUILD DOM ─────────────────────────────────────────────────────────────
document.getElementById('root').innerHTML = `

<!-- ── LOGIN ── -->
<div id="screen-login" class="screen visible">
  <div class="login-deco-top"></div>
  <div class="login-deco-bot"></div>
  <div class="login-inner">

    <div class="logo-wrap fu fu1">
      <div class="logo-emblem">${ic('ic-scissors','')}</div>
      <div class="logo-name">Ateliê <em>Bella</em></div>
      <div class="logo-tagline">Costura · Modelagem · Alta Costura</div>
    </div>

    <div class="login-card fu fu2">
      <div class="login-title">Bem-vinda, <em>costureira</em></div>
      <div class="login-subtitle">Acesse para gerenciar os pedidos do ateliê</div>

      <div class="field">
        <label class="field-label" for="inp-user">Usuário</label>
        <div class="field-wrap">
          ${ic('ic-person','field-icon')}
          <input id="inp-user" type="text" placeholder="Seu usuário" autocomplete="off"/>
        </div>
      </div>

      <div class="field">
        <label class="field-label" for="inp-pass">Senha</label>
        <div class="field-wrap">
          ${ic('ic-lock','field-icon')}
          <input id="inp-pass" type="password" placeholder="Sua senha" autocomplete="off"/>
          <button class="eye-btn" id="eye-btn" aria-label="Mostrar senha">
            ${ic('ic-eye','')}
          </button>
        </div>
      </div>

      <div id="err-msg" class="error-msg"></div>

      <div class="forgot"><a href="#">Esqueceu a senha?</a></div>

      <button class="btn-login" id="btn-login">
        Entrar ${ic('ic-arr','')}
      </button>

      <div class="stitch-line">
        <span class="stitch-long"></span>
        <span></span><span></span><span></span>
        <span class="stitch-long"></span>
      </div>

      <div class="login-footer">
        <span>Novo ateliê?</span>
        <a href="#">Solicitar cadastro</a>
      </div>
    </div>

    <div class="version-tag fu fu3">Ateliê Bella · v1.0</div>
  </div>
</div>

<!-- ── MAIN ── -->
<div id="screen-main" class="screen hidden-right">

  <div class="app-header">
    <div class="h-left">
      <div class="h-emblem">${ic('ic-scissors','')}</div>
      <div>
        <div class="h-name">Ateliê <em>Bella</em></div>
        <div class="h-sub">Gestão de Pedidos</div>
      </div>
    </div>
    <div class="h-right">
      <button class="icon-btn" id="notif-btn" aria-label="Notificações">
        ${ic('ic-bell','')}
        <div class="notif-pip"></div>
      </button>
      <button class="avatar-btn" id="avatar-btn" aria-label="Sair">AB</button>
    </div>
  </div>

  <div class="nav-tabs" id="nav-tabs">
    <button class="nav-tab active" data-view="dashboard">Dashboard</button>
    <button class="nav-tab" data-view="clientes">Clientes</button>
    <button class="nav-tab" data-view="vitrine">Vitrine</button>
    <button class="nav-tab" data-view="encomendas">Encomendas</button>
    <button class="nav-tab" data-view="doacoes">Doações</button>
  </div>

  <div class="main-scroll">

    <!-- Stats -->
    <div class="stats-row">
      <div class="stat-card s-prod">
        <div class="stat-dot" style="background:var(--status-prod-dot)"></div>
        <div class="stat-num" id="cnt-prod">0</div>
        <div class="stat-lbl">Em Produção</div>
      </div>
      <div class="stat-card s-ag">
        <div class="stat-dot" style="background:var(--status-ag-dot)"></div>
        <div class="stat-num" id="cnt-ag">0</div>
        <div class="stat-lbl">Agendados</div>
      </div>
      <div class="stat-card s-prova">
        <div class="stat-dot" style="background:var(--status-prova-dot)"></div>
        <div class="stat-num" id="cnt-prova">0</div>
        <div class="stat-lbl">Para Prova</div>
      </div>
      <div class="stat-card s-ent">
        <div class="stat-dot" style="background:var(--status-ent-dot)"></div>
        <div class="stat-num" id="cnt-ent">0</div>
        <div class="stat-lbl">Entregues</div>
      </div>
    </div>

    <!-- Search -->
    <div class="search-row">
      <div class="search-wrap">
        ${ic('ic-search','')}
        <input id="search-inp" type="text" placeholder="Buscar cliente, serviço ou peça…"/>
        <button class="clear-btn" id="clear-btn" aria-label="Limpar" style="display:none">
          ${ic('ic-x','')}
        </button>
      </div>
      <button class="filter-btn" id="filter-btn" aria-label="Filtros">
        ${ic('ic-sliders','')}
      </button>
    </div>

    <!-- List -->
    <div id="list-wrap"></div>
  </div>

  <button class="fab" id="fab-btn" aria-label="Novo pedido">
    ${ic('ic-plus','')}
  </button>
</div>

<!-- ── MODAL ── -->
<div class="modal-overlay" id="modal-ov">
  <div class="modal-sheet" id="modal-inner"></div>
</div>
`;

// Stats
document.getElementById('cnt-prod').textContent  = cnt('Em Produção');
document.getElementById('cnt-ag').textContent    = cnt('Agendado');
document.getElementById('cnt-prova').textContent = cnt('Pronto para Prova');
document.getElementById('cnt-ent').textContent   = cnt('Entregue');

// ── EVENTS ────────────────────────────────────────────────────────────────

// Eye toggle
let passVis = false;
document.getElementById('eye-btn').addEventListener('click', () => {
  passVis = !passVis;
  document.getElementById('inp-pass').type = passVis ? 'text' : 'password';
  document.querySelector('#eye-btn use').setAttribute('href', passVis ? '#ic-eye-off' : '#ic-eye');
});

// Login
document.getElementById('btn-login').addEventListener('click', () => {
  const u = document.getElementById('inp-user').value.trim();
  const p = document.getElementById('inp-pass').value.trim();
  const e = document.getElementById('err-msg');
  if (!u || !p) {
    e.textContent = !u ? 'Informe seu usuário.' : 'Informe sua senha.';
    e.classList.add('show'); return;
  }
  e.classList.remove('show');
  renderList();
  showScreen('main');
});
['inp-user','inp-pass'].forEach(id =>
  document.getElementById(id).addEventListener('keydown', ev => {
    if (ev.key === 'Enter') document.getElementById('btn-login').click();
  })
);

// Notif
document.getElementById('notif-btn').addEventListener('click', () =>
  alert('Você tem 2 notificações: prova da Ana às 09h e entrega do Daniel às 14h.')
);

// Avatar / logout
document.getElementById('avatar-btn').addEventListener('click', () => {
  if (confirm('Deseja sair do ateliê?')) showScreen('login');
});

// Search
document.getElementById('search-inp').addEventListener('input', e => {
  query = e.target.value;
  document.getElementById('clear-btn').style.display = query ? '' : 'none';
  if (currentView === 'dashboard') renderList();
});
document.getElementById('clear-btn').addEventListener('click', () => {
  query = '';
  document.getElementById('search-inp').value = '';
  document.getElementById('clear-btn').style.display = 'none';
  if (currentView === 'dashboard') renderList();
});

document.querySelectorAll('.nav-tab').forEach(btn => {
  btn.addEventListener('click', () => renderView(btn.dataset.view));
});

document.getElementById('filter-btn').addEventListener('click', () =>
  alert('Filtros avançados por período e status em breve!')
);

document.getElementById('fab-btn').addEventListener('click', () => {
  const type = currentView === 'dashboard' ? 'pedidos' : currentView;
  if (type === 'dashboard') return;
  openEntityForm(type);
});

// Card click (delegation)
document.getElementById('list-wrap').addEventListener('click', e => {
  const actionBtn = e.target.closest('[data-action]');
  if (actionBtn) {
    const type = actionBtn.dataset.type;
    const id = Number(actionBtn.dataset.id);
    if (actionBtn.dataset.action === 'new') {
      openEntityForm(type);
      return;
    }
    if (actionBtn.dataset.action === 'edit') {
      fetchJson(`${ENTITY_DEFS[type].endpoint}/${id}`).then(item => openEntityForm(type, item)).catch(alert);
      return;
    }
    if (actionBtn.dataset.action === 'delete') {
      deleteEntity(type, id);
      return;
    }
  }

  const btn = e.target.closest('.details-btn');
  if (!btn) return;
  if (btn.dataset.view === 'produto') {
    openProductModalFromApi(btn.dataset.id);
    return;
  }
  openModal(btn.dataset.id);
});

document.getElementById('modal-inner').addEventListener('submit', async e => {
  if (e.target && e.target.id === 'entity-form') {
    try {
      await submitEntityForm(e);
    } catch (error) {
      alert(error.message);
    }
  }
});

// Close modal
document.getElementById('modal-ov').addEventListener('click', e => {
  if (e.target.id === 'modal-ov') closeModal();
});
