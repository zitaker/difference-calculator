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

test:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
	poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
	poetry run gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json --format stylish
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json --format plain
	poetry run gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format plain
	poetry run gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format json
	poetry run pytest -vv
	poetry run flake8 gendiff
	poetry run flake8 tests

#first_installation:
	#poetry shell
	#pip3 install PyYAML
	#poetry install
	#poetry build
	#poetry publish --dry-run
	#python3 -m pip install --user dist/*.whl

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

#poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
#poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml
#poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
#poetry run gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml

#poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json --format stylish
#poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json --format plain

#poetry run gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format plain

#poetry run gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format json
