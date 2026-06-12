# Tasks do Projeto — Site 1° Encontro GEI

> Para o **histórico completo** do que foi feito, ver `SESSION_LOG.md`.

## Pendentes — Aguardando dados externos

- [ ] TASK-1030: Configurar GA4 + Meta Pixel — preciso do Measurement ID e Pixel ID
- [ ] TASK-1090: Confirmar Magda Chambriard (Petrobras) na conferência magna Dia 1
- [ ] TASK-1091: Definir local Dia 1 (atualmente "Local em definição" no `index.html:674`)
- [ ] TASK-1092: Liberar logos parceiros conforme confirmações — descomentar dentro de `<!-- PARCEIROS-OCULTOS -->` (`index.html:967`) e `<!-- APOIO-OCULTO -->` (`index.html:648`)
- [ ] TASK-1123: Even3 — criar a entrada Visita Técnica D2 quando as jornadas forem confirmadas (site mostra "Inscrições em breve" desde 12/06). Descrição da entrada presencial corrigida em 12/06 ("três dias" → Dias 1 e 3). ⚠️ Alinhar vagas: painel = 500, site = 400
- [x] TASK-1140: Even3 — checkbox LGPD revisado aplicado no formulário de inscrição em 12/06 (substituiu termo antigo que citava Escola de Regulação e e-mail desativado contato@encontrogei.com.br)
- [ ] TASK-1141: LGPD — validação jurídica final: acordo entre controladoras conjuntas (minuta) + lista nominal de acessos. Preenchidos em 12/06: CNPJs/endereços, DPO (Prof. Alexandre Beraldi Santos) e prazos de retenção (5/2 anos)

## Pendentes — Decisões futuras (parar aqui, retomar quando solicitado)
- [ ] TASK-1130: Reincluir Raul Araujo Silva na Comissão do Seminário (`organizadores/index.html`) quando houver autorização — removido em 04/06 (commit `7e15dcd`); definir nome/cargo/afiliação ao reincluir
- [ ] TASK-1094: Reativar Escola de Regulação se solicitado — descomentar `<!-- ESCOLA DE REGULACAO OCULTA -->` (`index.html:963`)
- [ ] TASK-1095: Adicionar foto/avatar real da Magda Chambriard quando confirmar
- [ ] TASK-1103: Confirmar URL oficial do GIGS · UNICAMP e converter o `<div class="ptc">` em `<a href>` (card atual em `index.html` ~linha 973, sem href)

## Completadas (sessão 12/06/2026 — parte 2: Even3 operacional)

- [x] TASK-1142: Even3 — vagas da entrada presencial ajustadas de 500 → 400 (alinhado ao site)
- [x] TASK-1143: Even3 — ficha de avaliação de reação: complemento "Questionário de avaliação do evento" instalado e configurado (21 perguntas: padrão + visitas técnicas, modalidade, transmissão online, recomendação; duplicata corrigida). Rascunho — publicar próximo ao evento (task painel 8.2.3 ✅)
- [x] TASK-1144: Even3 — Certificado de Participação com arte personalizada (fundo gerado por `scripts/gerar_fundo_certificado.py` com logo do evento + 6 logos das realizadoras; TEP/PPGEP invertido p/ fundo claro) — salvo no editor (task painel 8.2.4 iniciada)
- [x] TASK-1145: LGPD — todos os placeholders removidos dos 3 docs e da página (QR code real embutido no cartaz; seções acordo/lista retiradas — ver TASK-1141); verificação automatizada = 0 marcadores

## Pendentes (novas, 12/06)
- [ ] TASK-1147: Even3 — publicar o questionário de avaliação próximo ao evento (hoje em rascunho)
- [ ] TASK-1148: Even3 — se decidido, elevar limite de autores 4 → 5 após o pico de 16/06 (Recebimento > Configurações > Restrições)
- [x] TASK-1146: Even3 — arte aplicada nos 6 certificados (12/06): Participação, Atividade, Convidado, Submissão, Apresentação, Avaliador (task painel 8.2.4 ✅)
- [x] TASK-1149: Even3 — confirmado limite global de 4 autores por submissão (4 modalidades) + site/PDFs informam "até 4" (task painel 8.2.6 ✅)

## Completadas (sessão 12/06/2026 — modalidades "em breve" + pacote LGPD)

