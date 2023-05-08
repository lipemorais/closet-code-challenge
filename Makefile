test:
	pytest

t: test

run:
	flask --app src.main run --debug -h 0.0.0.0

r: run

lint:
	ruff check --fix .
	black .

l: lint

setup:
	./setup.sh

s: setup
