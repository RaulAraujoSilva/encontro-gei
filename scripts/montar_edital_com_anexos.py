"""Monta um único PDF: Edital de publicação + as normas de submissão como anexos.

Regenera o edital (gerar_edital_consolidado) e os 4 PDFs de regras
(gerar_regras_pdf), cria uma página divisória "Anexos" no mesmo layout e
funde tudo em um arquivo só, com marcadores (bookmarks) de navegação.

Uso: python scripts/montar_edital_com_anexos.py
Saída: docs/edital/edital-1o-encontro-gei-com-anexos.pdf
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gerar_regras_pdf as base          # noqa: E402  (cores, estilos, header/footer, build_header)
import gerar_edital_consolidado as edital  # noqa: E402

from reportlab.lib.pagesizes import A4   # noqa: E402
from reportlab.lib.units import cm       # noqa: E402
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer  # noqa: E402
from pypdf import PdfWriter              # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EDITAL = ROOT / "docs" / "edital" / "edital-1o-encontro-gei.pdf"
REGRAS = ROOT / "assets" / "regras"
OUT = ROOT / "docs" / "edital" / "edital-1o-encontro-gei-com-anexos.pdf"
CAPA = ROOT / "docs" / "edital" / "_anexos-capa.pdf"  # temporária

# Anexos, na ordem (rótulo + arquivo). "Artigo (resumo)" segue as normas do resumo (Anexo I).
ANEXOS = [
    ("Anexo I — Resumo Expandido (Fase 1)", REGRAS / "resumo-expandido.pdf"),
    ("Anexo II — Pôster A3", REGRAS / "poster.pdf"),
    ("Anexo III — Relatório A3 (modelo DMAIC)", REGRAS / "relatorio-a3.pdf"),
    ("Anexo IV — Artigo Completo", REGRAS / "artigo-completo.pdf"),
]


def gerar_capa_anexos():
    doc = SimpleDocTemplate(
        str(CAPA), pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.6 * cm, bottomMargin=2.6 * cm,
        title="Anexos — Normas de Submissão · 1° Encontro GEI",
        author="1° Encontro GEI",
    )
    s = []
    base.build_header(s)
    s.append(Paragraph("Anexos — Normas de Submissão por Modalidade", base.H_TITLE))
    s.append(Paragraph("Parte integrante do Edital — Chamada de Trabalhos e Participação", base.H_SUB))
    s.append(base.deadline_box(
        "As normas técnicas completas de cada modalidade integram este edital como "
        "<b>anexos</b>, nas páginas seguintes."))
    s.append(Spacer(1, 14))
    s.append(Paragraph("Relação de anexos", base.H1))
    for titulo, _ in ANEXOS:
        s.append(Paragraph("• " + titulo, base.LI))
    s.append(Spacer(1, 8))
    s.append(Paragraph(
        "A modalidade <b>Artigo (resumo)</b> — resumo de até 700 palavras digitado no "
        "formulário da Even3 — segue as normas do <b>Resumo Expandido (Anexo I)</b>.", base.P))
    doc.build(s, onFirstPage=base.header_footer, onLaterPages=base.header_footer)


def _regenerar():
    """Regenera as peças-fonte (best-effort: tolera arquivo aberto/bloqueado)."""
    for rotulo, fn in (("PDFs de regras", base.main),
                       ("edital", lambda: edital.build(publicacao=True))):
        try:
            fn()
        except PermissionError:
            print(f"AVISO: {rotulo} em uso (arquivo aberto?) — usando a versão já em disco.")


def main():
    # 1) Regenera as peças-fonte para garantir consistência (best-effort)
    _regenerar()
    gerar_capa_anexos()

    # 2) Funde tudo num único arquivo, com marcadores de navegação
    writer = PdfWriter()
    writer.append(str(EDITAL), outline_item="Edital — Chamada de Trabalhos e Participação")
    writer.append(str(CAPA), outline_item="Anexos — Normas de Submissão")
    for titulo, caminho in ANEXOS:
        writer.append(str(caminho), outline_item=titulo)
    with open(OUT, "wb") as f:
        writer.write(f)
    writer.close()

    CAPA.unlink(missing_ok=True)  # remove a capa temporária
    n = len(writer.pages)
    print(f"OK {OUT.relative_to(ROOT)}: {OUT.stat().st_size // 1024} KB · {n} páginas")


if __name__ == "__main__":
    main()
