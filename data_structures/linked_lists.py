"""
Linked lists Tutorial from Real Python
https://realpython.com/linked-lists-python/
"""
"""
Each element in a linked list is called a node and every node has 2 fields,
data and next. a collection of nodes is a linked list. The last node has a
reference pointing to None.

Linked lists can be used for queues and stacks and graphs, and is efficient 
compared to an adjacency matrix

linked lists have a performance advantage of normal lists when implementing 
a queue (FIFO) when elements are continuously added at the start of the list, 
but perform similarly when elements are inserted and removed at the end.

Lists perform better when retrieving elements, because you need to  traverse the
whole list to find an element in a linked list

Both lists and linked lists perform similarly when searching for a specific element
because you need to iterate through the whole list
"""
from collections import deque

#create a linked list with deque
linked_list = deque('abcdef')
print('\ncreate a linked list with deque')
print(linked_list)

#add to the linked list
linked_list.append('g')
print('\nadd to the linked list with append')
print(linked_list)

#remove from end
print('\nremove from the end of the list with "pop"')
print('popped element is:', linked_list.pop())

print('\nadd elements from left side of linked list with "appendleft"')
linked_list.appendleft('z')
print(linked_list)

print('\nremove elements from left side of lnked list with "popleft"')
print('popped element is: ', linked_list.popleft())

#Implementing a queue (FIFO), for example a restaurant queue
#
queue = deque()
queue.append("John")
queue.append("Paul")
queue.append("George")
queue.append("Ringo")
print('\n',queue)

#removing the head element
print('Popping the first customer in the queue',queue.popleft())
print('Popping the next customer in the queue', queue.popleft())

#Implementing a stack
#for example the back button or history on a web browser
#items get add to the left of the stack and then popped from the left
print('\nImplementing a stack, (LIFO)')
history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
print(history)
print('\nremoving the most recent entry from the stack with popleft()')
print('the last web address was:', history.popleft())