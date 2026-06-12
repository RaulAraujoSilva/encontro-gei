# Operações da Plataforma Even3

Documentação operacional completa do evento `722003` na Even3. Cobre acesso, mapa do painel, automação via Chrome MCP, API REST e operações comuns de manutenção.

---

## 1. Acesso e credenciais

| Item | Valor |
|---|---|
| **URL do painel** | https://www.even3.com.br/organizador/home/ |
| **URL pública do evento** | https://www.even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003 |
| **Conta organizador** | `Raul Araujo` (login Google) |
| **Event ID** | `722003` |
| **Slug do evento** | `1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003` |
| **API Token** | `da1c37f7-538f-4c93-bf7e-f6154fab02f8` (também salvo em `EVEN3_API_TOKEN` no Vercel) |
| **API Base URL** | `https://www.even3.com.br/api/v1/` |
| **Header de autenticação** | `Authorization-Token: <token>` |

> **Onde regenerar o token:** Painel > GERAL > Integrações > **API Even3** > Gerenciar > "Criar chave de acesso"

---

## 2. Mapa do painel · status atual

### GESTÃO

| Aba | URL | Status |
|---|---|---|
| **Início** | `/organizador/home/` | Dashboard com checklist + métricas live |
| **Pessoas** | `/organizador/people/` | Lista inscritos (preenche automaticamente) |
| **Vendas** | `/organizador/sales/` | N/A (evento gratuito) |

### PRÉ-EVENTO

| Aba | URL | Status |
|---|---|---|
| **Inscrições > Entradas e valores** | `/organizador/registration/` | ✅ 2 entradas ativas desde 10/06 (Presencial Completo · 400, Participação Online · ilimitada). Visita Técnica D2: entrada ainda não criada ("em breve" no site). ⚠️ Descrição da entrada presencial diz "acesso aos três dias" — corrigir para Dias 1 e 3 (visita técnica é inscrição própria) |
| **Inscrições > Formulário de inscrição** | `?tab=Formulário%20de%20inscrição` | ✅ Nome + e-mail + instituição + telefone celular + Termo LGPD (obrigatório) |
| **Inscrições > Configurações** | `?tab=Configurações` | Default · não há cobrança |
| **Página do Evento (hotsite)** | `/organizador/hotsite/` | ✅ CSS custom aplicado (paleta navy/yellow/green/blue + Manrope/Outfit) |
| **Programação > Atividades** | `/organizador/programacao/` | ✅ 22 atividades (5 Dia 1 · 8 jornadas Dia 2 · 9 Dia 3) |
| **Programação > Convidados** | `?tab=convidados` | ✅ 6 palestrantes (Magda, Miguel, Calado, Li Li Min, Raul, Vladimir) |
| **Programação > Configurações** | `?tab=configuracao` | ✅ Cronograma 04/05–07/07 para visitas técnicas |
| **Submissões > Recebimento > Modalidades** | `/organizador/trabalhocientifico/submissaogeral?tab=Modalidades` | ✅ 4 modalidades (Artigo, Pôster, Relatório A3, Resumo) com PDFs anexados |
| **Submissões > Áreas Temáticas** | `?tab=Áreas%20Temáticas` | ✅ 13 eixos alinhados ao projeto executivo |
| **Submissões > Configurações** | `?tab=Configurações` | ✅ Cronograma 04/05–16/06 · Comissão: Profa. Silvia Cristina Rufino |
| **Avaliação > Avaliadores** | `/organizador/trabalhocientifico/avaliacaogeral?tab=Avaliadores` | ✅ 7 avaliadores cadastrados |
| **Avaliação > Configurações** | `?tab=Configurações` | ✅ Cronograma 17/06–22/06 · Tipo: por critérios · Quantidade: 2 (double-blind) |

### EVENTO

| Aba | URL | Status |
|---|---|---|
| **Credenciamento** | `/organizador/credenciamento/` | Default · pronto pra leitura QR no dia |

