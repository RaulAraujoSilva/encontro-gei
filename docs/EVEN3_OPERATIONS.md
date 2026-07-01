# Operações da Plataforma Even3

Documentação operacional completa do evento `722003` na Even3. Cobre acesso, mapa do painel, automação via Chrome MCP, API REST e operações comuns de manutenção.

---

## 1. Acesso e credenciais

| Item | Valor |
|---|---|
| **URL do painel** | https://www.even3.com.br/organizador/home/ |
| **URL pública do evento** | https://www.even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003 |
| **Conta organizador** | `Raul Araujo` (login Google) |
| **Event ID** | `722003` |
| **Slug do evento** | `1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003` |
| **API Token** | `da1c37f7-538f-4c93-bf7e-f6154fab02f8` (também salvo em `EVEN3_API_TOKEN` no Vercel) |
| **API Base URL** | `https://www.even3.com.br/api/v1/` |
| **Header de autenticação** | `Authorization-Token: <token>` |

> **Onde regenerar o token:** Painel > GERAL > Integrações > **API Even3** > Gerenciar > "Criar chave de acesso"

---

## 2. Mapa do painel · status atual

### GESTÃO

| Aba | URL | Status |
|---|---|---|
| **Início** | `/organizador/home/` | Dashboard com checklist + métricas live |
| **Pessoas** | `/organizador/people/` | Lista inscritos (preenche automaticamente) |
| **Vendas** | `/organizador/sales/` | N/A (evento gratuito) |

### PRÉ-EVENTO

| Aba | URL | Status |
|---|---|---|
| **Inscrições > Entradas e valores** | `/organizador/registration/` | ✅ **2 entradas ativas**: Presencial Completo ("Dias 1 e 3") = **500 vagas** (elevada 400→500 em 24/06); Participação Online · ilimitada. ⚠️ **As 4 entradas de Visita Técnica criadas mais cedo em 24/06 foram EXCLUÍDAS no mesmo dia** — a Even3 só permite **1 inscrição por pessoa por evento**, então uma 2ª inscrição (visita) dava "Participante já está inscrito". As visitas viraram **Atividades** (inscrição em atividades) — ver §6 "Publicar nova jornada" e a linha **Programação > Atividades**. Como não há mais categoria "visita", o `api/inscritos.js` retorna `visita: 0` (inerte; presencial = count − online segue correto). |
| **Inscrições > Formulário de inscrição** | `?tab=Formulário%20de%20inscrição` | ✅ Nome + e-mail + instituição + telefone celular + Termo LGPD (obrigatório) |
| **Inscrições > Configurações** | `?tab=Configurações` | Default · não há cobrança |
| **Página do Evento (hotsite)** | `/organizador/hotsite/` | ✅ CSS custom aplicado (paleta navy/yellow/green/blue + Manrope/Outfit) |
| **Programação > Atividades** | `/organizador/programacao/` | ✅ As **4 visitas confirmadas** são Atividades tipo **"Visita Técnica"** com **Inscrição Gratuita + Limite de vagas** (é isso que faz a visita aparecer na tela de inscrição do participante): J01 · TermoRio (**43** vagas, +12 já inscritos), J02 · Guandú+Lameirão/CEDAE (**39**), J03 · Icaraí+Camboinhas (**26**), J04 · Braskem (**38**) — todas 09/07. As jornadas sem detalhamento (Gerdau/Eneva/IRM/CSN) e os placeholders antigos foram **excluídos** em 24/06. As atividades do Dia 1/Dia 3 ("Não requer inscrição") foram **mantidas** (não aparecem na tela de inscrição). **▶ Para publicar as próximas jornadas, ver §6 "Publicar nova jornada (visita técnica)".** |
| **Programação > Convidados** | `?tab=convidados` | ✅ 6 palestrantes (Magda, Miguel, Calado, Li Li Min, Raul, Vladimir) |
| **Programação > Configurações** | `?tab=configuracao` | ✅ **Inscrição em atividades**: cronograma 04/05→**01/07/2026** · **Cortesias e limitações = máx. 1 atividade/pessoa** (cada participante escolhe só 1 visita) · **Restrição = precisa estar inscrito no evento** (presencial OU online escolhem sem 2ª inscrição). Config global — vale para todas as jornadas, não refazer por atividade. |
| **Submissões > Recebimento > Modalidades** | `/organizador/trabalhocientifico/submissaogeral?tab=Modalidades` | ✅ 4 modalidades (Artigo, Pôster, Relatório A3, Resumo) com PDFs anexados |
| **Submissões > Áreas Temáticas** | `?tab=Áreas%20Temáticas` | ✅ 13 eixos alinhados ao projeto executivo |
| **Submissões > Configurações** | `?tab=Configurações` | ✅ Cronograma 04/05–16/06 · Comissão: Profa. Silvia Cristina Rufino |
| **Avaliação > Avaliadores** | `/organizador/trabalhocientifico/avaliacaogeral?tab=Avaliadores` | ✅ 7 avaliadores cadastrados |
| **Avaliação > Configurações** | `?tab=Configurações` | ✅ Cronograma 17/06–22/06 · Tipo: por critérios · Quantidade: 2 (double-blind) |

### EVENTO

| Aba | URL | Status |
|---|---|---|
| **Credenciamento** | `/organizador/credenciamento/` | Default · pronto pra leitura QR no dia |

### PÓS-EVENTO

| Aba | URL | Status |
|---|---|---|
| **Certificados** | `/organizador/certificate/` | ✅ 6 templates **publicados** (Participação, Atividade, Convidado, Submissão, Apresentação, Avaliador) |

### GERAL

