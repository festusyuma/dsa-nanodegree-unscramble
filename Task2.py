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
    outgoing = call[0]
    incoming = call[1]
    current_time_spent = int(call[3])

    outgoing_time = time_spent.get(outgoing)
    incoming_time = time_spent.get(incoming)

    if outgoing_time:
        time_spent[outgoing] += current_time_spent
    else:
        time_spent[outgoing] = current_time_spent

    if incoming_time:
        time_spent[incoming] += current_time_spent
    else:
        time_spent[incoming] = current_time_spent

for no in time_spent:
    if most_time is None or time_spent[no] > time_spent[most_time]:
        most_time = no

print('{} spent the longest time, {} seconds, on the phone during September 2016.'
      .format(most_time, time_spent[most_time]))
