# Session Log — Site 1° Encontro GEI

> **Última atualização:** 2026-06-25
> **Status global:** Site no ar (`encontrogeig.org`). **Prorrogação divulgada (17/06):** submissão até **25/06**, resultado **27/06**, programa **28/06** (apresentação 10/07, artigo 30/09, anais dez/26 mantidos). Even3: 5 modalidades — inclui **Artigo Completo** criada (envio de arquivo na **versão cega**, autores no formulário, prazo 30/09, ordem de envio). **Escola de Regulação** incluída como realizadora (site). Ver **Sessão 17/06** e os **pontos abertos da reunião 16h**.

## Visão geral do projeto

**Evento:** 1° Encontro de Governança, Estratégia e Inovação Governamental
**Datas:** 08, 09 e 10 de julho de 2026
**Locais:** Rio de Janeiro (Dias 1 e 2) + Niterói/UFF Gragoatá (Dia 3)
**Realização:** UFF · ABAR · PPGEP/UFF · GIGS/UNICAMP · **Escola de Regulação** (reativada em 17/06 com o logo oficial AGETRANSP/AGENERSA)

**Cronograma atual da chamada de trabalhos:**

| # | Fase | Data |
|---|---|---|
| 1 | Fase 1 · Resumo + vídeo (submissão) | até **25/06/2026** 23h59 |
| 2 | Resultado · Aprovação | até **27/06/2026** |
| 3 | Programa Definitivo | **28/06/2026** |
| 4 | Fase 2 · Apresentação | 10/07/2026 · NAB UFF |
| 5 | Artigo · Versão final | até 30/09/2026 |
| 6 | Livro · Anais ISBN | dezembro/2026 |

**Fluxo do vídeo (Fase 1):** Even3 não aceita upload de arquivo de vídeo. Autor hospeda em link público (Google Drive, OneDrive ou YouTube unlisted) e cola a URL no **corpo do documento** (resumo expandido). Há também campo opcional "URL do vídeo de apresentação" no formulário da Even3 para reforço.

---

## Sessão 24–25/06/2026 — Visitas viram Atividades (corrige "já inscrito"), link direto e destaques de abertura

Commits (push em `main` → deploy Vercel): `e715f02` (visita = atividade, CTAs → Área do Participante) · `ca9c538` (CTAs → link direto `/participante/sessions/`) · `2ebd084` (docs Even3 §6/§9) · `587a485` (remove selo "confirmada" dos cards) · `c7cd7de` (destaques de abertura) · `a217a8c` (banners lado a lado + botão verde) · `9e36fe4` (remove moderação/painelistas) · `61da612` (reduz fonte dos banners). Mudanças de plataforma Even3 são manuais (sem commit).

**Correção estrutural — "Participante já está inscrito" (Even3):** a Even3 só permite **1 inscrição por pessoa por evento**. As 4 entradas de Visita Técnica criadas em 24/06 eram duplicata (as visitas já existiam como **Atividades**, com a Jornada 01/TermoRio já tendo 12 inscritos). Solução: **modelo = inscrição em atividades**. Feito via Chrome MCP:
- **4 visitas confirmadas como Atividade** "Visita Técnica" + Inscrição **Gratuita** + **Limite de vagas**: J01 TermoRio **43** (12 inscritos preservados), J02 Guandú+Lameirão/CEDAE **39**, J03 Icaraí+Camboinhas **26**, J04 Braskem **38** — todas 09/07.
- **Excluídas** as jornadas sem detalhamento (Gerdau/Eneva/IRM/CSN) e os placeholders antigos; **excluídas as 4 entradas de visita** (restam só Presencial 500 + Online).
- **Programação > Configurações:** máx. **1 atividade/pessoa** · janela até **01/07** · **restrito a inscritos** (presencial OU online escolhem sem 2ª inscrição).
- **Descrições (Resumo) das 4 atividades enriquecidas = espelho do site** (corrigido "~25 vagas" da J01 → 43; horário J01 alinhado 07:30–13:30). Fonte canônica em `docs/EVEN3_OPERATIONS.md` §9.

**Link direto p/ o participante** (nativo Even3, faz login → cai direto na lista só das 4 visitas com "Realizar inscrição"): `https://www.even3.com.br/evento/login?evento=<slug>&ReturnUrl=%2fparticipante%2fsessions%2f&lang=pt`. Como essa tela já filtra só "Visita Técnica", **não** foi preciso limpar as atividades do Dia 1/Dia 3 (mantidas; decisão do organizador, p/ preservar Programação pública do hotsite + certificados).

