# Prorrogação Fase 1 + entrega do vídeo por URL pública

## Contexto

Duas mudanças combinadas, ambas amarradas à mesma janela:

1. **Cronograma**: o prazo da Fase 1 (Resumo + vídeo) e do Resultado precisam ser empurrados em 2 semanas — a Even3 está em produção há semanas e até agora o sistema **não permite upload de arquivo de vídeo** dentro do fluxo de submissão. Com isso o autor fica sem como entregar o vídeo, e a solução de contorno (link público em drive + idealmente um campo URL dedicado na Even3) precisa ser divulgada antes que o prazo atual feche em 7 dias.
2. **Entrega do vídeo**: o site, os PDFs de regras e a configuração da Even3 hoje dizem "upload de arquivo de vídeo" — orientação que não funciona. Precisamos trocar para "link público (Google Drive, OneDrive ou YouTube unlisted) colado no corpo do documento" e tentar adicionar, dentro do painel da Even3, um campo dedicado de URL do vídeo na submissão.

Datas finais combinadas (apenas 2 mudaram em relação ao atual; as outras 4 permanecem):

| # | Fase | Data nova | Data antiga |
|---|---|---|---|
| 1 | Fase 1 · Resumo + vídeo | **até 16/06/2026** | até 01/06/2026 |
| 2 | Resultado · Aprovação | **até 22/06/2026** | até 17/06/2026 |
| 3 | Programa Definitivo | 25/06/2026 | (sem mudança) |
| 4 | Fase 2 · Apresentação | 10/07 · NAB UFF | (sem mudança) |
| 5 | Artigo · Versão final | até 30/09/2026 | (sem mudança) |
| 6 | Livro · Anais ISBN | dezembro/2026 | (sem mudança) |

Tom: **apenas substituir as datas** — sem badge de "prazo prorrogado" no hero, sem destaque de extensão.

---

## Mudanças no site (`index.html`)

Todas concentradas em poucas linhas — patterns idênticas, substituição literal:

- **L638** (`navDeadlineText`): `Submissão até 01/06` → `Submissão até 16/06`
- **L653** (`urgency-pill`): `01.06 · 23h59 BRT` → `16.06 · 23h59 BRT`
- **L855** (timeline, dot 1): `até 01/06/2026` → `até 16/06/2026`
- **L856** (timeline, dot 2): `até 17/06/2026` → `até 22/06/2026`
- **L847** (caixa `dl-date`, "Prazo Fase 1"): `1 de junho · 23h59` → `16 de junho · 23h59`
- **L958** (embed Even3, intro): `01/06/2026 23h59` → `16/06/2026 23h59`
- **L973** (embed Even3, rodapé): `01/06/2026 · 23h59` → `16/06/2026 · 23h59`
- **L976** (após embed): `resultado até 17/06/2026` → `resultado até 22/06/2026`
- **L1181** (JS countdown): `new Date('2026-06-01T23:59:00-03:00')` → `new Date('2026-06-16T23:59:00-03:00')`

Entrega do vídeo (separado das datas, mesmo arquivo):

- **L947** (normas, item "Vídeo"): `até 10 min · upload de arquivo` → `até 10 min · link público no documento`
- **L969** (passo 3 do embed): `Faça upload do arquivo + vídeo de 10 min` → `Faça upload do documento + cole o link público do vídeo de 10 min no corpo do texto (e no campo "URL do vídeo" da Even3, se disponível)`
- **L842** (sec-desc da chamada): inserir frase curta sobre vídeo via link público — manter texto enxuto.

---

## Mudanças nos PDFs de regras (`scripts/gerar_regras_pdf.py`)

Fonte única de verdade dos 4 PDFs. Após editar, **rodar `python scripts/gerar_regras_pdf.py`** para regerar os 4 arquivos em `assets/regras/`.

Cronograma (tabela única usada nos 4 PDFs):

- **L177**: `"até 01/06/2026 · 23h59 (Brasília)"` → `"até 16/06/2026 · 23h59 (Brasília)"`
- **L178**: `"até 17/06/2026"` → `"até 22/06/2026"`
- **L152** (caixa amarela `deadline_box`): `1 de junho de 2026` → `16 de junho de 2026`

Seção "Vídeo de apresentação" do **Resumo Expandido** (L241-245) — reescrever:

```python
{"h": "Vídeo de apresentação", "items": [
    "Duração máxima: 10 minutos",
    "Hospedar o vídeo em link público acessível (Google Drive, OneDrive, YouTube unlisted ou similar)",
    "Colar a URL no <b>corpo do documento</b> (final do resumo, antes das referências)",
    "Se a plataforma Even3 disponibilizar campo dedicado de URL na submissão, preencher também — o link no documento é a garantia mínima",
    "Formatos aceitos: MP4 (recomendado), MOV ou WebM"
]}
```

Mesma ressalva no parágrafo de submissão (L201-205) e na descrição do Artigo Completo (L319) — só conferir; não há menção a upload de vídeo nos outros 3 PDFs (pôster, A3, artigo).

---

## Mudanças em docs e README

