# Plano — Ajustes pós-reunião (06/05/2026)

## Context

Reunião com a equipe gerou 8 ajustes no site (`index.html` + `patrocinadores/index.html`), nos PDFs de regras e na configuração Even3. O fio condutor é **(a) tirar a Escola de Regulação** de toda a comunicação pública, **(b)** dar mais protagonismo à **data do evento** (08–10 jul 2026), **(c)** ajustar a **copy** de submissão para evitar duplo sentido ("Submeta sua pesquisa" → "Envie seu trabalho"; "Como preparar sua submissão" → "Orientação aos Autores"), e **(d)** ocultar temporariamente blocos cuja confirmação ainda virá (modalidade Remoto/Online + bloco "Parceiros institucionais e de apoio") preservando o markup comentado para reativação fácil.

## Escopo detalhado

### 1. Nav — `index.html:590`

Antes: `<span class="nav-meta">UFF · ABAR<br>PPGEP · Escola</span>`
Depois: `<span class="nav-meta">UFF · ABAR<br>PPGEP/UFF</span>`

E **adicionar a data sempre visível** no nav. Inserir entre `.nav-logo` e `.menu-toggle` um novo elemento:
```html
<span class="nav-date" aria-label="Data do evento">08–10 jul · 2026</span>
```
+ regras CSS na zona do `.nav-meta` (linha 85): cor amarela (`var(--yellow)`), font Manrope 700, `font-size:13px`, `letter-spacing:.05em`. Mostrar a partir de `min-width:780px` (esconder no mobile pra não competir com o burger). Override de tema claro junto com `.nav-meta` no bloco `[data-theme="light"]` (linha 503).

### 2. Hero — destacar a data — `index.html:613` e seguintes

- `.h-badge` (linha 613, "08–10 julho 2026 · Rio + Niterói"): aumentar font. Trocar de pill discreto para uma faixa de destaque: `font-size:clamp(15px,2vw,18px)`, `font-weight:700`, e a parte da data em `var(--yellow)` com tipografia Manrope.
- `#prog-title` ("Três dias de alto nível", `index.html:694`): adicionar antes do `<h2>` um `<p class="sec-lbl prog-date">08–10 julho 2026</p>` em `var(--yellow)`, font 18-22px, peso 700 — vira um sublabel forte da data acima do título da seção. Reaproveitar a regra `.sec-lbl` (já existe) com modifier `.prog-date` para o estilo extra.

### 3. Modalidades — ocultar Remoto/Online — `index.html:783`

Comentar o `<article>` da Modalidade 3 (Remoto / Online) preservando o HTML para reativação:
```html
<!-- MOD-3 OCULTA (reativar se transmissão online for contratada)
<article class="mod-card fi d2"><div class="mod-tag">Modalidade 3</div>...</article>
-->
```
**Não renumerar** os cards restantes — manter "Modalidade 4 — Visitante Técnico" como está. A numeração reflete o conjunto original; mexer nela criaria divergência com `docs/CONTENT.md` e Even3.

### 4. Copy "Submeta sua pesquisa" — `index.html:795`

Antes: `Submeta sua <em>pesquisa</em>`
Depois: `Envie seu <em>trabalho</em>`

(`id="sub-title"` permanece.)

### 5. Copy "Como preparar sua submissão" — `index.html:874`

Antes: `Como preparar sua <em>submissão</em>`
Depois: `Orientação aos <em>Autores</em>`

### 6. Even3 — alinhar copy

Via Chrome DevTools MCP (login já ativo na sessão):
- **"Envie sua submissão"** → **"Envie seu trabalho"** (página pública e/ou painel onde aparecer).
- **"Orientações de Submissão"** → **"Orientações aos Autores"**.
- Manter "Acesse sua área de submissão" / "Acessar área de submissão" no card-CTA (`index.html:901–909`) como está.

### 7. "Quatro moedas" → "Quatro modalidades"

`index.html`:
- linha 937: `As <em>quatro moedas</em> de apoio` → `As <em>quatro modalidades</em> de apoio`

`patrocinadores/index.html`:
- linha 7 (meta description): "Quatro Moedas — modelo..." → "Quatro Modalidades — modelo..."
- linha 104 (h1): `As <em>Quatro Moedas</em><br>de apoio ao Encontro` → `As <em>Quatro Modalidades</em><br>de apoio ao Encontro`
- linha 114: "Cada uma das quatro moedas..." → "Cada uma das quatro modalidades..."

(Classnames CSS `.coin-*` ficam — só identificadores internos.)

### 8. Realização — remover Escola de Regulação — `index.html:963`

Comentar o `<a>` do bloco Realização preservando markup:
```html
<!-- ESCOLA DE REGULACAO OCULTA (reativar se solicitado)
<a href="https://www.rj.gov.br/agenersa/escola-de-regulacao" ...>...</a>
-->
```
Os 3 logos restantes (UFF, ABAR, PPGEP) ficam em grid 3-col.

### 9. "Parceiros institucionais e de apoio" — comentar bloco inteiro — `index.html:967-979`

Envolver `<div class="pt-tier">...</div>` (parceiros institucionais) num comentário HTML, preservando os 8 `<a>` para reativar um a um:
```html
<!-- PARCEIROS-OCULTOS (reativar logos individualmente conforme confirmação)
<div class="pt-tier">
  <p class="pt-tier-lbl fi">Parceiros institucionais e de apoio</p>
  <div class="pt-grid">
    <a href="https://www.firjan.com.br" ...>...</a>
    ...
  </div>
</div>
-->
```

