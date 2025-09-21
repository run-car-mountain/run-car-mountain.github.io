---
title: "Automating the Link Collection"
date: 2024-03-06
draft: false
tags:
  - automation
  - python
  - reproducibility
---

The link collection that powers this site started as a loose set of bookmarks and small notes. Manual curation quickly became tedious:
keeping categories consistent, trimming duplicates, and keeping the page in sync with the latest additions all took too much time.
To keep the curation fun, I built a small Python pipeline that generates the published HTML directly from the spreadsheet we already maintain.

## Keeping the pipeline reproducible

The script lives in [`scripts/python/link_collection_converter.py`](https://github.com/run-car-mountain/run-car-mountain.github.io/blob/main/scripts/python/link_collection_converter.py).
It has a single entry point (`main`) that reads `data/link_collection.xlsx`, renders deterministic HTML, and saves it to `content/link-collection/link_collection.html`.
Because all inputs are version-controlled alongside the blog, anyone cloning the repository can run the script and regenerate the exact same output.

A couple of implementation choices keep that promise:

- **No implicit configuration** – the paths to the spreadsheet and generated HTML are defined in constants, so running the script from any directory uses the same sources.
- **Minimal dependencies** – only `pandas` and `openpyxl` are required (declared in `scripts/python/pyproject.toml`), which makes recreating the environment straightforward via `uv` or `pip`.
- **Idempotent writes** – the script rewrites the entire HTML document on each run, so repeated executions do not accumulate stray edits.

## Managing a large catalog

The spreadsheet contains hundreds of rows covering articles, videos, and podcasts. Rather than trusting humans to keep it tidy, the script normalizes each row before writing anything out.
It removes empty rows, trims whitespace, and requires the triad of category, title, and URL before an entry is rendered.
Optional columns such as author, keywords, and media are rendered only when supplied.
That lets us keep quick notes in the sheet without worrying about broken markup.

For readers, the script groups entries by category and inserts a table of contents that links to each group.
This structure makes it feasible to scroll through a large corpus and still jump directly to, say, "Systems" or "Applied ML".

## Sorting during editing

Deterministic sorting is the final piece that makes the workflow predictable.
Before rendering, the script sorts the normalized entries by lowercase category and lowercase title.
When editing the spreadsheet with collaborators, the HTML output therefore remains stable: the same links stay grouped together and the diff after running the script is minimal.

That stability is particularly helpful when reviewing changes in pull requests.
A single new row produces a small, obvious diff instead of reflowing half the document.
You can also regenerate the page locally to verify the preview without wondering whether the order changed because of manual edits.

## Running the conversion yourself

From the repository root:

```bash
uv run scripts/python/link_collection_converter.py
```

This will install the declared dependencies, read the spreadsheet, and write the refreshed HTML.
Once committed, Hugo will pick up the updated file during the next site build.

The result is a small, repeatable workflow that turns a living spreadsheet into a publishable resource without losing the ability to manage a large volume of links.
