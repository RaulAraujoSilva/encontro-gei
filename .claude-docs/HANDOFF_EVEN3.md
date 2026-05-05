# Handoff — Configuração Even3 (manual, ~20 min)

> Os campos de data da Even3 não cooperaram com o Chrome MCP (máscara dd/mm/aaaa truncou os valores). Como já estamos logados na sua janela do Chrome controlado pelo MCP, **complete os passos abaixo manualmente** — todos os dados estão prontos pra colar.
>
> **Já feito por mim:**
> - ✅ Datas do evento: 08/07/2026 09:00 → 10/07/2026 20:00
> - ✅ Carga horária: 24h
> - ✅ Evento já está publicado e público

---

## 1. Configuração > Evento — completar (URL: `/organizador/configuracao/evento`)

### Bloco "Divulgação"
- **Tipo:** alterar para `Científico - Congresso/Simpósio`
- **Assunto principal:** alterar para `Engenharias`
- **Palavras-chaves** (uma a uma, com Enter ou botão Adicionar):
  ```
  governança pública
  regulação
  inovação governamental
  GovTech
  engenharia de produção
  Lean Six Sigma
  inteligência governamental
  sandbox regulatório
  ```
- **Descrição curta:** colar exatamente:
  ```
  A primeira plataforma nacional a integrar excelência operacional, engenharia de produção, regulação de infraestrutura e inteligência governamental. 4 eventos oficiais, 8 visitas técnicas, 3 dias. 08–10 de julho de 2026, Rio de Janeiro / Niterói. Realização: UFF, ABAR, PPGEP/UFF, Escola de Regulação. Anais com ISBN.
  ```
- → Clicar **Salvar informações de divulgação**

### Bloco "Local"
- **Estado:** `Rio de Janeiro`
- **Cidade:** `Rio de Janeiro` (a maior parte do evento — Niterói entra como observação)
- **Local (texto livre):** `Rio de Janeiro / Niterói — RJ (locais a confirmar)`
- → Clicar **Salvar informações do local**

### Bloco "Organizado por"
- **Responsável:** `Secretaria do 1º Encontro GEI`
- **E-mail:** `contato@encontrogei.com.br` *(ou seu e-mail institucional)*
- **Telefone:** `(21) XXXXX-XXXX` *(opcional)*
- **Logo:** clicar "Anexar logo" → upload do arquivo `assets/logo-swirl.png` da pasta do projeto
- → Clicar **Salvar informações do organizador**

---

## 2. Inscrições — 4 modalidades (URL: `/organizador/registration/`)

Para cada uma: clicar **+ Adicionar entrada**, escolher **Gratuita**, preencher e Salvar.

| # | Categoria | Quantidade | Válido de | Válido até |
|---|---|---|---|---|
| 1 | `Participante Presencial Completo (3 dias)` | `400` | `05/05/2026` | `07/07/2026` |
| 2 | `Participante Presencial Dias 1 e 3` | `200` | `05/05/2026` | `07/07/2026` |
| 3 | `Participante Remoto / Online` | (deixar ilimitado) | `05/05/2026` | `09/07/2026` |
| 4 | `Visitante Técnico — Apenas Dia 2` | `200` | `05/05/2026` | `07/07/2026` |

---

## 3. Programação — 3 dias + 8 jornadas (URL: `/organizador/programacao/`)

### Atividades agrupadas por Dia

**Dia 1 — 08/07/2026 (Quarta) · Abertura Institucional · Rio de Janeiro**
- 13h30–14h15 — Credenciamento digital e recepção
- 14h15–15h30 — Mesa de abertura institucional
- 15h30–16h10 — Painel de apresentação do evento
- 16h10–17h00 — **Conferência magna**: Magda Chambriard (Petrobras) — Moderador: Miguel (CREA-RJ)
- 17h00–19h00 — Coquetel de networking institucional

**Dia 2 — 09/07/2026 (Quinta) · Visitas Técnicas (8 jornadas paralelas)**

Cadastrar como **8 atividades simultâneas, com vagas limitadas e inscrição obrigatória**:

| Jornada | Local | Vagas | Tags |
|---|---|---|---|
| 01 | Petrobras | 25 | Energia · Regulação |
| 02 *(integrada)* | Águas do Rio (CCO) + ETE/Biogás | 25 | Saneamento · ESG |
| 03 | Guandu / Lameirão | 25 | Infraestrutura Hídrica |
| 04 | Ternium · Santa Cruz | 25 | Indústria · Lean |
| 05 | Gerdau · Santa Cruz | 25 | Indústria · Digital |
| 06 *(integrada)* | Eneva + TAG | 25 | Energia · GovTech |
| 07 *(integrada)* | IRM + AGENERSA | 25 | Inteligência · Sandbox |
| 08 | CSN | 25 | Indústria · Lean |

