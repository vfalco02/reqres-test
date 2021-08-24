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

.PHONY: test-e2e
test-e2e:
	( \
        source venv/bin/activate; \
        pytest tests -m e2e -p no:warnings; \
	)

.PHONY: test-regression
test-regression:
	( \
        source venv/bin/activate; \
        pytest tests -m regression -p no:warnings; \
	)