# Plano — Avaliação Site/Even3 + Ajuste de modalidades + Pacote LGPD

## Contexto

Tarefas sob responsabilidade do Raul no painel (frentes 8 e 9, prazo 12/06): avaliar a configuração de inscrições e submissões no site/Even3, refletir que **por enquanto só há 2 entradas de inscrição abertas** (Presencial + Online; Visita Técnica ainda sem entrada na Even3), confirmar o fluxo de URL de vídeo no resumo expandido, e **criar a documentação LGPD** (tasks 9.5.1–9.5.4) considerando que o evento será gravado, fotografado e transmitido ao vivo no YouTube.

Decisões do usuário: Visita Técnica fica no card com selo **"Inscrições em breve"**; controladores dos dados = **AGENERSA + UFF (corealização)**; entrega LGPD = **página no site + documentos Word**.

## Parte A — Avaliação (estado atual, já levantado)

**Inscrições:** site mostra 3 modalidades em `#modalidades` (Presencial 400 / Visita Técnica 200 / Online ilimitado), mas a Even3 tem só 2 entradas (Presencial Completo 400 + Participação Online ilimitada, criadas 10/06). Divergência a corrigir no site (Parte B). `api/inscritos.js` já segmenta presencial/online corretamente.

**Submissão (artigos/resumo):** 4 modalidades configuradas na Even3 e no site (Resumo Expandido, Pôster A3, Relatório A3, Artigo Completo) com regras em PDF e modelos. O formulário Even3 **já tem** o campo personalizado "URL do vídeo de apresentação" (resposta curta, visível ao avaliador — `docs/EVEN3_OPERATIONS.md`). O site orienta "link público no documento" (linha 1077 e norma "Vídeo" ~linha 1056), mas **não explicita** que o vídeo deve estar em drive aberto ("qualquer pessoa com o link pode ver") — reforço na Parte B.

A avaliação consolidada (incluindo checagem ao vivo via API Even3, GET attendees, read-only) será reportada no resumo final da execução.

## Parte B — Edições no `index.html`

