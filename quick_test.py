import urllib.request
import json

tests = ['JAYCE', 'GRAVDAHL', 'GEORGE', 'MITCHELL']

print("Testing deployed app...\n")
for name in tests:
    url = f'https://roster-app-243571769407.us-central1.run.app/search?query={name}'
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        print(f"Search '{name}': {len(data)} results")
        if len(data) > 0:
            print(f"  -> {data[0]['student_name']} (Flight {data[0]['flight_number']})")
    except Exception as e:
        print(f"Search '{name}': ERROR - {e}")
    print()

