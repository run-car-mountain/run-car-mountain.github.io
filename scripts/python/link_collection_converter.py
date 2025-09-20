from pathlib import Path
import pandas as pd

dir_data = Path("../../data")

df = pd.read_excel(dir_data / "link_collection.xlsx")
df = df.dropna(how="all")

html_lines = []
toc_lines = []
current_category = None

for index, row in df.iterrows():
    category = row["category"]
    title = row["title"]
    url = row["url"]
    date = row["date"]
    author = row["author"]
    keywords = row["keywords"]
    comment = row["comment"]
    media = row["media"]
    date_added = row["date_added"]
    
    # Create a new section if the category changes
    if category != current_category:
        if current_category is not None:
            html_lines.append('<br class="small-break">')  # Blank line between sections
        anchor = category.replace(" ", "-").lower()
        html_lines.append(f'<h1 id="{anchor}">{category}</h1>')
        toc_lines.append(f'<li><a href="#{anchor}">{category}</a></li>')
        current_category = category
    
    # Create a short HTML snippet
    # html_lines.append(f"<h3>{title}</h3>")
    title_line = f'<a href="{url}">{title}</a>'
    if pd.notna(author):
        title_line += f" | {author}"
    html_lines.append(f"<p>{title_line}</p>")
    if pd.notna(keywords):
        html_lines.append(f"<p><strong>keywords:</strong> {keywords}</p>")
    if pd.notna(comment):
        html_lines.append(f"<p><strong>comment:</strong> {comment}</p>")
    info_line = []
    if pd.notna(media):
        info_line.append(f"{media}")
    if pd.notna(date):
        info_line.append(f"{date}")
    if info_line:
        html_lines.append(f"<p><strong>info:</strong> {' | '.join(info_line)}</p>")
    html_lines.append('<br class="small-break">')  # Blank line between entries

# Combine TOC and content
final_html_lines = ["<ul>"] + toc_lines + ["</ul>"] + html_lines

# Write out to a single HTML file
fpath_out = Path("../../content/link-collection/link_collection.html")
with open(fpath_out, "w", encoding="utf-8") as f:
    for line in final_html_lines:
        f.write(line + "\n")
print("wrote to ", fpath_out.absolute())
