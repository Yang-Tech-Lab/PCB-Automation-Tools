"""
InvoiceSynthesis Pro: Enterprise Document Orchestration Engine
--------------------------------------------------------------
A high-fidelity document generation suite designed for automated 
fiscal reporting and professional technical service verification.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Automation / Fintech
Date: March 24, 2026
"""

import logging
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Final, Optional

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

@dataclass
class ServiceItem:
    description: str
    details: str
    rate: float
    quantity: int = 1
    
    @property
    def subtotal(self) -> float:
        return self.rate * self.quantity

class InvoiceOrchestrator:
    def __init__(self, invoice_id: str, client_name: str, project_name: str):
        self.invoice_id: Final[str] = invoice_id
        self.client_name: Final[str] = client_name
        self.project_name: Final[str] = project_name
        self.provider_id: Final[str] = "Yang Jiacheng (Yang-Tech-Lab)"
        
        # Professional Color Palette (2026 Industrial Aesthetic)
        self.primary_color = colors.HexColor("#1B2631")  # Deep Charcoal Navy
        self.accent_color = colors.HexColor("#27AE60")   # Professional Emerald
        
        self.vault_path = Path("Vault/Invoices")
        self.vault_path.mkdir(parents=True, exist_ok=True)

    def _get_styles(self):
        """Standardizes typography for the document lifecycle."""
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='EnterpriseHeader',
            fontSize=24,
            textColor=self.primary_color,
            spaceAfter=20,
            fontName='Helvetica-Bold'
        ))
        styles.add(ParagraphStyle(
            name='TechnicalNote',
            fontSize=8,
            textColor=colors.grey,
            leading=10
        ))
        return styles

    def synthesize(self, items: List[ServiceItem]):
        """Orchestrates the synthesis of a structured PDF asset."""
        target_file = self.vault_path / f"INV_{self.invoice_id}_{self.client_name.replace(' ', '_')}.pdf"
        doc = SimpleDocTemplate(str(target_file), pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
        
        styles = self._get_styles()
        story = []

        # --- Phase 1: Header & Branding ---
        story.append(Paragraph("TAX INVOICE", styles['EnterpriseHeader']))
        
        # Meta Info Table (Provider vs Client)
        meta_data = [
            [Paragraph(f"<b>FROM:</b><br/>{self.provider_id}<br/>Applied Electronic Tech Specialist", styles['Normal']),
             Paragraph(f"<b>BILL TO:</b><br/>{self.client_name}<br/>Project: {self.project_name}", styles['Normal'])]
        ]
        meta_table = Table(meta_data, colWidths=[3*inch, 3*inch])
        story.append(meta_table)
        story.append(Spacer(1, 0.4 * inch))

        # --- Phase 2: Transaction Metadata ---
        story.append(Paragraph(f"Invoice ID: <b>{self.invoice_id}</b>", styles['Normal']))
        story.append(Paragraph(f"Date of Issue: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

        # --- Phase 3: Financial Table Logic ---
        table_data = [['DESCRIPTION', 'TECHNICAL DETAILS', 'QTY', 'RATE (USD)', 'SUBTOTAL']]
        total_accrued = 0.0
        
        for item in items:
            table_data.append([
                item.description,
                item.details,
                str(item.quantity),
                f"${item.rate:,.2f}",
                f"${item.subtotal:,.2f}"
            ])
            total_accrued += item.subtotal

        # Footer Row
        table_data.append(['', '', '', 'TOTAL PAYABLE', f"${total_accrued:,.2f}"])

        # Table Styling Orchestration
        # 
        t = Table(table_data, colWidths=[1.5*inch, 2.5*inch, 0.5*inch, 1.2*inch, 1.3*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), self.primary_color),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 1), (1, -2), 'LEFT'), # Descriptions left-aligned
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor("#F8F9F9")),
            ('GRID', (0, 0), (-1, -2), 0.5, colors.lightgrey),
            # Total Row Styling
            ('FONTNAME', (-2, -1), (-1, -1), 'Helvetica-Bold'),
            ('TEXTCOLOR', (-2, -1), (-1, -1), self.accent_color),
            ('FONTSIZE', (-2, -1), (-1, -1), 12),
            ('LINEABOVE', (-2, -1), (-1, -1), 1, self.primary_color),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.5 * inch))

        # --- Phase 4: Technical Appendix & Terms ---
        story.append(Paragraph("<b>TECHNICAL SPECIFICATIONS & TERMS:</b>", styles['Normal']))
        notes = [
            "1. Impedance Control: Verified against JLC04161H-3313 stackup standards.",
            "2. Deliverables: Includes Gerber X2, IPC-D-356 netlist, and Pick-and-Place (CPL) files.",
            "3. Firmware: Pre-configured for ESP-IDF v5.2 environment.",
            "4. Jurisdiction: All disputes are governed by the laws of Guangzhou, PRC."
        ]
        for note in notes:
            story.append(Paragraph(note, styles['TechnicalNote']))

        # Build Final Asset
        try:
            doc.build(story)
            logging.info(f"✅ Success! Strategic invoice persisted at: {target_file.resolve()}")
        except Exception as e:
            logging.error(f"❌ Synthesis Failure: {e}")

if __name__ == "__main__":
    # Deployment in High-Value Node
    orchestrator = InvoiceOrchestrator(
        invoice_id="YTL-2026-0324",
        client_name="Global Robotics Inc.",
        project_name="High-Speed STM32 Motion Controller"
    )

    # Line Item Acquisition
    service_payload = [
        ServiceItem("PCB Layout Design", "6-Layer, Blind/Buried Vias, DDR3 Routing", 35.00),
        ServiceItem("BOM Optimization", "Supply chain resilience check & Alternative sourcing", 10.00),
        ServiceItem("Firmware Porting", "Real-time FreeRTOS task scheduling implementation", 15.00)
    ]

    print("\n--- Yang-Tech-Lab: Document Orchestration Active ---")
    orchestrator.synthesize(service_payload)