| Aba | URL | Status |
|---|---|---|
| **Configuração > Evento** | `/organizador/configuracao/evento` | ✅ Datas 08-10/07/2026 · 24h · Tipo Científico · Engenharias · 8 keywords · Descrição · RJ |
| **Configuração > Organizadores** | `/organizador/configuracao/organizadores` | Apenas Raul (organizador único — adicionar membros se necessário) |
| **Configuração > Financeiro** | `/organizador/configuracao/dadosbancario` | Pular (gratuito) |
| **Ferramentas > Funcionalidades** | `/organizador/tools/` | Default |
| **Ferramentas > Integrações** | `/organizador/integrations/` | ✅ API Even3 ativa |

---

## 3. Truque do JS dispatch · contornar máscara dd/mm

A Even3 usa **inputs com máscara JS** (campos de data dd/mm/aaaa). O `mcp__chrome-devtools__fill` e `fill_form` simples interpretam o valor como `mm/dd/yyyy` e geram lixo (ex: `04/05/2026` vira `05/20/2605`).

**Solução:** usar o `value setter nativo` do `HTMLInputElement.prototype` + dispatch manual de eventos.

```js
// Cole no console do navegador (F12 → Console) ou use via mcp__chrome-devtools__evaluate_script
window.setVal = (el, v) => {
  const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
  setter.call(el, v);
  el.dispatchEvent(new Event('input',  { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
  el.dispatchEvent(new Event('blur',   { bubbles: true }));
};

// Helper pra clicar botão por texto (regex)
window.click = sel =>
  Array.from(document.querySelectorAll('button, a'))
       .find(b => sel.test(b.innerText.trim()) && b.offsetParent !== null)
       ?.click();

// Exemplo de uso: setar 2 datas e salvar
const inputs = Array.from(document.querySelectorAll('input'))
                    .filter(i => (i.placeholder||'').includes('aaaa') && i.offsetParent !== null);
setVal(inputs[0], '04/05/2026');
setVal(inputs[1], '15/05/2026');
click(/^Salvar/i);
```

**Por que funciona:** o React/AngularJS usado pela Even3 escuta o `input` event nativo. Setar `el.value = '...'` direto NÃO dispara esse listener; o setter prototype-nativo + `dispatchEvent` simula o que um humano faria ao digitar.

---

## 4. Automação via Chrome DevTools MCP

### Setup

1. Abrir o Chrome controlado pelo MCP (separado da sessão regular do usuário)
2. Navegar para `https://www.even3.com.br/login/` e fazer login (Google)
3. A sessão fica ativa enquanto a janela MCP estiver aberta

### Padrão de execução

```js
// 1. Navegar
mcp__chrome-devtools__navigate_page({ url: "https://www.even3.com.br/organizador/..." })

// 2. Aguardar carregar + tirar snapshot
mcp__chrome-devtools__take_snapshot()
// → retorna lista uid=X_Y de elementos clicáveis/preenchíveis

// 3. Para forms simples (texto, número):
mcp__chrome-devtools__fill_form({ elements: [{uid: "X_Y", value: "..."}] })
mcp__chrome-devtools__click({ uid: "X_Z" })

// 4. Para forms mascarados (datas, telefone):
mcp__chrome-devtools__evaluate_script({ function: "async () => { /* JS dispatch */ }" })

// 5. Para upload de arquivos:
mcp__chrome-devtools__upload_file({ uid: "X_W", filePath: "C:\\..." })
// IMPORTANTE: aguardar 5+ segundos antes de salvar (upload assíncrono)
```

### Limitações descobertas

| Sintoma | Causa | Workaround |
|---|---|---|
| Datas viram `05/20/2605` | Máscara dd/mm interpretada como mm/dd | `setVal` + dispatch (acima) |
| Modal "Comunicação" abre vazio | DOM lazy-loaded sem fallback do snapshot | Usar `evaluate_script` com timeout de 3s+ |
| Ações que recarregam a página fecham o contexto JS | Navigation destruction | Fazer 1 ação por chamada · re-snapshot depois |
| Cache CDN serve PNG antigo | Vercel edge cache | Append `?v=N` ao src no HTML |
| Upload de PDF não persiste se salvar imediatamente | Upload assíncrono em segundo plano | `await wait(5500)` antes de clicar Salvar |

---

## 5. API REST Even3 — endpoints úteis

Base URL: `https://www.even3.com.br/api/v1/`
Header obrigatório em todas as chamadas: `Authorization-Token: <TOKEN>`

| Método | Endpoint | Retorno |
|---|---|---|
| GET | `/event` | Dados gerais do evento |
| GET | `/attendees` | Lista de inscritos (paginada) |
| POST | `/attendees/create` | Criar inscrição programática |

### Exemplos

```bash
# Conferir o número de inscritos
TOK="da1c37f7-538f-4c93-bf7e-f6154fab02f8"
curl -s -H "Authorization-Token: $TOK" \
  "https://www.even3.com.br/api/v1/attendees" | jq '.data | length'

# Endpoint do site (cache 5 min)
curl -s https://encontrogeig.org/api/inscritos
# {"count":4,"eventId":"722003","updatedAt":"..."}
```

> **Não documentados oficialmente** mas confirmados: `?page=N&per_page=M` para paginar; resposta tem `{ "data": [...] }` envelopando o array.

---

## 6. Operações comuns

### ▶ Publicar nova jornada (visita técnica) como Atividade com inscrição

> **Modelo adotado em 24/06:** cada visita é uma **Atividade** (Programação), tipo **"Visita Técnica"**,
> com **Inscrição Gratuita + Limite de vagas**. É isso — e **NÃO uma entrada** — que coloca a visita na
> tela de escolha do participante (`/participante/sessions/`). Criar a visita como *entrada* está
> ERRADO: a Even3 só permite **1 inscrição por pessoa por evento**, então uma 2ª inscrição dá
> "Participante já está inscrito". As 4 visitas confirmadas (J01–J04) já estão nesse modelo; use o
> passo a passo abaixo para publicar **J05+ quando confirmadas**.

