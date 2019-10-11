SHELL=/bin/bash

.PHONY: setup, setup-mobile

setup:
	-	virtualenv venv -p python3.6
	- 	source venv/bin/activate && \
			pip install -e .

setup-mobile:
	- pkg install python
	- python -m pip install -e .

run:
	- source venv/bin/activate && \
		python suamae.py