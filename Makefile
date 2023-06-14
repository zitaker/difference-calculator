install:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl

flake8:
	pip install flake8
	poetry run flake8 gendiff
	
pytest:
	pip install pytest
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=gendiff
	
coverage:
	poetry add pytest-cov
	
#flake8:
#	poetry run flake8 gendiff

#make lint:
#	poetry run flake8 gendiff
#	poetry run pytest -vv


#first_installation:
#		poetry install
#		poetry build
#		poetry publish --dry-run
#		python3 -m pip install --user dist/*.whl
#		#python3 -m pip install --force-reinstall dist/*.whl

#poetry run gendiff
#poetry run python -m gendiff.scripts.diff
#gendiff -h
#poetry run gendiff --help
#poetry run gendiff -h
#gendiff file1.py file2.yaml
#poetry run gendiff file1.py file2.yaml
#gendiff filepath1.yaml filepath2.yaml
#poetry run gendiff file1.json file2.json
#gendiff file1.json file2.json

#poetry run gendiff gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json
#poetry run gendiff gendiff/tests/fixtures/file1.yaml gendiff/tests/fixtures/file2.yaml
#poetry run gendiff gendiff/tests/fixtures/file1.yml gendiff/tests/fixtures/file2.yml
#poetry run gendiff gendiff/tests/fixtures/filepath1.yaml gendiff/tests/fixtures/filepath2.yaml

#poetry run gendiff gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json --format one_level_formatter
#poetry run gendiff gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json --format stylish

