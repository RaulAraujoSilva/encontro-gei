# Plano — Organização da pasta + documentação completa

## Context

A pasta `Site do congresso` cresceu organicamente: contém o site live (`index.html`, `api/`, `assets/`), arquivos originais do briefing (Word/PowerPoint/PDF), drafts antigos, assets intermediários gerados durante iterações (PNGs do esboço, alt logos), e documentação espalhada em `.claude-docs/`. Precisa de:

1. **Reorganização física** — separar originais (referência apenas) dos artefatos em produção e dos intermediários descartáveis.
2. **README + docs** consolidados na raiz para retomada futura sem precisar reler conversa de chat.
3. **Documentação operacional do Even3** — credenciais, painel, truque do JS dispatch, scripts de batch, abas e o que cada uma faz.

## Reorganização — nova estrutura de pastas

```
Site do congresso/
├── README.md                       ← NOVO · entrada principal
├── docs/                           ← NOVA pasta · documentação técnica
│   ├── EVEN3_OPERATIONS.md         ← painel, abas, API, JS dispatch
│   ├── DEPLOY.md                   ← Vercel + GitHub + env vars
│   ├── LANDING_GUIDE.md            ← estrutura HTML/CSS, temas, edição
│   └── CONTENT.md                  ← palestrantes, eixos, parceiros, fontes
│
├── _referencia/                    ← NOVA · originais (read-only, não tocar)
│   ├── PROJETO_EXECUTIVO_UNIFICADO_21-04_v2 Calado (1).docx
│   ├── BRIEFING_REVISAO_APRESENTACAO.docx
│   ├── Reunião 30.04.2026 - manhã.docx
│   ├── 7__Formulario_para_celebracao_de_TACCMA_*.docx
│   ├── APRESENTACAO_1ENCONTRO_v3 (1).pptx
│   ├── APRESENTAÇÃO - 1-Encontro-de-Governanca-*.pptx
│   ├── Esboço da arte.pdf
│   ├── WhatsApp Image 2026-05-01 at 14.35.26.jpeg
│   ├── WhatsApp Image 2026-05-01 at 14.35.27.jpeg
│   ├── landing_page_evento_21-04 (1).html  (draft inicial)
│   ├── book_patrocinadores_21-04 (1).html  (draft inicial)
│   └── Regras de submissão/         (4 PDFs originais XII Lean Six Sigma)
│
├── _scratch/                       ← NOVA · intermediários (podem ser apagados)
│   ├── esboco-full.png             (render PDF)
│   ├── esboco-img0.png .. img5.png (extrações Pillow)
│   ├── logo-alt.jpg
│   ├── logo-completo.jpg           (substituído por .png transparente)
│   ├── logo-uff.png                (extraído mas não usado)
│   ├── logo-swirl.png              (extraído mas não usado)
│   ├── Logo_agenersa.jpg
│   └── WhatsApp Image *.jpeg       (cópia)
│
├── assets/                         ← em produção
│   ├── logo-completo.png           (transparente · hero dark)
│   ├── logo-fundo-branco.png       (hero light + PDFs)
│   ├── logo-nav.png                (favicon do nav)
│   ├── favicon.png
│   ├── og-image.png
│   ├── logos/                      (12 logos parceiros)
│   └── regras/                     (4 PDFs adaptados)
│
├── api/inscritos.js                ← serverless Vercel
├── scripts/gerar_regras_pdf.py     ← gerador PDFs reportlab
├── patrocinadores/index.html       ← sub-página
├── index.html                      ← landing principal
├── package.json
├── vercel.json
├── .gitignore
└── .claude-docs/                   ← docs internas do Claude (mantém)
    ├── tasks.md, features.md, constitution.md
    ├── HANDOFF_EVEN3.md            (legado · será substituído por docs/EVEN3_OPERATIONS.md)
    ├── plans/
    └── screenshots/                (mover screenshots-*.png pra cá)
```

## Etapas de execução

### 1. Mover arquivos (~3 min)
- Criar `_referencia/`, `_scratch/`, `docs/`, `.claude-docs/screenshots/`
- `mv` dos arquivos originais para `_referencia/` (mantendo a pasta `Regras de submissão/` original)
- `mv` dos intermediários para `_scratch/`
- `mv` dos screenshot-*.png para `.claude-docs/screenshots/`
- `.gitignore` já cobre `_referencia/*` (docx/pptx/pdf/jpeg) e podemos adicionar `_scratch/`

### 2. Criar `README.md` na raiz (~5 min)
Sumário executivo de 1 página:
- O que é (1º Encontro GEI · 08-10/07/2026)
- Stack (HTML estático + Vercel + Even3 backend)
- URLs (site, repo, Even3, contador API)
- Estrutura de pastas (referência ao quadro acima)
- Como editar (10 comandos comuns: subir conteúdo, redeploy, regerar PDFs)
- Links para docs/ específicas