- [x] TASK-1135: Site — card Visita Técnica com "Inscrições em breve"; textos de #modalidades, #inscricao e FAQ 03/05/07 ajustados para refletir as 2 entradas abertas (Presencial + Online)
- [x] TASK-1136: Site — orientação do vídeo reforçada: hospedar em drive aberto ("qualquer pessoa com o link pode ver") ou YouTube não listado, testar em janela anônima; norma "Vídeo" e passo 3 da submissão
- [x] TASK-1137: Criar página pública `/privacidade/` (Política de Privacidade LGPD, 13 seções, controladoras AGENERSA + UFF, placeholders destacados) + link nos footers do index, organizadores e patrocinadores + nota LGPD abaixo do iframe de inscrição (tasks painel 9.5.1–9.5.3)
- [x] TASK-1138: Gerar 3 docs Word em `docs/lgpd/` via `scripts/gerar_docs_lgpd.py`: termo de imagem/voz (com anexo de textos curtos), aviso de gravação/transmissão A4 (cartaz + textos YouTube/MC) e política de guarda e retenção (task painel 9.5.4)
- [x] TASK-1139: Documentar checkbox LGPD revisado e pendências Even3 em `docs/EVEN3_OPERATIONS.md`; corrigida linha desatualizada das entradas (4 antigas → 2 ativas)

## Completadas (sessão 04/06/2026 — visita ETE Camboinhas + página PPGEP + contador)

- [x] TASK-1125: Confirmar Jornada 03 = ETE Camboinhas (biogás, Niterói) com pop-up de detalhes (data 09/07, encontro DER, saída 9h, capacidade 27, link bioproj); modal genérico acessível `.vtmodal` — commit `6249982`, deploy verificado ao vivo
- [x] TASK-1126: Criar página `/organizadores/` (Organização acadêmica PPGEP/UFF) com texto verbatim do `.docx`, links PPGEP + DTS nº 16/2026, Comissão do Seminário e corpo docente (21+5); bloco "Organização acadêmica" + botão em `#parceiros` e link no footer — commit `6249982`
- [x] TASK-1127: Corrigir colisão de classe CSS — `.modal` do pop-up colidia com `<section class="modal" id="modalidades">` e cobria a página; renomeado para `.vtmodal*` — commit `fc47f7f`, deploy verificado
- [x] TASK-1128: Remover Raul da Comissão do Seminário (aguardando autorização) — commit `7e15dcd` (ver TASK-1130 para reinclusão)
- [x] TASK-1129: Reativar contador de inscritos no hero (Even3 `/api/inscritos` retornando 270); descomentado HTML `#counter` + IIFE de fetch — commit `996f82c`, deploy verificado ao vivo

## Completadas (sessão 01/06/2026 — capacidade Dia 1 + reorganização das modalidades)

- [x] TASK-1120: Reduzir capacidade do presencial de 400 → 350 vagas (`index.html`, `docs/CONTENT.md`) — commit `e73bda6`, deploy verificado em produção
- [x] TASK-1121: Reorganizar modalidades de 4 → 3 formas de participar — unifica Presencial Completo + Dias 1 e 3 (350 vagas, base) e torna a Visita Técnica (Dia 2) inscrição independente (200 vagas, ~25/jornada); grid CSS 4→3 colunas; FAQ 03/05/07 e seção de visitas atualizados — commit `034e10e`, deploy verificado
- [x] TASK-1122: Remover menções à pré-inscrição prioritária (janela já encerrada) das seções Modalidades, Inscrição e CTA final — commit `034e10e`
- [x] TASK-1093: Modalidade Remoto/Online reativada (transmissão ao vivo contratada) — feito no commit `71f3ba0`, marcada aqui como concluída pois a lista estava desatualizada

## Completadas (sessão 25/05/2026 — prorrogação Fase 1 + URL do vídeo)

- [x] TASK-1110: Trocar datas de submissão — Fase 1 `01/06 → 16/06/2026`, Resultado `17/06 → 22/06/2026` (`index.html`, `scripts/gerar_regras_pdf.py`, `README.md`, `docs/CONTENT.md`, `docs/EVEN3_OPERATIONS.md`, `docs/LANDING_GUIDE.md`, `.claude-docs/constitution.md`) — commit `db99b9b`
- [x] TASK-1111: Substituir "upload de arquivo de vídeo" por "link público no documento" em todo o site e no PDF do Resumo Expandido (Google Drive, OneDrive ou YouTube unlisted) — commit `db99b9b`
- [x] TASK-1112: Regerar 4 PDFs em `assets/regras/` via `python scripts/gerar_regras_pdf.py` — commit `db99b9b`
- [x] TASK-1113: Even3 — mover cronograma de submissão para encerrar em 16/06/2026 (`Submissões > Configurações`)
- [x] TASK-1114: Even3 — mover cronograma de avaliação para 17/06–22/06/2026 (`Avaliação > Configurações`)
- [x] TASK-1115: Even3 — criar campo "URL do vídeo de apresentação (Fase 1 — Resumo Expandido)" no formulário de submissão, tipo Resposta curta, opcional, visível ao avaliador, com instruções de preenchimento
- [x] TASK-1116: Even3 — re-anexar os 4 PDFs novos às modalidades (Artigo, Pôster, Relatório A3, Resumo) — hashes confirmados em `static.even3.com/geral/`
- [x] TASK-1117: Documentar fluxo de pergunta personalizada na Even3 + nota de propagação CDN em `docs/EVEN3_OPERATIONS.md` — commit `b0cd143`

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
