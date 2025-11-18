
import pandas as pd
import re
from datetime import datetime
from pathlib import Path

# Configuration
COMPANY_NAME = "Pharmaceutical Corporation"
INDUSTRY = "Pharmaceutical/Healthcare"
CURRENT_TIME = datetime.now().strftime("%B %d, %Y")

# Load data
base_path = Path("./artifacts/part1")
assessments_df = pd.read_csv(base_path / "technology_assessments.csv")
categorization_df = pd.read_csv(base_path / "categorization_matrix.csv")

with open(base_path / "research_findings.txt", 'r', encoding='utf-8') as f:
    research_content = f.read()

# Parse technology details from research
def parse_tech_section(tech_name, research_text):
    """Extract technology section from research"""
    # Find technology section
    pattern = rf"Technology \d+\.\d+:\s*{re.escape(tech_name)}.*?(?=Technology \d+\.\d+:|---\n\n|$)"
    match = re.search(pattern, research_text, re.DOTALL | re.IGNORECASE)
    
    if match:
        return match.group(0)
    return ""

# Extract citations
def extract_citations(text):
    """Extract unique citations"""
    source_lines = []
    for line in text.split('\n'):
        if any(keyword in line for keyword in ['Source:', 'https://', 'http://', 'MarketsandMarkets', 'Grand View Research', 'Accenture', 'Deloitte', '[1]', '[2]', '[3]', '[4]']):
            if line.strip() and len(line.strip()) > 20:
                source_lines.append(line.strip())
    
    return list(set(source_lines))[:60]

citations = extract_citations(research_content)

print(f"Generating comprehensive Part 1 report...")
print(f"Technologies: {len(assessments_df)}")
print(f"Citations: {len(citations)}")

# Save script completion marker
with open(base_path / "report_gen_ready.txt", 'w') as f:
    f.write("Report generator script ready\n")
    f.write(f"Technologies: {len(assessments_df)}\n")
    f.write(f"Citations: {len(citations)}\n")

print("✅ Report generator prepared")
