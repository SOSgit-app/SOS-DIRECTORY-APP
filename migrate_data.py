import json
import os
import shutil

def migrate_data():
    try:
        # Source and destination paths
        source_file = 'static/class25f_roster.json'
        dest_file = 'static/roster_data.json'
        
        # Ensure static directory exists
        os.makedirs('static', exist_ok=True)
        
        # Read the JSON data to verify it
        with open(source_file, 'r') as file:
            students_data = json.load(file)
        
        print(f"Found {len(students_data)} students in JSON file")
        if len(students_data) > 0:
            print("Sample student data:", students_data[0])
        
        # Copy the roster file to the static directory
        shutil.copy2(source_file, dest_file)
        print(f"Copied roster data to {dest_file}")
        
        print("Data migration completed successfully!")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        raise

if __name__ == "__main__":
    migrate_data() 