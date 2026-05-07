# Tasks do Projeto — Site 1° Encontro GEI

> Para o **histórico completo** do que foi feito, ver `SESSION_LOG.md`.

## Pendentes — Aguardando dados externos

- [ ] TASK-1030: Configurar GA4 + Meta Pixel — preciso do Measurement ID e Pixel ID
- [ ] TASK-1090: Confirmar Magda Chambriard (Petrobras) na conferência magna Dia 1
- [ ] TASK-1091: Definir local Dia 1 (atualmente "Local em definição" no `index.html:674`)
- [ ] TASK-1092: Liberar logos parceiros conforme confirmações — descomentar dentro de `<!-- PARCEIROS-OCULTOS -->` (`index.html:967`) e `<!-- APOIO-OCULTO -->` (`index.html:648`)

## Pendentes — Decisões futuras (parar aqui, retomar quando solicitado)

- [ ] TASK-1093: Reativar Modalidade Remoto/Online se transmissão for contratada — descomentar `<!-- MOD-3 OCULTA -->` (`index.html:783`); ATENÇÃO: o slot 3 visual hoje é ocupado pelo Visitante Técnico (TASK-1100). Renumerar para Modalidade 4 ao reativar.
- [ ] TASK-1094: Reativar Escola de Regulação se solicitado — descomentar `<!-- ESCOLA DE REGULACAO OCULTA -->` (`index.html:963`)
- [ ] TASK-1095: Adicionar foto/avatar real da Magda Chambriard quando confirmar
- [ ] TASK-1103: Confirmar URL oficial do GIGS · UNICAMP e converter o `<div class="ptc">` em `<a href>` (card atual em `index.html` ~linha 973, sem href)

## Completadas (sessão 07/05/2026)

- [x] TASK-1105: Criar seção FAQ com 15 perguntas em acordeão (`<details>/<summary>`), agrupadas em 5 blocos (Participação, Visitas, Submissão, Certificação, Apoio); inserida após `#inscricao` antes do `#apoio`; novo link "FAQ" no menu superior e "Dúvidas frequentes" no footer; CSS dedicado com tema claro/escuro

## Completadas (sessão 06/05/2026 — segundo bloco)

- [x] TASK-1100: Renumerar Modalidade 4 (Visitante Técnico Dia 2) → Modalidade 3; título da seção "Quatro formas" → "Três formas" (commit `221ce24`)
- [x] TASK-1101: Programação Dia 3 — unificar premiação + coquetel + encerramento institucional em linha única às 16h30 (commit `221ce24`)
- [x] TASK-1102: Adicionar GIGS · UNICAMP como 4ª instituição realizadora — logo `assets/logos/gigs-unicamp.jpg` + menções em nav, hero, certificações, footer e JSON-LD organizer (commit `221ce24`); .gitignore atualizado para permitir JPGs em `assets/logos/` (commit `221ce24`)
- [x] TASK-1104: Substituir card PPGEP textual por logo TEP/PPGEP (`assets/logos/logo-eng-768x184.png`) com link `https://tpp-uff.com.br/`; aplicar `filter: invert()` no `<img>` para inverter logo branco sobre fundo branco do card (commit `d65f005`)

## Completadas (sessão 06/05/2026)

- [x] TASK-1080: Migração de e-mails @encontrogei.com.br → @encontrogeig.org + adicionar submissoes@ (commit `b87cd12`)
- [x] TASK-1081: Remoção da "Escola de Regulação" do lede do hero (commit `98cf49c`)
- [x] TASK-1082: Migrar emails para @encontrogeig.org + adicionar submissoes@ (consolidado em TASK-1080)
- [x] TASK-1083: Ajustes pós-reunião 06/05 — nav-date, hero badge, modalidades, copy submissão, quatro modalidades, Escola removida, parceiros ocultos, CTA final, PDFs regenerados, Even3 re-upload (commit `6c7f152`)
- [x] TASK-1084: Trocar "área de submissão" → "área de envio do trabalho" no card-CTA (commit `808a6db`)

## Completadas (sessões anteriores — 05/05/2026)

- [x] TASK-1015: Inicializar .claude-docs do projeto (2026-05-05)
- [x] TASK-1016: Verificar sessão Even3 via Chrome MCP (2026-05-05)
- [x] TASK-1017: Extrair logo do Esboço da arte.pdf → `assets/logo-swirl.png` (2026-05-05)
- [x] TASK-1018: Evento criado na Even3 — `722003` (2026-05-05)
- [x] TASK-1019: Configurar 4 modalidades de inscrição (2026-05-05)
- [x] TASK-1020: Configurar 8 jornadas técnicas (atividades Dia 2) (2026-05-05)
- [x] TASK-1021: Configurar Submissão de Trabalhos (13 eixos, 2 fases) (2026-05-05)
- [x] TASK-1022: Adicionar Programação 3 dias na Even3 (2026-05-05)
- [x] TASK-1023: Adicionar Convidados/Palestrantes (2026-05-05)
- [x] TASK-1024: Coletar embed codes + gerar API Token (2026-05-05)
- [x] TASK-1025: Criar `index.html` (2026-05-05)
- [x] TASK-1026: Criar `patrocinadores/index.html` ("Quatro Moedas" → "Quatro Modalidades") (2026-05-05)
- [x] TASK-1027: Sub-páginas via redirects vercel.json (2026-05-05)
- [x] TASK-1028: Criar `api/inscritos.js` (serverless Vercel + cache 5min) (2026-05-05)
- [x] TASK-1029: SEO Open Graph + JSON-LD Event (2026-05-05)
- [x] TASK-1031: Git init + repo + deploy Vercel (2026-05-05)
- [x] TASK-1032: Smoke test E2E (2026-05-05)
- [x] TASK-1033: Completar metadados Even3 (2026-05-05)
- [x] TASK-1040: Domínio encontrogeig.org adquirido + DNS Vercel (2026-05-05)
- [x] TASK-1041: Google Workspace configurado (3 e-mails operacionais) (2026-05-05)
- [x] TASK-1050: Geração e upload dos 4 PDFs de regras de submissão (2026-05-05)
- [x] TASK-1060: Tema claro/escuro com toggle persistido em localStorage (2026-05-05)
- [x] TASK-1070: Identidade visual com logo oficial PGN + paleta extraída (2026-05-05)
