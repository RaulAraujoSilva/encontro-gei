# Edital — fechar versão para publicação (1º Encontro GEI)

## Context

O **edital consolidado** (PDF de validação) já foi gerado por `scripts/gerar_edital_consolidado.py` →
`docs/edital/edital-consolidado-1o-encontro-gei.pdf`, reaproveitando o layout dos PDFs de regras
(`scripts/gerar_regras_pdf.py`). Ele trazia um apêndice com **6 pontos pendentes**. O usuário revisou,
**decidiu os 6 pontos** e ainda **incluiu um novo organizador**. Objetivo agora: **fechar a versão para
publicação** (sem framing interno e sem apêndice), aplicando todas as decisões.

### Decisões tomadas (todas a aplicar)
1. **Escola de Regulação (AGETRANSP/AGENERSA) = organizador pleno** → realização + certificação + LGPD +
   **rodapé dos PDFs de regras**.
2. **Instituto de Computação/UFF (IC/UFF) = organizador pleno** (novo) → mesmo tratamento da Escola de
   Regulação. Logo fornecido pelo usuário (salvar em `assets/logos/instituto-computacao-uff.png`).
   → A lista de realização passa a ter **6 instituições**: UFF · ABAR · PPGEP - LabDGE/UFF · GIGS/UNICAMP ·
   Escola de Regulação · Instituto de Computação/UFF.
3. **Vagas presenciais = 400** (site já reflete; alinhar Even3 para 400 é follow-up manual).
4. **Keynote da Conferência Magna = genérico** — não nomear o palestrante no edital.
5. **Política de Privacidade = referência limpa** — remeter a `/privacidade/` **sem** "sujeita a validação jurídica".
6. **Visitas técnicas do Dia 2 = manter** "locais a confirmar / inscrições em breve".
7. **"Artigo (resumo)" = 5ª modalidade distinta** — resumo em **texto no formulário da Even3, até 700
   palavras** (legada, 37 submissões), ao lado de Resumo Expandido (arquivo), Pôster A3, Relatório A3 e Artigo Completo.

> Fonte de verdade = `index.html` em produção. Cronograma vigente: Fase 1 **25/06** · resultado **27/06** ·
> programa **28/06** · apresentação **10/07** · artigo **30/09** · anais **dez/2026**.
> **Abrangência desta entrega:** edital de publicação + 4 PDFs de regras. Site (index.html/JSON-LD),
> `/privacidade/` e fundo do certificado **ficam para etapa seguinte** (decisão do usuário).

## Abordagem

Dois scripts já existentes; reaproveitar o sistema visual compartilhado. Salvar o logo do IC/UFF.

### A) `scripts/gerar_edital_consolidado.py` — versão de publicação
Parametrizar `build(publicacao=True)` (default). No modo publicação:
- **Subtítulo:** trocar "Documento interno para validação prévia…" por linha de realização com as **6
  instituições** (UFF · ABAR · PPGEP - LabDGE/UFF · GIGS/UNICAMP · Escola de Regulação · Instituto de
  Computação/UFF). Título → "Edital — Chamada de Trabalhos e Participação".
- **Certificação (seção 4):** atualizar para "emitida por UFF, ABAR, PPGEP - LabDGE/UFF, GIGS/UNICAMP,
  Escola de Regulação e Instituto de Computação/UFF".
- **Realização (seção 1):** acrescentar o item "Instituto de Computação/UFF" à lista de bullets.
- **Remover a seção 12 (apêndice)** e a nota final de validação (substituir por linha neutra
  "encontrogeig.org · junho de 2026").
- **Seção 6 (Submissões):** acrescentar a **5ª modalidade "Artigo (resumo)"** na `grid_table` (texto · até
  700 palavras · formulário Even3 · até 25/06 · "modalidade de Fase 1 mantida"); ajustar a remissão dos 4
  PDFs anexos.
- **LGPD (seção 10):** incluir o IC/UFF entre as instituições realizadoras e **remover** "(sujeita a
  validação jurídica…)".