Horário: 06h30 concentração no hub · 07h00–08h30 partidas escalonadas · 09h–17h visita · 18h retorno

**Dia 3 — 10/07/2026 (Sexta) · Trilhas, Sessões e Encerramento · NAB UFF Niterói**
- 09h00–10h30 — Plenária + Painel "IA e soberania nacional"
- 10h30–12h30 — **Trilhas A, B, C, D simultâneas** (criar 4 atividades)
- 12h30–14h00 — Almoço
- 14h00–16h00 — Sessões técnicas e acadêmicas (apresentação de trabalhos aprovados)
- 16h30–17h30 — Premiação dos melhores trabalhos
- 18h00 — Encerramento institucional
- 19h00 — Coquetel de encerramento

---

## 4. Submissões — Configurações + Áreas + Modalidades (URL: `/organizador/trabalhocientifico/submissaogeral?tab=settings`)

### Cronograma (Configurações)
- **Início submissão:** 06/05/2026
- **Fim submissão Fase 1:** 15/05/2026 23:59
- **Início avaliação:** 16/05/2026
- **Fim avaliação:** 31/05/2026
- **Resultado:** 31/05/2026
- **Fim submissão Fase 2 (artigo final):** 30/09/2026 23:59

### Áreas Temáticas (13 eixos — adicionar uma por uma na aba "Áreas Temáticas")
1. Regulação de infraestrutura, energia e saneamento
2. Sandbox regulatório e inovação institucional
3. Gestão pública inovadora e GovTech
4. Lean Six Sigma e excelência operacional em serviços públicos
5. Sustentabilidade e ESG em organizações reguladas
6. Inteligência governamental e apoio à decisão
7. Governança de dados e interoperabilidade
8. Transformação digital e inovação em serviços públicos
9. Capacidade analítica e uso de evidências no setor público
10. Saúde digital e dados conectados
11. Inteligência artificial e soberania nacional
12. Trabalho, ergonomia e segurança em sistemas produtivos
13. Pesquisa operacional, otimização e logística

### Modalidades de submissão (aba "Modalidades")
1. **Resumo Estendido + Vídeo (Fase 1)** — 2 a 4 páginas + vídeo de até 5 min (URL YouTube/Vimeo)
2. **Artigo Completo (Fase 2)** — pós-evento, 8–15 páginas para os Anais com ISBN
3. **Relato de Visita Técnica** — 2 a 3 páginas, exclusivo para participantes do Dia 2

---

## 5. Página do Evento — CSS custom (opcional, URL: `/organizador/hotsite/`)

Se quiser que o hotsite Even3 tenha a mesma identidade da landing externa, em "Configuração avançada" cole:

```css
:root{ --gei-navy:#0A1628; --gei-lime:#B8E839; --gei-ink:#06090F; }
body, .even3-hotsite { background:var(--gei-ink) !important; color:#fff !important; }
.btn-primary, .btn-success { background:var(--gei-lime) !important; color:var(--gei-ink) !important; border-radius:100px !important; font-weight:700 !important; }
h1, h2, h3 { font-family:'Fraunces',serif !important; letter-spacing:-.01em !important; }
```

---

## 6. Coletar embeds (após config 1-5) — URL: `/organizador/integrations/` ou `/organizador/tools/`

Procurar **"Incluir Even3 no meu site"**. Copiar 4 snippets:

- ☐ Embed: **Inscrição** (botão ou aba completa)
- ☐ Embed: **Submissão de trabalhos**
- ☐ Embed: **Programação**
- ☐ Embed: **Convidados/Palestrantes**

E me cole aqui no chat ou salve em `embeds.txt` na raiz do projeto.

---

## 7. API Token (para contador ao vivo)

Em `/organizador/integrations/` → procurar **API REST** → "Gerar token" → copiar o `Authorization-Token`.

Salvar em `.env.local` (que já vai para `.gitignore`):
```
EVEN3_API_TOKEN=cole_aqui_o_token
EVEN3_EVENT_ID=722003
```

---

## Quando terminar, me avise:
- "embeds prontos" → eu plugo na landing e faço o deploy
- "qualquer dúvida" → eu volto pelo Chrome MCP em pontos específicos
