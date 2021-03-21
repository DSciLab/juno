PIP            := pip
REQUIREMENTS   := requirements.txt
PYTHON         := python


.PHONY: install dep clean


install: dep
	$(PYTHON) setup.py install


dep: $(REQUIREMENTS)
	$(PIP) install -r $^


clean:
	-rm -rf .eggs .tox build MANIFEST
