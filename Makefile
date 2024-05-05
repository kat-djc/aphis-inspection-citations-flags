.PHONY: venv flags aphis-inspection-reports

requirements.txt: requirements.in
	pip-compile requirements.in

venv: requirements.txt
	python -m venv venv
	venv/bin/pip install -r requirements.txt

aphis-inspection-reports:
	git submodule update

flags: scripts
	nbexec scripts