**Site (`index.html`):**
- CTAs das visitas (4 modais J01–J04 + card de inscrição) apontam para o **link direto**; framing mudou de "entrada/selecione a Visita Técnica" → "escolha 1 jornada na Área do Participante".
- **Destaques de abertura:** 2 banners **lado a lado** no topo — 🟡 "Último dia" (25/06 submissão) e 🟢 "Inscrições abertas" (visitas, link direto); fonte do corpo reduzida (15,5→13px). Hero ganhou 3º botão **"Inscrição nas Visitas técnicas"** (verde). Seção de visitas ganhou badge "Inscrições abertas · até 01/07" + botão "Inscrever-se em uma visita técnica" (fora dos modais).
- Removido o selo "confirmada" dos cards (redundante) e o bloco **Moderação/Painelistas** (Miguel/Calado/Li Li Min/Raul/Vladimir) das Palestras de abertura.

**Docs/memória:** `docs/EVEN3_OPERATIONS.md` atualizado — entradas 6→2, modelo atividades, **§6 "Publicar nova jornada (visita técnica)"** (runbook p/ J05+), **§9 descrições canônicas**. Memórias atualizadas (visita=atividade, link direto).

**Pendência aberta (p/ próxima sessão):** incluir o link direto também no card **#modalidades "Visita Técnica — Dia 2"** (único sem link). Registrada em `memory/project_pendencia_link_modalidades.md`.

---

## Sessão 17–18/06/2026 — Edital consolidado, decisões dos pontos abertos e Instituto de Computação/UFF

Commit (push em `main` → deploy Vercel): `757de5a` (IC/UFF + Escola de Regulação como organizadores plenos em todo o site + edital com anexos). Deploy confirmado ao ar (encontrogeig.org já mostra o IC/UFF na Realização).

**Edital consolidado (novo):** criado um documento único com todas as informações do evento, no layout dos PDFs de regras. Script `scripts/gerar_edital_consolidado.py` (`build(publicacao=True/False)`; importa `gerar_regras_pdf` para reaproveitar cores/estilos/header/footer). Saídas em `docs/edital/` (gitignored): `edital-1o-encontro-gei.pdf` (publicação, 5 págs.), `edital-consolidado-...pdf` (snapshot de validação com apêndice) e **`edital-1o-encontro-gei-com-anexos.pdf`** (16 págs. — edital + as 4 normas de submissão como Anexos I–IV, com bookmarks; montado por `scripts/montar_edital_com_anexos.py` via pypdf, com capa "Anexos").

**Decisões dos 6 pontos abertos (fecham a reunião 16h de 17/06):** (1) **Escola de Regulação = organizador pleno** → certificação + LGPD + **rodapé dos PDFs de regras**; (2) vagas presenciais = **400** (site; alinhar Even3); (3) keynote da Magna **genérico** no edital (sem nomear); (4) privacidade no edital com **referência limpa** (sem "sujeita a validação jurídica"); (5) visitas Dia 2 = manter "inscrições em breve"; (6) **"Artigo (resumo)" = 5ª modalidade** (texto no formulário, até 700 palavras) mantida.

**Novo organizador — Instituto de Computação/UFF (IC/UFF):** co-realizadora plena. Logo enviado pelo usuário salvo em `assets/logos/ICU.png` e copiado p/ o nome canônico `assets/logos/instituto-computacao-uff.png`. Incluído (junto com a Escola de Regulação) em **todas as peças**: edital + 4 PDFs de regras (rodapé reestruturado em 3 linhas, faixa navy 20mm, p/ caber as 6 instituições); site (`index.html` 8 pontos incl. card de logo; `organizadores`, `patrocinadores`, `privacidade`); fundo do certificado (`gerar_fundo_certificado.py` → 8 logos, com guarda p/ logo ausente). Docx LGPD usa "instituições realizadoras" genérico (não enumera). Arquivos `_referencia/*.html` são snapshots antigos — não tocados.

**Pendências operacionais (continuam):** Even3 — alinhar presencial p/ **400** (painel mostra 500), abrir entrada "Visita Técnica" do Dia 2, e em **25/06** ocultar as modalidades de Fase 1 deixando só Artigo Completo até 30/09; **e-mail de prorrogação** ainda a disparar (texto pronto, falta validar e-mail do organizador).

---

## Sessão 16–17/06/2026 — prorrogação, programa 10/07, artigo cego e Escola de Regulação

