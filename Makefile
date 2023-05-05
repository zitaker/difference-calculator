install:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl

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
#poetry run gendiff file1_json.json file2_json.json
#gendiff file1_json.json file2_json.json


#poetry run flake8 gendiff