### 10. Remover "Escola de Regulação" das certificações e rodapé

`index.html`:
- linha 37 (JSON-LD organizer): remover `{"@type":"Organization","name":"Escola de Regulação..."}`
- linha 642 (`.partners-pcs` resumo no hero-card sidebar): remover `<span class="pc">Escola de Regulação RJ</span>`
- linha 929 (texto sob iframe inscrição): `UFF, ABAR, PPGEP/UFF e Escola de Regulação` → `UFF, ABAR e PPGEP/UFF`
- linha 987 (`<p class="ct">`): igual
- linha 1016 (`.foot-text`): "Realização: UFF · ABAR · PPGEP/UFF · Escola de Regulação..." → "Realização: UFF · ABAR · PPGEP/UFF."
- linha 1039 (copyright): `© 2026 1° Encontro GEI · UFF · ABAR · PPGEP/UFF · Escola de Regulação` → `© 2026 1° Encontro GEI · UFF · ABAR · PPGEP/UFF`

`patrocinadores/index.html`:
- linha 110: "rede formada por UFF, ABAR, PPGEP/UFF e Escola de Regulação" → "rede formada por UFF, ABAR e PPGEP/UFF"
- linha 202 (copyright): igual ao de cima

`docs/CONTENT.md`:
- linha 32 (tabela Realizadores): remover linha "Escola de Regulação"
- linha 237 (Certificações): "UFF · ABAR · PPGEP/UFF · Escola de Regulação" → "UFF · ABAR · PPGEP/UFF"

`README.md`:
- linha 6 (Realização no header): remover "Escola de Regulação"

`scripts/gerar_regras_pdf.py`:
- footer dos PDFs: remover "Escola de Regulação" (mantendo `UFF · ABAR · PPGEP/UFF`)
- Rodar `python scripts/gerar_regras_pdf.py` → regerar os 4 PDFs
- Re-upload no Even3 (Artigo, Pôster, Relatório A3, Resumo) — fluxo já praticado.

### 11. CTA final — `index.html:1004`

Antes: `<a href="#trabalhos" class="btn-s">Submeter trabalho</a>`
Depois: `<a href="#trabalhos" class="btn-s">Enviar seu trabalho</a>`

---

## Arquivos a modificar

| Arquivo | Linhas afetadas |
|---|---|
| `index.html` | 37, 590, 613, 642, 694 (vizinhança), 783, 795, 874, 929, 937, 963, 967–979, 987, 1004, 1016, 1039 + bloco CSS p/ `.nav-date` e `.prog-date` |
| `patrocinadores/index.html` | 7, 104, 110, 114, 202 |
| `docs/CONTENT.md` | 32, 237 |
| `README.md` | 6 |
| `scripts/gerar_regras_pdf.py` | footer dos PDFs |
| `assets/regras/*.pdf` | regenerar 4 PDFs |
| Even3 (painel) | textos "Envie sua submissão" e "Orientações de Submissão"; re-upload dos 4 PDFs |

## Verificação end-to-end

1. **Lint visual local:** abrir o site após push — conferir:
   - Nav mostra "08–10 jul · 2026" em amarelo a partir de 780px
   - Hero badge maior + sublabel amarelo "08–10 julho 2026" sobre "Três dias de alto nível"
   - Modalidades: 3 cards (Modalidade 1, 2, 4)
   - Submissão: "Envie seu trabalho" + "Orientação aos Autores"
   - Apoio: "As quatro modalidades de apoio"
   - Realização: 3 logos (UFF, ABAR, PPGEP) — sem Escola
   - Bloco "Parceiros institucionais" não aparece
   - Cert + footer + copyright sem "Escola de Regulação"
2. **Grep:** `git grep -n "Escola de Regulação"` retorna apenas snapshots históricos em `.claude-docs/plans/*-2026-05-05-*.md` e os comentários HTML reservados (linha 963).
3. **PDFs:** abrir `assets/regras/resumo-expandido.pdf` e conferir footer sem "Escola de Regulação".
4. **Even3:** página pública + painel com a copy nova.
5. **Tema claro:** alternar e validar contraste do `.nav-date` e do sublabel `.prog-date`.
6. **Mobile (<780px):** `.nav-date` oculto; `.h-badge` continua legível.
7. **Reativação fácil:** descomentar `<!-- MOD-3 OCULTA -->`, `<!-- ESCOLA DE REGULACAO OCULTA -->` e `<!-- PARCEIROS-OCULTOS -->` recupera o estado anterior.

## Commit (mensagem sugerida)

```
copy+layout: ajustes pos-reuniao 06/05

- Nav: data 08-10 jul sempre visivel + remove Escola
- Hero: destaque maior pra data; sublabel amarelo em "Tres dias de alto nivel"
- Modalidades: oculta Remoto/Online (comentado, reativavel)
- Submissoes: "Envie seu trabalho" / "Orientacao aos Autores"
- Apoio: "Quatro modalidades" (em vez de "moedas") + Even3 alinhado
- Realizacao: remove Escola de Regulacao do site, PDFs, docs e Even3
- Parceiros institucionais: oculta bloco (comentado, reativavel)
- CTA final: "Enviar seu trabalho"
```