### PÓS-EVENTO

| Aba | URL | Status |
|---|---|---|
| **Certificados** | `/organizador/certificate/` | ✅ 6 templates **publicados** (Participação, Atividade, Convidado, Submissão, Apresentação, Avaliador) |

### GERAL

| Aba | URL | Status |
|---|---|---|
| **Configuração > Evento** | `/organizador/configuracao/evento` | ✅ Datas 08-10/07/2026 · 24h · Tipo Científico · Engenharias · 8 keywords · Descrição · RJ |
| **Configuração > Organizadores** | `/organizador/configuracao/organizadores` | Apenas Raul (organizador único — adicionar membros se necessário) |
| **Configuração > Financeiro** | `/organizador/configuracao/dadosbancario` | Pular (gratuito) |
| **Ferramentas > Funcionalidades** | `/organizador/tools/` | Default |
| **Ferramentas > Integrações** | `/organizador/integrations/` | ✅ API Even3 ativa |

---

## 3. Truque do JS dispatch · contornar máscara dd/mm

A Even3 usa **inputs com máscara JS** (campos de data dd/mm/aaaa). O `mcp__chrome-devtools__fill` e `fill_form` simples interpretam o valor como `mm/dd/yyyy` e geram lixo (ex: `04/05/2026` vira `05/20/2605`).

**Solução:** usar o `value setter nativo` do `HTMLInputElement.prototype` + dispatch manual de eventos.

```js
// Cole no console do navegador (F12 → Console) ou use via mcp__chrome-devtools__evaluate_script
window.setVal = (el, v) => {
  const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
  setter.call(el, v);
  el.dispatchEvent(new Event('input',  { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
  el.dispatchEvent(new Event('blur',   { bubbles: true }));
};

// Helper pra clicar botão por texto (regex)
window.click = sel =>
  Array.from(document.querySelectorAll('button, a'))
       .find(b => sel.test(b.innerText.trim()) && b.offsetParent !== null)
       ?.click();

// Exemplo de uso: setar 2 datas e salvar
const inputs = Array.from(document.querySelectorAll('input'))
                    .filter(i => (i.placeholder||'').includes('aaaa') && i.offsetParent !== null);
setVal(inputs[0], '04/05/2026');
setVal(inputs[1], '15/05/2026');
click(/^Salvar/i);
```

**Por que funciona:** o React/AngularJS usado pela Even3 escuta o `input` event nativo. Setar `el.value = '...'` direto NÃO dispara esse listener; o setter prototype-nativo + `dispatchEvent` simula o que um humano faria ao digitar.

---

## 4. Automação via Chrome DevTools MCP

### Setup

1. Abrir o Chrome controlado pelo MCP (separado da sessão regular do usuário)
2. Navegar para `https://www.even3.com.br/login/` e fazer login (Google)
3. A sessão fica ativa enquanto a janela MCP estiver aberta

### Padrão de execução

```js
// 1. Navegar
mcp__chrome-devtools__navigate_page({ url: "https://www.even3.com.br/organizador/..." })

// 2. Aguardar carregar + tirar snapshot
mcp__chrome-devtools__take_snapshot()
// → retorna lista uid=X_Y de elementos clicáveis/preenchíveis

// 3. Para forms simples (texto, número):
mcp__chrome-devtools__fill_form({ elements: [{uid: "X_Y", value: "..."}] })
mcp__chrome-devtools__click({ uid: "X_Z" })

// 4. Para forms mascarados (datas, telefone):
mcp__chrome-devtools__evaluate_script({ function: "async () => { /* JS dispatch */ }" })

// 5. Para upload de arquivos:
mcp__chrome-devtools__upload_file({ uid: "X_W", filePath: "C:\\..." })
// IMPORTANTE: aguardar 5+ segundos antes de salvar (upload assíncrono)
```