Commits (push em `main` → deploy Vercel): `c5bad92` (modalidade Artigo Completo criada na Even3, 16/06) · `f7591e9` (prorrogação + destaque topo) · `036c617`/`b0ff744`/`caea4ad`/`6f702a0` (programa 10/07) · `cabba87`/`599b5a7` (artigo versão cega) · `c319329`/`b01c8fb` (Escola de Regulação).

**Prorrogação (divulgada 17/06):** submissão **25/06** · resultado **27/06** · programa **28/06** (demais datas mantidas). Atualizado em site (banner "Prazo prorrogado" no topo do hero + nav/pílula/timeline/embed/countdown) e nos **4 PDFs de regras** (re-anexados na Even3). Janela global da Even3 já estava em 25/06. **E-mail de divulgação:** existe o recurso **Pessoas → "Notificar pessoas"**, mas exige **validar o e-mail do organizador** antes do 1º envio; o **texto já está pronto** (assunto + corpo).

**Programa 10/07:** +2 painéis (Painel 3 · Lean e transformação digital 11h30; Painel 5 · Sistemas em Engenharia de Produção 15h00); renomeados (Painel 2 saneamento = "Do marco regulatório à entrega: o desafio da universalização do saneamento"; Painel 4 energia = "Governança do setor energético: regulação, investimento e segurança de suprimento"); **renumerados 1–5** (Painel 1 = plenária "IA e soberania"). Só informações de programa (sem notas operacionais internas).

**Artigo Completo (normas internas UFF — avaliação cega):** envio de **arquivo único na versão cega** (sem autoria no texto nem nas propriedades); autores cadastrados nos **campos nativos de autor do formulário Even3** (nome + e-mail por autor — decidido manter o nativo, sem campo extra); **avaliação cega** por pares; ordem de envio; prazo 30/09. PDF regenerado e re-anexado. Modalidade legada **"Artigo (Resumo)"** (39 subs) mantida como está, por decisão.

**Escola de Regulação** incluída como realizadora no site: card de logo reativado (logo oficial AGETRANSP/AGENERSA, `assets/logos/escola-regulacao.jpg`) + crédito em nav, hero, pills, certificação, rodapé, copyright, JSON-LD e subpáginas (organizadores, patrocinadores, privacidade).

### ⏳ Pontos abertos — DECIDIR na reunião das 16h (17/06)
1. **Escola de Regulação na certificação** — o site afirma "Certificação emitida por … e Escola de Regulação". Confirmar se é **co-emissora**; se não, remover da linha de certificação.
2. **Escola de Regulação na política de privacidade** — entrou como "instituição certificadora e realizadora" que **recebe dados** (certificação/anais). Confirmar se trata dados; se não, remover dessa cláusula.
3. **Crédito de realização nos 4 PDFs de regras (Even3)** — ainda creditam só UFF · ABAR · PPGEP · GIGS/UNICAMP. Decidir se **inclui a Escola de Regulação** (regenerar `gerar_regras_pdf.py` + re-anexar os 4 na Even3).

### 🔜 Pendências operacionais (continuar depois)
- **Em 25/06:** ocultar na Even3 as modalidades de Fase 1 (Resumo Expandido, Pôster, Relatório A3, "Artigo (Resumo)"), deixando só **Artigo Completo** aberto até 30/09 (Even3 tem janela única; não há prazo por modalidade).
- **Disparar o e-mail de prorrogação:** validar e-mail do organizador na Even3 → Pessoas → "Notificar pessoas" → segmentar (inscrições confirmadas / autores) → colar texto pronto → enviar.

---

## Sessão 12/06/2026 — pacote LGPD + Even3 operacional completa (tasks S2 fechadas)

Commits: `e15bb07` (pacote LGPD + modalidades "em breve"), `8f08bd7` (CNPJs), `c4e7549` (DPO + prazos), `64d0fe7` (checkbox aplicado), `aa1000f` (arte certificado + QR + placeholders), `ba32057` (fechamento). Todos em produção.

**1. Pacote LGPD (tasks painel 9.5.1–9.5.4 ✅)**
- Página pública **`/privacidade/`** (13 seções; AGENERSA + UFF controladoras conjuntas com CNPJs; DPO **Prof. Alexandre Beraldi Santos** — alexandreberaldisantos@id.uff.br; prazos: inscrição/presença 5 anos, e-mails 2 anos; Even3 operadora art. 39; Res. CD/ANPD 15/2024). Link nos 3 footers + nota na seção de inscrição.
- 3 docs Word em `docs/lgpd/` (gerados por `scripts/gerar_docs_lgpd.py`; `*.docx` no gitignore — o script regenera): termo de imagem/voz (com checkbox e texto de balcão em anexo), **aviso de gravação/transmissão A4 com QR code embutido**, política de guarda e retenção. **Zero placeholders** (a pedido do Raul, seções do acordo entre controladoras e lista de acessos foram retiradas — reintroduzir quando o jurídico definir). Cópias no Drive: pasta `11 — Jurídico › LGPD` (`1Rss9F71eKwUQyJL9e7JfafMjAb1eUix8`).
- **Checkbox LGPD revisado aplicado na Even3** (substituiu termo antigo que citava Escola de Regulação e e-mail desativado contato@encontrogei.com.br).

