# Start with official Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file to the working directory
COPY requirements.txt .

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the application with Uvicorn as the ASGI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
