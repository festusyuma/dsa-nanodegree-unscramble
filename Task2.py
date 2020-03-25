"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_spent = {}
most_time = None

for call in calls:
    if call[0] not in time_spent:
        time_spent[call[0]] = 0

    if call[1] not in time_spent:
        time_spent[call[1]] = 0

    time_spent[call[0]] += int(call[3])
    time_spent[call[1]] += int(call[3])

    if most_time is None or time_spent[call[0]] > time_spent[most_time]:
        most_time = call[0]

    if time_spent[call[1]] > time_spent[most_time]:
        most_time = call[1]

print('{} spent the longest time, {} seconds, on the phone during September 2016.'
      .format(most_time, time_spent[most_time]))