**Onde:** `/organizador/programacao/` (aba **Atividades**) → **+ Adicionar atividade** (ou clicar numa
atividade existente para editar).

No modal **"Atividade"** / **"Editar Atividade"**:

1. **Título:** `Jornada 0X · <Empresa/Local>` (ex.: `Jornada 05 · Gerdau · Santa Cruz`).
2. **Descrição (Resumo):** é o texto exibido em **"Mais informações"** na tela de inscrição — **espelhar
   o card do site** (modais `#vt-jNN` em `index.html`; ver lista resumida na §9). Manter vagas/horário
   coerentes com a atividade.
3. **Tipo:** `Visita Técnica`. ← obrigatório para entrar no filtro da tela de inscrição.
4. **Inscrição:** `Gratuita`. ← "Não requer inscrição" = **NÃO** aparece para escolher.
5. **Duração:** `Um dia` → isso **revela** os campos **Data / Início / Fim**.
6. **Data / Início / Fim:** usar o truque **setVal** (§3) — campos com máscara `dd/mm/aaaa` e `__:__`
   (ex.: `09/07/2026`, `08:00`, `13:00`). `fill_form` simples corrompe a máscara.
7. Expandir **"Adicione local, carga horária, limite de vagas, tags…"** e preencher **Limite de vagas**
   (input com placeholder `"Ilimitado"`). **Nunca deixar ilimitado** nas visitas.
8. **Salvar atividade** (deixar "Notificar participantes" desmarcado).

**Conferir:** a linha aparece com tipo "Visita Técnica" + "X vagas" e a atividade surge em
`/participante/sessions/` (filtro Visita Técnica). A **config global já cobre** a nova jornada
(máx. 1 atividade/pessoa · janela até 01/07 · restrito a inscritos — Programação > Configurações);
**não** reconfigurar por jornada.

**Excluir uma jornada:** abrir a atividade → botão **Excluir** (exclui **direto**, toast "Sucesso",
sem diálogo de confirmação extra).

**Atalhos via Chrome MCP** — as comboboxes Tipo/Inscrição/Duração **não são `<select>` nativo**
(`querySelectorAll('select')` não acha): use `fill_form` pelos uids do modal, ou clique a combobox + a
opção. Padrão usado em 24/06:
```js
// 1) Título/Tipo/Inscrição/Duração via fill_form (pegar uids no snapshot do modal)
fill_form([{uid:'..',value:'Jornada 0X · ...'},{uid:'..tipo',value:'Visita Técnica'},
           {uid:'..insc',value:'Gratuita'},{uid:'..dur',value:'Um dia'}])
// 2) Data + horas via evaluate_script (setVal da §3)
const dlg = document.querySelector('div[role="dialog"]');
setVal(dlg.querySelector('input[placeholder="dd/mm/aaaa"]'), '09/07/2026');
const t = dlg.querySelectorAll('input[placeholder="__:__"]'); setVal(t[0],'08:00'); setVal(t[1],'13:00');
// 3) Expandir vagas e preencher
Array.from(dlg.querySelectorAll('*')).find(e=>e.children.length===0 && /limite de vagas/i.test(e.textContent))?.click();
setVal(Array.from(dlg.querySelectorAll('input')).find(i=>i.placeholder==='Ilimitado'), '40');
// 4) Salvar
Array.from(dlg.querySelectorAll('button')).find(b=>/Salvar atividade/i.test(b.textContent))?.click();
```

**Link direto p/ o participante escolher** (faz login → cai **direto** na lista só das 4 visitas, cada
uma com "Realizar inscrição"; já usado nos CTAs do site — modais J01–J04 + card de inscrição,
commit `ca9c538`):
```
https://www.even3.com.br/evento/login?evento=1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003&ReturnUrl=%2fparticipante%2fsessions%2f&lang=pt
```
> A tela `/participante/sessions/` já **filtra só "Visita Técnica"** — por isso **não** é preciso
> limpar/ocultar as atividades do Dia 1/Dia 3 (decisão 24/06: manter, p/ não afetar a Programação
> pública do hotsite e os certificados de atividade).

### Comunicar resultado / carta de aceite (por modalidade)

