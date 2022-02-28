import json

f = open('../data/raw/calendarEvent.json')

event = json.load(f)

print(event['categories'])

f.close()