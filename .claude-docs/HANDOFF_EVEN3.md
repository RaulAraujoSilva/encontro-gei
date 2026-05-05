# Handoff Even3 — Status atual + Scripts JS para console

> **Atualizado:** 2026-05-05 · Boa parte foi configurada via Chrome MCP usando truque de JS dispatch (bypassa máscara dd/mm).

## ✅ Já configurado pelo Claude

- **Datas do evento:** 08/07/2026 09:00 → 10/07/2026 20:00
- **Carga horária:** 24h
- **Inscrições (4 modalidades, todas gratuitas):**
  - Presencial Completo (300 vagas) — você adicionou
  - Presencial Dias 1 e 3 (300 vagas) — você adicionou
  - Remoto / Online (ilimitado) — Claude via MCP
  - Visitante Técnico Dia 2 (200 vagas) — Claude via MCP
- **Cronograma de submissões:** Início 06/05/2026 → Fim 15/05/2026

## ⚠️ Ajustes recomendados

### 1. Áreas temáticas — substituir as 14 atuais pelos 13 do projeto executivo

URL: `https://www.even3.com.br/organizador/trabalhocientifico/submissaogeral?tab=Áreas%20Temáticas`

As áreas atuais (com typo "Sis Sigma" + áreas não previstas como "ODS no Ensino") parecem de outro evento. Para alinhar ao projeto executivo:

**Apagar todas e recriar:**
1. Regulação de infraestrutura, energia e saneamento
2. Sandbox regulatório e inovação institucional
3. Gestão pública inovadora e GovTech
4. Lean Six Sigma e excelência operacional
5. Sustentabilidade e ESG em organizações reguladas
6. Inteligência governamental e apoio à decisão
7. Governança de dados e interoperabilidade
8. Transformação digital e serviços públicos
9. Capacidade analítica e uso de evidências
10. Saúde digital e dados conectados
11. Inteligência artificial e soberania nacional
12. Trabalho, ergonomia e segurança
13. Pesquisa operacional, otimização e logística

### 2. Configurações > Modalidades de submissão

URL: `/organizador/trabalhocientifico/submissaogeral?tab=Modalidades`

Adicionar 3 modalidades:
- **Resumo Estendido + Vídeo (Fase 1)** — 2-4pp + URL vídeo até 5min · prazo 15/05/2026
- **Artigo Completo (Fase 2)** — 8-15pp · prazo 30/09/2026
- **Relato de Visita Técnica** — 2-3pp · exclusivo participantes Dia 2

### 3. Comissão Científica

URL: `/organizador/trabalhocientifico/submissaogeral?tab=Configurações` → "Editar comissão"

- Responsável: a definir (Prof. Callado?)
- E-mail: contato@encontrogei.com.br
- Membros 4º Seminário SSEP: Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio, Silvia Cristina Rufino

---

## 🤖 Scripts JS — cole no console (F12) do navegador

### Pré-requisito
Abra o console do navegador na página da Even3 (F12 → Console) e cole o helper antes de qualquer script:

```js
// Helper universal para forçar valor em inputs mascarados
window.setVal = (el, v) => {
  const s = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
  s.call(el, v);
  el.dispatchEvent(new Event('input', { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
  el.dispatchEvent(new Event('blur', { bubbles: true }));
};
window.click = sel => Array.from(document.querySelectorAll('button, a')).find(b => b.innerText.trim().match(sel))?.click();
```

### Script A — Adicionar 13 áreas temáticas em batch

Cole na página `https://www.even3.com.br/organizador/trabalhocientifico/submissaogeral?tab=Áreas%20Temáticas` (depois de apagar as 14 atuais):

```js
const eixos = [
  'Regulação de infraestrutura, energia e saneamento',
  'Sandbox regulatório e inovação institucional',
  'Gestão pública inovadora e GovTech',
  'Lean Six Sigma e excelência operacional',
  'Sustentabilidade e ESG em organizações reguladas',
  'Inteligência governamental e apoio à decisão',
  'Governança de dados e interoperabilidade',
  'Transformação digital e serviços públicos',
  'Capacidade analítica e uso de evidências',
  'Saúde digital e dados conectados',
  'Inteligência artificial e soberania nacional',
  'Trabalho, ergonomia e segurança',
  'Pesquisa operacional, otimização e logística'
];
(async () => {
  for (const e of eixos) {
    click(/Adicionar área/i); await new Promise(r => setTimeout(r, 800));
    const inp = document.querySelector('.modal-dialog input[type="text"]');
    if (!inp) { console.warn('input não encontrado'); break; }
    setVal(inp, e); await new Promise(r => setTimeout(r, 200));
    click(/^Salvar/i); await new Promise(r => setTimeout(r, 1500));
    console.log('✓', e);
  }
})();
```

### Script B — Adicionar 8 jornadas técnicas como atividades do Dia 2

URL: `https://www.even3.com.br/organizador/programacao/`

