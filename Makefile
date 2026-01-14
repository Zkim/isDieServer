run:
	. .venv/bin/activate && python app.py

venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

shell:
	. .venv/bin/activate && bash
