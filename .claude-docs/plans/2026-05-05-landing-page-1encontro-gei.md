# Plano — Landing Page do 1º Encontro GEI (08–10 Jul 2026)

## Context

O **1º Encontro de Governança, Estratégia e Inovação Governamental** acontece de 08 a 10 de julho de 2026 (RJ + Niterói), com 400+ participantes, 4 trilhas oficiais (Lean Six Sigma Congress 13ª ed., SSEP 4ª ed., Sem. Regulação 2ª ed., Sem. Inteligência Governamental 1ª ed.), 8 visitas técnicas e anais com ISBN. **Deadline crítico: submissão Fase 1 em 15/05/2026 (~10 dias)** — exige landing publicada o quanto antes para abrir inscrições e chamada de trabalhos.

Realização: UFF, ABAR, PPGEP/UFF, Escola de Regulação. Parceiros: Firjan, IBP, ANP, Agenersa, Fecomércio, CAU, CREA-RJ.

**Decisões aprovadas pelo usuário:**
- Arquitetura: **Landing externa + embeds Even3** (máx. controle visual + backend robusto)
- Hosting: **Vercel + GitHub CI/CD**
- Prioridade: **URGENTE — antes de 15/05/2026**

## Arquitetura

```
encontrogei.com.br (Vercel)         Even3 (subdomínio)
┌──────────────────────────┐        ┌────────────────────────┐
│ Landing HTML estática    │        │ encontrogei.even3.com  │
│  (identidade visual:     │ embed →│ • Inscrição            │
│   Navy/Gold + logo)      │ embed →│ • Submissão de trabalho│
│  • Hero, dias, trilhas   │ embed →│ • Programação completa │
│  • Visitas, parceiros    │ link  →│ • Certificados / Anais │
│  • CTAs → embeds Even3   │        │ • API REST (admin)     │
└──────────────────────────┘        └────────────────────────┘
```

**Por que essa arquitetura:**
- Even3 oferece embed oficial de 4 áreas (Inscrição, Programação, Submissão, Convidados) via `<div>+<script>` documentado em `ajuda.even3.com.br/.../incluir-a-even3-dentro-do-meu-site`.
- Custo zero (Even3 cobra 10% só em inscrições pagas; este evento é gratuito).
- Anais ISBN/DOI nativos (Even3 Publicações — orçamento à parte).
- Certificados e credenciamento QR já estão no escopo (a documentação cita "Eventtree" mas Even3 cobre a mesma função).

## Reuso

- **`landing_page_evento_21-04 (1).html`** — draft completo já existe (499 linhas, 9 seções funcionais). Servirá de base; só precisamos ajustar identidade visual, trocar formulário inline pelos embeds Even3 e empacotar para Vercel.
- **`book_patrocinadores_21-04 (1).html`** — usar como sub-página `/patrocinadores` (modelo "Quatro Moedas").
- **Logo + paleta** — extrair do `Esboço da arte.pdf` e WhatsApp images (Navy `#0E2246`, Blue `#1B4C8E`, Gold `#C8A44A`, Cormorant Garamond + Outfit conforme briefing).

## Estrutura do site (sessões da landing)

Mantém a estrutura do draft existente, com ajustes:

1. **Nav fixa** — logo + Programação · Trilhas · Visitas · Parceiros · Submissão · **[Inscreva-se]** (CTA gold → embed Even3)
2. **Hero** — título + badge "08–10 Jul 2026 · RJ", métricas (4 eventos, 8 visitas, 13 eixos, 400+, 24h, ISBN), CTAs duplos
3. **Conferência magna** — Magda Chambriard (Petrobras, a confirmar) + painelistas
4. **Stats strip** — 5 métricas-chave
5. **3 Dias da Programação** — card por dia (Abertura · Visitas · Trilhas)
6. **4 Trilhas oficiais** (Eventos integrados) — A Lean6σ · B SSEP · C Regulação · D Inteligência Gov.
7. **8 Visitas Técnicas** — Petrobras · Águas do Rio+ETE · Guandu · Ternium · Gerdau · Eneva+TAG · IRM+Agenersa · CSN
8. **Parceiros** — grid Realização (4) + Parceiros institucionais (7)
9. **Certificação** — UFF, ABAR, PPGEP, Escola de Regulação · Lattes · ISBN dez/2026
10. **Submissão de trabalhos** — 13 eixos + deadlines + CTA "Submeter via Even3" (embed ou link)
11. **Inscrição** — substituir form fake do draft pelo **embed oficial Even3** (`<div id="even3-...">+<script>`)
12. **Patrocínio "Quatro Moedas"** (nova seção curta) — link para `/patrocinadores` com book completo
13. **Footer** — contatos institucionais + redes

## Etapas de execução (URGENTE — execução completa pelo Claude)

> **Modo de execução:** o usuário já está logado na Even3 no browser local. Vou conduzir o setup **via Chrome DevTools MCP** (`mcp__chrome-devtools__*`) navegando, clicando e preenchendo campos como um operador humano. Caminho alternativo via **API REST** descrito abaixo caso o MCP esbarre em algum fluxo.

