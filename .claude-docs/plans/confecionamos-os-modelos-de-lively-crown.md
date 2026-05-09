# Plano — Modelos Word para download + Padronização de 4 autores

## Contexto

Foram finalizados os modelos editáveis de submissão (Resumo Expandido, Pôster A3, Relatório A3, Artigo Completo) na pasta local `Modelos/`. Precisam estar disponíveis para download diretamente nos cards de "Normas por modalidade" do site.

Em paralelo, há duas regras a padronizar em **todas as fontes** de regulamento (PDFs gerados, site institucional, Even3):

1. **Remover a lista de nomes** dos membros da comissão científica do PDF (mantendo o conceito "comissão científica", o e-mail `comissao.cientifica@encontrogeig.org` e a citação genérica no site).
2. **Padronizar limite de 4 autores** em todas as 4 modalidades (hoje só o Resumo Expandido cita explicitamente "até 6 autores"; as demais são omissas).

## Mudanças

### 1. Templates Word — disponibilizar para download

**Origem:** `Modelos/` (raiz do repo)
**Destino servido:** `assets/modelos/` (novo diretório)

Renomear ao copiar (slugs alinhados com PDFs em `assets/regras/`):

| Origem | Destino |
|---|---|
| `Resumo Expandido_Template 1 Encontro de Governança, Estratégia e Inovação Governamental.docx` | `assets/modelos/resumo-expandido.docx` |
| `POSTER Encontro de Governança, Estratégia e Inovação.docx` | `assets/modelos/poster.docx` |
| `RELATÓRIO A3 Encontro de Governança, Estratégia e Inovação.pptx` | `assets/modelos/relatorio-a3.pptx` |
| `ARTIGO COMPLETO_Template1_Encontro Governanaça, Estratgia e Inovação Governamental.docx` | `assets/modelos/artigo-completo.docx` |

**Index.html (linhas 882–905):** adicionar segundo botão dentro de cada `.regra-card`, abaixo do `.regra-cta` existente.

Mudança estrutural mínima: o card hoje é um `<a>` único (clique abre PDF). Para acomodar dois botões precisamos converter o card de `<a>` para `<div>` e mover os dois links para dentro como `.regra-cta` (PDF) + `.regra-cta-alt` (DOCX/PPTX). CSS adicional será adicionado em `<style>` (buscar bloco `.regra-card` no `<style>` do index.html) para layout horizontal dos dois CTAs e manter responsividade.

Exemplo (Resumo Expandido):
```html
<div class="regra-card fi">
  <div class="regra-icon">RE</div>
  <div class="regra-t">Resumo Expandido</div>
  <div class="regra-d">Fase 1 · 2-4 páginas · até 700 palavras + vídeo de 5 min</div>
  <div class="regra-ctas">
    <a class="regra-cta" href="/assets/regras/resumo-expandido.pdf" download target="_blank" rel="noopener">Regras (PDF)</a>
    <a class="regra-cta-alt" href="/assets/modelos/resumo-expandido.docx" download>Modelo Word</a>
  </div>
</div>
```

Para o Relatório A3 o segundo botão será "Modelo PowerPoint" → `relatorio-a3.pptx`.

### 2. Padronização de 4 autores

**`scripts/gerar_regras_pdf.py`:**
- Linha 228: `"Autores: até 6"` → `"Autores: até 4"`
- Adicionar item `"Autores: até 4, alinhados à esquerda, Arial 12"` nas seções "Estrutura visual" das modalidades **Pôster A3** (após linha 265) e **Relatório A3** (na bloco "Formatação visual", após linha 302).
- **Artigo Completo:** adicionar item `"Autores: até 4 (nome completo, e-mail e instituição)"` na seção "Estrutura do artigo" (após linha 334).
- **Comissão científica (linhas 195–199):** remover a frase com os 7 nomes. Substituir por: `"A avaliação científica é conduzida em conjunto pelas instituições realizadoras (UFF, ABAR, PPGEP - LabDGE/UFF e GIGS/UNICAMP), em regime de avaliação por pares."`
- Linha 345 ("Dupla avaliação cega pela comissão científica do 4º SSEP") → `"Dupla avaliação cega por pares conduzida pelas instituições realizadoras"`.

Após editar, regenerar os 4 PDFs em `assets/regras/`:
```powershell
python scripts/gerar_regras_pdf.py
```

**`index.html`:**
- Lista "Orientação aos Autores" (linhas 918–927): adicionar `<li class="fi"><div><strong>Autores</strong><span>até 4 por trabalho</span></div></li>`.
- Linha 954: manter o texto atual "Avaliação por comissão científica" (conforme decisão — só remover nomes, não o conceito).
- Linha 1122 (footer): manter o e-mail `comissao.cientifica@encontrogeig.org`.

### 3. Even3 (via Chrome DevTools MCP)

Ao executar:
1. `mcp__chrome-devtools__new_page` para abrir `https://www.even3.com.br/`.
2. Pedir ao usuário para fazer login interativo (credenciais não estão no escopo da automação).
3. Navegar até a configuração de **Trabalhos científicos / Modalidades** do evento `1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003`.
4. Para cada modalidade, ajustar campo "número máximo de autores" para **4** (se existir tal campo); caso o Even3 só permita texto livre nas instruções, atualizar a descrição da modalidade incluindo "Limite: até 4 autores por trabalho".
5. Fazer screenshot final de cada tela como evidência.

> Caveat: a estrutura exata do painel do Even3 só é conhecida após login. O passo a passo acima pode precisar ser ajustado em runtime.

## Arquivos críticos

- `index.html` — linhas 877–906 (cards de regras), 918–927 (lista de normas).
- `scripts/gerar_regras_pdf.py` — linhas 195–199, 228, 265, 302, 334, 345.
- `assets/regras/*.pdf` — regenerados pelo script.
- `assets/modelos/` — novo diretório com 4 arquivos copiados de `Modelos/`.

## Verificação

1. **Templates:** abrir `index.html` localmente (live server ou Vercel preview), clicar em "Modelo Word" em cada card → arquivo baixa com nome correto. Verificar que o link "Regras (PDF)" continua funcionando.
2. **PDFs regenerados:** abrir cada um dos 4 PDFs em `assets/regras/` e confirmar:
   - Não há lista de nomes em "Comissão científica".
   - Cada modalidade contém "Autores: até 4".
3. **Site:** verificar que a lista "Orientação aos Autores" mostra o item "Autores · até 4 por trabalho".
4. **Even3:** revisar visualmente cada modalidade após edição via Chrome DevTools MCP (screenshots).
5. **Responsividade:** redimensionar viewport para 360px e confirmar que os dois CTAs nos cards não quebram layout.

## Fora de escopo

- Alterar o texto "Avaliação por comissão científica" no site (linha 954) e o e-mail de contato (linha 1122) — preservados conforme decisão do usuário.
- Modificar templates `.docx`/`.pptx` em si — apenas disponibilizá-los como estão.
