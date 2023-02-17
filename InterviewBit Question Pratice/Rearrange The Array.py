'''
    Time Complexity : O(N * log(N))
    Space Complexity : O(N)

    Where 'N' is the number of elements in the given array/list.
'''

from queue import PriorityQueue
from collections import defaultdict


# Compare class to order Priority Queue storing object with max frequency on top.
class Compare:
    def __init__(self, value, quantity):
        self.value = value
        self.quantity = quantity

    def __lt__(self, next):
        return self.quantity > next.quantity


def rearrange(num):
    output = []

    # Make a priority queue.
    priorityQueue = PriorityQueue()

    n = len(num)

    freq = defaultdict(int)

    # Store frequencies.
    for x in num:
        freq[x] += 1

    # Insert elements and frequency correspond to that element.
    for value, quantity in freq.items():
        # Pushing Compare class object representing value and frequency.
        priorityQueue.put(Compare(value, quantity))

    # For keep tracking to the recently added element into output.
    prev = Compare(-1, -1)

    # Traverse in priority queue.
    while (priorityQueue.qsize() > 0):

        # Get the top element.
        temp = priorityQueue.get()

        # Store the value.
        output.append(temp.value)

        ''' If frequency of previouse element has more
            frequency else it's use less.
        '''
        if (prev.quantity > 0):
            priorityQueue.put(prev)

        # Decrease frequence by one.
        temp.quantity = temp.quantity - 1

        # Make current as previous.
        prev = temp

    '''
        If size of rearranged array/list is not same
        as the size of given array/list then given is invalid.
    '''
    if (len(output) == n):
        return output
    else:
        return [-2147483648]