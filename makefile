.PHONY: help build clean-build 

.DEFAULT: help
help:
	@echo "make test       run tests"
	@echo "make format     run yapf formatter"


coverage: clean test
	coverage html

clean-coverage:
	rm -rf htmlcov

clean-pyc: ## remove Python file artifacts
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		find . -name '__pycache__' -exec rm -rf {} +
		find . -name '*.egg-info' -exec rm -fr {} +

clean: clean-pyc clean-coverage
	    rm -rf .tox
		find . -name '*.swp' -exec rm -rf {} +
		find . -name '*.bak' -exec rm -rf {} +

format: clean
	yapf -r -i .

test: clean
	pytest
