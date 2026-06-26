# Modificar a Carta de Aceite (ofício) nativa do Even3

## Contexto

O **ofício de aceite** entregue aos autores é a **Carta de Aceite nativa do Even3** — o
PDF que o autor baixa na *Área do Participante › Submissões* (botão "Carta de Aceite",
URL `…/participante/impressao/_impressaocartadeaceite?code=<nº>`). O **modelo** dessa carta
é editável pelo organizador em `/organizador/trabalhocientifico/modelocartadeaceite/`
("Documentos › Editar carta de aceite") — é **template único** (HTML/TinyMCE) usado para
**todas as modalidades**, com tags `{trabalho.titulo}`, `{DADOS_AUTORES}`,
`{trabalho.modalidade}`, `{data.aceite}`, `{assinatura.comissao}`, `{evento.*}` e botão
**Anexar Assinatura**.

O usuário identificou três ajustes a fazer no modelo atual (versão 25/06):

1. **Faltou o período do evento** — hoje a carta só mostra `{data.aceite}` (data do aceite),
   não o período "**08 a 10 de julho de 2026**".
2. **Frase de aprovação explícita** — usar "**ACEITO PARA PUBLICAÇÃO**" / a redação que o
   Edital PPGEP/UFF nº 01/2026 exige ("artigo completo (publicado ou aceito) em evento
   científico nacional"). Hoje o corpo está genérico: *"…foi ACEITO, conforme o edital da
   respectiva modalidade ({trabalho.modalidade}), no {evento.titulo}."*
3. **Assinatura nominal** — o **Prof. Li Li Min** passa a assinar **representando** a Comissão
   Científica. O bloco fica **exatamente**: `Prof. Li Li Min` / `Professor Titular` /
   `Comissão Científica`, **mantendo abaixo** as **instituições** e o **e-mail da Comissão
   Científica** (`comissao.cientifica@encontrogeig.org`) já configurados. Ou seja, **acrescenta**
   nome + cargo acima do bloco institucional existente (não é substituição total). *(Reverte
   parcialmente a decisão de 17–25/06 que tornara a assinatura só genérica — confirmado pelo
   usuário.)*

Antes de editar, **baixar do Even3 as cartas atuais** para inspeção (decisão do usuário).

> Acesso: painel `https://www.even3.com.br/organizador/home/`, evento **722003**, login
> Google (Raul Araujo). Edição feita por **navegador** (Claude in Chrome) — não há endpoint
> de API para o modelo da carta.

## Estado atual do template (verbatim, 25/06)

- Logo horizontal: `<img src="https://encontrogeig.org/assets/logo-fundo-branco.png" width=440>`
- Título: **CARTA DE ACEITE**
- Corpo: *"…foi **ACEITO, conforme o edital da respectiva modalidade** ({trabalho.modalidade}),
  no {evento.titulo}."*
- Local/data: *"Rio de Janeiro / Niterói – RJ, {data.aceite}."*
- Assinatura: **Comissão Científica** + instituições + e-mail (via `{assinatura.comissao}`).

## Mudança proposta (corpo do template, único p/ todas as modalidades)

```
<img src="https://encontrogeig.org/assets/logo-fundo-branco.png" width="440">

CARTA DE ACEITE

A Comissão Científica do {evento.titulo} — evento científico de abrangência nacional,
realizado em Niterói/RJ, de 08 a 10 de julho de 2026 — comunica que o trabalho intitulado
"{trabalho.titulo}", de autoria de {DADOS_AUTORES}, submetido na modalidade
{trabalho.modalidade}, foi ACEITO PARA PUBLICAÇÃO nos Anais do evento, com ISBN e DOI
individual, conforme o edital da respectiva modalidade.

Rio de Janeiro / Niterói – RJ, {data.aceite}.

Prof. Li Li Min
Professor Titular
Comissão Científica
[instituições da realização — manter as já configuradas]
comissao.cientifica@encontrogeig.org
```

Resumo das três edições: **(a)** período "de 08 a 10 de julho de 2026" no corpo;
**(b)** "**ACEITO PARA PUBLICAÇÃO** nos Anais do evento, com ISBN e DOI individual";
**(c)** assinatura: **acrescentar** as linhas `Prof. Li Li Min` + `Professor Titular` **acima**
do bloco institucional existente (`Comissão Científica` + instituições + e-mail
`comissao.cientifica@encontrogeig.org`), que é **mantido**. Preservar o espaçamento enxuto de
1 página já validado em 25/06.

### ⚠️ Nuance da modalidade (decisão a confirmar na execução)

O template é **único para todas as modalidades**. A frase forte e UFF-exata —
*"comprovante de aceite de **artigo completo**, para publicação, em evento científico
nacional"* — **só é correta para Artigo Completo**; aplicá-la a Resumo Expandido / Pôster /
Relatório seria sobre-afirmação. Por isso a redação acima usa **"ACEITO PARA PUBLICAÇÃO nos
Anais (ISBN + DOI), conforme o edital da respectiva modalidade"**, que é **verdadeira para
todas** (Edital do congresso §9: todos os aprovados vão aos anais com ISBN+DOI) e satisfaz o
pedido "aceito para publicação". A frase forte específica de artigo completo permanece **só
na Carta PDF custom Modelo A** (`scripts/gerar_cartas_aceite.py`), que já a contém. Se o
usuário quiser a frase forte literal no template nativo mesmo assim, registra-se que ela
ficará genérica para não-artigos.

## Execução (passo a passo, navegador)

1. **Carregar ferramentas do Chrome** (uma chamada `ToolSearch` com o core set) e
   `tabs_context_mcp` para ver as abas atuais; criar aba nova (não reusar).
2. **Confirmar login** no Even3 organizador (`/organizador/home/`). Se a sessão não estiver
   logada, **pedir ao usuário** para autenticar no Google (não é possível automatizar o
   login Google). Não disparar diálogos modais.
3. **Baixar as cartas atuais** (inspeção, "arquivos completos"): abrir a Carta de Aceite de
   pelo menos um dos trabalhos de teste (códigos **1648163, 1648166, 1648190, 1644279**) via
   `…/participante/impressao/_impressaocartadeaceite?code=<nº>` e salvar o PDF na pasta de
   scratchpad para conferência. Registrar como está hoje (sem período / assinatura genérica).
4. **Abrir o editor do modelo:** `/organizador/trabalhocientifico/modelocartadeaceite/`.
   Capturar o HTML atual do TinyMCE (preservar logo, título e estilos).
5. **Aplicar as três edições** (corpo conforme bloco acima). Preservar tags Even3 intactas
   (`{trabalho.titulo}`, `{DADOS_AUTORES}`, `{trabalho.modalidade}`, `{data.aceite}`,
   `{evento.titulo}`). Na assinatura, **acrescentar** as linhas "Prof. Li Li Min" +
   "Professor Titular" **acima** do bloco `{assinatura.comissao}` existente (que segue com
   "Comissão Científica" + instituições + e-mail) — **sem removê-lo**.
6. **Salvar** o modelo.
7. **Re-baixar** a carta de um trabalho de teste e conferir o PDF renderizado (1 página,
   período presente, frase "ACEITO PARA PUBLICAÇÃO", assinatura do Prof. Li Li Min). Lembrar
   que cabeçalho/rodapé do navegador no "Salvar como PDF" é do navegador (desmarcar
   "Cabeçalhos e rodapés").

## Atualização de docs no repositório (após a edição no Even3)

- **`docs/EVEN3_OPERATIONS.md`** (linhas ~306–318): atualizar a descrição do modelo da Carta
  de Aceite para refletir o novo corpo (período 08–10/07/2026, "ACEITO PARA PUBLICAÇÃO nos
  Anais ISBN+DOI") e a **nova assinatura nominal** (Prof. Li Li Min / Professor Titular,
  acima do bloco Comissão Científica + instituições + `comissao.cientifica@encontrogeig.org`,
  que permanece). Datar a alteração (26/06).
- Registrar no `.claude-docs/SESSION_LOG.md` a mudança do ofício.
- *(Opcional, fora do escopo escolhido)* `docs/CARTAS_ACEITE_EVEN3.md` e o e-mail de
  aprovação (`/emailtemplate/index/1`) ainda usam assinatura "Comissão Científica"; alinhar
  só se o usuário quiser consistência total.

## Verificação (end-to-end)

- PDF re-baixado da Carta de Aceite de um trabalho de teste mostra: período **08 a 10 de
  julho de 2026**, frase **ACEITO PARA PUBLICAÇÃO**, e assinatura **Prof. Li Li Min /
  Professor Titular / Comissão Científica** (com instituições e
  `comissao.cientifica@encontrogeig.org` abaixo), em **1 página**.
- Tags Even3 resolvem corretamente (título, autores, modalidade, data do aceite).
- `git diff docs/EVEN3_OPERATIONS.md` reflete o novo modelo. Sugerir commit ao usuário
  (push à `main` dispara deploy Vercel — só se autorizado).

## Pontos abertos

- **Assinatura confirmada:** Prof. Li Li Min / Professor Titular / Comissão Científica,
  mantendo abaixo as instituições e o e-mail `comissao.cientifica@encontrogeig.org`
  (sem e-mail pessoal nem ORCID; nome + cargo **acrescentados** ao bloco institucional).
- **Frase forte de artigo completo no template único?** Ver nuance acima — recomendação é
  manter genérico-seguro; confirmar na execução se quiser literal.