### Limitações descobertas

| Sintoma | Causa | Workaround |
|---|---|---|
| Datas viram `05/20/2605` | Máscara dd/mm interpretada como mm/dd | `setVal` + dispatch (acima) |
| Modal "Comunicação" abre vazio | DOM lazy-loaded sem fallback do snapshot | Usar `evaluate_script` com timeout de 3s+ |
| Ações que recarregam a página fecham o contexto JS | Navigation destruction | Fazer 1 ação por chamada · re-snapshot depois |
| Cache CDN serve PNG antigo | Vercel edge cache | Append `?v=N` ao src no HTML |
| Upload de PDF não persiste se salvar imediatamente | Upload assíncrono em segundo plano | `await wait(5500)` antes de clicar Salvar |

---

## 5. API REST Even3 — endpoints úteis

Base URL: `https://www.even3.com.br/api/v1/`
Header obrigatório em todas as chamadas: `Authorization-Token: <TOKEN>`

| Método | Endpoint | Retorno |
|---|---|---|
| GET | `/event` | Dados gerais do evento |
| GET | `/attendees` | Lista de inscritos (paginada) |
| POST | `/attendees/create` | Criar inscrição programática |

### Exemplos

```bash
# Conferir o número de inscritos
TOK="da1c37f7-538f-4c93-bf7e-f6154fab02f8"
curl -s -H "Authorization-Token: $TOK" \
  "https://www.even3.com.br/api/v1/attendees" | jq '.data | length'

# Endpoint do site (cache 5 min)
curl -s https://encontrogeig.org/api/inscritos
# {"count":4,"eventId":"722003","updatedAt":"..."}
```

> **Não documentados oficialmente** mas confirmados: `?page=N&per_page=M` para paginar; resposta tem `{ "data": [...] }` envelopando o array.

---

## 6. Operações comuns

### Reabrir submissões / mover datas

1. `/organizador/trabalhocientifico/submissaogeral?tab=Configurações`
2. Clicar **Editar cronograma**
3. Usar o snippet do JS dispatch (§3) ou digitar manualmente as novas datas
4. Salvar

### Adicionar novo eixo temático

1. `/organizador/trabalhocientifico/submissaogeral?tab=Áreas%20Temáticas`
2. Clicar **+ Adicionar área temática**
3. Preencher título e salvar

### Trocar PDF de regras anexado a uma modalidade

1. `/organizador/trabalhocientifico/submissaogeral?tab=Modalidades`
2. Clicar no nome da modalidade (abre modal de edição)
3. Clicar **"Trocar regras de submissão"** (ou "Regras de submissão" se ainda não tem)
4. Upload do novo PDF
5. **Aguardar 5+ segundos** antes de clicar **Salvar Modalidade**

> Após salvar, a linha da modalidade na grade pode aparecer momentaneamente como "Defina regras de submissão" enquanto a CDN propaga — recarregar a aba confirma o novo PDF (URL muda para `static.even3.com/geral/<slug>.<hash>.pdf` com hash novo).

### Adicionar pergunta personalizada ao formulário de submissão

Confirmado: a Even3 permite campos customizados no formulário de submissão (ex.: URL do vídeo, links externos).

1. `/organizador/trabalhocientifico/submissaogeral?tab=Formulário%20de%20submissão`
2. Clicar **"+ Adicionar pergunta"**
3. Escolher tipo "Submissão" (não "Autor") e formato adequado — para URL use **Resposta curta**
4. Preencher título da pergunta
5. Recomendado marcar:
   - **Exibir resposta da pergunta para o avaliador** (para o avaliador acessar o link)
   - **Incluir instruções de preenchimento ao participante** (orientações sobre formato/visibilidade do link)
6. **Pergunta válida para todas as modalidades** já vem marcada por padrão
7. Deixar **sem obrigatoriedade** se o campo só faz sentido em algumas modalidades (ex.: vídeo só é exigido na Fase 1 / Resumo Expandido)
8. Clicar **Salvar pergunta**

