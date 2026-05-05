# Plano — Incorporar melhorias do estudo UX (sem reescrita radical)

## Context

O usuário rodou o site no Claude Design e recebeu uma proposta de UX em `Estudo de UX/Evento de regula_o (1)/` (9 diagnósticos + 6 redesigns). A proposta sugere uma **reescrita editorial completa** (paleta navy/creme, tipografia Source Serif 4 + Inter Tight + JetBrains Mono, hero 2-colunas, mobile sticky bar, tracker pessoal etc.).

**Decisão:** não fazer reescrita radical (a identidade atual com Manrope/Outfit + paleta navy/yellow/green/blue baseada no logo oficial está aprovada). Incorporar apenas as melhorias de **alto impacto e baixo custo** que melhoram usabilidade sem desviar da proposta.

## O que incorporar (4 melhorias)

### 1. Nav refinada (alto impacto, baixo custo)

Quatro ajustes pequenos no `<nav>`:

- **Renomear links** para verbos de ação:
  - `Programação` → `Programa`
  - `Submissão` → `Submeter`
  - `Parceiros` → `Apoio`
- **Sigla institucional abaixo do logo** (mono · 9px · uppercase · letter-spacing alto):
  `UFF · ABAR · PPGEP · ESCOLA DE REGULAÇÃO`
  Aparece ao lado do logo no nav, ancora credibilidade no instante zero.
- **Indicador de prazo crítico** entre os links e o CTA, em cor coral/laranja com dot pulsante:
  `● SUBMISSÃO ATÉ 15/05`
  Some quando passar o prazo (lógica simples no JS).
- **Toggle de tema** simplifica pra apenas o ícone SVG (sol/lua), sem texto "Claro/Escuro" — fica mais discreto, não compete com links de seção.

### 2. Visitas técnicas — cor por setor (médio impacto, baixo custo)

A grade atual tem 8 cards visualmente idênticos. Aplicar cor de setor como **border-top: 3px** + **badge de setor** no canto superior direito de cada card `.vc`:

| Setor | Cor | Visitas |
|---|---|---|
| Energia | `#4DA8E0` (blue do logo) | 01 Petrobras · 06 Eneva+TAG |
| Saneamento | `#5BA833` (green AAA) | 02 Águas+ETE · 03 Guandu |
| Indústria | `#F58F4E` (orange já no sistema) | 04 Ternium · 05 Gerdau · 08 CSN |
| Inteligência | `#A95CB7` (magenta já no sistema) | 07 IRM+AGENERSA |

Mantém o badge "integrada" existente. **Não** adicionar barra de ocupação ao vivo (Even3 API pública não expõe contagem por atividade).

### 3. Indicador de urgência expandido (alto impacto, baixo custo)

Hoje o prazo "15/05" só aparece dentro da seção de submissão. Adicionar **pílula sticky de urgência** no hero (logo abaixo do `.h-badge`), em cor coral, formato editorial mono:

`⏱ FASE 1 ENCERRA EM X DIAS · 15.05.2026 · 23H59 BRT`

Calculado dinamicamente (JS) com base na data atual. Visível só enquanto faltarem ≤ 30 dias para o prazo.

### 4. Tipografia mono para metadados (baixo impacto, baixo custo, polimento)

Adicionar **JetBrains Mono** ao Google Fonts já carregado e usar em:
- Indicador de prazo da nav
- Pílula de urgência do hero
- `.h-counter` ("X profissionais inscritos")
- Selo `ISBN DEZ/26` no `.h-meta`
- Datas dentro dos cards de timeline da submissão

Tudo em `font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase;` — toque editorial sem mudar nada.

## O que NÃO incorporar (e por quê)

| Sugestão | Status | Justificativa |
|---|---|---|
| Reescrita tipográfica completa (Serif 4 + Inter Tight) | ❌ | Manrope + Outfit já aprovados visualmente; mudança radical sem ganho proporcional |
| Paleta navy/creme com base 8% creme | ❌ | Paleta atual extraída do logo oficial; mudar quebra o sistema de temas |
| Hero 2-colunas com keys-list lateral | ❌ | Layout centralizado atual aprovado; refazer = retrabalho grande |
| Sticky bottom bar mobile | ⏸ | Adiar — útil, mas a CTA do nav já é persistente em scroll |
| Filtros de visita por setor (mobile) | ⏸ | Cor por setor (item 2) já resolve a maior parte do problema |
| Tracker pessoal de inscrição | ❌ | Exige autenticação Even3 + state management — fora do escopo |
| Barra de ocupação ao vivo nas visitas | ❌ | API Even3 não expõe contagem por atividade |
| Princípios em página dedicada | ❌ | Conteúdo institucional, sem demanda direta do público externo |

## Arquivos a editar

- `index.html` — único arquivo. Mudanças localizadas em:
  - bloco `<nav>` (linha ~410)
  - CSS `.theme-toggle` e `.nav-logo` (linhas ~50-90)
  - CSS `.vc` e variáveis de setor (linhas ~270-290)
  - `<head>` para acrescentar JetBrains Mono ao import Google Fonts
  - `<script>` para countdown da urgência (linha ~1640)

## Etapas (~30 min)

1. Adicionar JetBrains Mono ao import Fonts (1 linha) + variável CSS `--mono`
2. Refatorar `<nav>`: renomear links, adicionar `.nav-meta` (sigla), adicionar `.nav-deadline` (prazo), simplificar `.theme-toggle` (só ícone)
3. CSS de setor para visitas: definir 4 vars `--sector-*`, aplicar via `[data-sector]` no HTML, atualizar 8 cards
4. Adicionar `.urgency-pill` no hero abaixo do badge, com countdown JS
5. JS countdown: function que calcula dias até `2026-05-15T23:59:00-03:00` e atualiza textos de prazo (nav + hero)
6. Commit + push + auto-deploy Vercel

## Verificação

- Visual desktop (Chrome MCP): nav mostra sigla + prazo + ícone toggle limpo · 8 visitas com 4 cores distintas · pílula de urgência abaixo do badge
- Visual mobile (responsivo): nav colapsa em hambúrguer mantendo prazo visível · cards de visita preservam cor de setor
- Funcional: countdown atualiza ao recarregar página · prazo "15/05" some quando passar a data
- Sem regressões: tema claro/escuro continua funcionando · iframes Even3 inscrição/submissão intactos · contador ao vivo do hero intacto

## Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Pílula de urgência polui o hero | Tamanho compacto · só aparece se faltam ≤ 30 dias · aliás texto editorial, não chamado de venda |
| Cor por setor conflita com `--ec-color` dos cards de eventos | Variável separada `--sector-*` aplicada via `[data-sector]`, sem colisão |
| Mono `JetBrains` adiciona peso à página | Carregada com `display=swap` + só pesos 400 e 500 |
| Renomear links quebra anchor `#programacao` etc | Manter os IDs HTML antigos (são âncoras, não label) — só muda o texto visível |
