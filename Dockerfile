# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy the Python script to container
COPY app.py .

# Install required Python packages
RUN pip install --no-cache-dir prometheus-client requests

# Expose port 8000 for Prometheus metrics
EXPOSE 8000

# Run the script when container launches
CMD ["python", "app.py"]