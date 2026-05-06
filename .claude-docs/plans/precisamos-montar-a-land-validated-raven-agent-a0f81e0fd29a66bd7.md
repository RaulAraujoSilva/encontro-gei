# Guia Operacional — E-mails profissionais para `encontrogeig.org`

Guia prático para criar `contato@`, `comissao.cientifica@` e `submissoes@encontrogeig.org` usando Google Workspace (com alternativas mais baratas no final). Domínio hospedado na Vercel.

---

## 1. Planos Google Workspace (Brasil, 2026)

Preços oficiais em BRL, plano anual, por usuário/mês (fonte: workspace.google.com/pricing).

| Plano | Preço (BRL/usuário/mês) | Armazenamento | Meet | Gemini AI / Notas |
|---|---|---|---|---|
| **Business Starter** | **R$ 40,90** | 30 GB pooled | até 100 participantes | Gemini incluído (recursos básicos), e-mail custom, sem gravação Meet |
| **Business Standard** | **R$ 81,80** | 2 TB pooled | 150 part., gravação | Gemini + NotebookLM, anotações IA |
| **Business Plus** | **R$ 128,40** | 5 TB pooled | 500 part., presença | Vault (eDiscovery), endpoint mgmt, Gemini avançado |
| **Enterprise** | Sob consulta (~USD 23/mês) | 5 TB+ | 1.000 part. | DLP, S/MIME, suporte premium |

> Reajuste vigente desde 16/01/2026 para novas assinaturas. Trial de 14 dias gratuito em todos os planos.

## 2. Plano recomendado para o evento

Para 2-3 caixas operacionais de baixo volume, **Business Starter já basta**:

- **Truque importante:** assine **1 único usuário** (`contato@`) por **R$ 40,90/mês** e use **aliases gratuitos** para `comissao.cientifica@` e `submissoes@` (Google permite **até 30 aliases por usuário sem custo adicional**). Todos chegam na mesma caixa.
- Custo total: **~R$ 40,90/mês** (≈ R$ 491/ano).
- Se preferir caixas separadas com login próprio: 3 usuários = **R$ 122,70/mês**.

## 3. Passo a passo técnico (Google Workspace)

### 3.1 Criar conta e iniciar trial
1. Acesse `https://workspace.google.com/business/signup` → "Começar avaliação gratuita".
2. Informe nome do evento ("Encontro GEIG"), número de funcionários (1-9), país (Brasil).
3. Em "Você tem um domínio?" → **Sim**, digite `encontrogeig.org`.
4. Crie o usuário admin: `contato@encontrogeig.org` + senha forte.
5. Forneça cartão (não cobra durante os 14 dias de trial).

### 3.2 Verificar posse do domínio (TXT)
O Console exibirá um token `google-site-verification=...`. Adicione na Vercel:

| Type | Name | Value | TTL |
|---|---|---|---|
| `TXT` | `@` | `google-site-verification=ABC123XYZ...` (valor fornecido pelo console) | 3600 |

### 3.3 Registros MX (valor oficial Google 2026)

Desde abril/2023 o Google adotou **MX único**, mas os 5 legados continuam suportados. Use o moderno:

**Opção moderna (recomendada):**
| Type | Name | Priority | Value |
|---|---|---|---|
| `MX` | `@` | `1` | `smtp.google.com` |

**Opção legada (5 registros, ainda válida):**
| Type | Name | Priority | Value |
|---|---|---|---|
| `MX` | `@` | `1` | `aspmx.l.google.com` |
| `MX` | `@` | `5` | `alt1.aspmx.l.google.com` |
| `MX` | `@` | `5` | `alt2.aspmx.l.google.com` |
| `MX` | `@` | `10` | `alt3.aspmx.l.google.com` |
| `MX` | `@` | `10` | `alt4.aspmx.l.google.com` |

> **IMPORTANTE:** apague qualquer MX pré-existente (placeholder Vercel/registrador) antes de adicionar.

### 3.4 SPF (TXT)

| Type | Name | Value |
|---|---|---|
| `TXT` | `@` | `v=spf1 include:_spf.google.com ~all` |

Apenas **um** registro SPF por domínio. Se já existir, edite — não duplique.

### 3.5 DKIM
1. No Admin Console: **Apps → Google Workspace → Gmail → Authenticate email**.
2. Selecione o domínio `encontrogeig.org` → **Generate new record** (escolha **2048 bits**).
3. Copie `Hostname` (algo como `google._domainkey`) e o `TXT record value` (longo, começa com `v=DKIM1; k=rsa; p=...`).
4. Adicione na Vercel:

| Type | Name | Value |
|---|---|---|
| `TXT` | `google._domainkey` | `v=DKIM1; k=rsa; p=MIIBIjANBgkq...` (valor longo do console) |

5. Volte ao Admin Console → **Start authentication** (ativa após propagação DNS, ~1h).

### 3.6 DMARC (TXT)

| Type | Name | Value |
|---|---|---|
| `TXT` | `_dmarc` | `v=DMARC1; p=none; rua=mailto:contato@encontrogeig.org; ruf=mailto:contato@encontrogeig.org; fo=1` |

