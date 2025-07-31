import json

# Load the roster data
with open('25D_Roster_from_new_pdf.json', 'r') as f:
    data = json.load(f)

# Extract all flight numbers
flight_numbers = [student['flight_number'] for student in data]
unique_flights = sorted(set(flight_numbers))

print(f"Total students: {len(data)}")
print(f"Unique flight numbers: {unique_flights}")

# Analyze flight prefixes and ranges
flight_prefixes = sorted(set([flight[0] for flight in unique_flights]))
print(f"Flight prefixes: {flight_prefixes}")

# Calculate ranges for each prefix
flight_ranges = {}
for flight in unique_flights:
    prefix = flight[0]
    number = flight[1:]
    
    if prefix not in flight_ranges:
        flight_ranges[prefix] = {'min': number, 'max': number}
    else:
        if number < flight_ranges[prefix]['min']:
            flight_ranges[prefix]['min'] = number
        if number > flight_ranges[prefix]['max']:
            flight_ranges[prefix]['max'] = number

# Print the ranges for each prefix
print("\nFlight number ranges:")
for prefix, range_data in flight_ranges.items():
    print(f"{prefix}: {prefix}{range_data['min']} - {prefix}{range_data['max']}") 