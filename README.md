# Cloning repo on new PC
- `git submodule update --init --recursive`

# Update PaperMod
- `git submodule update --remote --merge`

# Debugging Locally
- `make debug` to run `hugo server -D` with drafts enabled
- `make server` to run `hugo server` with published content only

# Rebuild link-collection
- `make link-collection` or `(cd scripts/python && uv run link_collection_converter.py)`

