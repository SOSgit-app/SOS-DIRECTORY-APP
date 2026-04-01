# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy build timestamp to force rebuild (cache buster)
COPY .buildtime /app/.buildtime

# Copy the rest of the application including static files
COPY . .

# Verify roster data was copied and display first student
RUN echo "=== VERIFYING ROSTER DATA ===" && \
    ls -lh static/roster_data.json && \
    head -20 static/roster_data.json && \
    python3 -c "import json; data=json.load(open('static/roster_data.json', encoding='utf-8-sig')); print(f'Total students: {len(data)}'); gravdahl=[s for s in data if 'GRAVDAHL' in s.get('student_name','')]; print(f'GRAVDAHL found: {len(gravdahl)}'); [print(f\"  {s['student_name']}\") for s in gravdahl]" && \
    echo "=== VERIFICATION COMPLETE ==="

# Expose port 8080
EXPOSE 8080

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app 