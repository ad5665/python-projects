VENV ?= .venv
PY ?= $(VENV)/bin/python
PIP ?= $(VENV)/bin/pip

SRC_DIR ?= src
BUILD_DIR ?= build
ARTIFACT ?= function.zip

.PHONY: help venv deps update-deps test lint fmt typecheck build clean distclean

help:
	@echo "make venv           # create venv"
	@echo "make deps           # install deps + dev tools"
	@echo "make update-deps    # upgrade deps to latest (pip-tools optional)"
	@echo "make test           # run pytest"
	@echo "make lint           # run ruff (no fixes)"
	@echo "make fmt            # ruff --fix + black"
	@echo "make typecheck      # mypy (if installed)"
	@echo "make build          # build Lambda ZIP -> $(ARTIFACT)"
	@echo "make clean          # remove build artifacts"
	@echo "make distclean      # clean + remove venv"

venv:
	python -m venv $(VENV)

deps: venv
	$(PIP) install -r requirements.txt
	$(PIP) install pytest black ruff
	@echo "Tip: add mypy/coverage if you want:  pip install mypy coverage"

update-deps: venv
	# Optional if you use pip-tools; otherwise remove this target
	# $(PIP) install pip-tools && pip-compile --upgrade && pip-sync
	$(PIP) install --upgrade -r requirements.txt

test:
	$(PY) -m pytest

lint:
	$(VENV)/bin/ruff check $(SRC_DIR) tests

fmt:
	$(VENV)/bin/ruff check --fix $(SRC_DIR) tests
	$(VENV)/bin/black $(SRC_DIR) tests

typecheck:
	@if [ -x "$(VENV)/bin/mypy" ]; then \
	  $(VENV)/bin/mypy $(SRC_DIR); \
	else \
	  echo "mypy not installed. Run: $(PIP) install mypy"; \
	fi

build:
	rm -rf $(BUILD_DIR) $(ARTIFACT)
	mkdir -p $(BUILD_DIR)
	# Install runtime deps into build/ (no dev tools)
	$(PIP) install -r requirements.txt -t $(BUILD_DIR)
	# Copy your source into the build root so handler path is correct
	cp -r $(SRC_DIR)/* $(BUILD_DIR)/
	cd $(BUILD_DIR) && zip -r ../$(ARTIFACT) .

clean:
	rm -rf $(BUILD_DIR) .pytest_cache __pycache__ */__pycache__ $(ARTIFACT)

distclean: clean
	rm -rf $(VENV)
