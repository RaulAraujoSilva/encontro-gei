# Plano — E-mail de divulgação das Visitas Técnicas a todos os inscritos

## Context

As 4 Visitas Técnicas do Dia 2 (09/07/2026) do 1º Encontro GEI estão com inscrição
aberta na Even3 **até 07/07** e ainda têm vagas. Hoje é **01/07/2026** — restam ~6 dias.
A adesão depende de o participante, já inscrito no evento, **entrar na Área do Participante
e escolher 1 jornada** (passo que muita gente não fez). Precisamos de um empurrão de
divulgação para **todos os inscritos confirmados (presencial + online), em todas as
modalidades**, com **baixo risco de spam** e sem manusear e-mails/PII fora da plataforma.

**Decisões já tomadas pelo usuário (AskUserQuestion):**
- **Canal:** Even3 (comunicado/e-mail da própria plataforma) — remetente aquecido, lista
  interna, menor risco de spam. *(Fallback documentado: e-mail de gestão via SMTP.)*
- **Público:** todos os inscritos **confirmados** (presencial + online).
- **Formato:** **HTML com identidade visual + links** (fallback texto para entregabilidade).

**Resultado pretendido:** uma peça HTML pronta (com os links de inscrição), enviada como
comunicado da Even3 a todos os confirmados, aumentando as inscrições nas jornadas antes de 07/07.

---

## Entregável 1 — Peça HTML de divulgação (o núcleo do trabalho)

Criar `docs/email/divulgacao-visitas-tecnicas.html` — **e-mail-safe** (tabelas + estilos
*inline*, sem CSS externo, sem JS), para colar no editor de comunicados da Even3 **e**
servir de corpo no fallback SMTP. Criar também a versão texto `…-visitas-tecnicas.txt`
(espelho do HTML) e um `docs/email/README.md` com assunto, pré-cabeçalho e passo a passo.

**Identidade visual** (paleta do site, `index.html`): Navy `#091136`, Amarelo `#F5C842`,
Verde `#7AC74F`, Azul `#4DA8E0`. Fontes com fallback web-safe (Arial/Helvetica) — clientes
de e-mail não carregam Manrope de forma confiável. Logo por **URL no próprio domínio**
(`https://encontrogeig.org/assets/logos/…` ou o `bimi/logo.svg` já hospedado), pequeno;
**nunca** o flyer inteiro como uma imagem única (gatilho nº 1 de spam).

**Estrutura da peça:**
1. Cabeçalho: logo + "1º Encontro GEI · 08–10 jul · Niterói/RJ".
2. Chamada: *Visitas Técnicas — Dia 2 (09/07). Escolha 1 das 4 jornadas. Vagas limitadas,
   inscrições até 07/07.*
3. **Um bloco por jornada (J01–J04)** com setor, resumo de 1 linha, ponto de encontro,
   horário, capacidade e nota de EPI quando houver, + botão **"Inscrever-se nesta jornada"**.
4. CTA principal: **"Escolha sua jornada na Área do Participante"** → link único.
5. "Como funciona": é preciso já estar inscrito no evento (presencial ou online); 1 jornada
   por pessoa; gratuito; a escolha é feita na Área do Participante.
