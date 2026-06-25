# Plano — Link direto para a escolha das visitas (Área do Participante)

**Data:** 2026-06-24
**Slug:** precisamos-modificar-o-numero-glistening-frog (reutilizado)

## Context

Após migrar as visitas para **Atividades** da Even3 (concluído), os links dos cards do site apontavam
para a **página do evento** — o participante tinha que logar no canto, achar "Programação" e procurar as
visitas no meio de muitas atividades. O organizador pediu **um link o mais direto possível** (login →
cair direto na escolha das visitas) e avaliou limpar as demais atividades.

**Descoberta (read-only, hotsite + /participante/sessions/):** existe um link nativo do hotsite
("QUERO PARTICIPAR DAS ATIVIDADES") que faz **login → redireciona direto** para
`/participante/sessions/`, e essa tela mostra **somente as 4 Visitas Técnicas** (cada uma com botão
"Realizar inscrição" + filtros Tipo/Data). As atividades do Dia 1/Dia 3 **não aparecem** ali. Logo:
- O link direto **resolve 100%** o pedido.
- **Limpar as demais atividades é desnecessário** (a tela de inscrição já é limpa) e foi **descartado**
  pelo organizador (preserva a Programação pública do hotsite Even3 e certificados/credenciamento).

**Link direto a usar (encode exato):**
```
https://www.even3.com.br/evento/login?evento=1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003&ReturnUrl=%2fparticipante%2fsessions%2f&lang=pt
```
- Deslogado → pede login e cai em `/participante/sessions/` (as 4 visitas).
- Logado → vai direto para a tela das 4 visitas.

## Mudanças (`index.html`)

1. **4 modais de jornada (J01–J04):** trocar o `href` do CTA
   `<a class="vtmodal-link" ...>Escolher esta jornada na Área do Participante ↗</a>` (hoje aponta para a
   página do evento) pelo **link direto** acima. Texto → "**Inscrever-se nesta jornada ↗**".
   (Usar `replace_all` — os 4 CTAs são idênticos.)
2. **Card `#inscricao` "Atividade · Visita Técnica":** acrescentar um link/botão claro com o **link
   direto** — ex.: "**Quero participar de uma visita técnica →**" — para quem chega pela seção de
   inscrição. Manter o texto do passo a passo (Programação › Minhas Atividades) como apoio.
3. (Opcional) **Card `#modalidades` "Visita Técnica — Dia 2":** sem link hoje; pode receber o mesmo
   link direto se quisermos 1 clique a partir das modalidades — baixo impacto, avaliar.

**Não mexer:** atividades do Dia 1/Dia 3 na Even3 (decisão: manter); entradas (Presencial/Online);
config das atividades (máx. 1, janela 01/07, restrito a inscritos) — já feitas.

## Verificação

1. **Deslogado (aba anônima):** abrir o link direto → deve cair na tela de **login** e, após autenticar,
   em `/participante/sessions/` mostrando **só as 4 visitas** com "Realizar inscrição".
2. **Logado:** abrir o link → vai direto às 4 visitas.
3. **Site (pós-deploy):** nos modais J01–J04 e no card de inscrição, o CTA aponta para o link direto
   (conferir `href` no DOM); `grep` por `participante/sessions` no `index.html` deve achar os CTAs.

## Deploy / registro

- `git add index.html` → commit → push `main` (deploy Vercel).
- Atualizar memória `project_visitas_confirmadas_dia2` / `project_entradas_even3` com o link direto e a
  decisão de não limpar atividades (a tela de inscrição já filtra só as visitas).
