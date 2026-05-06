# Features do Projeto — Site 1° Encontro GEI

| Feature | Status | Notas |
|---------|--------|-------|
| identidade-visual | ✅ Completa | Logo PGN oficial, paleta navy/amarelo/verde/azul, tipografia Manrope+Outfit |
| landing-principal | ✅ Completa | `index.html` ~1700 linhas, single-file, hero-card lateral 2/3+1/3 |
| sub-paginas | ✅ Completa | `patrocinadores/index.html` ("Quatro Modalidades") |
| serverless-api | ✅ Completa | `api/inscritos.js` proxy Even3 com cache 5 min |
| seo-analytics | 🟡 Parcial | Open Graph + JSON-LD ok; GA4/Meta Pixel pendente (aguarda IDs) |
| deploy | ✅ Completa | Vercel auto-deploy via `main`, domínio `encontrogeig.org` |
| validacao-e2e | ✅ Completa | Smoke test inicial + visualização live |
| setup-even3 | ✅ Completa | 4+4 modalidades, 13 eixos, 22 atividades, 6 palestrantes, 7 avaliadores, 6 certificados |
| pdfs-regras | ✅ Completa | 4 PDFs gerados via reportlab + uploadeados nas modalidades Even3 |
| tema-claro-escuro | ✅ Completa | Toggle persistido em localStorage |
| dominio-emails | ✅ Completa | encontrogeig.org + 3 emails Google Workspace |
| copy-pos-reuniao | ✅ Completa (06/05) | Nav-date, hero badge, "trabalho" em vez de "submissão", "modalidades" em vez de "moedas" |
| ocultacoes-reativaveis | 🟡 Em standby | Mod 3, Escola Regulação, Parceiros, Apoio inline — preservados em comentários HTML |
