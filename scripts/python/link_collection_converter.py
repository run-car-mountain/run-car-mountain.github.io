"""Generate a link collection HTML page from the spreadsheet source.

The script is intentionally lightweight so it can be described alongside a
blog post. It reads the curated spreadsheet, builds a table of contents, and
renders each entry as a small HTML snippet.
"""

from pathlib import Path
from typing import List, Optional, Tuple

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = REPO_ROOT / "data" / "link_collection.xlsx"
OUTPUT_FILE = REPO_ROOT / "content" / "link-collection" / "link_collection.html"


def load_links(path: Path) -> pd.DataFrame:
    """Read the spreadsheet and drop rows that are entirely empty."""

    df = pd.read_excel(path)
    return df.dropna(how="all")


def optional_text(value) -> Optional[str]:
    """Return a stripped string if the cell has content; otherwise None."""

    if pd.isna(value):
        return None
    text = str(value).strip()
    return text or None


def category_anchor(category: str) -> str:
    """Convert a category label to a lowercase anchor string."""

    return category.lower().replace(" ", "-")


def generate_sections(df: pd.DataFrame) -> Tuple[List[str], List[str]]:
    """Return the (toc_lines, html_lines) generated from the link rows."""

    toc_lines: List[str] = []
    html_lines: List[str] = []
    current_category: Optional[str] = None

    for _, row in df.iterrows():
        category = optional_text(row.get("category"))
        title = optional_text(row.get("title"))
        url = optional_text(row.get("url"))

        # Skip rows missing the minimum fields for a useful entry.
        if not category or not title or not url:
            continue

        if category != current_category:
            if current_category is not None:
                html_lines.append('<br class="small-break">')
            anchor = category_anchor(category)
            html_lines.append(f'<h1 id="{anchor}">{category}</h1>')
            toc_lines.append(f'<li><a href="#{anchor}">{category}</a></li>')
            current_category = category

        author = optional_text(row.get("author"))
        keywords = optional_text(row.get("keywords"))
        comment = optional_text(row.get("comment"))
        media = optional_text(row.get("media"))
        date = optional_text(row.get("date"))

        title_line = f'<a href="{url}">{title}</a>'
        if author:
            title_line += f" | {author}"
        html_lines.append(f"<p>{title_line}</p>")

        if keywords:
            html_lines.append(f"<p><strong>keywords:</strong> {keywords}</p>")
        if comment:
            html_lines.append(f"<p><strong>comment:</strong> {comment}</p>")

        info_line = []
        if media:
            info_line.append(media)
        if date:
            info_line.append(date)
        if info_line:
            html_lines.append(f"<p><strong>info:</strong> {' | '.join(info_line)}</p>")

        html_lines.append('<br class="small-break">')

    return toc_lines, html_lines


def write_html(lines: List[str], path: Path) -> None:
    """Persist the rendered HTML to the expected output path."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def main() -> None:
    df = load_links(DATA_FILE)
    toc_lines, html_lines = generate_sections(df)

    final_html_lines = ["<ul>", *toc_lines, "</ul>", *html_lines]
    write_html(final_html_lines, OUTPUT_FILE)

    print(f"wrote to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
