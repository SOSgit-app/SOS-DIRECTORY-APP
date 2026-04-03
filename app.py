from flask import Flask, render_template, jsonify, request, url_for
import json
import os

# Version: 26D-2026-04-03 (Class 26D - 568 students)
app = Flask(__name__, static_folder='static')

# Load student data from JSON file
def load_student_data():
    try:
        file_path = os.path.join(app.static_folder, 'roster_data.json')
        print(f"Attempting to load student data from: {file_path}")
        if not os.path.exists(file_path):
            print(f"ERROR: File does not exist: {file_path}")
            return []
            
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            print(f"Successfully loaded {len(data)} student records")
            if len(data) > 0:
                print(f"Sample record: {data[0]}")
            return data
    except Exception as e:
        print(f"Error loading student data: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dha-remote-access')
def dha_remote_access():
    return render_template('dha_remote_access.html')

@app.route('/search')
def search():
    try:
        search_term = request.args.get('query', '').upper()
        print(f"Search request received. Query: '{search_term}'")
        
        if not search_term:
            print("Empty search query, returning empty results")
            return jsonify([])
        
        # Load student data
        students = load_student_data()
        print(f"Loaded {len(students)} student records for search")
        
        # Filter students based on search term
        results = [
            student for student in students 
            if search_term in student.get('student_name', '').upper()
        ]
        
        print(f"Found {len(results)} matches for '{search_term}'")
        if len(results) > 0:
            print(f"First match: {results[0]}")
        
        return jsonify(results)
    except Exception as e:
        print(f"Search error: {e}")
        return jsonify({"error": "An error occurred while searching"}), 500

if __name__ == '__main__':
    # Check if data is available on startup
    student_count = len(load_student_data())
    print(f"Application starting with {student_count} student records loaded")
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080))) 