# Mapa Estruturado dos Módulos Configuráveis da Even3

> Fonte: docs.even3.com.br (sitemap oficial: readme, autenticacao, pessoas, evento, pagamentos, programacao, submissao, empresas, pagina-do-evento, credenciamento, certificados, models, api-fgv) + ajuda.even3.com.br (Central de Ajuda).
> "(?)" indica recurso citado oficialmente mas com path do painel não confirmado nesta varredura.

---

## A. PRÉ-EVENTO

### A1. Configuração geral do evento
- **Nome:** Configurações do Evento
- **URL:** `/organizador/.../configuracoes` (Configurações > Evento) (?)
- **O que é:** Metadados centrais do evento — título, datas (início/fim), local físico (país/estado/cidade/venue + lat/long), datas de inscrição, descrição (`summary` + `description`), banner/imagem, carga horária (`credit_hour`), tipo (presencial/online/híbrido), URL amigável, idioma.
- **Obrigatório:** título, datas (start/end), local (mesmo que online), organizador, URL amigável, datas de inscrição.
- **Opcional:** descrição/resumo, banner, lat/long, palavras-chave, redes sociais, carga horária.
- **Pré-requisitos:** conta Even3 (organizador) já criada.

### A2. Inscrições — Entradas/Categorias
- **Nome:** Inscrições > Entradas (categorias/tickets)
- **URL:** `/organizador/.../inscricoes` (?)
- **O que é:** Modalidades de inscrição (`tickets`) com `title`, `registration_quantity` (limite), e `prices` (lotes com data/valor).
- **Obrigatório:** ao menos 1 entrada (mesmo gratuita).
- **Opcional:** múltiplos lotes, limite de vagas, valores diferenciados.
- **Pré-requisitos:** A1.

### A3. Inscrições — Formulário customizado e campos pessoais
- **Nome:** Inscrições > Formulário / Campos personalizados
- **O que é:** Campos coletados na inscrição (nome, email, CPF, instituição, etc.) e campos extras customizados; formulário internacional (sem CPF) para estrangeiros.
- **Obrigatório:** nome + email.
- **Opcional:** CPF, instituição, campos custom, formulário multi-idioma.
- **Pré-requisitos:** A2.

### A4. Inscrições — Restrições (categorias/instituições/listas)
- **Nome:** Restrição de Inscrição / Entradas exclusivas
- **O que é:** Lista exclusiva (nome/email/CPF) que limita quem pode se inscrever em determinada categoria; também restringe quais atividades cada categoria acessa.
- **Obrigatório:** Não.
- **Opcional:** Sim.
- **Pré-requisitos:** A2 + A3.

### A5. Inscrições — Cupons de desconto
- **Nome:** Cupons de Desconto (Inscrições > Cupons)
- **O que é:** Códigos alfanuméricos com % ou valor fixo, aplicáveis a uma ou todas as categorias; também há cupons para atividades.
- **Obrigatório:** Não.
- **Opcional:** Sim.
- **Pré-requisitos:** A2 (e A8 para inscrições pagas).

### A6. Página do Evento (hotsite)
- **Nome:** Página do Evento
- **URL:** `/organizador/.../pagina-do-evento` (?)
- **API:** `GET /api/v1/hotsite/`
- **O que é:** Áreas configuráveis: Sobre, Inscrições, Atividades (programação), Palestrantes, Submissões, Local, Patrocinadores (com imagem/título/link), Seções customizadas (jsonObj livre). Cada área tem título/subtítulo/ordem.
- **Obrigatório:** título + áreas mínimas (Sobre, Inscrições).
- **Opcional:** Patrocinadores, customizadas, banners, CSS custom (?), logo.
- **Pré-requisitos:** A1.

