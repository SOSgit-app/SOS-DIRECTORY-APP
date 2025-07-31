import json
import os
import sys

def test_json_file():
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    
    file_path = 'static/roster_data.json'
    print(f"Checking file: {file_path}")
    
    try:
        if not os.path.exists(file_path):
            print(f"ERROR: File does not exist: {file_path}")
            return
        else:
            print(f"File exists, size: {os.path.getsize(file_path)} bytes")
            
        with open(file_path, 'r') as file:
            print("File opened successfully")
            try:
                data = json.load(file)
                print(f"Successfully loaded {len(data)} student records")
                if len(data) > 0:
                    print(f"Sample record: {data[0]}")
            except json.JSONDecodeError as je:
                print(f"JSON decode error: {je}")
    except Exception as e:
        print(f"Error loading student data: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Test script started")
    test_json_file()
    print("Test script completed") 