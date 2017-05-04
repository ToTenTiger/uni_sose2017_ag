from itertools import filterfalse

from classes import Request
from operator import attrgetter

print("Start: Excise 04 Task 16")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

value = [[5, 17], [6, 24], [0, 16], [11, 16], [5, 14], [1, 7], [1, 3], [1, 2], [2, 23], [8, 12], [14, 15], [7, 13],
         [22, 24], [9, 10], [13, 23], [5, 20], [2, 13], [8, 19], [1, 13], [3, 4], [3, 24], [0, 10], [11, 13], [14, 18],
         [2, 22], [8, 24], [7, 21], [11, 16], [6, 16], [1, 15], [18, 23], [6, 14], [5, 15], [8, 22], [7, 16], [5, 12],
         [16, 18], [5, 22], [12, 18], [13, 23], [9, 11], [3, 12], [7, 19], [20, 24], [7, 20], [13, 16], [4, 24], [1, 4],
         [8, 21]]

print("\nUsing request list: {}\n".format(value))
new_input = input("Enter any other list to use or press [Enter] to continue: ")
if new_input:
    value = new_input
print()

requests = []
for (start, end) in value:
    requests.append(Request(start, end))
for x in requests:
    count = -1
    for y in requests:
        if not x.compatible(y):
            count += 1
    x.conflicts = count

comparison_by = ["interval_start", "interval_length", "interval_end", "conflicts"]

for i, compare_var in enumerate(comparison_by):
    requests_sorted = sorted(requests, key=attrgetter(compare_var))
    selected_requests = []
    while len(requests_sorted) > 0:
        r = requests_sorted.pop(0)
        selected_requests.append(r)
        requests_sorted[:] = filterfalse(lambda x: not r.compatible(x), requests_sorted)
    print("Strategie {}: {}".format(i + 1, selected_requests))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\nEnd: Excise 04 Task 16")
