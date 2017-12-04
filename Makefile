install:
	pip install -r requirements.txt

test:
	cd src && pytest
