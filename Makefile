.PHONY: parse serve open dev clean help

PORT ?= 8000

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

parse: ## Parse watch-history.html into data.json
	python3 parse.py

serve: ## Start local server on PORT (default 8000)
	@echo "Serving at http://localhost:$(PORT)"
	python3 -m http.server $(PORT)

open: ## Open the app in your browser
	open http://localhost:$(PORT)

dev: parse ## Parse data then start the server
	$(MAKE) serve

clean: ## Remove generated data.json
	rm -f data.json
