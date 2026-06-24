"""Gera o Edital Consolidado do 1° Encontro GEI (documento para validação prévia).

Reúne em um único PDF todas as informações do evento — identificação, participação
presencial/online, submissões, avaliação, cronograma, publicação dos resultados
(anais ISBN + DOI), LGPD e contato — reaproveitando o layout dos PDFs de regras
(scripts/gerar_regras_pdf.py): paleta navy/amarelo, cabeçalho com logo e rodapé navy.

Uso: python scripts/gerar_edital_consolidado.py
Saída: docs/edital/edital-consolidado-1o-encontro-gei.pdf
"""
import sys
from datetime import date
from pathlib import Path

# Reaproveita cores, estilos e helpers visuais dos PDFs de regras (fonte única de layout).
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gerar_regras_pdf as base  # noqa: E402

from reportlab.lib.pagesizes import A4  # noqa: E402
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.lib.units import cm  # noqa: E402
from reportlab.lib.colors import HexColor  # noqa: E402
from reportlab.lib.enums import TA_LEFT  # noqa: E402
from reportlab.platypus import (  # noqa: E402
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "edital"
OUT.mkdir(parents=True, exist_ok=True)

ORANGE = HexColor("#F2913D")  # laranja "Estratégia" da marca — usado no apêndice de pendências

# Estilos de célula de tabela (derivados do corpo padrão)
CELL = ParagraphStyle("Cell", parent=base.P, fontSize=9, leading=12,
                      alignment=0, spaceAfter=0)
CELL_B = ParagraphStyle("CellB", parent=CELL, fontName="Helvetica-Bold")
CELL_H = ParagraphStyle("CellH", parent=CELL, fontName="Helvetica-Bold",
                        textColor=HexColor("#FFFFFF"))
PEND_T = ParagraphStyle("PendT", parent=base.P, fontName="Helvetica-Bold",
                        fontSize=10, leading=13, spaceAfter=2, textColor=base.NAVY2)
PEND_P = ParagraphStyle("PendP", parent=base.P, fontSize=9.5, leading=13, spaceAfter=0)
# Bullets alinhados à esquerda (evita estiramento de linhas com URLs longas).
LI_LEFT = ParagraphStyle("LILeft", parent=base.LI, alignment=TA_LEFT)


# ---------------------------------------------------------------- helpers
def section(story, titulo):
    story.append(Paragraph(titulo, base.H1))


def sub(story, titulo):
    story.append(Paragraph(titulo, base.H2))


def para(story, texto):
    story.append(Paragraph(texto, base.P))


def bullets(story, itens):
    for it in itens:
        story.append(Paragraph("• " + it, LI_LEFT))


def kv_table(story, linhas, c1=6.0 * cm, c2=10.0 * cm):
    """Tabela de 2 colunas (rótulo em negrito + valor), padrão do cronograma."""
    data = [[Paragraph(f"<b>{a}</b>", CELL), Paragraph(b, CELL)] for a, b in linhas]
    t = Table(data, colWidths=[c1, c2])
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, base.LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t)


def grid_table(story, cabecalho, linhas, larguras):
    """Tabela com cabeçalho navy + linhas (primeira coluna em negrito)."""
    head = [Paragraph(h, CELL_H) for h in cabecalho]
    data = [head]
    for ln in linhas:
        row = [Paragraph(ln[0], CELL_B)] + [Paragraph(c, CELL) for c in ln[1:]]
        data.append(row)
    t = Table(data, colWidths=larguras, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), base.NAVY),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, base.LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t)


def pending_item(titulo, texto):
    """Caixa com filete laranja à esquerda para cada ponto pendente."""
    t = Table([[Paragraph(titulo, PEND_T)], [Paragraph(texto, PEND_P)]], colWidths=[16 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FBF0E2")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (0, 0), 8),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
        ("TOPPADDING", (0, -1), (-1, -1), 0),
    ]))
    return KeepTogether([t, Spacer(1, 6)])


