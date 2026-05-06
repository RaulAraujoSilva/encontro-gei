# Deploy · Vercel + GitHub

## Stack de hospedagem

- **Repositório:** `RaulAraujoSilva/encontro-gei` (GitHub, branch `main`)
- **Vercel project:** `encontro-gei` (scope `raularaujosilvas-projects`)
- **URL produção:** https://encontrogeig.org
- **Auto-deploy:** push para `main` dispara build automático no Vercel (~30s)

---

## Variáveis de ambiente (Vercel)

| Variável | Valor | Uso |
|---|---|---|
| `EVEN3_API_TOKEN` | `da1c37f7-538f-4c93-bf7e-f6154fab02f8` | Header `Authorization-Token` ao chamar API Even3 |
| `EVEN3_EVENT_ID` | `722003` | ID do evento na Even3 (não usado atualmente — endpoint `/attendees` retorna todos do token) |

Listar/editar:
```bash
vercel env ls --scope raularaujosilvas-projects
vercel env add EVEN3_API_TOKEN production
vercel env rm EVEN3_API_TOKEN production
```

---

## Deploy manual

```bash
# Carregar token Vercel (uma vez por sessão)
set -a; source <(grep -E "^export VERCEL_TOKEN=" "/c/.claude/claude-secrets.env" | sed 's/^export //'); set +a

# Deploy de produção
vercel deploy --prod --yes --token="$VERCEL_TOKEN" --scope raularaujosilvas-projects
```

Saída típica:
```
Production: https://encontro-XXXXXXX-raularaujosilvas-projects.vercel.app [14s]
Aliased: https://encontrogeig.org
```

---

## Auto-deploy via Git

```bash
git add -A
git commit -m "feat: descrição da mudança"
git push origin main
# Vercel detecta o push e faz build automático
```

Acompanhar build: https://vercel.com/raularaujosilvas-projects/encontro-gei

---

## Cache busting

Vercel + CDN da Vercel pode demorar a invalidar imagens. Truques:

1. **Anexar query string ao src:**
   ```html
   <img src="/assets/logos/agenersa.png?v=4">
   ```
   Mudar `?v=N` força fetch fresco. Necessário quando substitui um arquivo mantendo o nome.

2. **Hard refresh no browser:**
   - Windows: `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`

3. **Verificar HTML servido em produção:**
   ```bash
   curl -s https://encontrogeig.org/ | grep -oE 'src="[^"]*"' | head
   ```

---

## Rollback

1. Painel Vercel: https://vercel.com/raularaujosilvas-projects/encontro-gei/deployments
2. Localizar deploy anterior estável
3. Botão **"Promote to Production"**

Alternativa via CLI:
```bash
vercel rollback --token="$VERCEL_TOKEN" --scope raularaujosilvas-projects
```

---

## Headers de segurança

Configurados em `vercel.json`:
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: geolocation=(), microphone=(), camera=()`

Cache de assets: `public, max-age=31536000, immutable` em `/assets/*`.

Redirects úteis:
- `/inscricao` → `/#inscricao`
- `/programa` → `/#programacao`
- `/submissao` → `/#trabalhos`

---

## Troubleshooting

| Problema | Causa provável | Solução |
|---|---|---|
| Deploy fica em build infinito | Quota grátis Vercel atingida | Aguardar reset mensal ou upgrade |
| Imagem antiga aparece | Cache CDN | `?v=N` query string |
| `/api/inscritos` retorna `count:0` | Token Even3 inválido/expirado | Regerar token (ver `EVEN3_OPERATIONS.md` §6) |
| `404` em sub-página | Rota mal configurada em `vercel.json` | Adicionar redirect ou criar `<pasta>/index.html` |
| `git push` rejeitado | Push para `main` sem permissão | Verificar `gh auth status` |