> **Política (25/06, v2) — 3 grupos:** **Artigo Completo** → Modelo **A** (carta UFF-válida: "artigo
> completo aceito em evento científico nacional", item 2 da Tabela 3 do Edital PPGEP/UFF nº 01/2026).
> **Artigo (resumo)** → Modelo **B** (APROVADO p/ apresentação + submeter artigo completo até 30/09).
> **Resumo Expandido / Pôster A3 / Relatório A3** → Modelo **C** (ACEITE definitivo, anais ISBN+DOI;
> sem fase posterior). Reprovados → Modelo **E**. Entrega = **e-mail Even3 + Carta PDF assinada**.
> **Textos prontos e mapa modalidade→modelo em [`CARTAS_ACEITE_EVEN3.md`](CARTAS_ACEITE_EVEN3.md).**
> Carta PDF (3 tipos) gerada por `scripts/gerar_cartas_aceite.py` (saída `assets/cartas-aceite/`, gitignored).

> **⚠️ Realidade do painel (verificada 25/06 via Chrome MCP):** os e-mails de resultado são
> **templates ÚNICOS/GLOBAIS por status** — **não** há texto por modalidade. Editor TinyMCE em:
> - **Aprovação:** `/organizador/emailtemplate/index/1`
> - **Reprovação:** `/organizador/emailtemplate/index/2`
> - (demais: aprovação com ressalva, desclassificação, comprovante — ids subsequentes)
>
> **Tags disponíveis:** `{submissao.titulo}` · `{submissao.id}` · `{submissao.data.insercao}` ·
> `{submissao.modalidade}` · `{submissao.areatematica}` · `{submissao.autores}` · `{evento.titulo}` ·
> `{evento.responsavelcomissao.nome}` · `{evento.responsavelcomissao.email}` · `{{evento.urlCliente}}`.
> Disparo via **Resultado → Divulgar Resultados** (`/organizador/trabalhocientifico/resultado/`);
> filtro por **status** (Aprovado/Não Aprovado/Divulgado/…), **não** por modalidade.

**Abordagem adotada (decisão 25/06):** **e-mail global neutro** (usa `{submissao.modalidade}`) +
**diferenciação na Carta PDF** por modalidade (gerada por `scripts/gerar_cartas_aceite.py`).

**Status (staged em 25/06):**
- ✅ **Template de aprovação (index/1)** reescrito: texto neutro (aprovação para qualquer modalidade,
  menção à carta de aceite, anais ISBN+DOI, caminho opcional do artigo completo até 30/09),
  **assinatura genérica** ("Comissão Científica" — removido `{...responsavelcomissao.nome}`).
- ✅ **Template de reprovação (index/2)** reescrito (Modelo E), mantendo o link "ACESSAR MEUS
  TRABALHOS" (`{{evento.urlCliente}}participante/trabalhocientifico`), assinatura genérica.
- ⏳ **Envio pendente:** avaliações **não finalizadas** (em 25/06: **96 submissões, 0 avaliações**).
  A divulgação/envio só ocorre após o fechamento dos resultados.

**No disparo (após avaliação):**
1. **Resultado → Divulgar Resultados**: o template global de aprovação vai a todos os Aprovados; o de
   reprovação aos Não Aprovados. Para **texto distinto por grupo** (se desejado), usar **lotes**:
   editar o template, divulgar um grupo, repetir (quem já é "Divulgado" não recebe de novo).
2. **Carta PDF (A/B/C):** gerar com o script e entregar por **link** no corpo do e-mail (ou envio
   individual pela comissão) — o envio em massa não anexa PDF único por autor.
3. **Teste antes do lote:** botão **"Enviar exemplo"** no editor de cada template.

**Mecânica confirmada (teste 25/06):** aprovar/definir resultado **sem avaliador externo** é possível —
na aba **Avaliação** (lista de trabalhos), botão **"Finalizar avaliação"** (gavel) → modal **"Parecer
final"** → SELECT (Aprovado/Não Aprovado/Desclassificado) + Justificativa → **Finalizar**. O trabalho
passa a aparecer em **Resultado** (`/organizador/trabalhocientifico/resultado/`). Lá, cada linha tem
**"Divulgar resultado"** (`divulgarResultadoIndividual`) que **divulga só aquele trabalho e envia o
e-mail** aos autores (status vai de "Não divulgado" → **"Divulgado"**); o e-mail usa o **template
global** vigente (`/emailtemplate/index/1`). Há também **"Divulgar Resultados"** (todos) e **"Notificar
autores"** (e-mail avulso por trabalho). A lista de Avaliação é paginada/ordenada por número e **cega**
(sem autores) — usar o campo **Buscar** pelo número; os autores aparecem em `editarsubmissao/{nº}` e na
aba Resultado. **A divulgação notifica TODOS os autores** do trabalho, não só o submissor.
> **Teste (25/06):** 4 Artigo Completo do organizador — **1648163, 1648166, 1648190** (Raul autor) e
> **1644279** (Raul coautor; autor principal Samuel) — todos com **parecer Aprovado** (direto) +
> **divulgados** com o template **Modelo A** (versão b). E-mail vai a **todos os autores** de cada
> trabalho. Template index/1 ficou em **Modelo A** (reverter ao neutro ao concluir os testes de artigo
> completo). Cartas PDF em `assets/cartas-aceite/carta-aceite-<nº>.pdf`. ⚠️ Esses 4 ficaram
> Aprovado/Divulgado sem avaliação real — reabrir/ajustar status depois, se necessário.

**Entrega do ofício (Carta de Aceite):** a Even3 **não anexa PDF** ao e-mail nem o "Notificar autores"
tem campo de anexo. O ofício oficial é a **Carta de Aceite nativa**: após a divulgação, o autor
**baixa na Área do Participante › Submissões**, botão **"Carta de Aceite"** (coluna Documentos) —
URL `…/participante/impressao/_impressaocartadeaceite?code=<nº>`. O **modelo** dessa carta se edita em
`/organizador/trabalhocientifico/modelocartadeaceite/` ("Documentos › Editar carta de aceite"): é
**template único** (tags `{trabalho.titulo}`, `{DADOS_AUTORES}`, `{trabalho.modalidade}`,
`{data.aceite}`, `{assinatura.comissao}`, `{evento.*}`; botão **Anexar Assinatura**). **Modelo
reescrito em 25/06** (layout 1 página): logo **horizontal** via `<img src="https://encontrogeig.org/
assets/logo-fundo-branco.png" width=440>` (substitui o `{evento.logo}`, que era quadrado/pequeno);
título **"CARTA DE ACEITE"**; corpo *"…foi **ACEITO, conforme o edital da respectiva modalidade**
({trabalho.modalidade}), no {evento.titulo}."*; linha de local/data "Rio de Janeiro / Niterói – RJ,
{data.aceite}."; assinatura formatada (**Comissão Científica** + instituições + e-mail). Logo do
evento (quadrado) também foi subido em Configuração › Organizador (resolve `{evento.logo}` em outros
docs). **Espaçamento enxuto** corrigiu a quebra em 2 páginas. ⚠️ O **cabeçalho/rodapé do navegador**
(data/URL/nº de página) ao "Imprimir/Salvar PDF" é do navegador — desmarcar "Cabeçalhos e rodapés"
na caixa de impressão; não é controlável pela Even3.
> **Atualizado em 26/06 (v3):** corpo passou a *"…foi **ACEITO PARA PUBLICAÇÃO** nos Anais do evento,
> com ISBN e DOI individual, conforme o edital da respectiva modalidade ({trabalho.modalidade}), no
> {evento.titulo} — evento científico de abrangência nacional, realizado em Niterói/RJ, **de 08 a 10
> de julho de 2026**."* (inclui a frase "aceito para publicação" alinhada ao Edital UFF e o período do
> evento, antes ausentes). A **assinatura** ganhou linha nominal **"Prof. Li Li Min"** acima de
> **"Comissão Científica"** (instituições + `comissao.cientifica@encontrogeig.org` mantidos; sem cargo
> "Professor Titular" — o "Prof." já é o tratamento). Confirmado via "Visualizar Resultado" (tags
> resolvem; 1 página). ⚠️ **Mecânica de salvar:** o editor é **inline (TinyMCE)** — alterar via JS
> `setContent` e **clicar "Salvar modelo"** (o POST redireciona p/ `…?tab=settings&config=communication`,
> sinal de sucesso). Se **não** redirecionar, o save **não** efetivou — repetir o clique e reconferir
> recarregando o modelo.
O **e-mail de aprovação (index/1)** foi atualizado (25/06) com o parágrafo **"Carta de aceite (ofício)"**
explicando como acessar (link `{{evento.urlCliente}}participante/trabalhocientifico`). As cartas PDF
custom (com hash) em `assets/cartas-aceite/` ficam como alternativa/registro, não como entrega primária.

