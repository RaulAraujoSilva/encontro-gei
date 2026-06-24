# Plano — Aumentar vagas presenciais de 400 para 500 (Even3 + site)

**Data:** 2026-06-24
**Slug:** precisamos-modificar-o-numero-glistening-frog

## Context

O organizador decidiu **ampliar a capacidade presencial do 1º Encontro GEI de 400 para 500 vagas**.
A mudança nasce na plataforma Even3 (onde a inscrição realmente acontece), mas a capacidade é um
número público que aparece em vários lugares do projeto. O histórico mostra que site e Even3 já
estiveram divergentes (em 12/06 a entrada foi ajustada de 500→400 justamente para alinhar; em 17/06
ficou decidido que 400 era o oficial). Para **não reabrir essa divergência**, o organizador optou
(decisão de hoje) por **alinhar tudo em 500**: Even3 **e** o site/edital/conteúdo.

Decisões do organizador (24/06):
- **Escopo:** alterar a Even3 para 500 **e** atualizar o site para refletir 500 (alinhamento total).
- **Login Even3:** a conta é Google OAuth (`raularaujo@crie.coppe.ufrj.br`). O **organizador
  completará o sign-in Google (incl. 2FA)** na janela do Chrome controlada pelo MCP; depois eu sigo.

> Nota: a API REST da Even3 só expõe `GET /event`, `GET /attendees`, `POST /attendees/create` — **não
> há endpoint para editar vagas de entrada**. Por isso a alteração na Even3 só é possível pela UI
> (Chrome MCP), como solicitado.

---

## Parte A — Even3 (Chrome DevTools MCP)

Referência operacional: `docs/EVEN3_OPERATIONS.md` (§2 mapa do painel, §4 padrão de automação).

**Alvo:** Painel → *Inscrições > Entradas e valores* → `/organizador/registration/` → entrada
**"Presencial Completo (Dias 1 e 3)"** → campo de **vagas** → `400` ➜ `500`.
É campo numérico simples (sem máscara de data), então `fill_form` resolve — **não** precisa do truque
de `setVal`/dispatch (esse só é necessário para campos de data dd/mm).

Passos:
1. Abrir/usar o Chrome do MCP e navegar para `https://www.even3.com.br/organizador/registration/`.
2. **Login:** se cair na tela de login Google, pausar e pedir ao organizador para completar o
   sign-in (incl. 2FA) naquela janela; aguardar (`wait_for`) o painel carregar e então continuar.
3. `take_snapshot` na página de entradas; localizar a entrada **"Presencial Completo"** e abrir seu
   editor (clicar no nome/ícone de editar).
4. **Conferir o valor atual** do campo de vagas antes de mexer (esperado: 400; se já estiver 500,
   parar e avisar — nada a fazer).
5. `fill_form` no campo de vagas com `500`.
6. Clicar **Salvar**. (1 ação por chamada; após salvar, recarregar/re-`take_snapshot` — ações que
   recarregam a página derrubam o contexto JS, conforme §4 do doc.)
7. **Verificar:** recarregar `/organizador/registration/` e confirmar que a entrada presencial exibe
   **500 vagas**. Tirar `take_screenshot` como evidência.

---

## Parte B — Site, edital e conteúdo (alinhar para 500)

Edições de texto (`400`/`350` → `500`):

| Arquivo | Linha | Mudança |
|---|---|---|
| `index.html` | 969 | `<div class="mod-vagas">400 vagas</div>` → `500 vagas` (card "Presencial — Dias 1 e 3") |
| `scripts/gerar_edital_consolidado.py` | 180–181 | "…24h … · **400 vagas** presenciais…" → `500 vagas` |
| `scripts/gerar_edital_consolidado.py` | 194 | linha da tabela "Presencial — Dias 1 e 3" → `500 vagas` |
| `docs/CONTENT.md` | 21 | "**350** vagas presenciais …" → `500` (estava defasado) |
| `docs/CONTENT.md` | 138 | tabela "Presencial — Dias 1 e 3 \| **350**" → `500` |

Documentação operacional (refletir o novo número e registrar a data):
- `docs/EVEN3_OPERATIONS.md:38` — remover a nota "⚠️ … 500 no painel; site anuncia 400 — alinhar"
  e deixar consistente (presencial = 500, alinhado em 24/06).
- `docs/EVEN3_OPERATIONS.md:284` — acrescentar linha: vagas presenciais elevadas de 400 → **500** em
  24/06 (Even3 + site alinhados).

Regenerar o edital publicado:
- Rodar `python scripts/gerar_edital_consolidado.py` para regerar `docs/edital/edital-1o-encontro-gei.pdf`
  com "500 vagas". (Conferir no início do script o caminho/nome de saída e dependências —
  `reportlab` etc.)
- ⚠️ O edital é documento **formal/publicado** com "400 vagas" entre os pontos decididos em 17/06.
  Elevar para 500 muda um número oficial — está coberto pela decisão de hoje, mas vale o organizador
  reconfirmar ao revisar o PDF regenerado antes de qualquer redistribuição.

Deploy do site:
- `git add` dos arquivos alterados → `commit` → `push` para `main` (dispara deploy automático na
  Vercel). Token de push válido até 27/06/2026 (`GITHUB_TOKEN`).

**Opcional / a confirmar (NÃO incluído por padrão):** as "metas 400/200/200" de inscritos em
`Plano de projeto/01-eap-entregaveis.md:220,230` e `scripts/gerar_planilha_acompanhamento.py:181`
são *metas de captação por modalidade*, não o limite de vagas. Posso ajustar para 500/200/200 se o
organizador quiser — fora do escopo a menos que peça.

---

## Verificação (end-to-end)

1. **Even3:** screenshot da entrada "Presencial Completo" mostrando **500 vagas** no painel.
2. **Site (pós-deploy):** abrir https://encontrogeig.org (ou preview Vercel) e confirmar no card
   *Modalidades* "Presencial — Dias 1 e 3 → **500 vagas**". `grep` por `400 vagas`/`350` no
   `index.html` e `CONTENT.md` deve voltar vazio para a presencial.
3. **Edital:** abrir o PDF regenerado e confirmar "500 vagas" na seção *Números do evento* e na
   tabela de modalidades.
4. **Consistência:** nenhuma menção residual de capacidade presencial divergente (400/350) nos
   arquivos de produção (`index.html`, `CONTENT.md`, `gerar_edital_consolidado.py`, edital PDF).

---

## Registro (ao final)

- Atualizar `.claude-docs/SESSION_LOG.md` com a sessão de 24/06 (vagas 400→500, Even3 + site).
- Atualizar a memória `project_entradas_even3` (limite presencial agora 500) e, se aplicável,
  `project_edital_consolidado`.
- Conferir `.claude-docs/tasks.md` (TASK-1123/1142 antigas falam de 400 — adicionar nota de que em
  24/06 o oficial passou a 500, sem reescrever histórico).
