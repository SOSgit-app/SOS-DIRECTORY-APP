import json

with open('static/roster_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total students: {len(data)}')
print(f'First student: {data[0]["student_name"]} - Flight {data[0]["flight_number"]}')
print(f'Last student: {data[-1]["student_name"]} - Flight {data[-1]["flight_number"]}')