Comece com `p=none` (apenas observa). Depois de 2-4 semanas de relatórios, suba para `p=quarantine`.

### 3.7 Criar usuários e aliases
- **Usuário principal:** já existe (`contato@`).
- **Aliases (grátis):** Admin Console → **Directory → Users → contato@encontrogeig.org → Add alternate email** → adicione `comissao.cientifica@encontrogeig.org` e `submissoes@encontrogeig.org`.
- **Caixas separadas (pago):** Admin Console → **Add new user** (mais R$ 40,90 cada).

## 4. Onde configurar DNS (Vercel)

Provável que o domínio `.org` esteja num registrador internacional (Vercel Domains, Namecheap, Porkbun, GoDaddy — `.org` **não é Registro.br**). Se foi comprado **via Vercel** ou aponta NS para Vercel:

1. Vercel Dashboard → **Domains** → clique em `encontrogeig.org` → **DNS Records**.
2. Se ainda não estiver ativo, clique **Enable Vercel DNS**.
3. Para cada linha das tabelas acima → **Add Record** → preencha `Type`, `Name` (use `@` para apex), `Value`, e `Priority` (somente MX). TTL padrão 60s está ok.
4. CLI alternativa: `vercel dns add encontrogeig.org '@' MX smtp.google.com 1`.

Se o domínio estiver em outro registrador (Namecheap/Porkbun/GoDaddy), procure "Advanced DNS" / "DNS Management" e adicione os mesmos registros — os campos são equivalentes.

## 5. Alternativas mais baratas

| Opção | Custo | Prós | Contras |
|---|---|---|---|
| **Cloudflare Email Routing** | **Grátis** | Forward `contato@` → seu Gmail pessoal; até 200 regras; 5 min de setup | Apenas **recebe**; enviar exige config "Send As" no Gmail via SMTP terceiro; domínio precisa estar no Cloudflare (mover NS) |
| **Zoho Mail Free** | **Grátis** | 5 usuários, 5 GB cada, domínio próprio, webmail completo | Sem IMAP/POP (só web/app Zoho); região-restrita; sem cliente desktop |
| **Microsoft 365 Business Basic** | ~R$ 30/usuário/mês | 50 GB caixa, Teams, OneDrive 1 TB | Sem Gemini; Outlook web-first |
| **iCloud+ Custom Domain** | R$ 14,90/mês (200 GB) | Até 5 domínios, 3 e-mails/domínio, integra Apple Mail | Só faz sentido se já é usuário Apple |
| **Forward do registrador** | Grátis (Porkbun/Namecheap) | Zero config além de MX | Apenas forward, sem caixa real |

### Setup rápido Cloudflare (alternativa zero-custo)
1. Mova o domínio para Cloudflare (NS change, ~24h) — mantém Vercel como hosting.
2. Dashboard → **Email → Email Routing → Enable**.
3. Cloudflare adiciona MX + SPF automaticamente.
4. **Routing rules:** `contato@encontrogeig.org` → `seu-email@gmail.com` (idem para os outros).
5. Para **enviar como** `contato@`: Gmail → Configurações → Contas → "Adicionar outro endereço" → use SMTP relay (ex: Brevo grátis 300/dia, ou Gmail SMTP com app password).

## 6. Recomendação final

Para um evento acadêmico de baixo volume (2-3 endereços, picos perto de deadlines):

- **Se orçamento permite (~R$ 40/mês):** **Google Workspace Business Starter com 1 usuário + 2 aliases**. Profissionalismo total, Gemini, integração Google Acadêmico/Forms/Drive — ideal para submissões e comissão científica.
- **Se quer custo zero:** **Cloudflare Email Routing** (forward para Gmail pessoal) + "Send As" via SMTP relay grátis. Funciona, mas requer mover NS para Cloudflare e configurar envio manualmente.
- **Meio-termo:** **Zoho Mail Free** se aceita usar só webmail do Zoho.

**Veredicto:** para um evento acadêmico que valoriza confiabilidade de entrega (DKIM/DMARC bem configurados raramente caem em spam), vale os ~R$ 491/ano do Google Workspace.

## 7. Tempo estimado

| Etapa | Tempo |
|---|---|
| Criar conta + trial | 10 min |
| Adicionar TXT verificação + MX/SPF/DKIM/DMARC na Vercel | 15 min |
| Propagação DNS | 15 min – 24 h (geralmente < 2 h) |
| Ativar DKIM no Console (após propagação) | 5 min |
| Criar aliases | 5 min |
| **Total ativo:** | **~35 min** + janela de propagação |

## Fontes
- [Google Workspace — Comparar planos (BRL)](https://workspace.google.com/pricing?hl=pt)
- [Google Support — Set up MX records (2026)](https://support.google.com/a/answer/16004259?hl=en)
- [Manual do Usuário — Reajuste Google Workspace 2026](https://manualdousuario.net/google-workspace-gemini-ia-aumento/)
- [Cloudflare Email Routing](https://www.cloudflare.com/developer-platform/products/email-routing/)
- [Zoho Mail — Custom domain free 5 users](https://www.zoho.com/mail/custom-domain-email.html)
- [Vercel Docs — Managing DNS Records](https://vercel.com/docs/domains/managing-dns-records)
