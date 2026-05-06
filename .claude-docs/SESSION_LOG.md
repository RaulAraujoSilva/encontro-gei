# Session Log — Site 1° Encontro GEI

> **Última atualização:** 2026-05-06
> **Status global:** Site no ar (`encontrogeig.org`), Even3 configurada, 4 PDFs de regras publicados, e-mails Google Workspace ativos. Pausando aqui — pronto para retomar com ajustes incrementais.

## Visão geral do projeto

**Evento:** 1° Encontro de Governança, Estratégia e Inovação Governamental
**Datas:** 08, 09 e 10 de julho de 2026
**Locais:** Rio de Janeiro (Dias 1 e 2) + Niterói/UFF Gragoatá (Dia 3)
**Realização:** UFF · ABAR · PPGEP/UFF · GIGS/UNICAMP (Escola de Regulação ocultada em 06/05 — preservada em comentários; GIGS adicionado em 06/05 — segundo bloco)

---

## Sessão 06/05/2026 — segundo bloco (ajustes pós-revisão 2)

Commits: `221ce24` e `d65f005` (push para `main`).

**Mudanças no `index.html`:**
1. **Modalidade 4 → 3** (card "Visitante Técnico — Dia 2"): a antiga Modalidade 3 (Remoto/Online) está oculta, então só existem 3 modalidades visíveis. Título da seção também ajustado: "Quatro formas" → "Três formas". Comentário `<!-- MOD-3 OCULTA -->` mantido — se reativada, deve virar Modalidade 4.
2. **Programação Dia 3:** os dois `<li>` finais (16h30 premiação + 18h encerramento/19h coquetel) unificados em **linha única às 16h30**: "Premiação dos trabalhos, coquetel e encerramento institucional". Motivo: adiantar para participantes com voo à noite.
3. **GIGS · UNICAMP** adicionado como 4ª instituição realizadora:
   - Logo `assets/logos/gigs-unicamp.jpg` (cópia do `WhatsApp Image 2026-05-05 at 15.31.08.jpeg` — mantido JPEG original)
   - `.gitignore` atualizado: `!assets/logos/*.jpg|jpeg|png` para liberar JPGs em logos
   - Card no bloco Realização renderizado como `<div class="ptc fi d3">` (sem `<a href>` por ora — URL oficial pendente)
   - Menções textuais atualizadas: nav-meta, hero h-lede, hero chips Realização, modalidades, inscrição, certificação (caixa central), certificação (aside), footer, copyright e JSON-LD organizer
4. **Card PPGEP** (antes texto "PPGEP" estilizado) **substituído por logo** `assets/logos/logo-eng-768x184.png` com link `https://tpp-uff.com.br/`. Logo é branco; aplicado inline `style="filter:invert(1) brightness(.15);"` para exibir escuro sobre o fundo branco do `.ptc-logo`.

**Pendências geradas:**
- TASK-1103: confirmar URL oficial do GIGS e converter o `<div>` em `<a href>`.
- TASK-1093 atualizada: ao reativar Modalidade Remoto, renumerar para Modalidade 4 (slot 3 hoje é Visitante Técnico).

---

## URLs ativas

| O que | URL |
|---|---|
| Site oficial | https://encontrogeig.org |
| Página de apoio | https://encontrogeig.org/patrocinadores/ |
| API contador | https://encontrogeig.org/api/inscritos |
| Página Even3 | https://www.even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003 |
| Painel admin Even3 | https://www.even3.com.br/organizador/home/ |
| Repo GitHub | https://github.com/RaulAraujoSilva/encontro-gei (branch `main`) |

## Stack

- **Frontend:** HTML estático single-file (`index.html` ~1700 linhas) + CSS embutido + JS inline
- **Tipografia:** Manrope (display) + Outfit (corpo) + JetBrains Mono (metadata)
- **Tema:** claro/escuro com toggle persistido em `localStorage`
- **Cores oficiais:** navy `#091136`, amarelo `#F5C842`, verde `#7AC74F`, azul `#4DA8E0`, cyan `#5BC6E5` — extraídas do logo
- **Backend:** Even3 (inscrição, submissão, avaliação, certificação) + Vercel serverless `/api/inscritos` (proxy + cache 5 min)
- **Hosting:** Vercel auto-deploy via push para `main`
- **Domínio:** `encontrogeig.org` (Name.com → vercel-dns.com)
- **E-mails:** Google Workspace — `contato@`, `comissao.cientifica@`, `submissoes@encontrogeig.org`
- **Geração PDFs:** Python + reportlab (`scripts/gerar_regras_pdf.py`)

## Estrutura