- **Saída:** `docs/edital/edital-1o-encontro-gei.pdf`. Manter a variante de validação via `build(publicacao=False)`.

### B) `scripts/gerar_regras_pdf.py` — incluir Escola de Regulação + IC/UFF
- **Rodapé (`header_footer`, ~l.55-71) — reestruturar para caber 6 instituições.** Hoje os créditos ficam
  numa única linha de 7.5pt que já está no limite; com 6 instituições estoura a faixa A4. Plano:
  mover os créditos institucionais para **uma linha própria** do rodapé, em **~7pt**, com rótulos compactos
  (`UFF · ABAR · PPGEP/UFF · GIGS/UNICAMP · Escola de Regulação · IC/UFF`), mantendo site+e-mails noutra
  linha e o nome do evento na linha de cima. Se necessário, aumentar a faixa navy (18mm → ~22mm) e o
  `bottomMargin` correspondente (2.6cm → ~3.0cm). **Verificar visualmente que nada estoura.** Como o edital
  reusa `base.header_footer`, o rodapé dele acompanha a mudança.
- **Subtítulo de realização (`gerar_pdf`, l.150):** listar as 6 instituições.
- **Comissão científica (l.199-201):** generalizar para "pelas instituições realizadoras do evento" (evita
  sugerir que todas fazem avaliação por pares).
- **Regenerar os 4 PDFs** de `assets/regras/` rodando o script.

### C) Salvar o logo do IC/UFF
Gravar a imagem enviada em `assets/logos/instituto-computacao-uff.png` (fundo branco). Não é usada nos PDFs
(que creditam por texto), mas fica pronta para a etapa seguinte (site + fundo do certificado).

## Arquivos
- **Editar:** `scripts/gerar_edital_consolidado.py` (modo publicação + 6 realizadoras + 5ª modalidade) e
  `scripts/gerar_regras_pdf.py` (créditos das 6 instituições + rodapé reestruturado).
- **Criar:** `assets/logos/instituto-computacao-uff.png`.
- **Reusar:** helpers visuais de `gerar_regras_pdf.py` (cores, estilos, `build_header`/`header_footer`/`deadline_box`/`eixos_box`).
- **Saídas:** `docs/edital/edital-1o-encontro-gei.pdf` + `assets/regras/{resumo-expandido,poster,relatorio-a3,artigo-completo}.pdf` (regenerados).

## Follow-ups manuais / etapa seguinte (registrar, fora desta entrega)
- **Even3:** alinhar entrada presencial para **400**; abrir entrada "Visita Técnica" do Dia 2; em **25/06**
  ocultar modalidades de Fase 1 conforme já planejado.
- **Site + certificado (próxima etapa):** incluir IC/UFF e Escola de Regulação como realizadores em
  `index.html` (logos/realização/certificação/JSON-LD), `/privacidade/` (receptores de dados) e no fundo do
  certificado (`scripts/gerar_fundo_certificado.py`, hoje com 6 slots de logo).

## Verificação
1. Rodar `python scripts/gerar_regras_pdf.py` e `python scripts/gerar_edital_consolidado.py` — sem erro.
2. Reabrir `docs/edital/edital-1o-encontro-gei.pdf` e conferir:
   - **Sem** subtítulo "Documento interno…" e **sem** seção 12 (apêndice).
   - Realização e certificação com as **6 instituições** (incl. Escola de Regulação e IC/UFF).
   - Seção 6 com **5 modalidades** (incl. "Artigo (resumo)", texto, até 700 palavras).
   - LGPD **sem** ressalva jurídica; keynote sem nome; **400 vagas**; visitas Dia 2 "inscrições em breve".
   - **Rodapé com as 6 instituições, sem overflow** da faixa navy, em todas as páginas.
   - Acentuação portuguesa correta.
3. Reabrir `assets/regras/artigo-completo.pdf` e confirmar o rodapé reestruturado com Escola de Regulação +
   IC/UFF, sem overflow.