# ---------------------------------------------------------------- conteúdo
def build(publicacao=True):
    nome = "edital-1o-encontro-gei" if publicacao else "edital-consolidado-1o-encontro-gei"
    out = OUT / f"{nome}.pdf"
    doc = SimpleDocTemplate(
        str(out), pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.6 * cm, bottomMargin=2.6 * cm,
        title="Edital — 1° Encontro GEI",
        author="1° Encontro GEI",
    )
    s = []
    base.build_header(s)
    titulo = ("Edital — Chamada de Trabalhos e Participação" if publicacao
              else "Edital Consolidado — Chamada de Trabalhos e Participação")
    s.append(Paragraph(titulo, base.H_TITLE))
    realizacao = ("Realização: UFF · ABAR · PPGEP - LabDGE/UFF · GIGS/UNICAMP · "
                  "Escola de Regulação (AGETRANSP/AGENERSA) · Instituto de Computação/UFF")
    if publicacao:
        s.append(Paragraph(realizacao, base.H_SUB))
    else:
        s.append(Paragraph(
            "Documento interno para <b>validação prévia</b> — não publicar antes da aprovação · " + realizacao,
            base.H_SUB))
    s.append(base.deadline_box(
        "Submissões abertas até <font color='#9A7D14'>25 de junho de 2026</font> · 23h59 (Brasília) — prazo prorrogado."
        "<br/><font size='9' color='#5C6781'>Resultado da Fase 1 em 27/06 · programa definitivo em 28/06 · evento em 08–10/07/2026.</font>"))
    s.append(Spacer(1, 12))

    # 1. Identificação
    section(s, "1. Identificação do evento")
    para(s, "O <b>1° Encontro de Governança, Estratégia e Inovação Governamental</b> (sigla "
            "<b>GEI</b>) é um evento gratuito, de natureza institucional, acadêmica e científica, "
            "realizado nos dias <b>08, 09 e 10 de julho de 2026</b>, no Rio de Janeiro e em "
            "Niterói/RJ, em <b>formato híbrido</b> (presencial e online, com transmissão ao vivo). "
            "Carga horária de <b>24h certificadas</b>.")
    sub(s, "Realização")
    bullets(s, [
        "<b>UFF</b> — Universidade Federal Fluminense",
        "<b>ABAR</b> — Associação Brasileira de Agências Reguladoras",
        "<b>PPGEP - LabDGE/UFF</b> — Programa de Pós-Graduação em Engenharia de Produção",
        "<b>GIGS/UNICAMP</b> — Grupo de Inovação e Gestão na Saúde",
        "<b>Escola de Regulação</b> — AGETRANSP · AGENERSA · RJ",
        "<b>Instituto de Computação/UFF</b> — Universidade Federal Fluminense",
    ])
    sub(s, "Locais")
    kv_table(s, [
        ("Dia 1 · 08/07", "Auditório do DER/RJ — Av. Presidente Vargas, 1100, 14º andar, Centro, Rio de Janeiro/RJ · CEP 20071-002"),
        ("Dia 2 · 09/07", "8 jornadas técnicas paralelas em campo — Região Metropolitana do Rio de Janeiro"),
        ("Dia 3 · 10/07", "NAB UFF — Campus da Praia Vermelha, Rua Edmundo March, s/n, Niterói/RJ · CEP 24210-310"),
    ])

    # 2. Apresentação e estrutura
    section(s, "2. Apresentação e estrutura")
    para(s, "O Encontro é a primeira plataforma nacional que integra governança pública, "
            "regulação, engenharia de produção e inteligência governamental, reunindo "
            "<b>quatro eventos oficiais</b> em trilhas simultâneas:")
    grid_table(s, ["Trilha", "Evento", "Edição"], [
        ["A", "Lean Six Sigma Congress", "13ª edição"],
        ["B", "Seminário em Sistemas de Engenharia de Produção (SSEP)", "4ª edição"],
        ["C", "Seminário de Regulação", "2ª edição"],
        ["D", "Seminário de Inteligência Governamental", "1ª edição"],
    ], [2.0 * cm, 11.0 * cm, 3.0 * cm])
    s.append(Spacer(1, 6))
    para(s, "<b>Números do evento:</b> 4 eventos integrados · 8 visitas técnicas · 13 eixos "
            "temáticos indexados aos ODS · 24h de carga horária certificada · 500 vagas "
            "presenciais + participação online ilimitada · anais com ISBN e DOI individual por trabalho.")

    # 3. Eixos temáticos
    section(s, "3. Eixos temáticos do evento (13)")
    para(s, "Toda submissão indica um dos eixos abaixo no momento do envio:")
    s.append(base.eixos_box())

    # 4. Participação e inscrições
    section(s, "4. Participação e inscrições")
    para(s, "A participação é <b>gratuita</b>, mediante <b>inscrição prévia obrigatória</b> pela "
            "plataforma Even3. Há três modalidades de participação, com inscrições independentes "
            "que podem ser combinadas:")
    grid_table(s, ["Modalidade", "Abrangência", "Vagas"], [
        ["Presencial — Dias 1 e 3", "Abertura institucional e conferência magna (DER) + trilhas, sessões e encerramento (NAB UFF)", "500 vagas"],
        ["Visita Técnica — Dia 2", "Uma das 8 jornadas paralelas em campo · inscrição independente da presencial", "Por jornada · inscrições em breve"],
        ["Remoto / Online", "Transmissão ao vivo (YouTube) das plenárias e painéis + acesso aos anais", "Ilimitado"],
    ], [4.0 * cm, 9.0 * cm, 3.0 * cm])
    s.append(Spacer(1, 6))
    sub(s, "Certificação")
    para(s, "Certificação emitida por <b>UFF, ABAR, PPGEP - LabDGE/UFF, GIGS/UNICAMP, Escola de "
            "Regulação e Instituto de Computação/UFF</b>, válida para o Currículo Lattes (CNPq) e "
            "como horas complementares. Requer <b>75% de presença</b> registrada via QR Code no "
            "credenciamento. Emissão em até 15 dias úteis após o evento.")
    para(s, "<b>Inscrições:</b> https://www.even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003/")

    # 5. Programação
    section(s, "5. Programação dos três dias")
    sub(s, "Dia 1 · 08/07/2026 (Quarta) — Abertura Institucional · Auditório do DER/RJ")
    kv_table(s, [
        ("13h30", "Credenciamento digital e recepção"),
        ("14h30", "Mesa de abertura institucional"),
        ("15h30", "Painel de apresentação do evento"),
        ("16h30", "Coffee-break"),
        ("17h00", "Conferência Magna de abertura — “Governança, Regulação e Inovação Governamental no Estado contemporâneo”"),
        ("18h00", "Coquetel de networking institucional"),
    ], c1=2.6 * cm, c2=13.4 * cm)
    sub(s, "Dia 2 · 09/07/2026 (Quinta) — 8 Jornadas Técnicas paralelas")
    kv_table(s, [
        ("06h30", "Concentração e distribuição de kits no hub"),
        ("07h00–08h30", "Partidas escalonadas (07h00 · 07h30 · 08h00 · 08h30)"),
        ("09h–17h", "Realização das visitas técnicas"),
        ("Produto", "Relato de Visita Técnica (2–3 pp.) para o livro"),
    ], c1=2.6 * cm, c2=13.4 * cm)
    sub(s, "Dia 3 · 10/07/2026 (Sexta) — Trilhas, Sessões e Encerramento · NAB UFF Niterói")
    kv_table(s, [
        ("09h00", "Plenária + Painel “IA e soberania”"),
        ("10h30", "Trilhas A, B, C e D simultâneas (4 salas) + Painel · Saneamento"),
        ("14h00", "Painel · Energia + Sessões de pôsteres e trabalhos"),
        ("16h30", "Premiação dos trabalhos e encerramento institucional"),
    ], c1=2.6 * cm, c2=13.4 * cm)

    # 6. Submissão de trabalhos
    section(s, "6. Submissão de trabalhos")
    para(s, "A chamada adota um <b>modelo faseado</b>: <b>Fase 1</b> — resumo estendido (2–4 pp.) "
            "+ vídeo de até 10 min; <b>Fase 2</b> — apresentação presencial no Dia 3; <b>artigo "
            "final</b> publicado no livro com ISBN em dezembro/2026. O <b>Artigo Completo</b> pode "
            "ainda ser submetido <b>diretamente</b>, sem resumo prévio. Modalidades:")
    grid_table(s, ["Modalidade", "Extensão", "Envio e prazo", "Observações"], [
        ["Resumo Expandido (Fase 1)", "2–4 pp. · até 700 palavras", ".docx/.pdf + vídeo 10 min · até 25/06", "Parágrafo único · 5 subtítulos · vídeo por link público"],
        ["Artigo (resumo)", "texto · até 700 palavras", "Texto no formulário Even3 · até 25/06", "Modalidade de Fase 1 mantida · resumo digitado no formulário"],
        ["Pôster A3", "A3 visual", ".docx/.pdf · até 25/06", "Mesma estrutura científica do resumo · sessão Dia 3"],
        ["Relatório A3", "1 página A3", ".docx/.pdf · até 25/06", "Modelo DMAIC (D/M/A à esquerda, I/C à direita)"],
        ["Artigo Completo", "8–15 pp. · até 8.000 palavras", ".pdf/.docx (versão cega) · até 30/09", "Submissão direta · ordem de envio · ABNT"],
    ], [3.6 * cm, 3.2 * cm, 4.0 * cm, 5.2 * cm])
    s.append(Spacer(1, 6))
    sub(s, "Normas técnicas gerais (todas as modalidades)")
    bullets(s, [
        "Formato: .docx ou .pdf · fonte <b>Arial 12</b> · espaçamento <b>1,5</b> entrelinhas · margens 2,5 cm",
        "Até <b>4 autores</b> por trabalho",
        "Vídeo (Fase 1): até 10 min, por <b>link público</b> (Google Drive, OneDrive ou YouTube não listado) colado no corpo do documento",
        "Citações e referências em conformidade <b>ABNT</b> (NBR 10520 e NBR 6023)",
        "Regras detalhadas nos <b>PDFs anexos</b> de Resumo Expandido, Pôster, Relatório A3 e Artigo Completo (<i>assets/regras/</i>); o <b>Artigo (resumo)</b> segue as mesmas normas do resumo (até 700 palavras), digitado no formulário da Even3",
    ])
    sub(s, "Como submeter (Even3)")
    bullets(s, [
        "Selecione a modalidade e a área temática (entre os 13 eixos)",
        "Faça upload do documento e cole o link público do vídeo no corpo do texto e no campo “URL do vídeo” do formulário",
        "Confirme e acompanhe o status pela mesma área · login Even3 obrigatório",
    ])

    # 7. Cronograma
    section(s, "7. Cronograma consolidado")
    kv_table(s, [
        ("Fase 1 · Resumo + vídeo", "até 25/06/2026 · 23h59 (Brasília) — prazo prorrogado"),
        ("Resultado da Fase 1", "até 27/06/2026"),
        ("Programa definitivo", "publicado em 28/06/2026"),
        ("Fase 2 · Apresentação presencial", "10/07/2026 · NAB UFF · Niterói"),
        ("Versão final do artigo", "até 30/09/2026"),
        ("Anais com ISBN", "dezembro/2026"),
    ], c1=6.5 * cm, c2=9.5 * cm)

    # 8. Avaliação
    section(s, "8. Avaliação")
    para(s, "A avaliação é conduzida por <b>comissão científica</b> em regime de <b>avaliação por "
            "pares</b>, com dois avaliadores por trabalho. O <b>Artigo Completo</b> é avaliado em "
            "<b>versão cega</b> (autoria informada apenas nos campos do formulário). São critérios "
            "de avaliação a aderência ao eixo temático, a originalidade, o rigor metodológico e a "
            "contribuição teórica/prática. O resultado da Fase 1 é divulgado <b>até 27/06/2026</b>. "
            "A composição da comissão está detalhada na página de organizadores do evento; contato: "
            "<b>comissao.cientifica@encontrogeig.org</b>.")

    # 9. Publicação dos resultados
    section(s, "9. Publicação dos resultados (anais)")
    para(s, "Os trabalhos aprovados comporão o <b>livro de anais com ISBN</b>, a ser publicado em "
            "<b>dezembro de 2026</b>. <b>Cada publicação receberá um DOI individual</b>, além do "
            "ISBN do conjunto. O acesso aos anais está incluído também para os participantes da "
            "modalidade online. Por se tratar de publicação científica, os trabalhos e os dados de "
            "autoria têm retenção permanente (art. 16, II, da LGPD).")

    # 10. Proteção de dados
    section(s, "10. Proteção de dados pessoais (LGPD)")
    para(s, "O Evento atua sob a Lei nº 13.709/2018 (LGPD), tendo como <b>controladoras conjuntas</b> "
            "a <b>AGENERSA</b> (CNPJ 07.694.194/0001-11) e a <b>UFF</b> (CNPJ 28.523.215/0001-06, por "
            "meio do PPGEP/UFF). A plataforma <b>Even3</b> atua como operadora (art. 39); a transmissão "
            "e as gravações são hospedadas pelo <b>YouTube/Google</b>. O titular pode exercer os "
            "direitos do art. 18 da LGPD. <b>Encarregado (DPO):</b> Prof. Alexandre Beraldi Santos "
            "(PPGEP/UFF) — <b>alexandreberaldisantos@id.uff.br</b>. A política completa está em "
            "<b>encontrogeig.org/privacidade</b>.")

    # 11. Contato
    section(s, "11. Contato")
    bullets(s, [
        "Secretaria do Encontro: <b>contato@encontrogeig.org</b>",
        "Submissões: <b>submissoes@encontrogeig.org</b>",
        "Comissão científica: <b>comissao.cientifica@encontrogeig.org</b>",
        "Inscrições (Even3): <i>even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003/</i>",
        "Site oficial: <b>encontrogeig.org</b> · Autoridade Nacional de Proteção de Dados (ANPD): gov.br/anpd",
    ])

    # 12. Apêndice — pontos pendentes (apenas na versão de validação)
    if not publicacao:
        section(s, "12. Apêndice — Pontos pendentes de validação")
        para(s, "Itens que dependem de decisão ou confirmação da organização <b>antes da publicação</b> "
                "deste edital. O corpo acima reflete o estado atual do site (encontrogeig.org).")
        pend = [
            ("Escola de Regulação (AGETRANSP/AGENERSA) — papel",
             "Confirmar: (a) é <b>co-emissora</b> da certificação? (b) <b>recebe dados pessoais</b> (cláusula "
             "LGPD)? (c) incluir crédito no <b>rodapé dos PDFs</b> de regras? Hoje consta como 5ª realizadora "
             "e na linha de certificação do site."),
            ("Conferência Magna — confirmação",
             "Palestra magna atribuída a <b>Magda Chambriard (Petrobras)</b> consta como “a confirmar”; "
             "confirmar palestrante e composição do painel."),
            ("Dia 2 — visitas técnicas",
             "Empresas/jornadas e hub de concentração ainda “a confirmar” no site; a entrada “Visita Técnica” "
             "na Even3 ainda não foi aberta (consta “inscrições em breve”)."),
            ("Modalidade legada “Artigo (resumo)” na Even3",
             "Contradição entre o limite de <b>700 palavras</b> (formulário) e <b>8.000 palavras</b> (PDF); a "
             "modalidade será <b>ocultada em 25/06</b> ao encerrar a Fase 1. Decidir se este edital menciona o "
             "tema ou se ele fica restrito ao operacional."),
            ("Validação jurídica da Política de Privacidade",
             "Acordo entre as controladoras conjuntas (AGENERSA e UFF) e a lista nominal de acessos ainda "
             "pendentes de validação jurídica."),
        ]
        for titulo, texto in pend:
            s.append(pending_item(titulo, texto))

    s.append(Spacer(1, 8))
    if publicacao:
        para(s, "<font size='8' color='#5C6781'>1° Encontro de Governança, Estratégia e Inovação "
                "Governamental · encontrogeig.org · contato@encontrogeig.org · junho de 2026.</font>")
    else:
        hoje = date.today()
        para(s, f"<font size='8' color='#5C6781'>Documento gerado em {hoje.day:02d}/{hoje.month:02d}/{hoje.year} "
                "a partir do conteúdo do site (encontrogeig.org) e da documentação interna do projeto · "
                "versão para validação.</font>")

    doc.build(s, onFirstPage=base.header_footer, onLaterPages=base.header_footer)
    print(f"OK {out.relative_to(ROOT)}: {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    build()
