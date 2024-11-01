# Makefile for setting up and running the Application

# Variables
VENV_DIR = env
PYTHON = python3
HOST = 0.0.0.0
PORT = 8000

# Make a virtual environment
.PHONY: venv
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies
.PHONY: install
install: venv
	@echo "Activating virtual environment and installing dependencies..."
	source $(VENV_DIR)/bin/activate && pip install -r requirements.txt

# Set up the environment file
.PHONY: env
env:
	@echo "Setting up .env file..."
	@touch .env
	@echo "Please add your GROQ_API and D-ID API keys to the .env file."

# Run the application
.PHONY: run
run:
	@echo "Starting the application on ws://$(HOST):$(PORT)/ws/conversation..."
	source $(VENV_DIR)/bin/activate && uvicorn main:app --host $(HOST) --port $(PORT)

# Clean up virtual environment
.PHONY: clean
clean:
	@echo "Cleaning up the environment..."
	rm -rf $(VENV_DIR)

# Full setup and run
.PHONY: setup
setup: venv install env run
	@echo "Application setup and started successfully."

# Stop the app
.PHONY: stop
stop:
	@echo "Stopping application (if running)..."
	@pkill -f "uvicorn main:app" || echo "Application not running."

# Help
.PHONY: help
help:
	@echo "Makefile for Real-Time Conversational AI Application"
	@echo "Usage:"
	@echo "  make venv        - Create a virtual environment"
	@echo "  make install     - Install dependencies in the virtual environment"
	@echo "  make env         - Create an .env file for environment variables"
	@echo "  make run         - Run the application with Uvicorn"
	@echo "  make clean       - Remove the virtual environment"
	@echo "  make setup       - Full setup (venv, install, env, run)"
	@echo "  make stop        - Stop the application if running"
	@echo "  make help        - Show this help message"