### Aceite + divulgação em massa das demais modalidades (26/06 — v4)

> **Contexto:** os 12 **Artigo Completo** já foram tratados à parte (cartas assinadas Li Li Min enviadas
> por e-mail). Para **aprovar e notificar todas as demais submissões** (Resumo Expandido, Pôster,
> Relatório A3, Artigo (Resumo)), revertemos o modelo ao **genérico** e disparamos o aceite em massa.

**1. Carta de Aceite nativa → revertida ao genérico + data fixa + espaçamento**
(`/organizador/trabalhocientifico/modelocartadeaceite/`, editor inline TinyMCE id `editor`):
- corpo voltou a *"…foi **ACEITO, conforme o edital da respectiva modalidade** ({trabalho.modalidade}),
  no {evento.titulo}, **realizado de 08 a 10 de julho de 2026**."* (removidos "ACEITO PARA PUBLICAÇÃO",
  ISBN/DOI/abrangência nacional do corpo);
- assinatura: removida a linha **"Prof. Li Li Min"** (ficou só "Comissão Científica" + instituições + e-mail);
- espaçamento: `margin: 50px 0 30px` no título "CARTA DE ACEITE", `margin-top: 42px` na data, `52px` na assinatura;
- salvar = JS `setContent` + clicar **"Salvar modelo"** (redireciona p/ `…?tab=settings&config=communication`).

**2. E-mail de aprovação (index/1) → reescrito para NEUTRO por modalidade**
(`/organizador/emailtemplate/index/1`, editor TinyMCE id `mce_0`):
- trocado *"…ACEITE do seu **ARTIGO COMPLETO**… **ACEITO PARA PUBLICAÇÃO**…"* por
  *"…ACEITE do seu trabalho "{submissao.titulo}", na modalidade **{submissao.modalidade}**… aceito
  conforme o edital da respectiva modalidade… Anais (ISBN), dezembro de 2026, com DOI individual…"*;
- mantém a tag de link `{{evento.urlCliente}}participante/trabalhocientifico` (⚠️ o snapshot mostra o href
  resolvido absoluto, mas o conteúdo salvo guarda o placeholder relativo — está OK);
- salvar = **"Salvar modelo"** (botão fica "Carregando…" e persiste; reabrir p/ conferir).

**3. Aprovação em massa (101 pendentes) — sem enviar e-mail**
A Even3 **não tem aprovação em lote** (cada trabalho = modal "Parecer final", gavel `<i class="fa fa-gavel">`,
`ng-click="abrirModalProcesso(row.idProcesso,'mostraEmitirParecer')"`, botão Finalizar = `salvarParecer()`).
O painel é **AngularJS** com `.scope()` bloqueado. O "Finalizar" dispara:
- **`POST /organizador/trabalhocientifico/alterarstatusprocesso`** · `Content-Type: application/json`
- corpo: `{"idProcesso": <nº>, "idStatusProcesso": 3, "motivoParecer": "<texto>"}` (`3` = Aprovado;
  `idProcesso` == o **número** da submissão) · usa cookies da sessão, **sem token no corpo** ·
  resposta `{"IsValid": true, ...}`.
