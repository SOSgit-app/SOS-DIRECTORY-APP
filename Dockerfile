# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make sure the static directory exists
RUN mkdir -p static

# Run the migration script to copy the roster data
RUN python migrate_data.py

# Expose port 8080
EXPOSE 8080

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app 