### Cadastrar novo avaliador

1. `/organizador/trabalhocientifico/avaliacaogeral?tab=Avaliadores`
2. Clicar **Convidar avaliador**
3. Preencher Nome + E-mail + (opcional) modalidades/áreas
4. Clicar **Salvar avaliador**

### Republicar certificado (após mudança no template)

1. `/organizador/certificate/`
2. Linha do certificado: clicar **Despublicar** → **Alterar modelo** → editar → **Salvar Certificado**
3. Voltar à lista e clicar **Publicar**

### Gerar novo API Token

1. `/organizador/integrations/`
2. Bloco **API Even3** → **Gerenciar**
3. Clicar **+ Criar chave de acesso**, dar nome (ex: "Landing Vercel")
4. Copiar a chave gerada
5. Atualizar no Vercel: `vercel env add EVEN3_API_TOKEN production`
6. Redeploy: `vercel deploy --prod`

---

## 7. Conteúdo configurado · resumo

- **Comissão Científica:** Profa. Silvia Cristina Rufino · `comissao.cientifica@encontrogeig.org`
- **7 avaliadores** cadastrados (Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio, Silvia Cristina Rufino)
- **13 áreas temáticas** alinhadas ao projeto executivo (não as 14 que vinham com typo "Sis Sigma")
- **4 modalidades** com PDFs de regras adaptados (gerados por `scripts/gerar_regras_pdf.py`)
- **22 atividades** de programação distribuídas nos 3 dias
- **6 templates de certificado** publicados, com tags dinâmicas (`{participante.nome}`, etc.)
- **Termo LGPD obrigatório** no formulário de inscrição (consentimento + cessão de imagem)
- **CSS custom** no hotsite (paleta navy/yellow/green/blue alinhada ao logo)

Detalhes do conteúdo factual: ver [`CONTENT.md`](CONTENT.md).

---

## LGPD — texto revisado do checkbox e pendências (12/06/2026)

Pacote LGPD criado em 12/06: página pública `/privacidade/` no site + 3 documentos em `docs/lgpd/`
(termo de imagem/voz, aviso de gravação/transmissão A4, política de guarda e retenção). Gerados por
`scripts/gerar_docs_lgpd.py`.

**Texto revisado do checkbox LGPD** (aplicar manualmente em Inscrições > Formulário de inscrição,
substituindo o termo atual — somente APÓS a página `/privacidade/` estar no ar):

> Li e concordo com a Política de Privacidade do Encontro GEI (encontrogeig.org/privacidade).
> Estou ciente de que o evento será gravado, fotografado e transmitido ao vivo, e autorizo,
> gratuitamente, o uso da minha imagem, voz e nome nos registros e materiais institucionais e
> científicos do evento, sem finalidade comercial, nos termos da Lei nº 13.709/2018 (LGPD) e do
> art. 20 do Código Civil.

**Pendências Even3:**
- [ ] Aplicar o checkbox revisado no formulário de inscrição (após deploy da página de privacidade)
- [ ] Corrigir descrição da entrada "Presencial Completo" ("três dias" → Dias 1 e 3)
- [ ] Criar a entrada da Visita Técnica D2 quando as jornadas forem confirmadas (site já diz "em breve")

**Pendências jurídicas (placeholders nos documentos):** CNPJ/endereço AGENERSA e UFF, nome do
encarregado (DPO), prazos de retenção (5 anos/2 anos), acordo entre controladoras conjuntas.

---

## 8. Recursos externos

- Documentação oficial: https://docs.even3.com.br/
- Central de Ajuda: https://ajuda.even3.com.br/hc/pt-br
- Sitemap da API: https://docs.even3.com.br/sitemap
- Sobre embed do Even3 no site: https://ajuda.even3.com.br/hc/pt-br/articles/360004093772
