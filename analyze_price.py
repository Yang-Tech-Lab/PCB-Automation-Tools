"""
MarketIntelligence Pro: Strategic Pricing Orchestrator
------------------------------------------------------
An advanced analytics engine designed to ingest competitor pricing data, 
perform statistical synthesis, and generate high-fidelity market insights.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Intelligence / Freelance Strategy
Date: March 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import logging
import re
from pathlib import Path
from typing import List, Dict, Final, Any

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class PricingOrchestrator:
    def __init__(self, asset_name: str = "PCB Design Services"):
        self.asset_name: Final[str] = asset_name
        self.output_dir: Final[Path] = Path("Vault/Market_Reports")
        self.brand_color: Final[str] = "#1DBF73"  # Fiverr Professional Green
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure local storage for analytical assets."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logging.info("🛠️ Analytics environment synchronized.")

    def _clean_payload(self, raw_data: List[str]) -> pd.Series:
        """
        Performs robust data sanitization using Regex.
        Handles currencies, commas, and whitespace variations.
        """
        logging.info(f"Ingesting raw payload: {len(raw_data)} nodes detected.")
        clean_data = []
        for entry in raw_data:
            # Regex: Extract digits and decimals, ignoring symbols like $, £, or commas
            match = re.search(r"(\d+[\d,.]*)", entry)
            if match:
                value = float(match.group(1).replace(",", ""))
                clean_data.append(value)
        
        return pd.Series(clean_data)

    def synthesize_insights(self, raw_data: List[str]) -> Dict[str, float]:
        """Orchestrates the statistical synthesis of market metrics."""
        series = self._clean_payload(raw_data)
        
        # Comprehensive Descriptive Statistics
        stats = {
            "Mean": series.mean(),
            "Median": series.median(),
            "Min": series.min(),
            "Max": series.max(),
            "Std_Dev": series.std() # Measure of market volatility/variance
        }
        
        logging.info(f"Synthesis Complete. Market Median: ${stats['Median']:.2f}")
        return stats, series

    def generate_visual_report(self, stats: Dict[str, float], data: pd.Series):
        """Synthesizes a high-fidelity distribution chart for executive review."""
        logging.info("Generating visual intelligence asset...")
        
        plt.style.use('seaborn-v0_8-muted') # Modern professional style
        fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

        # 1. Histogram Execution
        n, bins, patches = ax.hist(
            data, bins=8, color=self.brand_color, 
            edgecolor='#2C3E50', alpha=0.8, label="Competitor Count"
        )

        # 2. Critical Threshold Annotations
        # Average Line
        ax.axvline(stats['Mean'], color='#E74C3C', linestyle='--', linewidth=2, 
                   label=f"Market Mean: ${stats['Mean']:.2f}")
        
        # Median Line (The Strategic Pivot Point)
        ax.axvline(stats['Median'], color='#2980B9', linestyle='-', linewidth=2.5, 
                   label=f"Strategic Median: ${stats['Median']:.2f}")

        # 3. Metadata & Typography
        ax.set_title(f'Market Distribution: {self.asset_name}', fontsize=18, fontweight='bold', pad=20)
        ax.set_xlabel('Pricing Tiers (USD)', fontsize=12, labelpad=10)
        ax.set_ylabel('Frequency (Number of Sellers)', fontsize=12, labelpad=10)
        ax.legend(frameon=True, facecolor='white', edgecolor='lightgrey')
        ax.grid(axis='y', linestyle=':', alpha=0.6)

        # 4. Strategic Insight Annotation
        # Highlight the "Sweet Spot" for entry
        ax.annotate(
            'Recommended Strategic Entry', 
            xy=(stats['Median'], max(n)*0.8), 
            xytext=(stats['Median'] + 30, max(n)*0.9),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="orange", alpha=0.5)
        )

        # Persistence Layer
        output_file = self.output_dir / "Market_Pricing_Analysis.png"
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        logging.info(f"🏆 Strategic visual asset persisted: {output_file.name}")

if __name__ == "__main__":
    # Real-world data simulated from Fiverr scraping
    competitor_payload = [
        '$25', '$195', '$10', '$40', '$125', '$35', 
        '$30', '$225', '$95', '$150', '$20', '$50',
        '$15', '$30', '$25', '$45', '$60', '$180'
    ]

    print("\n" + "="*55)
    print("      YANG-TECH-LAB: PRICING INTELLIGENCE CORE")
    print("="*55 + "\n")
    
    orchestrator = PricingOrchestrator(asset_name="Fiverr PCB Design")
    market_stats, clean_series = orchestrator.synthesize_insights(competitor_payload)
    orchestrator.generate_visual_report(market_stats, clean_series)
    
    # Textual Intelligence Summary
    print(f"📊 Market Report Summary for {orchestrator.asset_name}:")
    print(f"   - Average Price: ${market_stats['Mean']:.2f}")
    print(f"   - Market Median: ${market_stats['Median']:.2f} (Recommended)")
    print(f"   - Risk Index (Std Dev): {market_stats['Std_Dev']:.2f}")
    print("\n--- Session Complete ---")