### A7. Programação / Atividades
- **Nome:** Programação > Atividades
- **URL:** `/organizador/.../programacao` (?)
- **API:** `GET /api/v1/session/:id`, `getschedule`
- **O que é:** Sessões com `title`, `description`, `type` (Conferência, Workshop, Mesa-redonda…), `venue` (auditório), `date`, `start_time`/`end_time`, `credit_hour`, `capacity`, `ticket_price`, `tags`, palestrantes vinculados.
- **Obrigatório:** ao menos 1 atividade para evento científico funcional; data/horário/título.
- **Opcional:** capacidade, preço por atividade, tags, vincular palestrante.
- **Pré-requisitos:** A1; A8 (para vincular palestrantes); A2 (para atividades pagas/restritas).

### A8. Convidados / Palestrantes
- **Nome:** Convidados (Speakers)
- **URL:** `/organizador/.../convidados` (?)
- **API:** `GET /api/v1/speaker/:id`
- **O que é:** `name`, `photo`, `resume` (mini-bio), `email`, redes (`facebook`, `linkedin`, `twitter`, `lattes`, `site`).
- **Obrigatório:** Não, mas necessário para vincular em A7 e emitir certificado A14.
- **Opcional:** redes sociais, foto.
- **Pré-requisitos:** A1.

### A9. Organizadores / Equipe
- **Nome:** Adicionar Organizadores
- **O que é:** Equipe gestora (nome + email) com permissões por área.
- **Obrigatório:** 1 organizador (criador).
- **Opcional:** organizadores adicionais.
- **Pré-requisitos:** A1.

### A10. Submissões científicas
- **Nome:** Submissão de Trabalhos
- **URL:** `/organizador/.../submissoes` (Submissões > Recebimento / Avaliação / Configurações) (?)
- **API:** `GET /api/v1/submission/`, `/list`
- **O que é:**
  - **Modalidades** (`id_submissiontype`): texto livre ou upload de arquivo (ex.: Artigo, Resumo Expandido, Pôster) com `url_roles` (PDF de regras anexável).
  - **Áreas Temáticas / Eixos** (`id_topicarea`).
  - **Cronograma:** período de submissão e período de revisão.
  - **Comissão Científica / Avaliadores:** cadastro de avaliadores e atribuição.
  - **Critérios de avaliação:** notas e parecer (configurados no menu Avaliação).
  - **Restrições:** quem pode submeter (limite por autor, instituição) (?).
  - **Comunicação por email:** templates de aceite/recusa/ajuste.
  - **Repasse de custo de submissão:** definido em Configurações.
- **Obrigatório (se houver submissão):** modalidade, área temática, cronograma, formulário.
- **Opcional:** comissão científica, critérios, custo, regras em PDF.
- **Pré-requisitos:** A1 + A8 (para avaliadores) + A18 (para custo).

### A11. Configuração financeira
- **Nome:** Perfil > Chaves Pix e dados bancários / Mercado Pago
- **O que é:** Cadastro da conta para repasse (Pix ou conta bancária); integração Mercado Pago; integração eNotas para nota fiscal automática.
- **Obrigatório (eventos pagos):** dados bancários/Pix.
- **Opcional:** eNotas (NF-e), Mercado Pago (vs. gateway padrão Even3).
- **Pré-requisitos:** A2 com entrada paga.
- **Nota:** Even3 retém taxa (~25% no exemplo da doc, varia por plano).

---

## B. EVENTO

### B1. Credenciamento
- **Nome:** Credenciamento (Área de Credenciamento)
- **URL:** `/organizador/.../credenciamento` (?)
- **API:** `POST /api/v1/checkin/attendees`, `POST /api/v1/checkin/sessions`
- **O que é:** Check-in geral via QR code (cada inscrito tem `checkin_code`) e check-in por sessão; leitor mobile via app Even3 Organizador.
- **Obrigatório (presencial):** habilitar; gerar credenciais.
- **Opcional:** check-in por sessão (necessário para certificado por presença).
- **Pré-requisitos:** A2 + inscritos confirmados.