### Fase 1 — Setup Even3 via Chrome DevTools MCP (Dia 1, ~2h)

**Pré-requisito:** confirmar que o Chrome está aberto e logado em `app.even3.com.br`. Se eu listar páginas com `list_pages` e não houver sessão Even3, peço para o usuário fazer login.

**Sub-etapas (cada uma vira task):**

1. **Navegar para "Criar evento"** (`navigate_page` → `https://app.even3.com.br/evento/criar`)
2. **Preencher metadados básicos** (`fill_form`):
   - Nome: "1º Encontro de Governança, Estratégia e Inovação Governamental"
   - Datas: 08/07/2026 a 10/07/2026
   - Local: "Rio de Janeiro / Niterói — RJ" (multi-local)
   - Categoria: Acadêmico/Científico
3. **Upload de logo + banner** (`upload_file`) — extrair primeiro do `Esboço da arte.pdf` para `assets/logo.png`
4. **Configurar identidade visual** (`navigate_page` → CSS avançado): colar paleta navy/gold + fontes Cormorant Garamond/Outfit
5. **Criar 4 modalidades de inscrição** (loop `click` + `fill`):
   - Presencial completo (3 dias) · gratuito · vagas: 400
   - Presencial Dias 1+3 · gratuito · vagas: 200
   - Remoto / Online · gratuito · ilimitado
   - Visitante Dia 2 (visita técnica) · gratuito · vagas: 200
6. **Criar campo customizado "Jornada técnica"** (8 opções, vagas limitadas por jornada — Petrobras 25, Águas+ETE 25, Guandu 25, Ternium 25, Gerdau 25, Eneva+TAG 25, IRM+Agenersa 25, CSN 25)
7. **Configurar Submissão de trabalhos**:
   - 13 eixos temáticos (lista completa do draft)
   - 2 fases: Fase 1 (resumo 2-4pp + vídeo 5min) deadline 15/05; Fase 2 (artigo completo) deadline 30/09
   - Campos: título, autores, eixo, resumo, upload PDF, URL vídeo, palavras-chave
8. **Configurar Programação** — adicionar 3 dias com placeholders das atividades já definidas no draft
9. **Configurar Convidados/Palestrantes** — Magda Chambriard (a confirmar), painelistas Callado, Li Li Min, Raul, Vladimir, mediador Miguel
10. **Coletar embed codes** (`navigate_page` → "Configurações > Incluir Even3 no meu site" → `take_snapshot`):
    - Embed: Inscrição (botão + aba)
    - Embed: Submissão de trabalhos
    - Embed: Programação
    - Embed: Palestrantes
11. **Gerar API Token** (Configurações > Integrações > API): copiar `Authorization-Token` para uso opcional futuro (contador ao vivo de inscritos)
12. **Publicar evento** + capturar URL pública (`encontro-gei.even3.com.br` ou similar)

**Onde o usuário gera coisas manualmente (se Chrome MCP falhar):**
- **API Token Even3:** painel do evento → menu lateral → **Configurações > Integrações > API** → "Gerar token". Aparece como `Authorization-Token: <chave>`.
- **Domínio próprio:** Configurações > Domínio do evento → apontar CNAME do registro `.com.br` para `apps.even3.com.br`.

### Caminho alternativo: API REST Even3
Caso algum passo da UI esteja bloqueado/diferente do esperado, posso usar a API:
- Base: `https://api.even3.com.br/v1/`
- Header: `Authorization-Token: <token-do-evento>`
- `POST /attendees/create` para criar inscrições teste, `GET /attendees` para listar
- Limitação: API não cobre criação inicial do evento nem submissões — só inscrições/listagem. Setup inicial **precisa** ser via UI/MCP.

### Fase 2 — Landing externa (Dia 1-2, ~6h)
**Arquivo principal:** `index.html` (HTML estático self-contained, padrão AGENERSA Mapa)

Modificações sobre o draft existente:
1. **Identidade visual** — alinhar com briefing:
   - Trocar `Playfair Display`/`DM Sans` por `Cormorant Garamond`/`Outfit`
   - Confirmar paleta `#0E2246` (navy) + `#1B4C8E` (blue) + `#C8A44A` (gold)
   - Inserir logo oficial do `Esboço da arte.pdf` (extrair PNG/SVG) no nav e hero
2. **Substituir form fake (linhas 437-477)** pelos embeds Even3:
   - Snippet Even3 "Aba de Inscrição" dentro de `<section id="inscricao">`
   - Snippet Even3 "Submissão" dentro de `<section id="trabalhos">` (substituir `<a href="#inscricao">`)
3. **Adicionar tracking** — GA4 (`G-XXXXX`) + Meta Pixel via `<head>` (campos nativos Even3 também, mas redundância garante landing externa coberta)
4. **Política de privacidade / LGPD** — link no footer (Even3 já cobre o lado backend)
5. **Acessibilidade** — alt em todas imagens, contraste WCAG AA verificado, navegação keyboard-only (já está bom no draft)

### Fase 3 — Sub-página patrocinadores (Dia 2, ~1h)
- Reaproveitar `book_patrocinadores_21-04 (1).html` como `patrocinadores/index.html`
- Ajustar paleta/fontes para casar com landing
- Linkar a partir da seção "Quatro Moedas" da landing

