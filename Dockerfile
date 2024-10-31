# Start with the official Python image for consistency and ease of setup
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI application with Uvicorn as the ASGI server
# The --host 0.0.0.0 option allows access from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
