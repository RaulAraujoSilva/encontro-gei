# Plano — Ajustes pós-revisão (modalidades, programação, realização)

## Contexto

Três ajustes pontuais solicitados pelo usuário no `index.html` após revisão do site:

1. **Modalidade "Visitante Técnico — Dia 2"** está rotulada como "Modalidade 4" (porque a antiga Modalidade 3 — Remoto/Online — foi ocultada). Como só existem 3 modalidades visíveis, renumerar para **Modalidade 3**.
2. **Programação Dia 3** lista "16h30 — Premiação" e "18h00 — Encerramento institucional · 19h coquetel" em horários separados. Unificar **premiação + coquetel em um único horário**, antecipando para liberar quem tem voo à noite.
3. **Realização** atualmente lista UFF, ABAR e PPGEP/UFF. Adicionar **GIGS · UNICAMP** (Grupo de Inovação e Gestão na Saúde) como quarta instituição realizadora, em todos os pontos do site onde "Realização" é mencionada.

## Mudanças

### 1. Renumerar Modalidade 4 → 3

**Arquivo:** `index.html`
**Linha 794:** Trocar `Modalidade 4` por `Modalidade 3` no card "Visitante Técnico — Dia 2".

(Manter o comentário HTML acima — `MOD-3 OCULTA (reativar se transmissão online for contratada)` — mas atualizar para refletir que o slot 3 agora é usado pelo Visitante Técnico; sugerir renomear para `MOD-REMOTO OCULTA (numeração anterior 3, hoje removida da grade)`.)

### 2. Unificar premiação + coquetel · Dia 3

**Arquivo:** `index.html`
**Linhas 740–741:** substituir os dois `<li>` finais por um único item, antecipando o horário para que participantes com voo consigam pegá-lo.

Proposta de redação (a confirmar com o usuário no horário exato):
```html
<li><strong>16h30</strong> — Premiação dos melhores trabalhos · coquetel de encerramento</li>
<li><strong>18h00</strong> — Encerramento institucional</li>
```

Alternativa mais enxuta (1 linha só, recomendada para "adiantar para quem vai pegar avião"):
```html
<li><strong>16h30</strong> — Premiação dos trabalhos, coquetel e encerramento institucional</li>
```

→ **Pendente decisão do usuário** entre as duas opções (ver pergunta abaixo).

### 3. Adicionar GIGS · UNICAMP como Realização

**3a. Salvar logo** (ação manual antes do código)
- Copiar `assets/WhatsApp Image 2026-05-05 at 15.31.08.jpeg` → `assets/logos/gigs-unicamp.png` (idealmente convertido para PNG com fundo transparente; se mantido JPEG, usar `.jpg` e aceitar fundo branco).

**3b. Bloco Realização — `index.html` linhas 968–977**
Adicionar 4º card após o PPGEP:
```html
<a href="https://www.fcm.unicamp.br" target="_blank" rel="noopener" class="ptc fi d3"><div class="ptc-logo"><img src="/assets/logos/gigs-unicamp.png" alt="GIGS · UNICAMP — Grupo de Inovação e Gestão na Saúde"></div><div class="pf">Grupo de Inovação e Gestão na Saúde · UNICAMP</div></a>
```
→ **Pendente confirmação do usuário** sobre a URL oficial do GIGS (FCM/UNICAMP, IG/UNICAMP, ou outra).

**3c. Outras menções textuais a "UFF, ABAR e PPGEP/UFF"** — acrescentar GIGS:
- Linha 594 (nav-meta): `UFF · ABAR · PPGEP/UFF · GIGS`
- Linha 621 (h-lede): `... UFF, ABAR, PPGEP/UFF e GIGS/UNICAMP.`
- Linha 647 (chips Realização do hero): adicionar `<span class="pc">GIGS/UNICAMP</span>`
- Linha 787 (modalidades — pré-inscrição prioritária): `... UFF, ABAR, PPGEP/UFF, GIGS/UNICAMP e instituições parceiras ...`
- Linha 932 (inscrição — pré-inscrição prioritária): idem.
- Linha 939 (certificação — caixa central): `Certificação emitida por UFF, ABAR, PPGEP/UFF e GIGS/UNICAMP ...`
- Linha 1001 (certificação — aside): idem.
- Linha 1030 (footer): `... Realização: UFF · ABAR · PPGEP/UFF · GIGS/UNICAMP.`
- Linha 1053 (copyright footer): `© 2026 1° Encontro GEI · UFF · ABAR · PPGEP/UFF · GIGS/UNICAMP`
- Linha 36 (JSON-LD organizer): adicionar `{"@type":"Organization","name":"GIGS · UNICAMP — Grupo de Inovação e Gestão na Saúde"}`

## Arquivos a modificar

- `index.html` — todas as alterações textuais e de markup
- `assets/logos/gigs-unicamp.png` (novo) — copiado/convertido a partir do WhatsApp Image fornecido

## Verificação

1. Abrir `index.html` no navegador (Live Server / dev server).
2. **Modalidades:** confirmar que aparecem 3 cards numerados 1, 2, 3 (sem pular para 4).
3. **Programação Dia 3:** confirmar que premiação + coquetel aparecem unificados às 16h30.
4. **Realização:** seção `#parceiros` deve mostrar 4 logos (UFF, ABAR, PPGEP, GIGS); verificar dimensões/proporção do logo GIGS.
5. **Buscar no DOM** por "PPGEP/UFF" para garantir que todas as ocorrências foram acompanhadas por GIGS.
6. Validar JSON-LD com https://validator.schema.org/ (colar o trecho).

## Decisões confirmadas pelo usuário

1. **Programação Dia 3:** unificar em linha única — `16h30 — Premiação dos trabalhos, coquetel e encerramento institucional`. Remover o `<li>` das 18h.
2. **Logo GIGS:** manter JPEG original. Copiar `assets/WhatsApp Image 2026-05-05 at 15.31.08.jpeg` → `assets/logos/gigs-unicamp.jpg`.
3. **Card Realização — GIGS:** renderizar como `<div>` (sem `<a>` href) até URL oficial ser confirmada. Markup:
   ```html
   <div class="ptc fi d3"><div class="ptc-logo"><img src="/assets/logos/gigs-unicamp.jpg" alt="GIGS · UNICAMP — Grupo de Inovação e Gestão na Saúde"></div><div class="pf">Grupo de Inovação e Gestão na Saúde · UNICAMP</div></div>
   ```
   → Verificar se `.ptc` sem `<a>` mantém o mesmo estilo visual; se necessário, ajustar CSS para aplicar a `div.ptc` também.
