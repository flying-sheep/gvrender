_default:
    @just --list

# Install package in development mode
dev:
    pip install -qe .[dev,test]

# Run tests. Use pytest args like e.g. `-k some_test_name`
test *args:
    pytest {{args}}

# Create test baselines
test-baseline:
    pytest --mpl-generate-path=tests/baseline
