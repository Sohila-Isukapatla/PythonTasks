import pandas as pd
import re

# File paths
input_file = "C:/Users/Sohila I/Downloads/Literature Review.xlsx"
output_file = "C:/Users/Sohila I/Downloads/output9.xlsx"

# Load Excel file
df = pd.read_excel(input_file)

# Cleaning function for column B
def clean_column_b(text):
    if pd.isna(text):
        return text

    lines = str(text).splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if line.lower() in ['pdf', 'summary', 'chat', 'podcast', 'request pdf']:
            continue
        if re.fullmatch(r"\d+", line):  # remove numeric-only lines
            continue
        cleaned_lines.append(line)

    cleaned_text = '\n'.join(cleaned_lines)
    match = re.search(r"\d+\.\s.*", cleaned_text, re.DOTALL)
    if match:
        return match.group(0).strip()
    return cleaned_text.strip()

# Apply cleaning to column B
df.iloc[:, 1] = df.iloc[:, 1].apply(clean_column_b)

# Function to extract "Name et al., Year" or fallback
def extract_author_year(text):
    if pd.isna(text):
        return ''

    lines = text.splitlines()
    author = ''
    year = ''

    for line in lines:
        line = line.strip()

        # Try to find a year
        if not year:
            match_year = re.search(r'\b(20\d{2}|19\d{2})\b', line)
            if match_year:
                year = match_year.group(1)

        # Try to find the name
        if not author:
            if ',' in line:
                author = line.split(',')[0].strip()
            elif 'valley' in line.lower():  # For "Kathmandu Valley"
                author = line.split(',')[0].strip()
            elif re.match(r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+$', line):
                author = line.strip()

    if author and year:
        return f"{author} et al., {year}"
    elif author:
        return f"{author} et al.,"
    elif year:
        return f"et al., {year}"
    else:
        return ''

# Generate column H
df['H'] = df.iloc[:, 1].apply(extract_author_year)

# Save final output
df.to_excel(output_file, index=False)
print("✅ Done! Final cleaned and tagged data saved to 'output9.xlsx'")
