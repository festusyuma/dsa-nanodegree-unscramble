"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bangalore_total_calls = 0
bangalore_to_bangalore_calls = 0
bangalore_calls_code = set()


def get_area_code(number):
    if number[0] == '(':
        return number[0:(number.find(')') + 1)]
    elif number[5] == ' ':
        return number[0:4]
    elif number[0:3] == '140':
        return '140'


for call in calls:
    outgoing_code = get_area_code(call[0])
    incoming_code = get_area_code(call[1])

    if outgoing_code == '(080)':
        bangalore_total_calls += 1
        bangalore_calls_code.add(incoming_code)

        if incoming_code == '(080)':
            bangalore_to_bangalore_calls += 1

bangalore_to_bangalore_percentage = (bangalore_to_bangalore_calls/bangalore_total_calls) * 100
bangalore_calls_code = sorted(bangalore_calls_code)

print('The numbers called by people in Bangalore have codes:')
print('\n'.join(bangalore_calls_code))

print('{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'
      .format(bangalore_to_bangalore_percentage))
