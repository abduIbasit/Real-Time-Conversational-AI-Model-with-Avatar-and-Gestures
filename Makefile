# Define variables
APP_NAME=my-fastapi-app
PORT=8000

# Build the Docker image
build:
	docker build -t $(APP_NAME) .

# Run the Docker container
run:
	docker run -p $(PORT):8000 $(APP_NAME)

# Stop the Docker container
stop:
	docker stop $(shell docker ps -q --filter ancestor=$(APP_NAME))

# Remove the Docker container
remove:
	docker rm $(shell docker ps -a -q --filter ancestor=$(APP_NAME))

# Clean up Docker images
clean:
	docker rmi $(APP_NAME)

# Rebuild the Docker image
rebuild: stop remove clean build run

# Run the app in a detached mode
start-detached:
	docker run -d -p $(PORT):8000 $(APP_NAME)

# Show logs from the running container
logs:
	docker logs -f $(shell docker ps -q --filter ancestor=$(APP_NAME))

# Run tests
test:
	pytest

# Lint the code
lint:
	flake8 .

# Format code with black
format:
	black .

# Generate requirements.txt
requirements:
	pip freeze > requirements.txt