### Fase 4 — Deploy (Dia 2, ~1h)
1. `git init` na pasta atual + `.gitignore` (excluir .docx, .pptx, .pdf, .jpeg)
2. Criar repo `RaulAraujoSilva/encontro-gei` (privado ou público) no GitHub
3. Push + conectar Vercel (auto-deploy)
4. Configurar domínio (sugestão: `encontrogei.vercel.app` inicial; depois apontar `.com.br` se contratado)
5. Smoke test: embed Even3 carrega, formulário Even3 abre, links de visitas funcionam, mobile responsivo

### Fase 5 — Validação (Dia 3, ~2h)
- Submeter inscrição teste no embed → verificar se cai no painel Even3
- Submeter trabalho teste → verificar fluxo até confirmação
- Lighthouse: performance >85, acessibilidade >90, SEO >90
- Compartilhar URL com 2-3 stakeholders (UFF/ABAR/AGENERSA) para revisão

## Arquivos críticos

| Arquivo | Ação |
|---|---|
| `index.html` | **CRIAR** a partir do draft `landing_page_evento_21-04 (1).html` com ajustes |
| `patrocinadores/index.html` | **CRIAR** a partir do `book_patrocinadores_21-04 (1).html` |
| `assets/logo.svg` (ou `.png`) | **EXTRAIR** do `Esboço da arte.pdf` |
| `.gitignore` | **CRIAR** — ignorar .docx, .pptx, .pdf, .jpeg, originais de trabalho |
| `vercel.json` | **CRIAR** (opcional) — só se precisar de redirects |
| `.claude-docs/tasks.md` | **ATUALIZAR** com tasks deste plano (hydration pattern) |

**Não tocar:** PDFs, DOCXs e PPTXs originais permanecem na raiz como referência (ignorados pelo git).

## Verificação end-to-end

1. **Local:** abrir `index.html` no browser → todas as 13 seções visíveis, embeds Even3 carregam (precisa internet)
2. **Inscrição:** clicar CTA "Inscreva-se" → modal/aba Even3 abre dentro da página → preencher dados teste → confirmação chega por e-mail Even3
3. **Submissão:** clicar "Submeter trabalho" → fluxo Even3 completo (login + upload PDF teste + URL vídeo) → painel admin Even3 mostra submissão
4. **Mobile:** testar iPhone SE (375px) e Galaxy (412px) — nav colapsa, grids reorganizam, embeds Even3 são responsivos
5. **Performance:** Lighthouse mobile ≥85 perf, ≥95 acessibilidade
6. **Deploy:** push → Vercel build verde → URL produção 200 OK → embeds funcionando em produção
7. **Stakeholders:** review por UFF/ABAR antes de divulgação ampla (D-1 antes do dia 15/05)

## Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Embed Even3 quebra estilo da landing | Encapsular em `<div class="embed-wrap">` com `iframe { max-width: 100% }`; testar antes do deploy |
| Conta institucional Even3 demora a ser criada | Criar conta pessoal temporária; migrar evento depois (Even3 permite transferência) |
| Logo de alta resolução ainda não está pronto | Usar versão do PDF/PPTX como placeholder; trocar quando finalizar |
| Magda Chambriard não confirmar | Manter badge "a confirmar" no draft; já está previsto |
| Domínio `.com.br` não estará pronto até 15/05 | Lançar com `*.vercel.app`; redirecionar quando DNS propagar |

## Versão completa (pós-MVP) — já incluída nesta entrega

Conforme solicitado, vamos executar o **completo** desde já, não só o MVP de 15/05:

1. **Contador "X inscritos" ao vivo** — pequeno endpoint serverless (`/api/inscritos`) na Vercel que consulta `GET /attendees` da API Even3 com cache de 5min, exibido no hero
2. **Contagem regressiva** — JS vanilla até 08/07/2026 09h00 BRT, animada
3. **Sub-página `/patrocinadores`** — book completo "Quatro Moedas" (a partir do `book_patrocinadores_21-04 (1).html`)
4. **Sub-página `/visitas`** — detalhamento das 8 jornadas com itinerário, horário de partida, vagas restantes (puxa da API Even3)
5. **Sub-página `/programa`** — embed completo de Programação Even3
6. **Sub-página `/submissao`** — embed completo de Submissão + guia de autores
7. **OG tags / SEO** — Open Graph, Twitter Card, schema.org Event JSON-LD (Google indexa como evento)
8. **Acessibilidade AA** — Libras, captions, navegação keyboard-only documentada
9. **i18n leve** — pelo menos inglês para a página principal (audiência internacional do tema regulação)
10. **Anais ISBN+DOI** — instruções para o usuário contratar Even3 Publicações (link + briefing)
11. **Domínio próprio** — registrar `encontrogei.com.br` (ou similar) e apontar Vercel + Even3
12. **Analytics duplo** — GA4 na landing externa + GA4 no evento Even3, com mesma propriedade

Tudo vira tasks no `.claude-docs/tasks.md` no início da execução.
