from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:

    """
    Take arr, popleft k elements, append k elements to deque made up of arr

    Iterate through range of (0, k), pop left element, append it to empty deque
    
    """
    
    queue = deque(arr)
    # print(f"Value of Queue: {queue}")

    for i in range(0, k):
        top_element = queue.popleft()
        queue.append(top_element)

    return queue








# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
