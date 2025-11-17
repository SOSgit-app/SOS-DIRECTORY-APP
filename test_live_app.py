import urllib.request
import json
import urllib.error

url = 'https://roster-app-243571769407.us-central1.run.app/search?query=JAYCE'
print(f"Testing live app: {url}\n")

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    print(f"[OK] Search successful!")
    print(f"Results found: {len(data)}")
    
    if len(data) > 0:
        print("\nResults:")
        for s in data:
            print(f"  - {s['student_name']} | Flight {s['flight_number']} | {s['instructor_name']}")
    else:
        print("\n[ERROR] No results found for 'JAYCE'")
        print("\nTrying to get total student count...")
        
        # Try searching for a common letter to see if app is working
        test_url = 'https://roster-app-243571769407.us-central1.run.app/search?query=SMITH'
        test_response = urllib.request.urlopen(test_url)
        test_data = json.loads(test_response.read().decode('utf-8'))
        print(f"Search for 'SMITH' returned: {len(test_data)} results")
        
        if len(test_data) > 0:
            print(f"Example: {test_data[0]['student_name']}")
            print("\n[WARNING] App is working but JAYCE not found - deployment may have old data")
        
except urllib.error.HTTPError as e:
    print(f"[ERROR] HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"[ERROR] URL Error: {e.reason}")
except Exception as e:
    print(f"[ERROR] Error: {e}")

