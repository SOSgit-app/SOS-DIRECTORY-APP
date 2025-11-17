import urllib.request
import json

url = 'https://roster-app-243571769407.us-central1.run.app/search?query=JAYCE'
print(f"Testing: {url}\n")

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))

print(f"Results for 'JAYCE': {len(data)}")
if len(data) > 0:
    for s in data:
        print(f"  - {s['student_name']} | Flight {s['flight_number']} | {s['instructor_name']}")
else:
    print("  NO RESULTS FOUND")
    print("\nTesting if app has ANY data...")
    test_url = 'https://roster-app-243571769407.us-central1.run.app/search?query=SMITH'
    test_response = urllib.request.urlopen(test_url)
    test_data = json.loads(test_response.read().decode('utf-8'))
    print(f"  Search for 'SMITH': {len(test_data)} results")
    if len(test_data) > 0:
        print(f"  Example: {test_data[0]['student_name']}")

