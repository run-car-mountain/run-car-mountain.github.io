.PHONY: debug server link-collection

# Run Hugo in draft-enabled debug mode
debug:
	@echo "Starting Hugo server with drafts enabled..."
	hugo server -D

# Run Hugo server with published content only
server:
	@echo "Starting Hugo server..."
	hugo server

# Regenerate the link collection data using the Python helper
link-collection:
	@echo "Rebuilding link collection..."
	cd scripts/python && uv run link_collection_converter.py
