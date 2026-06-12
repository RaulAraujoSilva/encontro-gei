# Features do Projeto — Site 1° Encontro GEI

| Feature | Status | Notas |
|---------|--------|-------|
| identidade-visual | ✅ Completa | Logo PGN oficial, paleta navy/amarelo/verde/azul, tipografia Manrope+Outfit |
| landing-principal | ✅ Completa | `index.html` ~1700 linhas, single-file, hero-card lateral 2/3+1/3 |
| sub-paginas | ✅ Completa | `patrocinadores/index.html` ("Quatro Modalidades") |
| serverless-api | ✅ Completa | `api/inscritos.js` proxy Even3 com cache 5 min |
| contador-inscritos | ✅ Ativo (04/06) | Reativado no hero (`#counter`); `/api/inscritos` retornando 270 (eventId 722003); oculta-se sozinho se count=0 ou erro |
| visita-ete-camboinhas | ✅ Completa (04/06) | Jornada 03 confirmada (ETE Camboinhas/biogás, Niterói) com pop-up de detalhes; modal genérico `.vtmodal` reaproveitável (`data-modal`) |
| pagina-organizadores | ✅ Completa (04/06) | `/organizadores/` (texto PPGEP verbatim, Comissão do Seminário, corpo docente); bloco+botão em `#parceiros` + link no footer; Raul removido da comissão p/ autorização |
| seo-analytics | 🟡 Parcial | Open Graph + JSON-LD ok; GA4/Meta Pixel pendente (aguarda IDs) |
| deploy | ✅ Completa | Vercel auto-deploy via `main`, domínio `encontrogeig.org` |
| validacao-e2e | ✅ Completa | Smoke test inicial + visualização live |
| setup-even3 | ✅ Completa | 4+4 modalidades, 13 eixos, 22 atividades, 6 palestrantes, 7 avaliadores, 6 certificados |
| pdfs-regras | ✅ Completa | 4 PDFs gerados via reportlab + uploadeados nas modalidades Even3 (regerados 25/05 com datas novas + seção vídeo via link) |
| cronograma-chamada | ✅ Completa (25/05) | Fase 1 até 16/06, Resultado até 22/06, Programa 25/06, Apresentação 10/07, Artigo 30/09, Anais dezembro/26 |
| entrega-video-fase-1 | ✅ Completa (25/05) | Link público (Drive/OneDrive/YouTube unlisted) colado no corpo do documento + campo opcional "URL do vídeo" na Even3 |
| tema-claro-escuro | ✅ Completa | Toggle persistido em localStorage |
| dominio-emails | ✅ Completa | encontrogeig.org + 3 emails Google Workspace |
| copy-pos-reuniao | ✅ Completa (06/05) | Nav-date, hero badge, "trabalho" em vez de "submissão", "modalidades" em vez de "moedas" |
| ocultacoes-reativaveis | 🟡 Em standby | Mod Remoto, Escola Regulação, Parceiros, Apoio inline — preservados em comentários HTML |
| ajustes-pos-revisao-2 | ✅ Completa (06/05) | Modalidade 4→3, premiação+coquetel+encerramento unificados às 16h30 D3, GIGS/UNICAMP como 4ª realização, card PPGEP convertido em logo TEP/PPGEP com link tpp-uff.com.br |
| reorganizacao-modalidades | 🟡 Parcial (12/06) | Even3 com 2 entradas ativas (Presencial 400 + Online ilimitada, confirmado via API 12/06); site ajustado: Visita Técnica = "Inscrições em breve". Pendente: criar entrada Visita Técnica D2 + corrigir descrição "três dias" (TASK-1123) |
| pacote-lgpd | ✅ Completa (12/06) | `/privacidade/` publicada (CNPJs, DPO Beraldi, prazos 5/2 anos); 3 docs Word sem placeholders (QR embutido); checkbox revisado aplicado na Even3. Pendência jurídica externa: acordo entre controladoras (TASK-1141) |
| even3-operacional-s2 | ✅ Completa (12/06) | Vagas 400; questionário de avaliação configurado (rascunho — publicar perto do evento); 6 certificados com arte (`scripts/gerar_fundo_certificado.py`); 4 autores confirmado; tasks painel 8.2.1–8.2.7 e 9.5.1–9.5.4 concluídas |
