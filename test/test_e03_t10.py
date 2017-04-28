import heapq as h
from itertools import groupby
from classes import HeapNode

print("Start: Excise 03 Task 10")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

string = "abrakadabra"
heap = [HeapNode()]

for c in string:
    node = HeapNode(c)
    heap[0].find_value(c)
    found_node.weight += 1
    h.heapify(heap)
    h.heappush(heap, node)

print(heap)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Excise 03 Task 10")