- **`README.md` L96-97**: trocar `01/06/2026 23h59` → `16/06/2026 23h59` e `17/06/2026` → `22/06/2026`.
- **`docs/CONTENT.md` L150-156**: mesma substituição. **L184** (`Vídeo | até 5 min · URL YouTube/Vimeo`): atualizar para `até 10 min · link público (drive ou unlisted)`. **L196** (`16/05 → 17/06/2026`): atualizar fim para `22/06/2026`.
- **`docs/EVEN3_OPERATIONS.md` L47, L49**: trocar `Cronograma 04/05–01/06` → `Cronograma 04/05–16/06` e `Cronograma 02/06–17/06` → `Cronograma 17/06–22/06` (refletir o que foi configurado na Even3).
- **`.claude-docs/constitution.md` L5**: trocar a nota histórica para `Deadline submissão Fase 1: 16/06/2026 23h59 (movido de 01/06 em 25/05/2026)`.

---

## Reconfiguração da Even3 (via Chrome DevTools MCP)

Seguir o playbook em `docs/EVEN3_OPERATIONS.md` §6 ("Reabrir submissões / mover datas" e "Trocar PDF de regras"). Resumo:

1. **Login** no Chrome MCP em `https://www.even3.com.br/organizador/home/` (conta Raul Araujo via Google).
2. **Mover cronograma de submissão** (`/organizador/trabalhocientifico/submissaogeral?tab=Configurações`):
   - Fim da submissão: `01/06/2026` → `16/06/2026`
   - Usar o snippet `setVal + dispatch` do §3 para contornar a máscara dd/mm.
3. **Mover cronograma de avaliação** (`/organizador/trabalhocientifico/avaliacaogeral?tab=Configurações`):
   - Início: `02/06/2026` → `17/06/2026`
   - Fim: `17/06/2026` → `22/06/2026`
4. **Adicionar campo "URL do vídeo" na submissão** — investigar nesta ordem:
   - Aba `Submissões > Recebimento > Modalidades`: ao editar uma modalidade, verificar se há "Campos adicionais" / "Perguntas extras" no modal.
   - Se não houver, abrir `Submissões > Configurações` e checar "Campos personalizados".
   - Como fallback, abrir uma submissão de teste no fluxo do autor (`/participante/trabalhocientifico/`) para confirmar visualmente os campos disponíveis.
   - Se a Even3 não permitir campo customizado, **a orientação fica só no PDF + no corpo do documento** — sem bloquear o resto do trabalho. Documentar o resultado em `docs/EVEN3_OPERATIONS.md` na seção "Operações comuns".
5. **Trocar os 4 PDFs de regras** anexados (§6 do EVEN3_OPERATIONS.md): para cada modalidade (Resumo, Pôster, Relatório A3, Artigo), abrir o modal, "Trocar regras de submissão", upload do novo PDF de `assets/regras/`, **aguardar 5+ segundos** antes de "Salvar Modalidade".

---

## Ordem de execução

1. Editar `index.html`, `scripts/gerar_regras_pdf.py`, `README.md`, `docs/CONTENT.md`, `docs/EVEN3_OPERATIONS.md`, `.claude-docs/constitution.md`.
2. Rodar `python scripts/gerar_regras_pdf.py` — confirma que os 4 PDFs em `assets/regras/` foram atualizados.
3. Abrir `index.html` localmente (ou `vercel dev`) e validar visualmente o que mudou.
4. Commit + push (auto-deploy Vercel em ~30s).
5. **Even3 (Chrome MCP)**: mover as duas datas, investigar campo URL, re-upload dos 4 PDFs.

---

## Verificação

Site (`https://encontrogeig.org` após deploy):

- [ ] Pill do hero mostra `16.06 · 23h59 BRT`.
- [ ] Nav deadline (quando ≤60 dias do prazo) mostra "Submissão · N dias" coerente com 16/06.
- [ ] Timeline da seção "Envie seu trabalho" mostra `até 16/06/2026` (Fase 1) e `até 22/06/2026` (Resultado).
- [ ] Card "Prazo Fase 1" mostra `16 de junho · 23h59`.
- [ ] Embed Even3 mostra `16/06/2026 · 23h59` e `resultado até 22/06/2026`.
- [ ] Item "Vídeo" nas normas diz "link público no documento" (não "upload de arquivo").
- [ ] Passo 3 do embed orienta colar o link do vídeo no documento.

PDFs (`assets/regras/resumo-expandido.pdf` etc.):

- [ ] Caixa amarela do prazo diz "16 de junho de 2026".
- [ ] Tabela de cronograma mostra 16/06 (Fase 1) e 22/06 (Resultado).
- [ ] Seção "Vídeo de apresentação" do resumo orienta link público no corpo do documento, **não** menciona upload de arquivo de vídeo na Even3 como obrigatório.

Even3:

- [ ] `Submissões > Configurações` mostra fim 16/06/2026.
- [ ] `Avaliação > Configurações` mostra cronograma 17/06–22/06.
- [ ] 4 PDFs novos anexados às 4 modalidades (abrir cada modalidade pelo painel e baixar para conferir).
- [ ] Resultado da investigação do campo URL documentado em `docs/EVEN3_OPERATIONS.md` (existe ou não, e como ficou).

JS:

- [ ] Console no browser: `new Date('2026-06-16T23:59:00-03:00') - new Date()` retorna positivo (deadline no futuro).
