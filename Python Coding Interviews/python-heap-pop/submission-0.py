import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:

    new_heap = []

    for i in range(0, len(heap)):
        element = heapq.heappop(heap)
        heapq.heappush(new_heap, element)

    
    return new_heap


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
