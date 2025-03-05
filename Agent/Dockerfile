# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for some Python libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel before installing dependencies
RUN pip install --upgrade pip setuptools wheel

# Copy the requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the WebSocket and API port
EXPOSE 8000

# Command to start the FastAPI WebSocket server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
