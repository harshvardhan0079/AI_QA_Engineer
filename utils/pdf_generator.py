from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path
from datetime import datetime


def generate_pdf_report(filename: str, analysis: dict):
    Path("reports").mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = f"reports/report_{timestamp}.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI QA Engineer Report</b>", styles["Title"]))
    story.append(Paragraph(f"<b>File:</b> {filename}", styles["Normal"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            f"<b>Quality Score:</b> {analysis.get('quality_score', 'N/A')}",
            styles["Normal"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Security:</b> {analysis.get('security', 'N/A')}",
            styles["Normal"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Performance:</b> {analysis.get('performance', 'N/A')}",
            styles["Normal"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Readability:</b> {analysis.get('readability', 'N/A')}",
            styles["Normal"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Maintainability:</b> {analysis.get('maintainability', 'N/A')}",
            styles["Normal"],
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            f"<b>Summary:</b><br/>{analysis.get('summary', 'No summary')}",
            styles["BodyText"],
        )
    )

    doc.build(story)

    return pdf_path