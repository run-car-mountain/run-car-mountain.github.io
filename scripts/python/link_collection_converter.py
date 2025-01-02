from pathlib import Path
import pandas as pd

dir_data = Path("../../data")

df = pd.read_excel(dir_data / "link_collection.xlsx")

print(df.to_string())
md_lines = []
current_category = None

for index, row in df.iterrows():
    category = row["category"]
    title = row["title"]
    date = row["date"]
    author = row["author"]
    keywords = row["keywords"]
    comment = row["comment"]
    media = row["media"]
    date_added = row["date_added"]
    
    # Create a new section if the category changes
    if category != current_category:
        if current_category is not None:
            md_lines.append("")  # Blank line between sections
        md_lines.append(f"# {category}")
        current_category = category
    
    # Create a short Markdown snippet
    md_lines.append(f"### {title}")
    if pd.notna(date):
        md_lines.append(f"- **Date**: {date}")
    if pd.notna(author):
        md_lines.append(f"- **Author**: {author}")
    if pd.notna(keywords):
        md_lines.append(f"- **Keywords**: {keywords}")
    if pd.notna(media):
        md_lines.append(f"- **Media**: {media}")
    if pd.notna(comment):
        md_lines.append(f"- **Comment**: {comment}")
    if pd.notna(date_added):
        md_lines.append(f"- **Date Added**: {date_added}")
    md_lines.append("")  # Blank line between entries

# Write out to a single Markdown file
with open(dir_data / "link_collection.md", "w", encoding="utf-8") as f:
    for line in md_lines:
        f.write(line + "\n")