```js
const jornadas = [
  { tit: 'Jornada 01 — Petrobras', desc: 'Visita técnica: Regulação de energia e transformação digital em operações de E&P' },
  { tit: 'Jornada 02 — Águas do Rio (CCO) + ETE/Biogás (integrada)', desc: 'Saneamento e regulação de infraestrutura, seguido de sustentabilidade e ESG' },
  { tit: 'Jornada 03 — Guandu / Lameirão', desc: 'Infraestrutura hídrica e governança ambiental' },
  { tit: 'Jornada 04 — Ternium · Santa Cruz', desc: 'Indústria consumidora de gás natural, ESG e Lean Six Sigma' },
  { tit: 'Jornada 05 — Gerdau · Santa Cruz', desc: 'Indústria consumidora de gás, transformação digital e ESG' },
  { tit: 'Jornada 06 — Eneva + TAG (integrada)', desc: 'Regulação de energia e GovTech, seguido de transporte de gás natural' },
  { tit: 'Jornada 07 — IRM + AGENERSA (integrada)', desc: 'Inteligência governamental e saneamento, seguido de sandbox regulatório' },
  { tit: 'Jornada 08 — CSN', desc: 'Indústria consumidora de gás, ESG e Lean Six Sigma' }
];
(async () => {
  for (const j of jornadas) {
    click(/Adicionar atividade/i); await new Promise(r => setTimeout(r, 1200));
    setVal(document.querySelector('input[name="titulo"]'), j.tit);
    const tx = document.querySelector('textarea[name="descricao"]');
    if (tx) { tx.value = j.desc; tx.dispatchEvent(new Event('input', {bubbles:true})); }
    // Manter os outros campos default (você pode editar depois)
    await new Promise(r => setTimeout(r, 400));
    click(/^Salvar/i); await new Promise(r => setTimeout(r, 2000));
    console.log('✓', j.tit);
  }
})();
```
*(Após o batch, edite cada uma para adicionar data 09/07/2026, horário 09:00–17:00, vagas 25, e marcar como visita técnica.)*

### Script C — Adicionar atividades do Dia 1

```js
const dia1 = [
  { tit: 'Credenciamento digital e recepção', h: '13:30' },
  { tit: 'Mesa de abertura institucional', h: '14:15' },
  { tit: 'Painel de apresentação do evento', h: '15:30' },
  { tit: 'Conferência magna — Magda Chambriard (Petrobras)', h: '16:10' },
  { tit: 'Coquetel de networking institucional', h: '17:00' }
];
(async () => {
  for (const a of dia1) {
    click(/Adicionar atividade/i); await new Promise(r => setTimeout(r, 1200));
    setVal(document.querySelector('input[name="titulo"]'), a.tit);
    await new Promise(r => setTimeout(r, 400));
    click(/^Salvar/i); await new Promise(r => setTimeout(r, 2000));
    console.log('✓', a.tit);
  }
})();
```

### Script D — Adicionar atividades do Dia 3

```js
const dia3 = [
  { tit: 'Plenária + Painel "IA e soberania nacional" (Prof. Li Li Min)', h: '09:00' },
  { tit: 'Trilha A — Lean Six Sigma Congress (13ª edição)', h: '10:30' },
  { tit: 'Trilha B — Seminário SSEP (4ª edição)', h: '10:30' },
  { tit: 'Trilha C — Seminário de Regulação (2ª edição)', h: '10:30' },
  { tit: 'Trilha D — Seminário de Inteligência Governamental (1ª edição)', h: '10:30' },
  { tit: 'Sessões técnicas e acadêmicas (apresentação de trabalhos)', h: '14:00' },
  { tit: 'Premiação dos melhores trabalhos', h: '16:30' },
  { tit: 'Encerramento institucional', h: '18:00' },
  { tit: 'Coquetel de encerramento', h: '19:00' }
];
(async () => {
  for (const a of dia3) {
    click(/Adicionar atividade/i); await new Promise(r => setTimeout(r, 1200));
    setVal(document.querySelector('input[name="titulo"]'), a.tit);
    await new Promise(r => setTimeout(r, 400));
    click(/^Salvar/i); await new Promise(r => setTimeout(r, 2000));
    console.log('✓', a.tit);
  }
})();
```

---

## 🔧 Configuração > Evento — completar manualmente

URL: `https://www.even3.com.br/organizador/configuracao/evento`

### Bloco "Divulgação"
- **Tipo:** alterar para `Científico - Congresso/Simpósio`
- **Assunto principal:** `Engenharias`
- **Palavras-chaves**: `governança pública, regulação, inovação governamental, GovTech, engenharia de produção, Lean Six Sigma, inteligência governamental, sandbox regulatório`
- **Descrição curta:**
  > A primeira plataforma nacional a integrar excelência operacional, engenharia de produção, regulação de infraestrutura e inteligência governamental. 4 eventos oficiais, 8 visitas técnicas, 3 dias. 08–10/07/2026, Rio/Niterói. Anais com ISBN.

### Bloco "Local"
- **Estado:** Rio de Janeiro
- **Cidade:** Rio de Janeiro
- **Local:** "Rio de Janeiro / Niterói — RJ (locais a confirmar)"

### Bloco "Organizado por"
- Responsável: `Secretaria do 1º Encontro GEI`
- E-mail: `contato@encontrogei.com.br`
- Logo: upload de `assets/logo-completo.jpg` (fundo navy + lockup)

---

## 📊 Coleta final (depois de tudo configurado)

### Embed codes — colar em `embeds.txt` na raiz
URL: `https://www.even3.com.br/organizador/integrations/` ou `/organizador/tools/`

Procurar **"Incluir Even3 no meu site"**:
- ☐ Embed Inscrição
- ☐ Embed Submissão
- ☐ Embed Programação
- ☐ Embed Convidados/Palestrantes

### API Token — salvar em `.env.local` (já no .gitignore)
URL: `/organizador/integrations/` → "API REST" → "Gerar token"

```env
EVEN3_API_TOKEN=cole_aqui
EVEN3_EVENT_ID=722003
```

Depois de configurar essas duas variáveis no Vercel (`vercel env add`), o contador "X profissionais já inscritos" do hero ativa automaticamente.

---

## Quando terminar
- Me cole `embeds.txt` aqui no chat → eu plugo na landing e faço novo deploy.
- Me passe o `EVEN3_API_TOKEN` em mensagem privada → eu adiciono no Vercel via CLI.
