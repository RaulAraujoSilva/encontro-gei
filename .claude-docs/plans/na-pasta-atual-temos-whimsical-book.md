# Plano — Atualização do site do 1º Encontro (programa, locais e transmissão)

## Context

O site do congresso (`index.html`, página única) precisa refletir decisões já validadas:

1. **Programa** — a programação detalhada foi consolidada em `Atualização/Programacao_1o_Encontro_limpa (1).docx`. Os cards de dia no site estão com horários antigos e sem coffee-breaks/almoço/painéis. Só a parte pública é válida — a seção **"USO INTERNO – Confirmação de participantes"** do .docx NÃO vai para o site.
2. **Locais** — os endereços dos Dias 1 e 3 foram definidos (`Atualização/Endereços.txt`). Hoje o site exibe "Local em definição". Precisamos (a) referência rápida inline e (b) uma seção dedicada com mapa incorporado do Google Maps + link.
3. **Transmissão ao vivo** — a modalidade "Remoto / Online" foi comentada no código ("reativar se transmissão online for contratada"). Foi decidido reativá-la como oferta confirmada.

**Decisões do usuário:** Campus do Dia 3 = **Praia Vermelha** (corrige "Gragoatá"); transmissão = **oferta confirmada** (sem selo); detalhe do programa = **completo (do .docx)**.

Arquivo único a modificar: `index.html`.

---

## Dados validados (fonte: .docx + Endereços.txt)

**Dia 1 · 08/07 — Abertura Institucional** · Auditório do DER, Av. Pres. Vargas, 1100 – 14º andar, Centro, Rio de Janeiro
- 13h30 Credenciamento digital e recepção
- 14h30 Mesa de abertura institucional
- 15h30 Painel de apresentação do evento
- 16h30 Coffee-break
- 17h00 Conferência Magna de abertura
- 18h00 Coquetel de networking institucional

**Dia 2 · 09/07 — Visitas Técnicas** · 8 jornadas paralelas · Região metropolitana
- 06h30 Concentração e distribuição de kits no hub
- 07h00 Primeira janela de partida
- 07h30 · 08h00 · 08h30 Partidas escalonadas
- 09h–17h Realização das visitas

**Dia 3 · 10/07 — Trilhas, Sessões e Encerramento** · NAB UFF, Rua Edmundo March, s/n – Campus da Praia Vermelha, Niterói
- 09h00 Plenária + Painel "IA e soberania"
- 10h00 Coffee-break
- 10h30 Trilhas A, B, C e D simultâneas — apresentação dos artigos selecionados (4 salas) + Painel 1 (Saneamento)
- 12h30–14h00 Intervalo para almoço
- 14h00 Painel 2 (Energia, auditório) + Sessões de posters (4 trilhas no mesmo local)
- 16h00 2º Coffee-break
- 16h30 Premiação dos trabalhos e encerramento institucional

**Endereços / Maps:**
- DER: `Av. Pres. Vargas, 1100 - Centro, Rio de Janeiro - RJ, 20071-002` → https://share.google/PJFWe9XyKWYAz5c6j
- NAB UFF: `Rua Edmundo March, s/n - Praia Vermelha, Niterói - RJ, 24210-310` → https://share.google/QjBLrQ0LQiNhCIWRu

---

## Mudanças em `index.html`

### 1. Programa (cards de dia) — linhas ~742-779
Substituir as 3 `<ul class="di">` pelos horários completos acima. Atualizar os rótulos de local (`.dl`):
- Dia 1 (`746`): `Local em definição · Rio de Janeiro` → `Auditório do DER · Av. Pres. Vargas, 1100 · Centro · Rio de Janeiro`.
- Dia 3 (`772`): `NAB UFF · Campus Gragoatá · Niterói` → `NAB UFF · Campus da Praia Vermelha · Niterói`.
- Texto do intro (`740`): trocar `Campus Gragoatá` por `Campus da Praia Vermelha`.

### 2. Keynote — linha ~718
`<div class="kd-i">julho 2026<br>Local em definição<br>Rio de Janeiro</div>` → `...<br>Auditório do DER<br>Centro · Rio de Janeiro`.

### 3. Nova seção "Locais do evento" — inserir após a seção VISITS (antes de `<!-- MODALIDADES -->`, ~linha 818)
- `<section class="sec" id="local">` com título e dois "venue cards" (Dia 1 — DER; Dia 3 — NAB UFF). Dia 2 fica como nota ("pontos de partida nas jornadas técnicas").
- Cada card: nome, endereço completo, **mapa incorporado** via iframe sem chave de API:
  `https://www.google.com/maps?q=<endereço URL-encoded>&output=embed` (com `loading="lazy"`, `title`, `referrerpolicy="no-referrer-when-downgrade"`).
- Botão "Abrir no Google Maps" apontando para os links `share.google` acima.
- Reaproveitar visual do bloco de embed existente (`.embed-wrap`/`.embed-iframe`, def. ~linhas 372-392); adicionar pouco CSS novo (grid de 2 colunas → 1 coluna em mobile) na folha de estilo `<style>`.
- Adicionar item de menu `<li><a href="#local">Local</a></li>` no nav (`631-637`).

### 4. Transmissão ao vivo (modalidades) — linhas ~822-831
- Descomentar o card MOD-3 OCULTA (Remoto / Online) e exibi-lo como oferta confirmada (sem selo).
- Renumerar: Remoto/Online = **Modalidade 3**; "Visitante Técnico — Dia 2" = **Modalidade 4**.
- Título (`822`): `Três formas de participar` → `Quatro formas de participar`.
- Conferir que `.modal-grid` acomoda 4 cards (grid já é responsivo; validar visualmente).

### 5. JSON-LD (SEO) — linha ~32 (opcional, recomendado)
Enriquecer `"location"` com os dois `Place` reais (DER e NAB UFF) e respectivos endereços, mantendo `MixedEventAttendanceMode` (coerente com a transmissão online).

---

## Fora do escopo (não alterar)
- Seção "USO INTERNO – Confirmação de participantes" do .docx (não publicar).
- Selos "a confirmar" dos palestrantes e das jornadas técnicas ("A confirmar") — permanecem como estão.
- Blocos já comentados não relacionados (COUNTER-OCULTO, APOIO-OCULTO, Escola de Regulação, etc.).

## Verificação
1. Abrir `index.html` no navegador (ou `python -m http.server` na pasta) e conferir:
   - Cards de dia com horários do .docx e locais corretos (DER / Praia Vermelha).
   - Nova seção "Local": dois mapas carregam e centralizam nos endereços corretos; botões abrem o Google Maps.
   - Modalidades: 4 cards, com "Remoto / Online" visível; título "Quatro formas de participar".
   - Link "Local" no menu rola até a seção.
2. Validar responsividade (mobile): mapas e grid de modalidades empilham corretamente.
3. Conferir acentuação PT-BR em todo o texto inserido.
