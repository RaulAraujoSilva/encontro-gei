# Ajustes pontuais no site do congresso (rodada 06/05)

## Contexto

Quatro alterações pontuais no `index.html` (e regeneração dos PDFs de regras) para refletir feedback de produto recebido em 06/05/2026:

1. **Contador de inscritos** — desligar temporariamente (pode voltar). Não apagar; apenas comentar para rollback simples.
2. **Bloco "Orientação aos Autores"** — remover a frase com os nomes da comissão científica do 4º Seminário SSEP (Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio, Silvia Cristina Rufino). Manter o título e a primeira frase da descrição.
3. **Vídeo de apresentação** — mudar de "URL YouTube/Vimeo" para upload direto de arquivo de vídeo. Mudança ecoa em 3 textos do site + 1 PDF de regras (resumo-expandido).
4. **Badges de certificação** — remover os 4 itens (`Participação · 75% presença`, `Apresentação de trabalho`, `Livro com ISBN`, `24h complementares UFF`) do rodapé `.cert`.

## Arquivos críticos

- `index.html` (raiz) — todos os ajustes do site
- `scripts/gerar_regras_pdf.py` — texto fonte do PDF de regras
- `assets/regras/resumo-expandido.pdf` — saída regenerada

## Mudanças detalhadas

### 1. Contador de inscritos (item 1)

**`index.html` linhas 640–643** — envolver o bloco `<div class="hc-counter" id="counter" hidden>...</div>` em comentário HTML `<!-- ... -->` com nota `<!-- COUNTER-OCULTO (reativar removendo este comentário) -->`.

**`index.html` linhas 1127–1137** — comentar o IIFE `(async () => { ... fetch('/api/inscritos') ... })();` com `/* ... */`. A rota `/api/inscritos` permanece intacta (API não removida; só o consumo no front).

### 2. Frase da comissão (item 2)

**`index.html` linha 885** — substituir o `<p class="sec-desc fi" ...>`:

- De: `Padronização técnica para garantir consistência editorial nos anais com ISBN. Comissão científica do 4º Seminário SSEP: <strong>Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio e Silvia Cristina Rufino</strong>.`
- Para: `Padronização técnica para garantir consistência editorial nos anais com ISBN.`

### 3. Vídeo: URL → upload de arquivo (item 3)

**`index.html`:**

- Linha 894 (lista de normas): `<strong>Vídeo</strong><span>até 5 min · URL YouTube/Vimeo</span>` → `<strong>Vídeo</strong><span>até 5 min · upload de arquivo</span>`
- Linha 905 (descrição da seção submissão): `(resumo estendido + URL do vídeo)` → `(resumo estendido + arquivo de vídeo)`
- Linha 916 (passo 3 do roteiro Even3): `Faça <strong>upload do arquivo</strong> + URL do vídeo de 5 min` → `Faça <strong>upload do arquivo</strong> + vídeo de 5 min`

**`scripts/gerar_regras_pdf.py` linhas 244–245** — substituir os dois bullets do bloco "Vídeo de apresentação" do PDF resumo-expandido:

- De:
  - `"Hospedado em YouTube/Vimeo (link público ou não-listado)"`
  - `"URL informada no formulário Even3 no momento da submissão"`
- Para:
  - `"Arquivo de vídeo enviado pela plataforma Even3 no momento da submissão"`
  - `"Formatos aceitos: MP4 (recomendado), MOV ou WebM"`

Os outros 3 PDFs (poster, relatorio-a3, artigo-completo) já não mencionam YouTube/Vimeo (verificado via grep).

### 4. Badges de certificação (item 4)

**`index.html` linhas 1003–1008** — remover as 4 `<span class="cb">...</span>` dentro do `<div class="cbg">`. A frase principal (`<p class="ct">...horas complementares.</p>` na linha 1002) permanece. Verificar se o container `.cbg` vazio fica visualmente OK ou também deve ser removido — pelo CSS atual ele tem flex/gap, então sem filhos não ocupa espaço; remover só os spans é seguro e reversível.

## Verificação

1. Abrir `index.html` no navegador (live server ou `python -m http.server`):
   - Hero: contador "X profissionais já inscritos" não aparece
   - Seção "Normas técnicas": título "Orientação aos Autores" mantido; descrição termina em "...anais com ISBN."; lista mostra "Vídeo · até 5 min · upload de arquivo"
   - Seção "Envie seu trabalho": descrição cita "arquivo de vídeo"; passo 3 sem "URL do vídeo"
   - Rodapé `.cert`: parágrafo de certificação presente; nenhum badge `.cb` abaixo
2. Console do browser: nenhuma chamada a `/api/inscritos` (Network tab limpo nesse fetch)
3. Regenerar PDF: `python scripts/gerar_regras_pdf.py` (na pasta raiz). Abrir `assets/regras/resumo-expandido.pdf` e confirmar bloco "Vídeo de apresentação" com novo texto sobre arquivo/formatos.
4. `git diff --stat` deve mostrar mudanças apenas em `index.html`, `scripts/gerar_regras_pdf.py` e `assets/regras/resumo-expandido.pdf`.
