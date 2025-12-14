# PCB-Automation-Tools
Python scripts for automating PCB quotations (PDF generation) and market price analysis.
# PCB Automation Tools 🐍

**Efficiency scripts for Freelance Hardware Engineers.**

This repository contains the Python toolchain I use at **Yang-Tech-Lab** to automate the non-engineering parts of my workflow.

## 🛠️ Tools Included

### 1. Auto-Quotation Generator (`make_invoice.py`)
- **What it does:** Generates professional PDF invoices/quotations instantly using the `reportlab` library.
- **Features:**
  - Auto-calculates totals including technical add-ons (Impedance Control, DFM).
  - Embeds technical notes and banking details.
  - **Result:** Turns a $50 service into a premium deliverable.

### 2. Market Price Analyzer (`analyze_price.py`)
- **What it does:** Visualizes competitor pricing data using `matplotlib` and `pandas`.
- **Use Case:** Helping freelancers find the "Blue Ocean" pricing strategy in crowded markets (e.g., Fiverr).

## 🚀 How to Run
```bash
# Install dependencies
pip install reportlab pandas matplotlib

👨‍💻 Hire the Developer
I don't just design PCBs; I build systems to design them faster.

### 🚧 Status
**Commercial Services Launching: Spring 2026**

Yang-Tech-Lab is currently in active development. 
- ⭐️ **Star this repo** to get notified when we launch.
- 📧 **Contact:** (Open an Issue for technical discussions)
# Generate a quote
python make_invoice.py