**2. Even3 operacional (tasks painel 8.2.1–8.2.7 ✅)**
- Entradas: descrição presencial corrigida ("três dias" → **Dias 1 e 3**) e vagas **500 → 400** (alinhado ao site).
- **Ficha de avaliação de reação** = complemento gratuito "Questionário de avaliação do evento": instalado e configurado com 21 perguntas (padrão + visitas técnicas, modalidade de participação, transmissão online, recomendação; duplicata corrigida). **Rascunho — publicar perto do evento** (envio automático ao final).
- **6 certificados com arte personalizada** (fundo 1754×1240 por `scripts/gerar_fundo_certificado.py`: logo do evento + faixa das 6 realizadoras; TEP/PPGEP invertido p/ fundo claro). Atividade cobre visitas técnicas; Submissão/Apresentação cobrem as 4 modalidades via tags.
- **4 autores confirmado**: restrição global (Recebimento > Configurações > Restrições) + site + 4 PDFs. Estratégia +1: elevar p/ 5 após 16/06, se decidido.

**3. Site**
- Card Visita Técnica → "Inscrições em breve" (#modalidades, #inscricao, FAQ 03/05/07); orientação do vídeo reforçada (drive aberto "qualquer pessoa com o link" + teste em janela anônima).

**4. Planilha de acompanhamento** — todas as linhas 8.2.x/9.5.x com status, data de conclusão, links de evidência (site ao vivo, API de inscritos, Drive, painel Even3) e observações.

**Próxima semana (S3 · 15–19/06):** publicar questionário (perto do evento); criar entrada Visita Técnica D2 quando jornadas confirmadas; decidir +1 autor após 16/06; jurídico (acordo entre controladoras + lista de acessos); fechamento da Fase 1 (16/06) e avaliação (17–22/06).

---

## Sessão 04/06/2026 — visita ETE Camboinhas + página PPGEP + contador reativado

Commits: `6249982` (visita + página), `fc47f7f` (fix colisão CSS), `7e15dcd` (remove Raul da comissão), `996f82c` (contador). Todos push para `main`; deploys verificados ao vivo via Playwright headless (o chrome-devtools MCP falhou porque o perfil do Chrome do usuário estava aberto).

**1. Visita técnica confirmada — Jornada 03 → ETE Camboinhas (`6249982`)**
- Card da Jornada 03 (antes "A confirmar") virou **"ETE Camboinhas · Biogás"** (Estação de Tratamento de Esgoto + planta de biogás, Niterói), com selo *confirmada* e link "Ver detalhes →".
- Card clicável (mouse + teclado `Enter`/`Espaço`; `role="button"`, `aria-haspopup`) abre um **pop-up/modal** com: Data **09/07/2026 · Dia 2**, Ponto de encontro **Prédio do DER — Av. Presidente Vargas, 1100 · Centro · RJ**, Saída **09h**, Capacidade **27 visitantes**, link oficial `bioproj.com.br/_ete/ete-camboinhas`.
- Modal genérico e acessível (fecha por `×`/backdrop/`Esc`, trava scroll, devolve foco), reaproveitável via `data-modal="<key>"` → `#modal-<key>`.

**2. Nova página `/organizadores/` — Organização acadêmica PPGEP/UFF (`6249982`)**
- Bloco **"Organização acadêmica · PPGEP/UFF"** na seção `#parceiros` ("Uma rede institucional de alto nível") com botão **"Ver participantes e comissão →"**.
- Página `organizadores/index.html` autocontida (identidade navy/Manrope do site principal), com: texto institucional verbatim do `.docx` (`Atualização/ppgep - texto para o site evento 1o encontro GEIG.docx`), hyperlinks para o **PPGEP** (`tpp-uff.com.br`) e a **DTS nº 16/2026** (`.../comissoes-determinacao-de-servico-dts-2/`), card da **Comissão do Seminário** e **corpo docente** (21 permanentes + 5 colaboradores).
- Link "Organização acadêmica" adicionado ao rodapé.

**3. Bug fix — colisão de classe CSS `.modal` (`fc47f7f`)**
- A seção `#modalidades` já usa `class="modal"`; o pop-up novo (também `.modal`) aplicou `position:fixed;z-index:1000` na seção de modalidades e cobriu a página inteira (sintoma relatado: "só sobrou as três formas de participar"). Componente renomeado para o namespace **`.vtmodal*`** (CSS + HTML + JS). Lição: validar **renderizando** (Playwright headless), não só checando presença do HTML via fetch/grep.

**4. Comissão — Raul removido (`7e15dcd`)**
- A pedido, removido o nome do Raul Araujo Silva da Comissão do Seminário na página `/organizadores/` (aguarda autorização para reincluir). Restaram os 4 professores designados pela DTS nº 16/2026, idêntico ao texto verbatim.

**5. Contador de inscritos reativado (`996f82c`)**
- A API `/api/inscritos` (proxy Even3 com cache de 5 min) já estava configurada e respondendo (**count=270**, eventId 722003). Descomentados o bloco HTML `#counter` no hero e o IIFE de `fetch`. Exibe "270 profissionais já inscritos" (degrada com segurança: se count=0 ou erro, fica oculto). Confirmado ao vivo.

---

## Sessão 25/05/2026 — prorrogação Fase 1 + URL do vídeo

Commits: `db99b9b` (mudanças) e `b0cd143` (doc operacional Even3) — push para `main`.

**Motivação:** A Even3 não permite upload de arquivo de vídeo no fluxo de submissão. Como o prazo Fase 1 atual (01/06) estava a 7 dias e os autores ficariam sem como entregar o vídeo, foi necessário (a) prorrogar Fase 1 e Resultado em 2 semanas e (b) trocar a entrega do vídeo para link público.

**Mudanças no site (`db99b9b`):**

1. **`index.html`** — datas atualizadas: nav deadline `Submissão até 16/06`, hero pill `16.06 · 23h59 BRT`, timeline (Fase 1 `até 16/06/2026`, Resultado `até 22/06/2026`), card `dl-date` "16 de junho · 23h59", embed Even3 (intro/rodapé com 16/06 e resultado 22/06), JS countdown para `2026-06-16T23:59:00-03:00`. Item Vídeo nas normas: "upload de arquivo" → "link público no documento". Passo 3 do embed orienta colar o link no corpo do texto e no campo URL da Even3.
2. **`scripts/gerar_regras_pdf.py`** — cronograma e caixa amarela atualizados; seção "Vídeo de apresentação" do Resumo Expandido reescrita para link público (Google Drive/OneDrive/YouTube unlisted) colado no corpo do documento.
3. **4 PDFs em `assets/regras/`** regerados via script.
4. **`README.md`, `docs/CONTENT.md`, `docs/EVEN3_OPERATIONS.md`, `docs/LANDING_GUIDE.md`, `.claude-docs/constitution.md`** sincronizados com as novas datas e o novo fluxo do vídeo.

**Mudanças na Even3 (via Chrome MCP, evento 722003):**

1. **Cronograma de submissão:** fim mudado para `16/06/2026` (`Submissões > Configurações`).
2. **Cronograma de avaliação:** `02/06 → 17/06` substituído por `17/06 → 22/06` (`Avaliação > Configurações`).
3. **Campo novo no formulário:** "URL do vídeo de apresentação (Fase 1 — Resumo Expandido)", tipo Resposta curta, opcional, com instruções detalhadas para o participante, visível ao avaliador (`Submissões > Recebimento > Formulário de submissão`).
4. **4 PDFs de regras re-anexados** (URLs novas em `static.even3.com/geral/`: `artigo-completo.6a32616c…`, `poster.2fcde367…`, `relatorio-a3.3a2981b5…`, `resumo-expandido.e7ddf078…`).

**Doc operacional atualizado (`b0cd143`):**

- `docs/EVEN3_OPERATIONS.md` ganhou seção "Adicionar pergunta personalizada ao formulário de submissão" e nota sobre propagação da CDN ao trocar PDF (linha pode mostrar "Defina regras de submissão" momentaneamente, recarregar confirma o hash novo).

**Pendências geradas:**

- Nenhuma. Próximas decisões dependem de input externo (avaliação dos trabalhos durante 17–22/06).

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
- **Comissão do Seminário (`/organizadores/`):** reincluir Raul Araujo Silva quando houver autorização (removido em 04/06)

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
