# Plano — Modelo de apresentação (.pptx) para o vídeo de submissão

## Contexto

A Fase 1 da chamada exige, junto com o Resumo Expandido, um **vídeo de até 5 minutos** com a apresentação síntese da pesquisa (Even3 + regras). Como o conteúdo desse vídeo é **comum a várias modalidades** (todas as submissões com vídeo seguem a mesma estrutura científica do Resumo Expandido: Introdução → Objetivo → Metodologia → Discussão/Resultados → Considerações Finais), faz sentido oferecer um **template único** de apresentação no padrão visual do evento.

O arquivo deve ser gerado e colocado em pasta do projeto para validação do usuário antes de ser disponibilizado no site.

## Identidade visual (extraída de `index.html` e `assets/`)

**Paleta:**
- Fundo navy: `#091136` (principal), `#0E1A4A`, `#142469` (cards)
- Amarelo: `#F5C842` (Governança)
- Verde: `#7AC74F` (Estratégia)
- Azul: `#4DA8E0` (Inovação)
- Ciano: `#5BC6E5` (decorativo)
- Branco: `#FFFFFF`

**Tipografia:** Manrope (headings) + Outfit (corpo) — não nativas no PowerPoint. **Fallback:** **Calibri** (ou Segoe UI) com pesos 800 / 400 para preservar contraste.

**Logos disponíveis (`assets/`):**
- Evento: `assets/logo-completo.png`, `assets/logo-fundo-branco.png` (versão para slide claro)
- Realizadoras (`assets/logos/`): `uff.svg`, `abar.png`, `labdge.png`, `gigs-unicamp.jpg`
  - Obs.: SVG não é aceito por python-pptx; será usada conversão prévia para PNG (ou manualmente, ou via biblioteca cairosvg/cli).

## Conteúdo dos slides (formato 16:9)

8 slides, 1280×720:

| # | Slide | Conteúdo |
|---|---|---|
| 1 | **Capa** | Fundo navy, logo do evento centralizado no topo, título do trabalho (placeholder), autores, instituições. Faixa decorativa amarelo/verde/azul/ciano na base + tira institucional com 4 logos pequenos das realizadoras |
| 2 | **Equipe e filiação** | Autores (até 4) e respectivas instituições, e-mails de contato. Logo do evento no canto |
| 3 | **Introdução / Contexto** | Título "Introdução" (Manrope-style, 40pt), área de texto vazia (placeholder com instrução discreta sobre o que escrever) |
| 4 | **Objetivo** | Mesma estrutura. Cor de destaque do título: amarelo |
| 5 | **Metodologia** | Cor de destaque: verde |
| 6 | **Resultados e discussão** | Cor de destaque: azul. Espaço para 1 figura/tabela |
| 7 | **Considerações finais** | Cor de destaque: ciano |
| 8 | **Encerramento** | "Obrigado(a)!" com logos das realizadoras + e-mail de contato + URL do evento |

Todos os slides (exceto capa e encerramento) terão **rodapé padronizado** com: logo mini do evento (esquerda), número/total de slides (direita), faixa decorativa fina nas 4 cores.

## Geração do arquivo

**Stack:** `python-pptx 1.0.2` (já disponível no ambiente).

**Novo script:** `scripts/gerar_pptx_apresentacao.py`
- Constrói a apresentação programaticamente (sem template binário); cores e textos definidos no código.
- Embute logos a partir de `assets/logo-fundo-branco.png` e `assets/logos/{uff,abar,labdge,gigs-unicamp}.png`.
- Para `uff.svg` (e `ibp.svg` que não será usado aqui): converter previamente para PNG via uma das opções:
  1. `cairosvg` (Python) — preferida se disponível;
  2. fallback: usar `assets/logo-completo.png` se `uff.svg` não for convertível.
- Saída: `Modelos/Apresentacao_Video_Encontro_GEI.pptx` (pasta original onde os outros modelos foram entregues, para validação).

**Comando:**
```powershell
python scripts/gerar_pptx_apresentacao.py
```

## Fora do escopo (próximo passo, após validação)

Não exponho ainda no site. Quando o usuário aprovar:
- copiar `.pptx` para `assets/modelos/apresentacao-video.pptx`
- adicionar **bloco destacado** no `index.html` logo após a `regras-grid` (linha ~907), por ex. um card único centralizado:
  > "Modelo de apresentação para o vídeo · usado em todas as modalidades com vídeo · [Baixar PowerPoint]"

Esse bloco ficaria entre os cards de modalidades e a seção "Normas técnicas" (linha 911), aproveitando o espaço natural do fluxo.

## Arquivos críticos

- **A criar:** `scripts/gerar_pptx_apresentacao.py` — gerador Python.
- **Saída:** `Modelos/Apresentacao_Video_Encontro_GEI.pptx`.
- **Read-only nesta etapa:** `assets/logo-fundo-branco.png`, `assets/logos/{uff.svg,abar.png,labdge.png,gigs-unicamp.jpg}`, `index.html` (apenas como referência de cores).

## Verificação

1. Rodar `python scripts/gerar_pptx_apresentacao.py` e confirmar que o arquivo foi gerado sem erros.
2. Abrir `Modelos/Apresentacao_Video_Encontro_GEI.pptx` no PowerPoint/LibreOffice e validar:
   - Capa com logo + paleta de fundo navy correta.
   - 8 slides na ordem certa.
   - Logos das 4 realizadoras presentes nos slides 1 e 8.
   - Texto-placeholder legível e em fonte Calibri.
3. **Aguardar aprovação do usuário** antes de mover para `assets/modelos/` e expor no site.