6. Rodapé LGPD: Comissão Organizadora, contato, **por que você recebeu** ("você está inscrito
   no 1º Encontro GEI") e como pedir descadastro (`gestao@encontrogeig.org`).

**Assunto (sem gatilhos de spam):**
`Visitas Técnicas (09/07) do 1º Encontro GEI — inscrições até 07/07`

**Link único de inscrição** (idêntico ao do site; leva à Área do Participante após login):
```
https://www.even3.com.br/evento/login?evento=1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003&ReturnUrl=%2fparticipante%2fsessions%2f&lang=pt
```

### Conteúdo canônico das 4 jornadas (fonte: `index.html`, modais L.1358–1437)

| Jornada | Setor | Ponto de encontro | Saída → Retorno | Vagas | EPI / obs. |
|---|---|---|---|---|---|
| **J01 · Petrobras UTE TermoRio** | Energia · Termelétrica | AGENERSA — Av. Pres. Wilson, 231 · Centro/RJ | 07h30 → ~13h30 | 43 (ônibus) | — |
| **J02 · ETA Guandú + EE Lameirão (CEDAE)** *(integrada)* | Saneamento · Água | CEDAE — Av. Pres. Vargas, 2655 · Centro/RJ | 08h → 18h | 39 | Coffee + transporte; almoço não incluído |
| **J03 · ETE Icaraí + Camboinhas (Águas de Niterói)** *(integrada)* | Saneamento · Pirólise | AGENERSA — Av. Pres. Wilson, 231 · Centro/RJ | 09h → 17h30 | 26 (microônibus) | Informe jaleco/bota nas observações |
| **J04 · Braskem** | Indústria · Petroquímica | AGENERSA — Av. Pres. Wilson, 231 · Centro/RJ | 08h → ~12h | 38 (ônibus) | Jaleco + bota obrigatórios; informe cargo/tamanhos |

> As capacidades acima são as do site. Antes do disparo, conferir vagas **restantes** em
> `GET /api/inscritos` (campo `visitas.j01..j04`) — se alguma jornada estiver cheia, ajustar
> a peça (ex.: "poucas vagas" / marcar como lotada) para não frustrar quem clicar.

---

## Entregável 2 — Canal (Even3) + verificação + fallback

O envio ocorre **no painel da Even3** (não pela API — a API `/attendees` é de leitura). Passos:

1. **Verificar a ferramenta de comunicado em massa** no painel do organizador (evento 722003).
   Procurar por **"E-mails" / "Comunicados" / "Divulgação"** que permita enviar a **todos os
   participantes** (não só submissões). *A doc do projeto (`docs/EVEN3_OPERATIONS.md`) só
   registra comunicado de submissão + "notificar participantes" por atividade; confirmar no
   painel se há broadcast a todos os inscritos.*
   - **Se existir:** definir destinatários = **todos os confirmados**, colar a peça HTML no
     editor (TinyMCE aceita HTML/inline), definir assunto, enviar teste, depois disparar.
   - **Se NÃO existir:** acionar o **fallback SMTP** (abaixo) — decisão a validar com o usuário
     antes de executar, pois muda o canal escolhido.

2. **Operação do painel:** ou o usuário executa seguindo o `docs/email/README.md`, ou — se
   autorizar e estiver logado — posso conduzir via automação de navegador (Chrome/`claude-in-chrome`).

### Fallback (só se a Even3 não tiver broadcast a todos) — `scripts/enviar_divulgacao_visitas.py`

Novo script espelhando `scripts/enviar_cartas_autores.py` (SMTP_SSL `smtp.gmail.com:465`,
remetente `gestao@encontrogeig.org`, App Password em `GESTAO_APP_PWD`, `EmailMessage`,
`make_msgid(domain="encontrogeig.org")`). Diferenças:
- **Lista de destinatários** via API Even3 `GET /api/v1/attendees` (header `Authorization-Token`,
  `EVEN3_API_TOKEN`), paginando e **deduplicando por `id`**; filtra `confirmed is True`;
  reusa a normalização `NFD`+lowercase de `api/inscritos.js` para segmentar/excluir "visita".
  *Risco: confirmar no `--dry-run` que a resposta traz `email`/`name` por attendee.*
- **MIME multipart/alternative** (text/plain espelhado + text/html da peça); logo por URL do
  próprio domínio.
- **Anti-spam:** 1 `To` por mensagem (nunca BCC gigante); `List-Unsubscribe` (mailto) +
  `Precedence: bulk`; throttle 4–9 s com pausa de lote a cada 50; personalização mínima (1º nome).
- **Modos:** `--dry-run`, `--test <email>`, `--send-all` (confirma "ENVIAR"), `--limit N`,
  `--resume` (log JSONL `scripts/data/envio-divulgacao-visitas-log.jsonl`, idempotente).
- **Pré-voo de entregabilidade** (só relevante no fallback SMTP): DKIM ativo no Admin;
  **DMARC em `p=none`** durante a campanha (ver `.claude-docs/plans/para-o-site-do-deep-dewdrop.md`);
  mail-tester ≥ 9/10 com a peça real; começar com `--limit 20` (seeds) antes de liberar.
  *Não versionar listas de e-mail/PII (respeitar `.gitignore`).*

---

## Entregável 3 — Execução da divulgação

1. Conferir vagas restantes em `/api/inscritos` e ajustar a peça se alguma jornada estiver cheia.
2. **Teste:** enviar a peça para `gestao@encontrogeig.org` (e, no fallback, ao mail-tester);
   validar render em Gmail (desktop + mobile), links clicáveis e ausência de "carregar imagens".
3. **Disparo:** pela Even3 (canal escolhido) a todos os confirmados; ou, no fallback, `--send-all`.
4. **Pós-envio:** registrar data/hora e alcance; acompanhar a evolução das jornadas em
   `/api/inscritos` nos dias seguintes; se necessário, um único lembrete perto de 07/07.

---

## Arquivos a criar / modificar

| Arquivo | Ação |
|---|---|
| `docs/email/divulgacao-visitas-tecnicas.html` | **Criar** — peça HTML e-mail-safe (deliverável nº 1) |
| `docs/email/divulgacao-visitas-tecnicas.txt` | **Criar** — fallback texto espelhado |
| `docs/email/README.md` | **Criar** — assunto, pré-cabeçalho, passo a passo Even3 + checklist |
| `scripts/enviar_divulgacao_visitas.py` | **Criar** — *somente se* fallback SMTP for necessário |
| `docs/EVEN3_OPERATIONS.md` | **Atualizar** — registrar a ferramenta de comunicado usada e o disparo |

**Reutilizar (não recriar):** `scripts/enviar_cartas_autores.py` (padrão SMTP/MIME/log),
`api/inscritos.js` (parsing/segmentação de attendees), paleta e cópia de `index.html`.

---

## Verificação end-to-end

- **Peça:** abrir o HTML no navegador (`SendUserFile` para revisão) e enviar um teste real a
  `gestao@` — conferir render em Gmail desktop/mobile, todos os links levando ao evento 722003,
  logo carregando, rodapé LGPD presente.
- **Público:** total de destinatários bate com `count` de `/api/inscritos` (confirmados).
- **Canal Even3:** teste interno recebido na caixa de entrada (não spam) antes do disparo geral.
- **Fallback (se usado):** mail-tester ≥ 9/10; `--dry-run` lista o nº esperado; `--resume` não
  reenvia; DMARC `p=none` confirmado (`nslookup -type=TXT _dmarc.encontrogeig.org`).

---

## Riscos & mitigação

- **Even3 sem broadcast a todos os inscritos** → verificação no painel é o 1º passo; se ausente,
  validar troca para o fallback SMTP com o usuário (muda o canal escolhido).
- **API `/attendees` sem campo de e-mail** (só no fallback) → `--dry-run` inspeciona as chaves do
  1º attendee; alternativa: exportar CSV de "Pessoas" no painel Even3.
- **Jornada lotada no momento do envio** → conferir `/api/inscritos` e ajustar a peça.
- **Spam/entregabilidade** → canal Even3 (aquecido) é o caminho de menor risco; no fallback,
  seguir o pré-voo e o throttle.
- **Encoding/acentuação** → UTF-8/NFC de ponta a ponta (evitar o mojibake visto no log das cartas).

---

## Pós-plano (conforme instruções globais)

- Salvar cópia deste plano (já está em `.claude-docs/plans/`).
- Extrair tasks para `.claude-docs/tasks.md`.
- Atualizar `MEMORY.md`/memória com o resultado (canal efetivo, data do disparo, alcance).
