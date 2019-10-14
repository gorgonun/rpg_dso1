SHELL=/bin/bash

.PHONY: setup, setup-mobile, run

setup:
	- virtualenv venv -p python3.6
	- source venv/bin/activate && \
			pip install -e .

setup-mobile:
	- pkg install python
	- python -m pip install -e .

run:
	- source venv/bin/activate && \
		python start.py

run-test:
	-source venv/bin/activate && \
		python start.py test