### 3. Criar `docs/EVEN3_OPERATIONS.md` (~10 min)
Documentação operacional definitiva. Inclui:

**Acesso e credenciais**
- URL: `https://www.even3.com.br/organizador/home/`
- Conta: `Raul Araujo` (login Google)
- Evento: `722003` · slug `1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003`
- API Token: salvo em `EVEN3_API_TOKEN` no Vercel (`vercel env ls`)
- API Token (gerado): `da1c37f7-538f-4c93-bf7e-f6154fab02f8`

**Mapa do painel (cada aba e o que está configurado)**
Tabela com: aba · URL · status · onde editar · referências.

**Truque do JS dispatch (bypass máscara dd/mm)**
Snippet completo + explicação de por que o `fill_form` simples não funcionou.

**Como configurar via Chrome MCP**
- Inicialização do MCP Chrome
- Login na sessão MCP (separada da regular)
- Padrões: `evaluate_script` com `setVal` para inputs mascarados
- Limitações descobertas (form de email vazio, modal navigation = page reload)

**Operações comuns**
- Reabrir submissões (mover datas)
- Adicionar novo eixo temático / modalidade
- Trocar PDF de regras anexado
- Republicar certificado
- Adicionar avaliador
- Consultar API REST (`https://www.even3.com.br/api/v1/attendees`)

**Endpoints Even3 confirmados**
- `GET /api/v1/event` — dados gerais
- `GET /api/v1/attendees` — lista de inscritos
- Header `Authorization-Token: <token>`

### 4. Criar `docs/DEPLOY.md` (~5 min)
- Deploy Vercel (`vercel deploy --prod`)
- Auto-deploy via push GitHub (main → produção)
- Variáveis de ambiente (`EVEN3_API_TOKEN`, `EVEN3_EVENT_ID`)
- Cache busting (anexar `?v=N` em assets quando não atualizar)
- Rollback (Vercel > Deployments > Promote)

### 5. Criar `docs/LANDING_GUIDE.md` (~7 min)
- Estrutura do `index.html` (15 seções, ordem)
- CSS variables principais (paleta, tipografia)
- Sistema de temas claro/escuro (`[data-theme]`, localStorage)
- IntersectionObserver de fade-in + failsafe 2.5s
- Sub-páginas (`patrocinadores/`)
- Edição comum (trocar palestrante, mudar data, adicionar parceiro)

### 6. Criar `docs/CONTENT.md` (~5 min)
Tabelas estruturadas com **toda a informação factual** do evento + fonte:
- Datas, local, organizadores, parceiros (com URLs dos logos)
- 4 trilhas (eventos integrados)
- 8 jornadas técnicas (Dia 2)
- 22 atividades de programação
- 6 palestrantes
- 13 eixos temáticos
- Cronograma de submissão/avaliação
- 7 avaliadores comissão científica
- Regulamento (Arial 12, ABNT, etc)

Cada bloco com referência ao arquivo do `_referencia/` que originou a informação (PROJETO_EXECUTIVO ou similar).

### 7. Atualizar `.gitignore` (~1 min)
Adicionar:
```
_scratch/
.claude-docs/screenshots/
```
Manter ignorando `*.docx`, `*.pptx`, `*.pdf` (com exceção de `assets/regras/*.pdf`).

### 8. Substituir `HANDOFF_EVEN3.md` (~1 min)
Deprecar o handoff antigo (era para usuário fazer manualmente). Substituir o conteúdo por um pointer:
```
> Esta documentação foi substituída por docs/EVEN3_OPERATIONS.md
> Tudo o que estava aqui foi configurado e está documentado de forma definitiva.
```

### 9. Commit + push final (~2 min)
- `feat: organização de pastas + documentação completa`
- Push pro GitHub

## Arquivos críticos a criar

| Arquivo | Linhas aprox. |
|---|---|
| `README.md` | ~100 |
| `docs/EVEN3_OPERATIONS.md` | ~250 |
| `docs/DEPLOY.md` | ~80 |
| `docs/LANDING_GUIDE.md` | ~150 |
| `docs/CONTENT.md` | ~200 |

## Verificação

- `git status` mostra pasta limpa, com novos arquivos commitáveis
- Estrutura final: `tree -L 2 -I .git` lista 4 pastas top-level (assets, api, scripts, patrocinadores) + 4 docs (README, docs/, .claude-docs/, _referencia/) + arquivos de config
- README abre direto e dá pra navegar pra qualquer doc específica em 1 clique
- `_referencia/` está intacta (originais preservados)
- Site continua funcional em produção (mudança é só de organização interna, sem afetar `index.html`/`assets/`)

## Premissas

- **Não renomear** os arquivos originais do briefing (preservar nomes, mesmo que confusos como "(1)")
- **Não deletar** nada do `_scratch/` — fica disponível mas isolado
- Pasta `Regras de submissão/` original mantém o nome com espaço (português) dentro de `_referencia/`
