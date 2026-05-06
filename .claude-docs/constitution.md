# Constituição — Site do 1º Encontro GEI

## Princípios

- **Deadline submissão Fase 1: 01/06/2026 23h59** (movido de 15/05 em 06/05/2026).
- **Identidade institucional sólida**: 4 realizadores (UFF, ABAR, PPGEP/UFF, Escola de Regulação) + 7 parceiros — design transmite seriedade acadêmica.
- **Acessibilidade WCAG AA** desde o primeiro deploy.
- **Backend Even3, frontend livre**: landing externa controla 100% do visual; Even3 cuida de inscrição, submissão, anais e certificados via embeds + API.

## Padrões de Código

- HTML estático self-contained sempre que possível (padrão AGENERSA Mapa).
- Paleta única: navy `#0E2246`, blue `#1B4C8E`, gold `#C8A44A`, white `#FFFFFF`, off `#F7F9FC`.
- Tipografia: `Cormorant Garamond` (títulos serif) + `Outfit` (sans-serif corpo) via Google Fonts.
- CSS inline minificado para performance; sem build step até a complexidade exigir.
- Mobile-first; breakpoints em 480/768/1000/1100 px.
- Commits em português com prefixo convencional (feat/fix/docs/style/refactor/chore).

## Restrições

- **Não criar README/docs.md** sem pedido explícito.
- **Não inventar dados** (palestrantes, vagas, datas) — sempre extrair do PROJETO_EXECUTIVO ou perguntar.
- **Não comprometer logo/identidade** — usar apenas o oficial extraído do `Esboço da arte.pdf`.
- **Não fazer commit + push automático** até validação local; usuário pediu commit+push em outros projetos mas aqui o site precisa de revisão visual antes.
- **PDFs/DOCXs/PPTXs originais** ficam fora do git (`.gitignore`) — material de referência apenas.
