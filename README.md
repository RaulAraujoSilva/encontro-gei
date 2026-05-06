# 1° Encontro de Governança, Estratégia e Inovação Governamental

Site oficial e configuração da plataforma de inscrição/submissão do **1° Encontro GEI** — 08, 09 e 10 de julho de 2026, Rio de Janeiro / Niterói.

> **Realização:** UFF · ABAR · PPGEP/UFF · Escola de Regulação das Agências Reguladoras do Estado do RJ
> **Parceiros:** Firjan · IBP · ANP · AGENERSA · Fecomércio · CAU/RJ · CREA-RJ · LabDGE/UFF
> **Conferência magna:** Magda Chambriard, Presidente da Petrobras (a confirmar)

---

## URLs

| O que | URL |
|---|---|
| **Site oficial** | https://encontrogeig.org |
| **Página de apoio** | https://encontrogeig.org/patrocinadores/ |
| **Plataforma Even3** | https://www.even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003 |
| **Painel admin Even3** | https://www.even3.com.br/organizador/home/ |
| **Repositório GitHub** | https://github.com/RaulAraujoSilva/encontro-gei |
| **Contador inscritos (API)** | https://encontrogeig.org/api/inscritos |

---

## Stack

- **Frontend:** HTML estático single-file (`index.html`) com CSS embutido. Tipografia Manrope + Outfit (Google Fonts). Tema claro/escuro persistido em `localStorage`.
- **Backend:** Plataforma **Even3** (gestão de inscrição, submissão, avaliação, certificação) + serverless function Vercel (`/api/inscritos`) que faz proxy da API Even3 para alimentar contador "X inscritos" no hero.
- **Hosting:** Vercel (auto-deploy via push para branch `main` no GitHub).
- **Geração de PDFs:** Python + reportlab (`scripts/gerar_regras_pdf.py`) gera os 4 PDFs de regras de submissão por modalidade.

---

## Estrutura de pastas

```
Site do congresso/
├── index.html                  ← landing page principal (single-file, ~1700 linhas)
├── patrocinadores/index.html   ← sub-página "Quatro Moedas" de apoio
├── api/inscritos.js            ← serverless Vercel · contador via API Even3
├── scripts/gerar_regras_pdf.py ← gerador dos 4 PDFs de regras
├── package.json · vercel.json · .gitignore
│
├── assets/                     ← em produção (servido pelo Vercel)
│   ├── logo-completo.png       ← logo transparente · hero tema escuro
│   ├── logo-fundo-branco.png   ← logo + fundo branco · hero claro + PDFs
│   ├── logo-nav.png            ← logo cropado pra nav (314x88)
│   ├── favicon.png · og-image.png
│   ├── logos/                  ← 12 logos parceiros (UFF, ABAR, AGENERSA…)
│   └── regras/                 ← 4 PDFs de normas por modalidade
│
├── docs/                       ← documentação técnica
│   ├── EVEN3_OPERATIONS.md     ← painel Even3, JS dispatch, MCP, API
│   ├── DEPLOY.md               ← deploy Vercel + GitHub + env vars
│   ├── LANDING_GUIDE.md        ← estrutura HTML/CSS, temas, edição
│   └── CONTENT.md              ← conteúdo factual (datas, palestrantes…)
│
├── _referencia/                ← originais do briefing (read-only)
│   ├── PROJETO_EXECUTIVO_*.docx (fonte da verdade do conteúdo)
│   ├── BRIEFING_*.docx · Reunião_30.04.2026.docx
│   ├── APRESENTAÇÃO_*.pptx (2 versões)
│   ├── Esboço da arte.pdf
│   ├── WhatsApp Image *.jpeg (artes do logo)
│   ├── landing_page_evento_21-04.html (draft inicial)
│   ├── book_patrocinadores_21-04.html (draft inicial)
│   └── Regras de submissão/ (4 PDFs originais XII Lean Six Sigma)
│
├── _scratch/                   ← assets intermediários (descartáveis)
│   └── esboco-*.png · logo-alt.jpg · etc.
│
└── .claude-docs/               ← documentos internos (constituição, tasks, plans, screenshots)
```

---

## Operações comuns

| O que quero fazer | Como |
|---|---|
| **Editar conteúdo da landing** | Editar `index.html` direto (HTML/CSS embutido). Veja `docs/LANDING_GUIDE.md` |
| **Subir nova versão** | `git add -A && git commit -m "..." && git push` (auto-deploy Vercel em ~30s) |
| **Deploy manual** | `vercel deploy --prod --scope raularaujosilvas-projects` |
| **Forçar refresh de imagem** | Anexar `?v=N` no `src` (ex: `agenersa.png?v=4`) — bypassa cache CDN |
| **Regerar os 4 PDFs de regras** | `python scripts/gerar_regras_pdf.py` (sai em `assets/regras/`) |
| **Configurar algo na Even3** | Veja `docs/EVEN3_OPERATIONS.md` (login, painel, JS dispatch trick) |
| **Trocar logo de parceiro** | Substituir arquivo em `assets/logos/<nome>.png` (manter nome) |
| **Verificar contador ao vivo** | `curl https://encontrogeig.org/api/inscritos` |
| **Ver inscritos via API** | `curl -H "Authorization-Token: $EVEN3_API_TOKEN" https://www.even3.com.br/api/v1/attendees` |
| **Adicionar palestrante/atividade** | Painel Even3 (`/organizador/programacao`, `/organizador/convidados`) — ver `docs/EVEN3_OPERATIONS.md` |

---

## Marcos do projeto

| Data | Marco |
|---|---|
| **01/06/2026 23h59** | Prazo Fase 1 (resumo + vídeo) |
| **17/06/2026** | Resultado da avaliação |
| **25/06/2026** | Programa definitivo publicado |
| **08-10/07/2026** | **Realização do evento** (3 dias) |
| **30/09/2026** | Prazo Fase 2 (artigo completo) |
| **dezembro/2026** | Anais com ISBN publicados |

---

## Documentação

- 📘 [`docs/EVEN3_OPERATIONS.md`](docs/EVEN3_OPERATIONS.md) — Como acessar, configurar e operar o painel Even3
- 🚀 [`docs/DEPLOY.md`](docs/DEPLOY.md) — Vercel, GitHub, variáveis de ambiente, rollback
- 🎨 [`docs/LANDING_GUIDE.md`](docs/LANDING_GUIDE.md) — Estrutura do `index.html`, sistema de temas, edição
- 📋 [`docs/CONTENT.md`](docs/CONTENT.md) — Conteúdo factual (palestrantes, eixos, programação, parceiros)

---

## Contato

Secretaria do Encontro: `contato@encontrogeig.org`
Comissão Científica: `comissao.cientifica@encontrogeig.org`
