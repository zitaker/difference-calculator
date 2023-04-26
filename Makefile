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
