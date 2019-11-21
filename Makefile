SHELL=/bin/bash

.PHONY: setup, setup-mobile, run

setup:
	- python3 -m pip install -e . &&  \
			python3 -m pip install -r requirements.txt

setup-pc:
	- virtualenv venv -p python3.6
	- source venv/bin/activate && \
			pip install -e . && \
			pip install -r requirements.txt

setup-mobile:
	- pkg install python
	- python -m pip install -e . && \
			pip install -r requirements.txt

run:
	- python3 start.py

run-pc:
	- source venv/bin/activate && \
		python start.py

run-test:
	- python3 start.py test