"""
linked list performance vs list

I want to prove that linked lists have a perfomance advantage over lists when
implementing a FIFO queue where elements are continuously added at the start of the list

"""
import time
import random
from collections import deque

RANDOM_INTEGERS = 100_000

#generate a list and add random integers, compare the time at
#the start and end to see how long it takes to run

print('\nImplementing list and adding', RANDOM_INTEGERS, 'random numbers')
list_start_time = time.time()

test_list = []
for i in range(RANDOM_INTEGERS):
    test_list.insert(random.randint(0,100), 0)

list_end_time = time.time()

list_total_time = list_end_time - list_start_time
print('total time for adding', RANDOM_INTEGERS, ' elements to start of a list = ', list_total_time)

#now implementing linked_list with random numbers added at the start
#compare time at the start and end
print("\nImplementing linked list and adding", RANDOM_INTEGERS, "random elements")
ll_start_time = time.time()

linked_list = deque()

for j in range(RANDOM_INTEGERS):
    linked_list.appendleft(random.randint(0, 100))

ll_end_time = time.time()

ll_total_time = ll_end_time - ll_start_time
print('total time for adding', RANDOM_INTEGERS, ' elements to start of linked list = ', ll_total_time)

if list_total_time > ll_total_time :
    print("\nLinked list is faster")
else:
    print("\nList is faster")