# Landing Page · guia de edição

`index.html` é um single-file de ~1700 linhas com CSS embutido. Single-file por escolha: facilita deploy estático no Vercel sem build step.

---

## Estrutura HTML (15 seções, na ordem)

| # | Seção | ID âncora | Conteúdo |
|---|---|---|---|
| 1 | Nav fixa | — | Logo + menu + toggle tema + CTA "Inscreva-se" |
| 2 | Hero | — | Logo grande + badge data + h-tag + h-meta strip + CTAs + h-counter (live) + h-partners |
| 3 | Keynote | — | Conferência magna · Magda Chambriard + painelistas |
| 4 | Stats strip | — | 5 números: 4 eventos · 8 visitas · 13 eixos · 80+ submissões · 24h |
| 5 | Programação (3 dias) | `#programacao` | 3 cards · Day 1/2/3 |
| 6 | Eventos (4 trilhas) | `#eventos` | Lean Six Sigma · SSEP · Regulação · Inteligência |
| 7 | Visitas técnicas | `#visitas` | 8 cards · jornadas Dia 2 |
| 8 | Modalidades | `#modalidades` | 4 cards · presencial completo/1+3/remoto/visitante |
| 9 | Submissão | `#trabalhos` | Header + timeline 6 steps + 13 eixos grid + 4 cards de regras PDF |
| 10 | Normas técnicas | — | 8 itens (Arial 12, ABNT, etc.) + comissão científica |
| 11 | Submissão (iframe Even3) | `#submeter` | Iframe `#submissoes` do hotsite |
| 12 | Inscrição (iframe Even3) | `#inscricao` | Iframe `tickets/get/...` |
| 13 | Apoio (Quatro Moedas) | `#apoio` | 4 cards + link para `/patrocinadores/` |
| 14 | Parceiros | `#parceiros` | 4 realização + 8 apoio · com logos |
| 15 | Cert + CTA final + Footer | — | Certificação · CTA · contato/links |

---

## Sistema de variáveis CSS

Todas as cores em `:root` (linha ~30):

```css
--bg:#091136;        /* fundo principal navy */
--bg-2:#0E1A4A;      /* navy médio */
--bg-3:#142469;      /* navy claro p/ cards */
--ink:#06091F;       /* mais escuro */
--yellow:#F5C842;    /* "Governança" no logo */
--green:#7AC74F;     /* "Estratégia" no logo */
--blue:#4DA8E0;      /* "Inovação" no logo */
--cyan:#5BC6E5;      /* linhas decorativas */
--white:#FFFFFF;     /* texto principal */
--muted:rgba(255,255,255,.62);
```

Para mudar paleta global: editar essas variáveis. Toda a página recompõe.

---

## Sistema de temas claro/escuro

- **Default:** dark (navy)
- **Toggle:** botão `#themeToggle` no nav (ícone SVG sol)
- **Persistência:** `localStorage.gei-theme` (`'dark'` | `'light'`)
- **Mecanismo:** `<html data-theme="...">` com overrides CSS em `[data-theme="light"] ...`

Bloco light theme: linha ~430 a ~530 do `index.html`. As variáveis `--bg`, `--white`, `--muted` etc. são **redefinidas**, então a maioria dos componentes muda automaticamente sem alterações específicas.

Logos com troca por tema:
```html
<img src="/assets/logo-completo.png" class="hero-logo logo-dark">
<img src="/assets/logo-fundo-branco.png" class="hero-logo logo-light">
```
Visibilidade controlada por `[data-theme="dark"] .logo-light{display:none}` e vice-versa.

---

## Tipografia

- **Display (títulos, hero, números):** `Manrope` (peso 700-800, letter-spacing -.025em)
- **Body (parágrafos, labels):** `Outfit` (peso 300-600)
- Fonte carregada do Google Fonts (`<link>` no `<head>`)

---

## IntersectionObserver de fade-in

Elementos com classe `.fi` começam invisíveis (`opacity:0; translateY(24px)`). Quando entram na viewport (com 200px de margem), recebem `.visible` e animam.

**Failsafe:** `setTimeout(() => fiEls.forEach(el => el.classList.add('visible')), 2500);`
Garante que conteúdo aparece mesmo se o IntersectionObserver não disparar (ex: full-page screenshot, scroll instantâneo).

Variantes de delay: `.d1` (70ms), `.d2` (140ms), `.d3` (210ms), `.d4` (280ms).

---

## Iframes Even3

Dois iframes embutidos:

| Seção | URL `src` |
|---|---|
| `#inscricao` | `https://www.even3.com.br/tickets/get/<slug>?even3_orig=get_tickets` |
| `#submeter` | `https://www.even3.com.br/<slug>/#submissoes` |

Ambos com `sandbox="allow-forms allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation"` (necessário para login Even3 e checkout).

Wrapper `.embed-wrap` tem barra superior `.embed-bar` com link "Abrir em nova aba ↗".

---

## Edições comuns

### Trocar uma data
Buscar a string da data antiga e usar `replace_all`:
```bash
grep -n "01/06/2026" index.html
# Editar pontualmente os blocos que precisam mudar
```
Cuidado: a data aparece em vários lugares (badge hero, timeline, dl-box, JSON-LD, footer).

### Adicionar um novo palestrante (keynote)
Editar a seção `<!-- KEYNOTE -->` (linha ~480). O bloco `.kn-spk` tem o avatar + nome + role + badge.

### Adicionar uma nova jornada técnica
Adicionar `<article class="vc fi"><div class="vn">Jornada XX</div>...` dentro de `.vis-grid` (linha ~570).

### Trocar logo de um parceiro
1. Substituir `assets/logos/<nome>.png` (manter o mesmo nome)
2. Anexar `?v=N` no `src` do `<img>` correspondente em `index.html` (cache bust)

### Adicionar nova categoria de regras de submissão
1. Editar `scripts/gerar_regras_pdf.py` adicionando uma chamada `gerar_pdf(...)` no `main()`
2. Rodar: `python scripts/gerar_regras_pdf.py`
3. Editar `index.html` adicionando um novo `<a class="regra-card">` no grid `.regras-grid`

---

## Sub-páginas

| Path | Arquivo | Conteúdo |
|---|---|---|
| `/patrocinadores/` | `patrocinadores/index.html` | Modelo "Quatro Moedas" de apoio institucional · standalone com mesmo theme system |

Para adicionar nova sub-página: criar `<nome>/index.html` na raiz. Vercel serve automaticamente.

---

## Acessibilidade

- `aria-label` em nav, sections principais, botões de ação
- `aria-hidden="true"` em decorações
- `<a href="#main" class="sr-only">Pular para o conteúdo</a>` (skip link)
- `:focus-visible` com outline amarelo (paleta evento)
- `@media (prefers-reduced-motion: reduce)` desabilita todas as animações

---

## SEO + Open Graph

- Title + meta description otimizados
- Open Graph: `og:title`, `og:description`, `og:image` (1200x630), `og:url`
- Twitter Card: `summary_large_image`
- JSON-LD: schema.org `Event` no `<head>` para indexação rich result do Google

OG image: `assets/og-image.png` (gerado a partir do logo)
