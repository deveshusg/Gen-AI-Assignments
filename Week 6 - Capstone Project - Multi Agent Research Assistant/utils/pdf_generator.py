from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    report_text,
    sources
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Multi-Agent Research Assistant Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    report_text = report_text.replace(
        "\n",
        "<br/>"
    )

    elements.append(
        Paragraph(
            report_text,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Sources",
            styles["Heading2"]
        )
    )

    for source in sources:

        elements.append(
            Paragraph(
                f"""
                <a href="{source['url']}">
                {source['title']}
                </a>
                """,
                styles["BodyText"]
            )
        )

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf