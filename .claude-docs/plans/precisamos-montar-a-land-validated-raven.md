# Plano — Polish final: AGENERSA + abrir submissões + regras de submissão (PDFs adaptados)

## Context

Iteração final de refinamento sobre o site já no ar (https://encontro-gei.vercel.app) e o evento Even3 já configurado. Três correções pontuais:

1. **AGENERSA invisível** — meu processamento anterior (Pillow alpha-strip com threshold RGB>235) destruiu o logo: agora 0 pixels opacos. Imagem original tinha texto fino em tons claros que caíram dentro do threshold de "branco".
2. **Even3 — Submissões fechadas** — cronograma configurado começa em 06/05/2026 e o user quer testar HOJE (05/05/2026). A área pública mostra "Submissão não disponível".
3. **Regras de submissão por modalidade** — existem 4 PDFs em `Regras de submissão/` referentes ao "II/XII Lean Six Sigma Congress 2024" que precisam ser adaptados para o 1º Encontro GEI, com o logo oficial, e:
   - Salvos como PDF
   - Disponibilizados para download na landing (nova seção)
   - Subidos como anexo nas Modalidades correspondentes da Even3

## Arquivos críticos

### Existentes (apenas leitura/referência)
- `assets/logos/agenersa.png` — destruído, precisa re-download
- `Regras de submissão/RESUMO EXPANDIDO XII LEAN SIX SIGMA CONGRESS.pdf` (2 pp.)
- `Regras de submissão/POSTER XII LEAN SIX SIGMA CONGRESS.pdf` (1 pp.)
- `Regras de submissão/RELATRIO A3 XII LEAN SIX SIGMA CONGRESS.pdf` (2 pp.)
- `Regras de submissão/ARTIGO COMPLETO XII LEAN SIX SIGMA CONGRESS.pdf` (2 pp.)
- `assets/logo-completo.png` — usar como cabeçalho dos PDFs
- `index.html` — adicionar bloco de download
- `.gitignore` — `*.pdf` está ignorado; precisa exceção para `assets/regras/*.pdf`

### Novos
- `assets/logos/agenersa.png` — re-baixar de `https://www.rj.gov.br/agenersa/sites/default/files/LogoAgenersa_Centro.png` (sem stripping de fundo — o card de parceiros já tem fundo branco)
- `assets/regras/resumo-expandido.pdf`
- `assets/regras/poster.pdf`
- `assets/regras/relatorio-a3.pdf`
- `assets/regras/artigo-completo.pdf`
- `scripts/gerar_regras_pdf.py` — gerador único (reportlab) que produz os 4 PDFs com header de logo + estilos consistentes

## Etapas

### 1. AGENERSA — restaurar logo (~3 min)
- `curl` da URL oficial → `assets/logos/agenersa.png`
- Verificar com Pillow que `total_opaque_pixels > 0`
- Não processar/strip — confiar no card de fundo branco já existente

### 2. Even3 — abrir submissões (~5 min via Chrome MCP)
- Navegar `/organizador/trabalhocientifico/submissaogeral?tab=Configurações`
- Clicar "Editar cronograma"
- Setar **Iniciar submissões em**: `04/05/2026` (hoje no fuso BR)
- Manter **Finalizar**: `15/05/2026`
- Salvar
- Validar via iframe da landing que aparece "Submissão aberta" ao invés de "Submissão não disponível"

### 3. Geração dos 4 PDFs adaptados (~10 min)

**Conteúdo a adaptar** (usar texto extraído como base — ver Phase 1):

Cada PDF terá a mesma estrutura visual:
- **Header** com logo (`logo-completo.png`, ~120px altura) + cabeçalho institucional "1° Encontro de Governança, Estratégia e Inovação Governamental · 08-10/07/2026 · Rio de Janeiro/Niterói"
- **Título** "Normas de Submissão — [Modalidade]"
- **Bloco de prazo destacado** com fundo amarelo claro: "Fase 1 — Resumo + Vídeo · até 15/05/2026 23h59"
- **Corpo** com as regras técnicas adaptadas (Arial 12, espaçamento, margens, etc — preservadas do original)
- **Lista de eixos temáticos** (13 do nosso projeto, não os do XII LSS)
- **Footer** com URL `https://encontro-gei.vercel.app` + e-mail contato + crédito UFF/ABAR/PPGEP/Escola

**Substituições de texto críticas em todos os 4:**
- "II/XII LEAN SIX SIGMA CONGRESS - 2024" → "1° Encontro de Governança, Estratégia e Inovação Governamental — 2026"
- "I CONGRESSO EM EXCELÊNCIA DE SERVIÇOS REGULADOS" → remover (não é o caso aqui)
- URLs do `even3.com.br/leansixsigmacongress2024` → URL do evento atual (`722003`)
- Templates Google Docs → manter como referência opcional, ou substituir por placeholders "[template em definição]"
- Adicionar comissão científica do 4º SSEP (Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio, Silvia Cristina Rufino)

**Especificidades por modalidade** (preservadas dos originais):

| PDF | Particularidades |
|---|---|
| Resumo Expandido | 700 palavras, 3-5 keywords, parágrafo único, 4 subtítulos (Intro/Obj/Metod/Disc/Conclusão) |
| Pôster A3 | Modelo visual A3, mesmas seções do resumo |
| Relatório A3 | Modelo DMAIC (Definir/Medir/Analisar à esquerda; Implementar/Controlar à direita), 1 página |
| Artigo Completo | 2 arquivos (com/sem identificação de autoria), 8.000 palavras max, ABNT |

**Implementação técnica:**
- Script Python único `scripts/gerar_regras_pdf.py` usando **reportlab**
- Função `gerar_pdf(modalidade, conteudo_dict)` chamada 4 vezes
- Estilos compartilhados: cores do evento (navy `#091136`, yellow `#F5C842`, green `#7AC74F`)
- Imagem de header reutilizada nas 4 saídas

### 4. Adicionar bloco de download na landing (~5 min)

Inserir na seção `#trabalhos`, **após** o grid de 13 eixos, um bloco "Normas por modalidade":

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ 📄 Resumo   │ 🖼 Pôster   │ 📊 Relatório│ 📑 Artigo   │
│ Expandido   │ A3          │ A3          │ Completo    │
│             │             │             │             │
│ Baixar PDF  │ Baixar PDF  │ Baixar PDF  │ Baixar PDF  │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

Cada card linka para `/assets/regras/<slug>.pdf` com `download` attribute.

### 5. Upload dos PDFs na Even3 — modalidades de submissão (~10 min via Chrome MCP)

Navegar `/organizador/trabalhocientifico/submissaogeral?tab=Modalidades`

Para cada uma das 4 modalidades existentes (Artigo, Pôster, Relatório A3, Resumo):
- Abrir modal de edição
- Localizar campo "Regras de submissão" / "Anexo" / "Documentação"
- Upload do PDF correspondente
- Salvar

Se a Even3 não tiver campo de upload nativo, alternativa: editar a descrição da modalidade incluindo o link público do PDF hospedado no Vercel (`https://encontro-gei.vercel.app/assets/regras/...pdf`).

### 6. Deploy e validação E2E

- `git add` + commit + push (`assets/regras/`, `assets/logos/agenersa.png`, `index.html`, `scripts/`)
- `vercel deploy --prod`
- Validar:
  1. AGENERSA aparece no grid de parceiros
  2. PDFs acessíveis em `/assets/regras/<slug>.pdf` (HTTP 200, content-type pdf)
  3. Bloco de download renderiza no `#trabalhos`
  4. Iframe Even3 mostra "Submissão aberta" e botão "Realizar Submissão" funcional
  5. Modalidades na Even3 têm regras anexadas (PDF ou link na descrição)

## Verificação

```bash
# Logos
curl -sI https://encontro-gei.vercel.app/assets/logos/agenersa.png | grep -i content-length
# PDFs (4)
for f in resumo-expandido poster relatorio-a3 artigo-completo; do
  curl -sI "https://encontro-gei.vercel.app/assets/regras/$f.pdf" | grep -E "HTTP|content-length"
done
# Even3 contador
curl -s https://encontro-gei.vercel.app/api/inscritos
```

Visualmente via Chrome MCP:
- Hero → ver logo nav cropado e meta strip
- `#parceiros` → AGENERSA visível
- `#trabalhos` → 13 eixos + 4 cards de regras
- Iframe `#submeter` → "Submissão aberta"

## Riscos e mitigações

| Risco | Mitigação |
|---|---|
| AGENERSA URL pode estar bloqueada por User-Agent | Tentar com `-A "Mozilla/5.0"`; se falhar, baixar versão Wikipedia Commons como backup |
| reportlab pode não renderizar caracteres especiais (cedilha, til) | Usar fonte Helvetica embutida ou Liberation Sans; embed UTF-8 explícito |
| Even3 pode não ter campo de upload de regras na modalidade | Fallback: incluir link do PDF na descrição da modalidade |
| `.gitignore` está bloqueando `*.pdf` | Adicionar exceção `!assets/regras/*.pdf` no .gitignore |