### B2. Transmissão online (Even3 Streaming)
- **Nome:** Even3 Streaming / Transmissão Online por Atividade
- **O que é:** Player nativo na plataforma Even3 (gravação até 30 dias). Alternativas: link YouTube (privado para inscritos), Zoom, Google Meet, Streamyard. Suporta Simulive (pré-gravado como ao vivo) e tradução simultânea.
- **Obrigatório (online/híbrido):** sim.
- **Opcional:** Even3 Streaming pago (vs. YouTube grátis), gravação, tradução.
- **Pré-requisitos:** A7 (atividades cadastradas para vincular link).

### B3. Chat de participantes
- **Nome:** Chat (em transmissões/atividades online) (?)
- **O que é:** Chat por sala/atividade com moderação.
- **Obrigatório:** Não.
- **Opcional:** Sim (componente da transmissão online).
- **Pré-requisitos:** B2.

---

## C. PÓS-EVENTO

### C1. Certificados
- **Nome:** Certificados
- **URL:** `/organizador/.../certificados` (?)
- **API:** `GET /api/v1/certificates`
- **Tipos:** Participação (todos inscritos ou só credenciados), Atividade (1 por sessão), Submissão (autores aprovados ou só apresentadores), Convidado/Palestrante, Organização, Avaliador.
- **Configuráveis:** modelo (imagem de fundo + texto), Tags dinâmicas (`{participante.nome}`, etc.), regras (presença mínima, tarefas), QR de validação automático Even3, modelo de email de envio.
- **Obrigatório:** Não para o evento rodar; Sim para entregáveis acadêmicos.
- **Pré-requisitos:** B1 (presença), A10 (submissões), A8 (palestrantes), A9 (organização).

### C2. Anais com ISBN/DOI (Even3 Publicações)
- **Nome:** Even3 Publicações / Anais Online
- **O que é:** Compilação dos trabalhos aprovados em anais publicados; solicitação de **ISBN** (publicação como um todo) e **DOI** (por trabalho — ~48h úteis); ISSN para periódicos.
- **Obrigatório:** Não.
- **Opcional:** Sim — produto à parte.
- **Pré-requisitos:** A10 com trabalhos aprovados.

### C3. Avaliação do evento
- **Nome:** Pesquisa/Questionário de Satisfação (?)
- **O que é:** Formulário de feedback enviado aos participantes pós-evento.
- **Obrigatório:** Não.
- **Opcional:** Sim.
- **Pré-requisitos:** B1.

---

## D. INTEGRAÇÕES E COMUNICAÇÃO

### D1. API Even3
- **Nome:** API (Configurações > Integrações)
- **O que é:** Token único por evento (`Authorization-Token`) que habilita os endpoints REST (`/api/v1/event`, `attendees`, `submission`, `session`, `certificates`, `checkin`, `payments`, `hotsite`, `custom/getdata` para LGPD).
- **Obrigatório:** Não.
- **Opcional:** Sim — integrações externas e site próprio.
- **Pré-requisitos:** A1.

### D2. Webhooks
- **Nome:** Webhook Even3 (Configurações > Integrações > Webhook)
- **O que é:** URL(s) destino + triggers selecionáveis; Even3 envia POST quando ações ocorrem; usa códigos HTTP padrão (4xx para erro de token).
- **Obrigatório:** Não.
- **Pré-requisitos:** A1.

### D3. Comunicação / Email
- **Nome:** Comunicação (templates de email + envio em massa)
- **O que é:** Templates editáveis: confirmação de inscrição, recuperação de senha, lembrete, certificado, comunicação de submissão (aceite/ajuste/recusa). Envio segmentado por categoria/status.
- **Obrigatório:** Os transacionais já vêm configurados.
- **Opcional:** Edição de modelos, campanhas em massa.
- **Pré-requisitos:** A2.

