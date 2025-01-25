# Define variables
PYTHON ?= python
DIST_DIR = dist

# Default target
all: build

# Build the project using setuptools
build:
	$(PYTHON) -m build

# Install the wheel
install: $(DIST_DIR)/*.whl
	$(PYTHON) -m pip install --force-reinstall --upgrade $<

# Clean up build artifacts
clean:
	rm -rf $(DIST_DIR) build *.egg-info

# Phony targets
.PHONY: all build install clean