```
Site do congresso/
├── index.html                  ← landing (single-file, ~1700 linhas)
├── patrocinadores/index.html   ← sub-página "Quatro Modalidades"
├── api/inscritos.js            ← serverless Vercel
├── scripts/gerar_regras_pdf.py ← gerador dos 4 PDFs
├── assets/
│   ├── logo-completo.png · logo-claro.png · logo-fundo-branco.png · logo-nav.png
│   ├── logos/ (12 logos parceiros)
│   └── regras/ (4 PDFs: artigo-completo, poster, relatorio-a3, resumo-expandido)
├── docs/
│   ├── EVEN3_OPERATIONS.md · DEPLOY.md · LANDING_GUIDE.md · CONTENT.md
└── .claude-docs/
    ├── SESSION_LOG.md (este arquivo) · HANDOFF_EVEN3.md
    ├── constitution.md · features.md · tasks.md
    └── plans/
```

---

## Linha do tempo de tudo que foi feito

### 1ª rodada (2026-05-05) — Construção inicial

- Criação do `index.html` com navy + amarelo/verde/azul (paleta extraída do logo oficial)
- Logo PGN cropado (6250×6250) → 4 versões (`logo-completo`, `logo-claro`, `logo-fundo-branco`, `logo-nav`)
- Landing single-file, hero 100vh, 13 eixos, 4 modalidades, 4 trilhas, 8 visitas técnicas
- Sub-página `patrocinadores/index.html` ("Quatro Moedas" → renomeado depois para "Quatro Modalidades")
- `api/inscritos.js` (serverless Vercel) com proxy à API Even3 + cache 5 min
- SEO: Open Graph + JSON-LD Event
- Git init + deploy Vercel + repo GitHub
- Tema claro/escuro com toggle persistido em `localStorage`

### 2ª rodada — Even3 e PDFs

- Configuração completa do evento Even3 (id `722003`):
  - 4 modalidades de inscrição (Presencial Completo, Presencial Dias 1+3, Remoto, Visitante Técnico)
  - 4 modalidades de submissão (Resumo, Pôster, Relatório A3, Artigo)
  - 13 áreas temáticas
  - 22 atividades de programação
  - 6 palestrantes/painelistas
  - 7 avaliadores
  - 6 templates de certificado
- Geração e upload dos 4 PDFs de regras (Resumo Expandido, Pôster, Relatório A3, Artigo Completo)
- Truque para inputs com máscara de data: `Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(el,v)` + dispatch manual

### 3ª rodada — Domínio + e-mails

- Aquisição de `encontrogeig.org` via Name.com (apontando para vercel-dns)
- Configuração Google Workspace (TXT verification, MX `smtp.google.com`, SPF, DKIM 2048-bit, DMARC `p=none`)
- Migração de todas as referências `@encontrogei.com.br` → `@encontrogeig.org` em código, docs e PDFs
- Adicionado `submissoes@encontrogeig.org` no rodapé dos PDFs e bloco de contato

### 4ª rodada (2026-05-06) — Ajustes pós-reunião

| # | Mudança | Reativação |
|---|---|---|
| 1 | Nav: removido "Escola"; adicionado `<span class="nav-date">08–10 jul · 2026</span>` em amarelo (≥780px) | Editar `index.html:590` direto |
| 2 | Hero `.h-badge`: maior, em amarelo, peso 700 | CSS embutido no head |
| 3 | Sublabel `<span class="prog-date">08–10 julho 2026</span>` antes de "Três dias de alto nível" | `index.html:700` |
| 4 | Modalidade 3 (Remoto/Online) **oculta** | Descomentar `<!-- MOD-3 OCULTA -->` em `index.html:783` |
| 5 | "Submeta sua pesquisa" → "Envie seu trabalho" | `index.html:795` |
| 6 | "Como preparar sua submissão" → "Orientação aos Autores" | `index.html:874` |
| 7 | "Acesse sua área de submissão" → "Acesse sua área de envio do trabalho" | `index.html:901` |
| 8 | Botão "Acessar área de submissão" → "Acessar área de envio do trabalho" | `index.html:909` |
| 9 | "Quatro Moedas" → "Quatro Modalidades" (em site + patrocinadores) | replace_all |
| 10 | Realização: Escola de Regulação **oculta** | Descomentar `<!-- ESCOLA DE REGULACAO OCULTA -->` em `index.html:963` |
| 11 | Bloco "Parceiros institucionais e de apoio" **oculto inteiro** | Descomentar `<!-- PARCEIROS-OCULTOS -->` em `index.html:967` |
| 12 | Lista inline "Apoio" no hero **oculta** | Descomentar `<!-- APOIO-OCULTO -->` em `index.html:648` |
| 13 | Cert/footer/copyright/JSON-LD: removida "Escola de Regulação" | replace_all |
| 14 | CTA final: "Submeter trabalho" → "Enviar seu trabalho" | `index.html:1004` |
| 15 | PDFs regenerados sem "Escola de Regulação" no footer | `python scripts/gerar_regras_pdf.py` |
| 16 | Re-upload dos 4 PDFs no Even3 | Painel Submissões → Recebimento → Modalidades |
| 17 | E-mail do organizador no Even3 atualizado para `contato@encontrogeig.org` | Painel Configuração → Evento |

