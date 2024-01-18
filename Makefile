.PHONY: test/go
test/go:
	@echo "Running Go tests..."
	cd go && go test -v ./...

.PHONY: test/python
test/python:
	@echo "Running Python tests..."
	cd python && python3 -m unittest discover -v

.PHONY: test
test: test/go test/python

.PHONY: clean
clean:
	@echo "Cleaning caches..."
	find ./python -type d -name '__pycache__' -exec rm -rf {} +
