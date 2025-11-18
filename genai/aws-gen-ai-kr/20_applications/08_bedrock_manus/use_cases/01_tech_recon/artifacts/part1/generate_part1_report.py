import pandas as pd
import re
from datetime import datetime
from pathlib import Path

# Configuration
COMPANY_NAME = "Pharmaceutical Corporation"
INDUSTRY = "Pharmaceutical/Healthcare"
CURRENT_TIME = datetime.now().strftime("%B %d, %Y")

# Load data
assessments_df = pd.read_csv("technology_assessments.csv")
categorization_df = pd.read_csv("categorization_matrix.csv")

with open("research_findings.txt", 'r', encoding='utf-8') as f:
    research_content = f.read()

# Extract citations
def extract_citations(text):
    """Extract unique citations from research text"""
    source_lines = []
    for line in text.split('\n'):
        if any(keyword in line for keyword in ['Source:', 'https://', 'http://', 'MarketsandMarkets', 'Grand View Research', 'Accenture', 'Deloitte', 'IBM', 'Gartner', 'Forrester']):
            if line.strip() and len(line.strip()) > 20:
                source_lines.append(line.strip())
    
    return list(set(source_lines))[:60]

citations = extract_citations(research_content)

# Start building the comprehensive report
report = f"""# Emerging Technology Reconnaissance Report - Part 1
## Technology Assessment and Prioritization for {COMPANY_NAME}

**Report Date:** {CURRENT_TIME}  
**Prepared for:** {COMPANY_NAME} CIO/Executive Team  
**Target Industry:** {INDUSTRY}

---

## Executive Summary

### Technology Landscape Overview

This comprehensive technology reconnaissance report analyzes **{len(assessments_df)} emerging technologies** across **{len(assessments_df['Domain'].unique())} major domains**, identifying strategic opportunities for {COMPANY_NAME} operations with emphasis on {INDUSTRY} applications.

**Analysis Scope:** {len(assessments_df['Domain'].unique())} domains | {len(assessments_df)} technologies evaluated | {len(categorization_df[categorization_df['Impact_Score'] >= 4])} meeting criteria (Impact ≥4)

### Key Findings

The assessment reveals a highly mature technology landscape with exceptional deployment readiness:

- **{len(categorization_df[categorization_df['Category'] == 'Deploy'])} Deploy** technologies (immediate implementation recommended)
- **{len(categorization_df[categorization_df['Category'] == 'Business Pilots'])} Pilot** technologies (6-18 month validation programs)
- **{len(categorization_df[categorization_df['Category'] == 'Experiments'])} Experiment** technologies (sandbox learning environments)
- **{len(categorization_df[categorization_df['Category'] == 'Monitor'])} Monitor** technologies (industry tracking and evaluation)

**Strategic Insight:** {(len(categorization_df[categorization_df['Category'] == 'Deploy']) / len(categorization_df) * 100):.0f}% of assessed technologies demonstrate production-ready maturity, indicating unprecedented opportunity for rapid digital transformation in {INDUSTRY}.

### Strategic Technology Priorities

**Deploy Category ({len(categorization_df[categorization_df['Category'] == 'Deploy'])} technologies):**

"""

# Add top 5 Deploy technologies
deploy_techs = categorization_df[categorization_df['Category'] == 'Deploy'].nlargest(5, 'Composite_Score')
for idx, row in deploy_techs.iterrows():
    report += f"- **{row['Technology_Name']}** (Score: {row['Composite_Score']:.1f}/9) - Transformative impact on pharmaceutical R&D, clinical operations, and patient care\n"

report += f"""

**Business Pilots Category ({len(categorization_df[categorization_df['Category'] == 'Business Pilots'])} technologies):**

"""

# Add Pilot technologies
pilot_techs = categorization_df[categorization_df['Category'] == 'Business Pilots']
for idx, row in pilot_techs.iterrows():
    report += f"- **{row['Technology_Name']}** (Score: {row['Composite_Score']:.1f}/9) - Requires validation in pharmaceutical workflows before enterprise deployment\n"

# Save initial report
print(f"✅ Executive Summary generated: {len(report):,} characters")

# Save to file
with open("part1_report.md", 'w', encoding='utf-8') as f:
    f.write(report)

print("✅ Initial report saved to part1_report.md")