### D4. Tracking — Google Analytics 4
- **Nome:** Configurar GA4 (Integrações)
- **O que é:** Cola o ID `G-XXXXXXXX` no painel; rastreia tráfego do hotsite.
- **Obrigatório:** Não.
- **Pré-requisitos:** A6 publicada.

### D5. Tracking — Pixel Meta (Facebook/Instagram)
- **Nome:** Pixel do Meta
- **O que é:** ID do pixel; rastreia visitas e conversões; verificação no Events Manager.
- **Obrigatório:** Não.
- **Pré-requisitos:** A6.

### D6. Multi-idiomas
- **Nome:** Módulo Multi-idiomas
- **O que é:** Tradução completa do hotsite em até 3 idiomas escolhidos; alternativa automática via Google Translate; formulário internacional sem CPF.
- **Obrigatório:** Não.
- **Opcional:** Sim — eventos internacionais.
- **Pré-requisitos:** A6.

### D7. eNotas (Nota Fiscal)
- **Nome:** Integração eNotas
- **O que é:** Emissão automática de NFS-e por inscrição paga.
- **Obrigatório:** Não.
- **Pré-requisitos:** A11 + entradas pagas.

### D8. Embed Even3 no site próprio
- **Nome:** Incluir Even3 dentro do meu site / Redirecionar
- **O que é:** Iframe do hotsite ou redirect de domínio.
- **Obrigatório:** Não.
- **Pré-requisitos:** A6.

---

## E. RESTRIÇÕES E CONFIGURAÇÕES AVANÇADAS

### E1. LGPD / Termos / Privacidade
- **Nome:** Configurações de Privacidade + endpoint LGPD (`/api/v1/custom/getdata` com logs)
- **O que é:** Termo de uso e política de privacidade exibidos na inscrição; logs de consentimento LGPD acessíveis via API custom.
- **Obrigatório:** Termos padrão Even3 sempre aceitos; customizar é opcional.
- **Pré-requisitos:** A1.

### E2. Restrições de submissão
- **Nome:** Configurações de Submissão > Restrições
- **O que é:** Limites por autor, vínculo institucional obrigatório, modalidades exclusivas a categorias de inscrição.
- **Obrigatório:** Não.
- **Pré-requisitos:** A10.

### E3. Páginas customizadas
- **Nome:** Seções customizadas do hotsite (FAQ, Regulamento, Sobre extra)
- **O que é:** Áreas livres em A6 com `jsonObj` para conteúdo arbitrário.
- **Obrigatório:** Não.
- **Pré-requisitos:** A6.

---

## Mapa de dependências (resumo)

```
A1 (Evento) → A2 (Entradas) → A3 (Form) → A4 (Restrição) / A5 (Cupom)
A1 → A6 (Hotsite) → D4/D5/D6/D8/E3
A1 → A8 (Speakers) → A7 (Programação) → B2 (Streaming) → B3 (Chat)
A1 → A9 (Organizadores)
A1 → A10 (Submissões) → C2 (Anais)
A2 → A11 (Financeiro) → D7 (eNotas)
A2 → B1 (Credenciamento) → C1 (Certificados) → C3 (Avaliação)
A1 → D1 (API) → D2 (Webhooks)
```

## Mínimo viável para evento científico-acadêmico end-to-end

Obrigatórios: **A1, A2, A3, A6, A7, A9, A10** (se houver trabalhos), **A11** (se pago), **B1**, **C1**.
Resto é opcional/aprimoramento.

---

## Fontes consultadas

- docs.even3.com.br: readme, autenticacao, evento, pagamentos, programacao, submissao, pagina-do-evento, credenciamento, certificados.
- ajuda.even3.com.br: artigos sobre cupons, restrições, certificados (modelos/tags), Even3 Streaming, GA4, Pixel Meta, Webhook, Multi-idiomas, eNotas, Anais/ISBN/DOI, Mercado Pago.
