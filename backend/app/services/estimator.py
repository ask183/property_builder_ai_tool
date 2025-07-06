from fpdf import FPDF
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def estimate_project(input):
    total = input.land_cost + input.permit_cost + input.construction_cost
    profit = input.sale_price - total
    timeline = 12  # basic default
    return {
        "total_cost": total,
        "profit": profit,
        "timeline_months": timeline
    }

def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for k, v in data.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
    pdf_path = "/tmp/report.pdf"
    pdf.output(pdf_path)
    return pdf_path

def send_email_with_pdf(email, pdf_path):
    message = Mail(
        from_email='you@example.com',
        to_emails=email,
        subject='Your Property Builder Report',
        html_content='<strong>Attached is your report</strong>'
    )
    with open(pdf_path, 'rb') as f:
        message.add_attachment(f.read(), 'application/pdf', 'report.pdf', 'attachment')
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    sg.send(message)