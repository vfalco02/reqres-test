.PHONY: setup
setup:
	( \
		python3 -m venv venv; \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)

.PHONY: test-all
test-all:
	( \
        source venv/bin/activate; \
        pytest tests -p no:warnings; \
	)