1. **Linha 937** (card Visita Técnica): `<div class="mod-vagas">200 vagas (~25/jornada)</div>` → `<div class="mod-vagas">Inscrições em breve</div>`.
2. **Linha 934** (sec-desc de #modalidades): reescrever para: inscrições abertas hoje = Presencial (Dias 1 e 3) e Online; a inscrição da Visita Técnica do Dia 2 será aberta em breve, independente e combinável com a presencial.
3. **Linha 1093** (sec-desc de #inscricao): "A visita técnica do Dia 2 tem inscrição independente..." → "...terá inscrição independente, **aberta em breve**."
4. **FAQ — linhas 1217, 1223, 1225**: ajustar os 3 itens que afirmam que a visita técnica "possui inscrição própria" para o tempo futuro ("terá inscrição própria, a ser aberta em breve").
5. **Linha 1077** (passo 3 da submissão) + **norma "Vídeo" (~1056)**: explicitar o drive aberto — ex.: "hospede o vídeo em Google Drive/OneDrive com acesso **'qualquer pessoa com o link'** (ou YouTube não listado) e cole o link no corpo do documento e no campo 'URL do vídeo' da Even3".
6. **Footer (~1260-1271)**: adicionar `<a href="/privacidade/">Política de privacidade</a>` na coluna "Site". Nota curta abaixo do iframe de inscrição (~1114): dados tratados pela Even3 (operadora) conforme a Política de Privacidade; evento gravado/transmitido.

Também adicionar o link de privacidade nos footers de `organizadores/index.html` e `patrocinadores/index.html`.

## Parte C — Pacote LGPD

**Pesquisa prévia (execução):** WebSearch/WebFetch sobre Lei 13.709/2018, guias ANPD (agentes de tratamento, cookies 2022, Res. CD/ANPD 15/2024 sobre incidentes) e políticas de privacidade de eventos acadêmicos híbridos semelhantes, para validar bases legais e linguagem antes de redigir.

**Bases legais (síntese a aplicar):**
- Dados de inscrição: art. 7º, V (procedimentos preliminares/execução de contrato — adesão ao evento gratuito); legítimo interesse (7º, IX) para logística/segurança/presença.
- Imagem/voz da plateia: legítimo interesse + CC art. 20, com aviso ostensivo e canal de oposição; palestrantes/autores (exposição individualizada e permanente): consentimento via termo de cessão (7º, I).
- Comunicações futuras: opt-in separado (7º, I). Sem dados sensíveis (declarar; se surgir campo de acessibilidade → art. 11, II, "a"). Público 18+. Retenção: art. 16 (I e II). Even3 = operadora (art. 39); YouTube/Google = transferência internacional (art. 33). Direitos: arts. 18–19. Incidentes: art. 48 + Res. 15/2024.

**Entregáveis:**

1. **`privacidade/index.html`** (pública, URL `/privacidade/`) — clonar padrão visual de `organizadores/index.html` (nav sticky com "← Voltar", hero com badge, paleta navy/yellow, Manrope/Outfit). 13 seções: quem somos (AGENERSA + UFF controladores conjuntos, CNPJ/endereço `[A VALIDAR]`); dados coletados; finalidades × bases legais (tabela); gravação/fotografia/transmissão; compartilhamento (Even3, YouTube, certificadoras); transferência internacional; retenção (tabela, prazos `[A VALIDAR]`); direitos do titular; cookies (GA4 ainda inativo — só previsão); menores; segurança; encarregado `[A VALIDAR]` + contato@encontrogeig.org; versão/data.
2. **`docs/lgpd/termo-consentimento-imagem-voz.docx`** — termo de cessão de imagem/voz/nome: identificação, considerandos (evento híbrido gravado/transmitido), objeto sem finalidade comercial, abrangência (YouTube, site, redes, anais; prazo indeterminado), gratuidade, fundamentos (LGPD 7º-I + CC art. 20), revogação (art. 8º §5º, efeitos prospectivos), bloco de assinatura para credenciamento + **anexo** com as versões curtas (checkbox Even3 e texto de balcão).
3. **`docs/lgpd/aviso-gravacao-transmissao-A4.docx`** — pág. 1: cartaz A4 para os ambientes ("Este evento está sendo gravado, fotografado e transmitido ao vivo" + finalidade + URL /privacidade/ + espaço p/ QR); pág. 2: textos para descrição do YouTube, slide de abertura e aviso verbal do mestre de cerimônias (cobre task 9.5.2 presencial e online).
4. **`docs/lgpd/politica-guarda-retencao-dados.docx`** (interna; cobre 9.5.4) — papéis (controladores conjuntos + acordo entre controladores conforme guia ANPD; Even3 operadora; acessos `[A PREENCHER]`), inventário de dados (tabela categoria · origem · finalidade · base · local · acesso · prazo · descarte), prazos de retenção `[A VALIDAR]`, descarte na Even3 pós-evento, fluxo de atendimento a titulares, fluxo de incidentes (3 dias úteis), vigência.

Geração dos .docx via skill **word-docx**, com acentuação correta e placeholders destacados em amarelo.

**Texto revisado do checkbox Even3** (entregue no termo e registrado em `docs/EVEN3_OPERATIONS.md` como pendência de aplicação manual na Even3): "Li e concordo com a Política de Privacidade do Encontro GEI (encontrogeig.org/privacidade). Estou ciente de que o evento será gravado, fotografado e transmitido ao vivo, e autorizo, gratuitamente, o uso da minha imagem, voz e nome nos registros e materiais institucionais e científicos do evento, sem finalidade comercial, nos termos da Lei nº 13.709/2018 (LGPD) e do art. 20 do Código Civil."

## Arquivos

| Ação | Arquivo |
|---|---|
| Modificar | `index.html` (linhas 934, 937, 1056, 1077, 1093, 1114, 1217, 1223, 1225, footer 1260-1271) |
| Criar | `privacidade/index.html` |
| Modificar | `organizadores/index.html`, `patrocinadores/index.html` (footer) |
| Criar | `docs/lgpd/` — 3 documentos .docx |
| Modificar | `docs/EVEN3_OPERATIONS.md` (checkbox revisado + pendências), `.claude-docs/tasks.md` e `features.md` |

## Verificação

1. Servir localmente (`python -m http.server`) e conferir via chrome-devtools: render desktop/mobile do index e da `/privacidade/`, links de footer, acentuação, console sem erros.
2. GET read-only na API Even3 (token em `docs/EVEN3_OPERATIONS.md`) para confirmar as 2 entradas ativas e relatar no resumo.
3. Abrir/inspecionar os .docx (acentos, placeholders destacados).
4. **Gate antes do push:** placeholders `[A VALIDAR]` (CNPJ, endereço, encarregado, prazos) precisam de validação jurídica — commit local + push só com autorização do usuário (push em main = deploy em produção). A atualização do checkbox na Even3 é manual e só após a página estar no ar.

## Riscos

- Não inventar CNPJ/endereço/DPO/prazos — sempre `[A VALIDAR]`.
- Não afirmar que GA4 está ativo; não prometer remoção retroativa de transmissões já realizadas.
- Footer cita realização "UFF · ABAR · PPGEP - LabDGE/UFF · GIGS/UNICAMP" sem AGENERSA — a política nomeará AGENERSA + UFF como controladores (decisão do usuário); destacar essa diferença na revisão jurídica.
