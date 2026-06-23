# Plano — Reativar a faixa "Parceiros institucionais" (apoiadores) na home

## Contexto

A AGENERSA enviou (22/06/2026, via Luíza Rafaelle) os logos das instituições que serão
**parceiras institucionais** do 1º Encontro GEI. O usuário quer exibi-los na home, **logo
abaixo da faixa "Realização"** (os organizadores), dentro da seção `#parceiros`
("Realização e parceiros"), **seguindo exatamente o mesmo padrão visual** das demais
faixas de logos.

A estrutura já existe: a seção `#parceiros` em `index.html` (linhas 1172–1215) usa o
padrão `.pt-tier` → `.pt-tier-lbl` → `.pt-grid` → `.ptc` → `.ptc-logo` + `.pf`, e há
inclusive um bloco **comentado** "PARCEIROS-OCULTOS" (linhas 1198–1212) que é o molde
exato — mas referencia outras instituições (Firjan, ANP, AGENERSA, etc.) ainda não
confirmadas. Não vamos reusar aquela lista; criaremos uma nova faixa com os 5 parceiros
confirmados. Todo o CSS necessário já está definido e ativo (nenhum estilo novo).

Decisões do usuário:
- Rótulo da faixa: **"Parceiros institucionais"**.
- Estilo dos cards: **nome (legenda) + link clicável**, igual à faixa "Realização".
- Nomes e links **conferidos por pesquisa na internet** antes de publicar.

## Os 5 parceiros (nomes e links pesquisados)

| Logo (arquivo de origem em `assets/Apoiadores/`) | Legenda (`.pf`) | Link | Confiança |
|---|---|---|---|
| `logo.afbc9ca6198a.svg` (IBP) — **idêntico ao já existente** `assets/logos/ibp.svg` | Instituto Brasileiro de Petróleo, Gás e Biocombustíveis | https://www.ibp.org.br | ✅ confirmado |
| `WhatsApp Image 2026-06-22 at 17.23.47.jpeg` (MBC) | Movimento Brasil Competitivo | https://www.mbc.org.br | ✅ confirmado |
| `WhatsApp Image 2026-06-22 at 17.24.31.jpeg` (Blue Ocean) | Blue Ocean Business Events | https://www.blueoceanevents.com.br | ✅ confirmado |
| `RealSeg Monitoramento Fundo Claro.png` | RealSeg Monitoramento | https://www.gruporealseg.com.br | ⚠️ provável (Grupo RealSeg, monitoramento eletrônico sediado no RJ/Barra) — **confirmar com a Rafaelle** |
| `Lavoro Logo Colorida (2).pdf` (a logo diz **"LAVORO SOLUTIONS"**) | Lavoro Solutions | https://lavoro-solutions.com | ✅ confirmado (consultoria ambiental + eventos em saneamento/energia/água — fit perfeito) |

> **Confirmações pendentes (não bloqueiam a publicação):**
> - **RealSeg**: linkar para `gruporealseg.com.br`? (empresa de monitoramento do RJ, casa
>   com o wordmark "RealSeg Monitoramento"). Se a Rafaelle indicar outro site, ajustamos.
> - **Lavoro**: nome genérico, sem como identificar com certeza pela logo. Entra **sem
>   link** (igual ao precedente do card GIGS/UNICAMP, que é `<div>` sem `<a>`) até a
>   AGENERSA passar a razão social e a URL.

## Implementação

### 1. Preparar os arquivos de logo em `assets/logos/`

Manter convenção do projeto (`/assets/logos/<nome>.<ext>`, kebab-case). Originais ficam
preservados em `assets/Apoiadores/` como fonte.

- **IBP** → **reusar** `assets/logos/ibp.svg` (já existe e é o mesmo arquivo). Nada a fazer.
- **MBC** → de `WhatsApp Image 2026-06-22 at 17.23.47.jpeg` para `assets/logos/mbc.png`.
- **Blue Ocean** → de `WhatsApp Image 2026-06-22 at 17.24.31.jpeg` para `assets/logos/blue-ocean.png`.
- **RealSeg** → de `RealSeg Monitoramento Fundo Claro.png` para `assets/logos/realseg.png`.
- **Lavoro** → **converter** `Lavoro Logo Colorida (2).pdf` (vetorial) → `assets/logos/lavoro.png`.

