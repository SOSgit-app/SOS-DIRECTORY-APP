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

# Copy the 26A roster data to the correct location
RUN cp "26A UPDATED.json" static/roster_data.json

# Expose port 8080
EXPOSE 8080

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app 