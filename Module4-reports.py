#! usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("/tmp/processed.pdf")
styles = getSampleStyleSheet()

def generate_report(attachment, title, paragraph):
    report_title = Paragraph(title, styles["h1"])
    report_body = 

    report.build([report_title])