Tratamento de imagem (importa porque o box `.ptc-logo` tem **fundo branco**):
- Os 2 JPEGs do WhatsApp têm fundo cinza-claro (~#f4f4f4). Achatar/normalizar o fundo
  para **branco (#fff)** (ou recortar para transparente) ao exportar PNG, para o logo
  fundir-se ao box branco sem moldura cinza visível.
- PDF do Lavoro: rasterizar a ~300 dpi com fundo branco/transparente. Como `pdftoppm` não
  está disponível nesta máquina, usar alternativa (Python `PyMuPDF`/`fitz`, ou `pdf2svg`/
  `pdftocairo`, ou a skill `adobe-pdf-services`). Vetorizar para SVG é opcional, mas PNG
  300 dpi é suficiente para o tamanho exibido (máx. 44 px de altura).
- Observação visual: a logo RealSeg é "quadrada" (marca empilhada sobre "MONITORAMENTO"),
  então renderiza pequena no limite de 44 px de altura. Aceitável para v1; se quisermos
  destaque igual aos horizontais, pedir uma versão horizontal à AGENERSA depois.

### 2. Inserir a nova faixa em `index.html`

Inserir **logo após o fechamento da faixa "Realização"** (após a linha 1187, `</div>` que
fecha o `.pt-tier` de Realização) e **antes** do bloco `.pep-org` (linha 1189) — assim as
duas faixas de logos ficam adjacentes (mesmo padrão), e o CTA acadêmico do PPGEP segue
abaixo de ambas. Bloco a inserir (reutiliza 100% das classes existentes; classes de
animação `fi d1 d2 d3 d4` para o stagger, igual às outras faixas):

```html
    <div class="pt-tier">
      <p class="pt-tier-lbl fi">Parceiros institucionais</p>
      <div class="pt-grid">
        <a href="https://www.ibp.org.br" target="_blank" rel="noopener" class="ptc fi"><div class="ptc-logo"><img src="/assets/logos/ibp.svg" alt="IBP — Instituto Brasileiro de Petróleo, Gás e Biocombustíveis"></div><div class="pf">Instituto Brasileiro de Petróleo, Gás e Biocombustíveis</div></a>
        <a href="https://www.mbc.org.br" target="_blank" rel="noopener" class="ptc fi d1"><div class="ptc-logo"><img src="/assets/logos/mbc.png" alt="MBC — Movimento Brasil Competitivo"></div><div class="pf">Movimento Brasil Competitivo</div></a>
        <a href="https://www.blueoceanevents.com.br" target="_blank" rel="noopener" class="ptc fi d2"><div class="ptc-logo"><img src="/assets/logos/blue-ocean.png" alt="Blue Ocean Business Events"></div><div class="pf">Blue Ocean Business Events</div></a>
        <a href="https://www.gruporealseg.com.br" target="_blank" rel="noopener" class="ptc fi d3"><div class="ptc-logo"><img src="/assets/logos/realseg.png" alt="RealSeg Monitoramento"></div><div class="pf">RealSeg Monitoramento</div></a>
        <div class="ptc fi d4"><div class="ptc-logo"><img src="/assets/logos/lavoro.png" alt="Lavoro"></div><div class="pf">Lavoro</div></div>
      </div>
    </div>
```

Notas:
- Lavoro entra como `<div class="ptc ...">` (sem `<a>`), exatamente como o card
  GIGS/UNICAMP já faz na faixa Realização — vira link quando a URL for confirmada.
- O bloco comentado "PARCEIROS-OCULTOS" (1198–1212) **fica como está** (não tocar); são
  outros parceiros a reativar no futuro "conforme confirmação".
- Atualizar o registro de sessão em `.claude-docs/SESSION_LOG.md` (já modificado) e salvar
  este plano (padrão do projeto).

### 3. (Opcional, não fazer agora) Badges de apoio no hero

Há um bloco comentado "APOIO-OCULTO" no hero (linhas ~787–790) com cápsulas de texto
(`.pc`). Fora do escopo deste pedido; deixar como está.

## Verificação (end-to-end)

1. **Servir a raiz do site** (os `src` são absolutos `/assets/logos/...`, exigem root):
   `python -m http.server 8080` na pasta do site e abrir `http://localhost:8080/`.
2. **Visual**: rolar até "Realização e parceiros" → confirmar a nova faixa **"Parceiros
   institucionais"** logo abaixo de "Realização", com os **5 logos** dentro de boxes
   brancos, sem moldura cinza residual (checar especialmente MBC e Blue Ocean), legenda
   sob cada um, e o efeito de *hover* (card sobe + leve scale no logo).
3. **Responsivo**: largura ≤880px → grid de 2 colunas; ≤480px → 1 coluna (CSS já cobre).
4. **Links**: clicar IBP, MBC, Blue Ocean, RealSeg → abrem o site correto em nova aba
   (`target=_blank rel=noopener`). Lavoro sem link (por ora).
5. **Acessibilidade**: conferir `alt` de cada `<img>`.
6. (Alternativa de QA) usar o Chrome DevTools MCP para carregar a página e tirar
   screenshot da seção, validando render dos 5 logos.

## Deploy

Commit + push para `main` dispara o deploy automático na Vercel (token disponível;
ver memória do projeto). Conferir a home publicada em encontrogeig.org após o deploy.

## Itens a confirmar com a AGENERSA (pós-publicação, se necessário)

- RealSeg: o link correto é `gruporealseg.com.br`?
- Lavoro: razão social completa + site oficial (para legenda e link).
