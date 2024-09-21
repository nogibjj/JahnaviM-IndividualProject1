install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --ignore-patterns=test_.*?py *.py
	ruff check *.py

test:
	python -m pytest -vv --nbval -cov=lib.py -cov=crime_analyze test_*.py PandasDescriptiveStatistics.ipynb

all:
	install format lint test
