first_installation::
		poetry install
		poetry build
		poetry publish --dry-run
		python3 -m pip install --user dist/*.whl

#poetry run gendiff
#poetry run python -m gendiff.scripts.diff
#gendiff -h
#poetry run gendiff --help
#poetry run gendiff -h
#gendiff file1.py file2.yml
#poetry run gendiff file1.py file2.yml
#gendiff filepath1.json filepath2.json
