.PHONY: test_python test_go

test-go:
	@echo "Running Go tests..."
	cd go && go test -v ./...

test-python:
	@echo "Running Python tests..."
	cd python && python3 -m unittest discover -v

test: test-go test-python