**Commits na rodada de 06/05:**
- `b87cd12` — `chore: migra emails para @encontrogeig.org`
- `98cf49c` — `copy: remove Escola de Regulacao do lede do hero`
- `6c7f152` — `copy+layout: ajustes pos-reuniao 06/05`
- `808a6db` — `copy: troca "area de submissao" por "area de envio do trabalho"`

---

## Estado atual dos blocos comentados (reativação fácil)

Todos os blocos abaixo estão preservados como comentários HTML — basta descomentar para reativar.

| Marcador | Localização | Conteúdo |
|---|---|---|
| `<!-- MOD-3 OCULTA -->` | `index.html:783` | Card "Modalidade 3 — Remoto / Online" (Ilimitado) |
| `<!-- APOIO-OCULTO -->` | `index.html:648` | Lista inline `<span class="pc">` no hero (Firjan, IBP, ANP, AGENERSA, Fecomércio, CAU, CREA-RJ) |
| `<!-- ESCOLA DE REGULACAO OCULTA -->` | `index.html:963` | Card Realização da Escola de Regulação |
| `<!-- PARCEIROS-OCULTOS -->` | `index.html:967` | Bloco inteiro "Parceiros institucionais e de apoio" (8 logos) |

---

## Pendências e próximos passos sugeridos

### Pendências externas (aguardando dados do usuário)
- **GA4 + Meta Pixel:** preciso do Measurement ID + Pixel ID para configurar tracking
- **Magda Chambriard:** confirmar presença na conferência magna do Dia 1
- **Local Dia 1:** definir e atualizar (`index.html:674` ainda diz "Local em definição")
- **Confirmações de parceiros institucionais:** liberar logos um a um descomentando dentro do `<!-- PARCEIROS-OCULTOS -->`

### Possíveis ajustes futuros
- Ativar Modalidade Remoto/Online se transmissão for contratada (descomentar)
- Reativar Escola de Regulação se solicitado (descomentar)
- Reativar bloco "Parceiros institucionais" parcial ou total conforme confirmações
- Ajustar copy adicional após mais rodadas com a equipe
- Adicionar foto/avatar real da Magda Chambriard quando confirmar

### Operações comuns (cheat sheet)

| O que quero fazer | Como |
|---|---|
| Editar conteúdo da landing | `index.html` direto + push pra `main` |
| Subir nova versão | `git add -A && git commit -m "..." && git push` (Vercel deploya em ~30s) |
| Regerar 4 PDFs | `python scripts/gerar_regras_pdf.py` |
| Re-upload PDFs Even3 | Painel → Submissões → Recebimento → abrir modalidade → "Trocar regras de submissão" → upload → wait 5s → "Salvar Modalidade" |
| Forçar refresh imagem | Append `?v=N` no `src` |
| Verificar contador | `curl https://encontrogeig.org/api/inscritos` |
| Reativar bloco oculto | Descomentar `<!-- NOME-OCULTO -->` no `index.html` |
| Carregar secrets globais | `. C:\.claude\load-secrets.ps1` |

---

## Documentação relacionada

- `README.md` — overview do projeto + URLs + ops comuns
- `docs/CONTENT.md` — fonte da verdade do conteúdo (palestrantes, eixos, programação, parceiros)
- `docs/EVEN3_OPERATIONS.md` — painel Even3, JS dispatch, MCP
- `docs/DEPLOY.md` — Vercel + GitHub + env vars
- `docs/LANDING_GUIDE.md` — estrutura HTML/CSS, sistema de temas, edição
- `.claude-docs/HANDOFF_EVEN3.md` — handoff Even3 inicial
- `.claude-docs/plans/` — todos os planos detalhados, em ordem cronológica

## Memória externa

Resumo deste projeto está em `C:\Users\raula\.claude\projects\C--Users-raula\memory\MEMORY.md` (linha sobre "Site Encontro GEI" se cadastrado lá) — útil em futuras conversações para retomar contexto rápido.