- Lista de pendentes coletada na aba **Avaliação** (`/avaliacaogeral/`, 2ª tabela, situação "Disponível
  para avaliação", paginação numerada); **101** trabalhos com gavel. Aprovados via `fetch` em lote (101/101).
- ⚠️ **`alterarstatusprocesso` NÃO envia e-mail** — só define o parecer (reversível). O e-mail só sai no "Divulgar".

**4. Divulgação (notificação)**
`/organizador/trabalhocientifico/resultado/` → botão **"Divulgar Resultados"** → modal "**104 Resultados
disponíveis para divulgar**" → confirmar. Envia o **template global de aprovação** (index/1, já neutro) a
**todos os autores** de cada trabalho. Quem já estava **"Divulgado"** (os 17 da leva anterior) **não** recebe
de novo. Resultado final: **121 Aprovado · 121 Divulgado · 0 pendente**.

> **Estado em 26/06:** 121 submissões aceitas e divulgadas (104 nesta leva + 17 anteriores). Modelo de carta
> e e-mail neutros valem para todas as modalidades; os 12 Artigo Completo seguem com entrega própria (PDF assinado).

### Aprovação + divulgação de submissão tardia (29/06)

Submissão **1652518** chegou em **28/06** (após a leva de 26/06): *"DA ESTAÇÃO DE TRATAMENTO À TORNEIRA:
DINÂMICA DO CLORO RESIDUAL NA REDE DE DISTRIBUIÇÃO E O PAPEL DA ATUAÇÃO DA AGÊNCIA REGULADORA…"*, modalidade
**Resumo Expandido**, área *Regulação de infraestrutura, energia e saneamento*; autores Carlos Alberto da
Silva Paulo (AGENERSA, principal) e Luis Perez Zotes (UFF). Era o **único** trabalho "Disponível para
avaliação" (gavel) na aba Avaliação. Fluxo aplicado (Chrome DevTools MCP, mesma mecânica da §"Aceite em massa"):
1. **Aprovado** via `POST /organizador/trabalhocientifico/alterarstatusprocesso` ·
   `{idProcesso:1652518, idStatusProcesso:3, motivoParecer:"…"}` → `IsValid:true` (não envia e-mail).
2. **Divulgado** em Resultado → **"Divulgar Resultados"** (modal "1 Resultado disponível") → e-mail de
   aprovação (template global neutro index/1) enviado a **todos os autores**; os 121 já "Divulgado" não
   receberam de novo.

> **Estado em 29/06:** **122 Aprovado · 122 Divulgado · 0 pendente**.

### Reabrir submissões / mover datas

1. `/organizador/trabalhocientifico/submissaogeral?tab=Configurações`
2. Clicar **Editar cronograma**
3. Usar o snippet do JS dispatch (§3) ou digitar manualmente as novas datas
4. Salvar

### Adicionar novo eixo temático

1. `/organizador/trabalhocientifico/submissaogeral?tab=Áreas%20Temáticas`
2. Clicar **+ Adicionar área temática**
3. Preencher título e salvar

### Trocar PDF de regras anexado a uma modalidade

1. `/organizador/trabalhocientifico/submissaogeral?tab=Modalidades`
2. Clicar no nome da modalidade (abre modal de edição)
3. Clicar **"Trocar regras de submissão"** (ou "Regras de submissão" se ainda não tem)
4. Upload do novo PDF
5. **Aguardar 5+ segundos** antes de clicar **Salvar Modalidade**

> Após salvar, a linha da modalidade na grade pode aparecer momentaneamente como "Defina regras de submissão" enquanto a CDN propaga — recarregar a aba confirma o novo PDF (URL muda para `static.even3.com/geral/<slug>.<hash>.pdf` com hash novo).

### Adicionar pergunta personalizada ao formulário de submissão

Confirmado: a Even3 permite campos customizados no formulário de submissão (ex.: URL do vídeo, links externos).

1. `/organizador/trabalhocientifico/submissaogeral?tab=Formulário%20de%20submissão`
2. Clicar **"+ Adicionar pergunta"**
3. Escolher tipo "Submissão" (não "Autor") e formato adequado — para URL use **Resposta curta**
4. Preencher título da pergunta
5. Recomendado marcar:
   - **Exibir resposta da pergunta para o avaliador** (para o avaliador acessar o link)
   - **Incluir instruções de preenchimento ao participante** (orientações sobre formato/visibilidade do link)
6. **Pergunta válida para todas as modalidades** já vem marcada por padrão
7. Deixar **sem obrigatoriedade** se o campo só faz sentido em algumas modalidades (ex.: vídeo só é exigido na Fase 1 / Resumo Expandido)
8. Clicar **Salvar pergunta**

### Cadastrar novo avaliador

1. `/organizador/trabalhocientifico/avaliacaogeral?tab=Avaliadores`
2. Clicar **Convidar avaliador**
3. Preencher Nome + E-mail + (opcional) modalidades/áreas
4. Clicar **Salvar avaliador**

### Republicar certificado (após mudança no template)

1. `/organizador/certificate/`
2. Linha do certificado: clicar **Despublicar** → **Alterar modelo** → editar → **Salvar Certificado**
3. Voltar à lista e clicar **Publicar**

### Gerar novo API Token

1. `/organizador/integrations/`
2. Bloco **API Even3** → **Gerenciar**
3. Clicar **+ Criar chave de acesso**, dar nome (ex: "Landing Vercel")
4. Copiar a chave gerada
5. Atualizar no Vercel: `vercel env add EVEN3_API_TOKEN production`
6. Redeploy: `vercel deploy --prod`

---

## 7. Conteúdo configurado · resumo

- **Comissão Científica:** Profa. Silvia Cristina Rufino · `comissao.cientifica@encontrogeig.org`
- **7 avaliadores** cadastrados (Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio, Silvia Cristina Rufino)
- **13 áreas temáticas** alinhadas ao projeto executivo (não as 14 que vinham com typo "Sis Sigma")
- **4 modalidades** com PDFs de regras adaptados (gerados por `scripts/gerar_regras_pdf.py`)
- **22 atividades** de programação distribuídas nos 3 dias
- **6 templates de certificado** publicados, com tags dinâmicas (`{participante.nome}`, etc.)
- **Termo LGPD obrigatório** no formulário de inscrição (consentimento + cessão de imagem)
- **CSS custom** no hotsite (paleta navy/yellow/green/blue alinhada ao logo)

Detalhes do conteúdo factual: ver [`CONTENT.md`](CONTENT.md).

---

## LGPD — texto revisado do checkbox e pendências (12/06/2026)

Pacote LGPD criado em 12/06: página pública `/privacidade/` no site + 3 documentos em `docs/lgpd/`
(termo de imagem/voz, aviso de gravação/transmissão A4, política de guarda e retenção). Gerados por
`scripts/gerar_docs_lgpd.py`.

**Texto do checkbox LGPD — ✅ APLICADO em 12/06/2026** (campo "Consentimento LGPD e cessão de
imagem", obrigatório, válido para todas as entradas; substituiu o termo antigo que ainda citava a
Escola de Regulação e o e-mail desativado contato@encontrogei.com.br). Texto aplicado (versão
estendida do checkbox com controladoras, prazo de 5 anos e DPO):

> Li e concordo com a Política de Privacidade do Encontro GEI (encontrogeig.org/privacidade).
> Estou ciente de que o evento será gravado, fotografado e transmitido ao vivo, e autorizo,
> gratuitamente, o uso da minha imagem, voz e nome nos registros e materiais institucionais e
> científicos do evento, sem finalidade comercial, nos termos da Lei nº 13.709/2018 (LGPD) e do
> art. 20 do Código Civil. Meus dados de inscrição serão tratados pela organização (AGENERSA e
> UFF, controladoras conjuntas) e pela Even3 (operadora) exclusivamente para gestão da minha
> participação, emissão de certificados e publicação dos anais, pelo prazo de 5 anos. Posso
> exercer meus direitos (acesso, correção, eliminação, portabilidade e revogação) pelo e-mail
> contato@encontrogeig.org — encarregado (DPO): Prof. Alexandre Beraldi Santos
> (alexandreberaldisantos@id.uff.br).

**Pendências Even3:**
- [x] Aplicar o checkbox revisado no formulário de inscrição — feito 12/06 (página /privacidade/ no ar)
- [x] Corrigir descrição da entrada "Presencial Completo" ("três dias" → Dias 1 e 3) — feito 12/06
- [x] Publicar a inscrição das Visitas Técnicas D2 — feito 24/06. **Modelo corrigido no mesmo dia:** as
  4 entradas de visita foram **substituídas por Atividades** (inscrição em atividades), pois entrada
  duplicada dava "Participante já está inscrito" (Even3 = 1 inscrição/pessoa). 4 visitas como Atividade
  "Visita Técnica" Gratuita + vagas 43/39/26/38, máx. 1/pessoa, janela até 01/07, restrito a inscritos.
  Site aponta para o link direto `/participante/sessions/` (commit ca9c538). Ver §6 e §9.
- [x] Alinhar limite de vagas presencial — ajustado para 400 no painel em 12/06 (igual ao site)
- [x] Capacidade presencial ampliada de **400 → 500** vagas em 24/06 via Chrome MCP (a entrada havia
  esgotado em 400/400 inscritos). Site, edital e CONTENT.md atualizados para 500 no mesmo dia.
- [x] Ficha de avaliação de reação — complemento gratuito "Questionário de avaliação do evento"
  instalado e configurado em 12/06 (21 perguntas; rascunho em `/organizador/questionnaire/`).
  Envio automático aos participantes ao final do evento. **Publicar próximo ao evento.**
- [x] Certificado de Participação com arte personalizada (fundo 1754×1240 gerado por
  `scripts/gerar_fundo_certificado.py`, em `assets/certificado/`) — aplicado e salvo em 12/06
- [x] Arte replicada nos 6 certificados em 12/06 (Participação, Atividade, Convidado, Submissão,
  Apresentação, Avaliador) — upload do mesmo fundo via "Imagem de Fundo > Anexar imagem" em cada editor
- [x] Restrição de autores confirmada em 12/06: máx. **4 autores por submissão** (global, vale p/ as
  4 modalidades) + "todos os autores inscritos" (Recebimento > Configurações > Restrições).
  Estratégia +1 após o pico: elevar para 5 nesse mesmo campo após 16/06, se decidido

**Pendências jurídicas:** acordo entre controladoras conjuntas (minuta) e lista nominal de acessos
ao painel Even3. Já preenchidos em 12/06: CNPJ/endereço AGENERSA (07.694.194/0001-11) e UFF
(28.523.215/0001-06), encarregado (DPO) = Prof. Alexandre Beraldi Santos
(alexandreberaldisantos@id.uff.br), prazos de retenção (inscrição/presença 5 anos; e-mails 2 anos).

> Nota 12/06: todos os placeholders `[A VALIDAR]` foram removidos dos documentos a pedido do
> organizador. As menções à **minuta do acordo entre controladoras** e à **lista nominal de
> acessos** foram retiradas/suavizadas na política de guarda — **reintroduzir** essas seções quando
> o jurídico definir os textos. O QR code do cartaz foi gerado e incorporado (página 1 do aviso A4).

---

## 9. Descrições canônicas das jornadas (espelho do site)

> **Regra:** o **Resumo/Descrição** da Atividade na Even3 (texto de "Mais informações") deve ter **as
> mesmas informações do site** (modais `#modal-jornadaN` em `index.html`). Ao mudar o site, atualizar
> aqui e na Even3. Vagas/horários devem bater com a configuração da atividade. Atualizado 24/06.

**J01 · Petrobras UTE TermoRio** — 09/07 · 43 vagas
> Dia 2 · Visita técnica à Usina Termelétrica TermoRio, no Complexo Petroquímico de Duque de Caxias,
> operada pela Petrobras. Programação: café de boas-vindas, briefing de segurança e recepção do gerente
> da planta, apresentação da usina no auditório e visita à área industrial.
> Ponto de encontro: AGENERSA — Av. Presidente Wilson, 231 (Ed. Palácio Austregésilo de Athayde),
> Centro, Rio de Janeiro. Saída estimada: 07h30 · Retorno previsto: ~13h30. Capacidade: 43 visitantes
> (ônibus).

**J02 · ETA Guandú + EE Lameirão (CEDAE)** — 09/07 · 39 vagas
> Dia 2 · Visita técnica integrada operada pela CEDAE: palestra institucional no auditório, Estação de
> Tratamento de Água do Guandú, macromedidores e pontos de entrega, e a Estação Elevatória do Lameirão.
> Ponto de encontro: CEDAE — Av. Presidente Vargas, 2655, Centro, Rio de Janeiro. Saída estimada: 08h ·
> Retorno previsto: 18h. Capacidade: 39 visitantes. Inclui coffee break e transporte; almoço não
> incluído (restaurante próximo).

**J03 · ETE Icaraí + Camboinhas (Águas de Niterói)** — 09/07 · 26 vagas
> Dia 2 · Visita técnica integrada às Estações de Tratamento de Esgoto Icaraí e Camboinhas, operadas
> pela Águas de Niterói. Inclui apresentação institucional, Centro de Controle Operacional, almoço e a
> planta de pirólise.
> Ponto de encontro: AGENERSA — Av. Presidente Wilson, 231 (Ed. Palácio Austregésilo de Athayde),
> Centro, Rio de Janeiro. Saída estimada: 09h · Retorno previsto: 17h30. Capacidade: 26 visitantes
> (microônibus). EPI: informe tamanho de jaleco e numeração de bota no campo de observações da
> inscrição, se aplicável.

**J04 · Braskem** — 09/07 · 38 vagas
> Dia 2 · Visita técnica às unidades industriais da Braskem no Polo Petroquímico de Campos Elíseos —
> Duque de Caxias/RJ. A Braskem é uma companhia petroquímica global, com portfólio completo de resinas
> plásticas e produtos químicos para diversos segmentos (embalagens, construção civil, automotivo,
> agronegócio, saúde e higiene, entre outros), com unidades no Brasil, EUA, México e Alemanha e
> exportação para mais de 71 países. Inclui apresentação institucional e tour pela planta industrial.
> Ponto de encontro: AGENERSA — Av. Presidente Wilson, 231 (Ed. Palácio Austregésilo de Athayde),
> Centro, Rio de Janeiro. Saída estimada: 08h · Retorno previsto: ~12h. Capacidade: 38 visitantes
> (ônibus). EPI obrigatório: jaleco e bota de segurança. Requisitos: a Braskem exige nome, cargo,
> instituição, CPF e tamanhos de jaleco e bota — nome, instituição e CPF já constam da inscrição;
> informe cargo, jaleco e bota no campo de observações da inscrição.

---

## 10. Comunicado/e-mail em massa aos inscritos ("Notificar pessoas")

> **Correção:** a Even3 **TEM** disparo de e-mail a todos os inscritos (não só comunicados de
> submissão). Fica em **Pessoas → "Notificar pessoas"** (`/organizador/people/`). Descoberto e usado
> em 01/07/2026 para a divulgação das Visitas Técnicas.

**Fluxo (painel do organizador, evento 722003):**
1. **Pessoas → "Notificar pessoas"**. Na 1ª vez pede **validar o e-mail** da conta (código enviado a
   `raularaujo@crie.ufrj.br`; o código chega em segundos).
2. Abre o compositor **"Envio de e-mail"** com: **Conteúdo** (Criar do zero / templates prontos),
   **Situação** (público) + **Categoria**, **Tipo de envio** (texto / imagem), **Assunto** e **Mensagem**.
3. **Público:** `Situação = Inscritos` + `Categoria = Todas as categorias` = **todos os confirmados**
   (presencial + online). Outras opções úteis: "Inscrito no evento e sem atividades" (quem ainda não
   escolheu jornada/atividade), "Autores", etc.
4. **Mensagem:** o editor é **Summernote** (WYSIWYG) e **aceita HTML** — dá para colar HTML com estilos
   inline (títulos coloridos, blocos, botões-link). A Even3 embrulha com **logo do evento (topo)** e
   **rodapé com contato + descadastro (LGPD)** automaticamente, então a peça foca no conteúdo.
5. **"Pré-visualizar"** abre o render final; **"Envio de exemplo"** manda 1 amostra ao e-mail da conta
   organizadora (`raularaujo@crie.ufrj.br`) — usar para validar antes; **"Enviar Mensagem"** dispara ao
   grupo (confirmação: *"Estamos notificando o grupo... você será notificado por e-mail ao finalizar"*).
6. Remetente: **`message@organizer.even3.com`** (infra aquecida da Even3 → baixo risco de spam; entrega
   na caixa de entrada confirmada no teste). Sem necessidade de manusear e-mails/PII fora da plataforma.

**Campanha de divulgação das Visitas Técnicas (01/07/2026):**
- Público: **Inscritos → Todas as categorias** (≈ **513 confirmados**; 428 presencial + 84 online).
- Assunto: `Visitas Técnicas (09/07) do 1º Encontro GEI — inscrições até 07/07`.
- Peça HTML (4 jornadas J01–J04 + link único de inscrição): `docs/email/divulgacao-visitas-tecnicas.html`
  (+ `.txt` e `README.md`). Motivo: em 01/07 havia **0 inscrições nas visitas** e 146 vagas abertas.
- Teste (envio de exemplo) validado na caixa de entrada; disparo geral confirmado no painel.

---

## 8. Recursos externos

- Documentação oficial: https://docs.even3.com.br/
- Central de Ajuda: https://ajuda.even3.com.br/hc/pt-br
- Sitemap da API: https://docs.even3.com.br/sitemap
- Sobre embed do Even3 no site: https://ajuda.even3.com.br/hc/pt-br/articles/360004093772
