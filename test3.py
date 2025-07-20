import pandas as pd
import re

# File paths
input_file = "C:/Users/Sohila I/Downloads/Literature Review.xlsx"
output_file = "C:/Users/Sohila I/Downloads/output5.xlsx"

# Load Excel file
df = pd.read_excel(input_file)

# Full cleaning and extraction function for Column B
def clean_and_extract(text):
    if pd.isna(text):
        return pd.Series([text, ''])

    lines = str(text).splitlines()

    cleaned_lines = []
    name_line = ''
    date_line = ''

    for i, line in enumerate(lines):
        line = line.strip()

        # Remove unwanted lines
        if line.lower() in ['pdf', 'summary', 'chat', 'podcast', 'request pdf']:
            continue
        if re.fullmatch(r"\d+", line):
            continue

        # Try to detect date-journal line
        if re.search(r'\d{1,2} \w+ \d{4}-', line):
            date_line = line
            if i > 0:
                name_line = lines[i - 1].strip()
            continue

        cleaned_lines.append(line)

    # Re-join cleaned B content (excluding name/date lines)
    cleaned_text = '\n'.join([line for line in cleaned_lines if line not in [name_line, date_line]])

    # Keep only the part starting from "1. ", "2. ", etc.
    match = re.search(r'\d+\.\s.*', cleaned_text, re.DOTALL)
    if match:
        cleaned_text = match.group(0).strip()

    # Final H column content
    h_text = f"{name_line}\n{date_line}" if name_line and date_line else ''

    return pd.Series([cleaned_text.strip(), h_text.strip()])

# Apply to Column B (index 1)
df[['B_Cleaned', 'H']] = df.iloc[:, 1].apply(clean_and_extract)

# Remove starting serial numbers like "1. ", "2. ", etc. at the END
df['B_Cleaned'] = df['B_Cleaned'].str.replace(r'^\d+\.\s*', '', regex=True)

# Replace original B with cleaned version
df.drop(df.columns[1], axis=1, inplace=True)
df.insert(1, 'B', df.pop('B_Cleaned'))  # Insert cleaned B in 2nd position

# Save to output Excel
df.to_excel(output_file, index=False)

print("✅ Done! Column B cleaned, serial numbers removed at end, names and dates moved to column H.")
