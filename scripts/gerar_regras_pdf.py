"""Gera 4 PDFs de regras de submissão para o 1° Encontro GEI.
Uso: python scripts/gerar_regras_pdf.py
Saída: assets/regras/{resumo-expandido,poster,relatorio-a3,artigo-completo}.pdf
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak,
    KeepTogether
)
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "logo-completo.png"
OUT = ROOT / "assets" / "regras"
OUT.mkdir(parents=True, exist_ok=True)

# Cores oficiais do evento
NAVY = HexColor("#091136")
NAVY2 = HexColor("#142469")
YELLOW = HexColor("#F5C842")
GREEN = HexColor("#7AC74F")
BLUE = HexColor("#4DA8E0")
CYAN = HexColor("#5BC6E5")
MUTED = HexColor("#5C6781")
LINE = HexColor("#D8DDE9")

# === Estilos ===
styles = getSampleStyleSheet()
H_TITLE = ParagraphStyle("HTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=20, leading=24, textColor=NAVY, alignment=TA_CENTER, spaceBefore=8, spaceAfter=4)
H_SUB = ParagraphStyle("HSub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10.5, leading=14, textColor=MUTED, alignment=TA_CENTER, spaceAfter=14)
H_EVENT = ParagraphStyle("HEvent", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=9, leading=12, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2)
H_DATE = ParagraphStyle("HDate", parent=styles["Normal"], fontName="Helvetica",
    fontSize=8.5, leading=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=18)
H1 = ParagraphStyle("H1", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=13, leading=18, textColor=NAVY, spaceBefore=14, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=styles["Heading3"], fontName="Helvetica-Bold",
    fontSize=11, leading=15, textColor=NAVY2, spaceBefore=10, spaceAfter=4)
P = ParagraphStyle("P", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=14, textColor=HexColor("#1A2238"), alignment=TA_JUSTIFY, spaceAfter=6)
LI = ParagraphStyle("LI", parent=P, leftIndent=14, bulletIndent=2, spaceAfter=3)
DEADLINE = ParagraphStyle("DL", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=11, leading=14, textColor=NAVY, alignment=TA_CENTER)
FOOTER = ParagraphStyle("Footer", parent=styles["Normal"], fontName="Helvetica",
    fontSize=8, leading=11, textColor=MUTED, alignment=TA_CENTER)


def header_footer(canv: canvas.Canvas, doc):
    canv.saveState()
    # Footer
    w, _ = A4
    canv.setFillColor(NAVY)
    canv.rect(0, 0, w, 18*mm, fill=1, stroke=0)
    canv.setFont("Helvetica", 8)
    canv.setFillColorRGB(1, 1, 1)
    canv.drawCentredString(w/2, 11*mm,
        "1° Encontro de Governança, Estratégia e Inovação Governamental · 08-10/07/2026")
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(HexColor("#A5B0C8"))
    canv.drawCentredString(w/2, 6*mm,
        "encontro-gei.vercel.app · contato@encontrogei.com.br · UFF · ABAR · PPGEP/UFF · Escola de Regulação")
    canv.setFont("Helvetica", 7.5)
    canv.drawString(15*mm, 6*mm, f"Pág. {doc.page}")
    canv.restoreState()


EIXOS = [
    "Regulação de infraestrutura, energia e saneamento",
    "Sandbox regulatório e inovação institucional",
    "Gestão pública inovadora e GovTech",
    "Lean Six Sigma e excelência operacional",
    "Sustentabilidade e ESG em organizações reguladas",
    "Inteligência governamental e apoio à decisão",
    "Governança de dados e interoperabilidade",
    "Transformação digital e serviços públicos",
    "Capacidade analítica e uso de evidências",
    "Saúde digital e dados conectados",
    "Inteligência artificial e soberania nacional",
    "Trabalho, ergonomia e segurança",
    "Pesquisa operacional, otimização e logística",
]


def deadline_box(text):
    """Caixa amarela com destaque do prazo."""
    t = Table([[Paragraph(text, DEADLINE)]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#FEF7DA")),
        ("BOX", (0,0), (-1,-1), 1.2, YELLOW),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 12),
        ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    return t


def eixos_box():
    cells = [[Paragraph(f"<b>{i+1}.</b> {e}", ParagraphStyle('eb', parent=P, fontSize=9, leading=12, spaceAfter=0))]
             for i, e in enumerate(EIXOS)]
    # 2 colunas
    cols = [[c[0] for c in cells[i::2]] for i in range(2)]
    rows = list(zip(*cols)) if len(cols[0]) == len(cols[1]) else None
    if rows is None:
        # 7 + 6
        data = [[cells[i][0] if i < len(cells) else '', cells[i+7][0] if i+7 < len(cells) else ''] for i in range(7)]
    else:
        data = [list(r) for r in rows]
    t = Table(data, colWidths=[8*cm, 8*cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t


def build_header(story):
    """Header reutilizável: logo + nome do evento."""
    if LOGO.exists():
        img = Image(str(LOGO), width=14*cm, height=14*cm * 354/1266)
        img.hAlign = "CENTER"
        story.append(img)
    story.append(Spacer(1, 6))
    story.append(Paragraph("1° Encontro de Governança, Estratégia e Inovação Governamental", H_EVENT))
    story.append(Paragraph("08, 09 e 10 de julho de 2026 · Rio de Janeiro / Niterói · RJ", H_DATE))


def gerar_pdf(slug, titulo, intro, especificas, prazo_extra=""):
    out = OUT / f"{slug}.pdf"
    doc = SimpleDocTemplate(
        str(out), pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.6*cm, bottomMargin=2.6*cm,
        title=f"Normas de Submissão — {titulo}",
        author="1° Encontro GEI"
    )
    story = []
    build_header(story)
    story.append(Paragraph(f"Normas de Submissão — {titulo}", H_TITLE))
    story.append(Paragraph("Chamada de trabalhos · Realização: UFF · ABAR · PPGEP/UFF · Escola de Regulação", H_SUB))
    story.append(deadline_box(
        f"Prazo Fase 1 — Resumo + Vídeo · até <font color='#9A7D14'>15 de maio de 2026</font> · 23h59 (Brasília)"
        + (f"<br/><font size='9' color='#5C6781'>{prazo_extra}</font>" if prazo_extra else "")
    ))
    story.append(Spacer(1, 12))

    if intro:
        story.append(Paragraph("Apresentação", H1))
        for par in intro:
            story.append(Paragraph(par, P))

    story.append(Paragraph("Especificações da modalidade", H1))
    for sec in especificas:
        if sec.get("h"):
            story.append(Paragraph(sec["h"], H2))
        for item in sec.get("items", []):
            story.append(Paragraph("• " + item, LI))
        if sec.get("p"):
            story.append(Paragraph(sec["p"], P))

    story.append(Paragraph("Eixos temáticos do evento (13)", H1))
    story.append(Paragraph("Selecione um dos eixos abaixo no momento da submissão:", P))
    story.append(eixos_box())

    story.append(Paragraph("Cronograma da chamada de trabalhos", H1))
    cron = [
        ("Fase 1 · Resumo + vídeo", "até 15/05/2026 · 23h59 (Brasília)"),
        ("Resultado da Fase 1", "até 31/05/2026"),
        ("Programa definitivo", "publicado em 25/06/2026"),
        ("Fase 2 · Apresentação presencial", "10/07/2026 · NAB UFF · Niterói"),
        ("Versão final do artigo", "até 30/09/2026"),
        ("Anais com ISBN", "dezembro/2026"),
    ]
    cron_data = [[Paragraph(f"<b>{a}</b>", P), Paragraph(b, P)] for a, b in cron]
    tcron = Table(cron_data, colWidths=[7*cm, 9*cm])
    tcron.setStyle(TableStyle([
        ("LINEBELOW", (0,0), (-1,-1), 0.5, LINE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    story.append(tcron)

    story.append(Paragraph("Comissão científica", H1))
    story.append(Paragraph(
        "Membros da Comissão Científica do 4º Seminário em Sistemas de Engenharia de Produção (SSEP/UFF): "
        "Ana, Flavia, Gabriella, Jucileia, Kelly, Pompilio e Silvia Cristina Rufino. "
        "Avaliação científica conduzida em conjunto pelas instituições realizadoras.", P))

    story.append(Paragraph("Submissão e contato", H1))
    story.append(Paragraph(
        "Submeta seu trabalho diretamente pela plataforma Even3 do evento: "
        "<b>https://www.even3.com.br/1-encontro-de-governanca-estrategia-e-inovacao-governamental-722003/</b>. "
        "Dúvidas: contato@encontrogei.com.br.", P))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"OK {out.name}: {out.stat().st_size//1024} KB")


def main():
    # === RESUMO EXPANDIDO ===
    gerar_pdf(
        "resumo-expandido",
        "Resumo Expandido (Fase 1)",
        intro=[
            "O Resumo Expandido é a peça obrigatória da Fase 1 da chamada de trabalhos do 1° Encontro de Governança, Estratégia e Inovação Governamental, acompanhado de um vídeo de até 5 minutos contendo apresentação síntese da pesquisa.",
            "Os trabalhos aprovados nesta fase serão convidados para apresentação presencial no Dia 3 (10 de julho de 2026, NAB UFF, Niterói) e poderão evoluir para artigo completo a ser publicado no livro com ISBN do evento (Fase 2)."
        ],
        especificas=[
            {"h": "Formato do arquivo", "items": [
                ".docx ou .pdf, página A4",
                "Submissão pela plataforma Even3 do evento (link no rodapé)"
            ]},
            {"h": "Estrutura visual", "items": [
                "Título: caixa alta, fonte <b>Arial 12</b>, negrito, alinhamento centralizado",
                "Autores: até 6, alinhados à esquerda, Arial 12",
                "Instituição: nome completo de cada autor, Arial 12",
                "Margens: superior e inferior 3 cm; esquerda e direita 2 cm",
                "Espaçamento simples entre linhas, texto justificado, sem recuo de parágrafo no início"
            ]},
            {"h": "Corpo do texto", "items": [
                "Parágrafo único de no máximo <b>700 palavras</b> (excluindo referências)",
                "Subtítulos em sequência: Introdução · Objetivo · Metodologia · Discussão com Resultados · Considerações Finais",
                "Palavras-chave: 3 a 5 termos, separados por ponto e vírgula, ao final"
            ]},
            {"h": "Referências e citações", "items": [
                "Conformidade <b>ABNT</b> (NBR 10520 e NBR 6023)",
                "Listadas ao final, fonte Arial 10"
            ]},
            {"h": "Vídeo de apresentação", "items": [
                "Duração máxima: 5 minutos",
                "Hospedado em YouTube/Vimeo (link público ou não-listado)",
                "URL informada no formulário Even3 no momento da submissão"
            ]}
        ]
    )

    # === PÔSTER A3 ===
    gerar_pdf(
        "poster",
        "Pôster A3",
        intro=[
            "O formato Pôster destina-se a trabalhos em estágio inicial de pesquisa, estudos exploratórios ou apresentação visual de resultados parciais. Será apresentado no Dia 3 do evento em sessão dedicada.",
            "O modelo segue a mesma estrutura científica do Resumo Expandido, porém com diagramação visual em formato A3."
        ],
        especificas=[
            {"h": "Formato do arquivo", "items": [
                "Documento A3 retrato ou paisagem (.docx ou .pdf)",
                "Submissão pela plataforma Even3 do evento"
            ]},
            {"h": "Estrutura visual", "items": [
                "Título: Arial 12, centralizado, negrito, caixa alta, espaçamento simples",
                "Autores e instituições: nome completo, e-mails e instituições, Arial 12",
                "Texto justificado, sem recuo de parágrafo"
            ]},
            {"h": "Conteúdo", "items": [
                "Introdução: contextualize a pesquisa e apresente os objetivos · Arial 12, máx. 700 palavras",
                "Metodologia: descreva métodos e procedimentos utilizados",
                "Discussão com Resultados: fundamentação teórica + resultados; figuras e tabelas devem ser numeradas e tituladas",
                "Conclusão: limitações e sugestões para trabalhos futuros",
                "Referências: ABNT (NBR 10520 e NBR 6023)"
            ]},
            {"h": "Apresentação presencial (Dia 3)", "items": [
                "Sessão dedicada para pôsteres no NAB UFF, Niterói",
                "O autor deverá levar a versão impressa em formato A3 para fixação"
            ]}
        ]
    )

    # === RELATÓRIO A3 ===
    gerar_pdf(
        "relatorio-a3",
        "Relatório A3 (modelo DMAIC)",
        intro=[
            "O Relatório A3 é a modalidade dedicada a trabalhos aplicados que propõem melhorias em processos ou produtos no setor público regulado. É uma ferramenta enxuta para identificar problemas e propor soluções de forma resumida em uma única página A3.",
            "O documento deve seguir o modelo <b>DMAIC</b> (Define, Measure, Analyze, Improve, Control), preservando a lateralidade prescrita."
        ],
        especificas=[
            {"h": "Formato do arquivo", "items": [
                "Documento A3 paisagem (.docx ou .pdf)",
                "Limite: <b>1 página única</b>, incluindo figuras, gráficos e tabelas",
                "Submissão pela plataforma Even3 do evento"
            ]},
            {"h": "Estrutura DMAIC obrigatória", "items": [
                "<b>Coluna esquerda</b> (estado pré-projeto): Definir · Medir · Analisar",
                "<b>Coluna direita</b> (pós-implementação): Implementar · Controlar",
                "O tamanho de cada tópico pode ser ajustado conforme necessidade, porém a lateralidade deve ser respeitada"
            ]},
            {"h": "Formatação visual", "items": [
                "Título: Arial 12, caixa alta, negrito, centralizado",
                "Subtítulos das fases DMAIC: Arial 12, negrito, alinhados à esquerda da coluna",
                "Texto: Arial 10, espaçamento simples, justificado",
                "Figuras/gráficos: legendas em Arial 9, numeradas sequencialmente"
            ]},
            {"h": "Apresentação presencial (Dia 3)", "items": [
                "Sessão dedicada a Relatórios A3 com discussão com a comissão científica",
                "Autor leva impressão A3 para a sessão"
            ]}
        ]
    )

    # === ARTIGO COMPLETO ===
    gerar_pdf(
        "artigo-completo",
        "Artigo Completo (Fase 2)",
        intro=[
            "O Artigo Completo é a forma de submissão da Fase 2 da chamada de trabalhos, destinada aos trabalhos aprovados na Fase 1 (Resumo Expandido + Vídeo). Os artigos completos comporão o livro de anais com ISBN, a ser publicado em dezembro de 2026.",
            "Submissão pela plataforma Even3 em <b>dois arquivos</b>: um com identificação de autoria e outro sem identificação (para avaliação cega)."
        ],
        especificas=[
            {"h": "Arquivos a submeter", "items": [
                "<b>Arquivo 1:</b> versão completa com nomes, e-mails e instituições dos autores",
                "<b>Arquivo 2:</b> versão sem identificação — não deve conter nomes, e-mails ou instituições, nem mesmo nas propriedades do arquivo (autor, último editor, etc.)",
                "Formatos aceitos: <b>.docx</b> ou <b>.pdf</b>"
            ]},
            {"h": "Estrutura do artigo", "items": [
                "Título: em português e inglês, até 120 caracteres, Arial 12, centralizado, negrito, caixa alta",
                "Resumo: até 150 palavras, em português e inglês, Arial 10, espaçamento simples",
                "Palavras-chave: 3 a 5, separadas por ponto e vírgula, Arial 10",
                "Corpo do texto: Arial 12, espaçamento 1,5, justificado, sem espaço entre parágrafos, recuo de 1,25 cm",
                "Margens: superior e inferior 3 cm, esquerda e direita 2 cm"
            ]},
            {"h": "Títulos e seções", "items": [
                "Títulos de seções: Arial 12, negrito, caixa alta, alinhados à esquerda, espaçamento 1,5, com 6 pt depois",
                "Subseções: Arial 12, negrito, caixa baixa, alinhados à esquerda, espaçamento 1,5, com 6 pt depois"
            ]},
            {"h": "Limites e referências", "items": [
                "Limite máximo: <b>8.000 palavras</b> (excluindo referências e anexos)",
                "Referências em conformidade <b>ABNT</b> (NBR 10520 e NBR 6023)",
                "Citações no corpo do texto: sistema autor-data"
            ]},
            {"h": "Avaliação", "items": [
                "Dupla avaliação cega pela comissão científica do 4º SSEP",
                "Critérios: aderência ao eixo temático, originalidade, rigor metodológico, contribuição teórica/prática"
            ]}
        ],
        prazo_extra="Submissão da versão final do Artigo Completo: até 30/09/2026"
    )


if __name__ == "__main__":
    main()
