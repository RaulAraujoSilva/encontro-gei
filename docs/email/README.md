# Divulgação das Visitas Técnicas — peça de e-mail

Peça para convidar **todos os inscritos confirmados** (presencial + online) a escolherem
1 das 4 jornadas técnicas do **Dia 2 (09/07)**. Prazo de inscrição na Even3: **até 07/07**.

> Situação em 01/07/2026 (via `GET https://encontrogeig.org/api/inscritos`):
> **512 confirmados** (428 presencial + 84 online) · **0 inscrições em visita** — as 4 jornadas
> estão totalmente abertas (146 vagas: J01 43 · J02 39 · J03 26 · J04 38).

## Arquivos

| Arquivo | Uso |
|---|---|
| `divulgacao-visitas-tecnicas.html` | Corpo HTML (e-mail-safe, tabelas + estilos inline). Colar no editor da Even3 **ou** usar como corpo HTML no SMTP. |
| `divulgacao-visitas-tecnicas.txt` | Versão texto espelhada (fallback multipart e leitura sem imagens). |

## Assunto e pré-cabeçalho

- **Assunto:** `Visitas Técnicas (09/07) do 1º Encontro GEI — inscrições até 07/07`
- **Pré-cabeçalho (preview):** já embutido no HTML — *"4 jornadas técnicas exclusivas no Dia 2 (09/07): Petrobras, CEDAE, Águas de Niterói e Braskem. Vagas limitadas — escolha a sua até 07/07."*
- **Remetente:** `gestao@encontrogeig.org` (nome: *Comissão Organizadora — 1º Encontro GEI*).
- **Link único de inscrição** (leva à Área do Participante após login):
  `https://www.even3.com.br/evento/login?evento=1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003&ReturnUrl=%2fparticipante%2fsessions%2f&lang=pt`

---

## Rota principal — Even3 (comunicado da plataforma)

**Por quê:** remetente já aquecido, lista dentro da plataforma, sem manusear e-mails/PII → menor risco de spam.

### Passo a passo (painel do organizador, evento 722003)
1. Acessar o painel da Even3 logado como organizador do evento.
2. Localizar a ferramenta de **comunicado/e-mail a participantes**. Caminhos prováveis:
   - **Divulgação → E-mails / Comunicados**, ou
   - **Participantes/Pessoas → Enviar e-mail**.
   > ⚠️ **A confirmar no painel:** a documentação do projeto (`docs/EVEN3_OPERATIONS.md`) só
   > registra o comunicado de **submissão** (atinge quem submeteu) e "notificar participantes"
   > por atividade. Se **não** houver disparo para **todos os inscritos**, usar a rota de
   > contingência (SMTP) abaixo — isso muda o canal e deve ser validado antes.
3. Destinatários: **todos os participantes confirmados** (não filtrar por submissão).
4. Assunto: colar o assunto acima.
5. Corpo: alternar o editor para **HTML/código-fonte** e colar `divulgacao-visitas-tecnicas.html`.
   (Se o editor não aceitar o documento completo, colar apenas o conteúdo interno do `<body>`.)
6. **Enviar um teste** para `gestao@encontrogeig.org`; conferir render (Gmail desktop + celular),
   logo carregando e todos os links levando ao evento 722003.
7. Disparar para todos. Registrar data/hora e nº de destinatários.

---

## Rota de contingência — e-mail de gestão via SMTP

Usar **apenas** se a Even3 não tiver disparo para todos os inscritos. Script:
`scripts/enviar_divulgacao_visitas.py` (espelha `scripts/enviar_cartas_autores.py`).

```bash
# 1) Prévia: lista destinatários da API Even3, sem enviar
EVEN3_API_TOKEN=xxxx python scripts/enviar_divulgacao_visitas.py --dry-run

# 2) Teste: envia 1 amostra
GESTAO_APP_PWD=xxxx EVEN3_API_TOKEN=xxxx python scripts/enviar_divulgacao_visitas.py --test gestao@encontrogeig.org

# 3) Aquecimento e produção (idempotente via log; --resume não reenvia)
GESTAO_APP_PWD=xxxx EVEN3_API_TOKEN=xxxx python scripts/enviar_divulgacao_visitas.py --send-all --limit 20
GESTAO_APP_PWD=xxxx EVEN3_API_TOKEN=xxxx python scripts/enviar_divulgacao_visitas.py --send-all
```

### Pré-voo de entregabilidade (só na rota SMTP)
- [ ] **DKIM ativo** no Google Workspace Admin (Apps → Gmail → Autenticar e-mail).
- [ ] **DMARC em `p=none`** durante a campanha — ver `.claude-docs/plans/para-o-site-do-deep-dewdrop.md`.
      Conferir: `nslookup -type=TXT _dmarc.encontrogeig.org`.
- [ ] **mail-tester.com ≥ 9/10** enviando a peça real.
- [ ] Começar com `--limit 20` (contas próprias/seeds) e conferir caixa de entrada antes de liberar.
- [ ] 1 `To` por mensagem (nunca BCC gigante); throttle já embutido no script.
- [ ] Não versionar listas de e-mail/PII (respeitar `.gitignore`).

---

## Checklist geral (qualquer rota)
- [ ] Conferir vagas restantes em `/api/inscritos` — se alguma jornada lotar, ajustar a peça.
- [ ] Teste recebido na **caixa de entrada** (não spam) antes do disparo geral.
- [ ] Links clicáveis e apontando ao evento 722003; logo carregando.
- [ ] Rodapé LGPD presente (motivo do recebimento + descadastro).
- [ ] Após o envio: registrar data/alcance e acompanhar a adesão nas jornadas.
