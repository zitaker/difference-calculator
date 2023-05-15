install:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl
pytest:
	poetry run pytest -vv
	
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
#gendiff file1.py file2.yml
#poetry run gendiff file1.py file2.yml
#gendiff filepath1.json filepath2.json
#poetry run gendiff file1.json file2.json
#gendiff file1.json file2.json
#poetry run gendiff gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json


