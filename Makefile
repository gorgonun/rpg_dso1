SHELL=/bin/bash

setup:
	-	virtualenv venv -p python3.6
	- 	source venv/bin/activate && \
			pip install -e .
