# Plano — Migrar e-mails para `@encontrogeig.org` (já ativos no Google Workspace)

## Context

O usuário concluiu a configuração do Google Workspace e tem **3 e-mails operacionais** no domínio próprio:
- `contato@encontrogeig.org` (caixa principal)
- `comissao.cientifica@encontrogeig.org` (alias)
- `submissoes@encontrogeig.org` (alias)

Agora precisa atualizar todas as referências do projeto que ainda usam `@encontrogei.com.br` (placeholder antigo) para os novos endereços.

## Escopo

### Substituições

| De | Para |
|---|---|
| `contato@encontrogei.com.br` | `contato@encontrogeig.org` |
| `comissao.cientifica@encontrogei.com.br` | `comissao.cientifica@encontrogeig.org` |

> Adicionalmente, **acrescentar** `submissoes@encontrogeig.org` em pontos relevantes (rodapé dos PDFs e bloco de contato do regulamento de submissão).

### Arquivos a atualizar (7 fontes + Even3)

| Arquivo | Mudança |
|---|---|
| `index.html` | mailto + textos de contato |
| `patrocinadores/index.html` | mailto |
| `scripts/gerar_regras_pdf.py` | footer dos PDFs + bloco "Submissão e contato" passa a citar `submissoes@` |
| `README.md` | seção Contato |
| `docs/CONTENT.md` | tabela de contatos |
| `docs/EVEN3_OPERATIONS.md` | comissão científica |
| **Even3** | Configuração > Evento > Organizado por > E-mail (via Chrome MCP) |

### Artefatos derivados

- `assets/regras/{resumo-expandido,poster,relatorio-a3,artigo-completo}.pdf` regenerar via `scripts/gerar_regras_pdf.py`
- Re-upload dos 4 PDFs nas modalidades Even3 (já pratiquei o fluxo várias vezes)

## Etapas (~10 min + uploads)

1. Buscar e substituir `encontrogei.com.br` → `encontrogeig.org` em 6 arquivos (Edit replace_all)
2. No `gerar_regras_pdf.py`, **adicionar `submissoes@encontrogeig.org`** ao footer e ao bloco de contato (não só substituir)
3. Atualizar Even3 organizador (e-mail) via MCP
4. Rodar `python scripts/gerar_regras_pdf.py` para regerar os 4 PDFs
5. Re-upload dos 4 PDFs nas modalidades Even3 via MCP (sequência conhecida: abrir modalidade → "Trocar regras de submissão" → upload_file → wait 5s → Salvar Modalidade)
6. `git add -A && git commit && git push` + `vercel deploy --prod`

## Verificação

- `grep -r "encontrogei.com.br"` retorna apenas referências em `.claude-docs/plans/*-2026-05-05-*.md` (snapshots históricos)
- `curl -s https://encontrogeig.org | grep -o "encontroge[^\"]*"` mostra apenas o domínio novo
- Cada modalidade Even3 mostra "Trocar regras de submissão" (PDF anexado)
- PDF gerado abre com footer atualizado em `assets/regras/resumo-expandido.pdf`

## Arquivos não tocados (intencionalmente)

- `.claude-docs/plans/2026-05-05-landing-page-1encontro-gei.md` — plano histórico, snapshot da rodada inicial; mantém o email da época.
