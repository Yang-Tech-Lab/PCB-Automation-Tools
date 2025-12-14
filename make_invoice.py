from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from datetime import datetime

def create_professional_invoice(filename):
    # 1. Setup Canvas (A4 Size)
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # --- Header: Branding Area ---
    # Simulate a Logo area (Replace with actual image path later)
    c.setFillColor(colors.HexColor("#1dbf73")) # Fiverr Green Style
    c.rect(0, height - 120, width, 120, fill=1, stroke=0)
    
    # Company Name (Large Font)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(50, height - 80, "Yang-Tech-Lab")
    
    # Slogan (Professional Tagline)
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 105, "Professional PCB Design & IoT Firmware Solutions")

    # --- Top Right: Invoice Details ---
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 14)
    c.drawRightString(width - 50, height - 60, "INVOICE")
    
    c.setFont("Helvetica", 10)
    today = datetime.now().strftime("%Y-%m-%d")
    c.drawRightString(width - 50, height - 80, f"Date: {today}")
    c.drawRightString(width - 50, height - 95, "Invoice #: YTL-2025-001")

    # --- Client Information ---
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, "Bill To:")
    
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 180, "Client Name: John Doe (Global IoT Corp)")
    c.drawString(50, height - 195, "Project: ESP32-S3 Smart Controller v1.0")

    # --- Core: Cost Breakdown Table ---
    # Detailed breakdown to increase perceived value of the service
    data = [
        ['DESCRIPTION', 'DETAILS', 'AMOUNT ($)'],
        ['Schematic Design', 'Power Tree, ESD Protection, Connectivity', '15.00'],
        ['PCB Layout', '4-Layer Stackup, Impedance Control (90 ohm)', '25.00'],
        ['DFM Analysis', 'Manufacturing Feasibility Check', '10.00'],
        ['Firmware Setup', 'ESP-IDF Environment & Basic Bootloader', '0.00 (Bonus)'],
        ['', '', ''], # Empty row for spacing
        ['', 'TOTAL', '50.00']
    ]

    # Create Table Object
    table = Table(data, colWidths=[150, 250, 80])
    
    # Define Table Style (Professional Look)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f2f2f2")), # Grey header
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'), # Align numbers to the right
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey), # Light grey grid lines
        # Highlight the Total row
        ('FONTNAME', (1, -1), (-1, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (1, -1), (-1, -1), colors.HexColor("#1dbf73")),
        ('SIZE', (1, -1), (-1, -1), 12),
    ])
    table.setStyle(style)
    
    # Draw table on canvas
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, height - 400)

    # --- Footer: Professional Terms & Notes ---
    # Disclaimer and technical notes to show expertise
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, 150, "Technical Notes:")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.darkgrey)
    note_y = 135
    notes = [
        "1. Impedance control is calculated based on JLC04161H-3313 stackup.",
        "2. All design files (Gerber, BOM, CPL) are included in the delivery package.",
        "3. Payment is due upon receipt of this invoice.",
        "4. Thank you for your business!"
    ]
    for note in notes:
        c.drawString(50, note_y, note)
        note_y -= 12

    # --- Finalize and Save PDF ---
    c.save()
    print(f"✅ Success! Professional invoice generated: {filename}")

if __name__ == "__main__":
    create_professional_invoice("Yang_Tech_Invoice_001.pdf")