# Name: Queue.py
# Author: Robin Goyal
# Last-Modified: January 15, 2018
# Purpose: Implement ADT for Queue from a Linked List


from LList import LinkedList


class Queue(LinkedList):
    '''
    An implementation of a Queue with necessary functionality.
    A queue is a FIFO (First In First Out) data structure
    where elements can be removed from the front and added
    at the back of the data structure.

    Attributes:
        head: A pointer to the first node of the queue
        _length: An integer representing the number of current items in the queue
    '''

    def __init__(self):
        '''
        Initializes an empty queue with no nodes.

        Inherited Attributes:
            - head
            - _length
        '''

        LinkedList.__init__(self)

    def enqueue(self, item):
        '''
        item -> any type: data to add to the end of the queue
        return -> nothing

        Adds an item to the end of the queue. This functionality is
        the same as the append() method defined in the LinkedList class.

        Examples:
            - enqueue(5): 2 -> 3 ===> 2 -> 3 -> 5
            - enqueue(True): Empty Queue ===> True
            - enqueue(23.5): 2 ===> 2 -> 23.5
        '''

        LinkedList.append(self, item)

    def dequeue(self):
        '''
        return -> any type: first item in queue

        Removes and returns the first item in the queue. This
        functionality is similar to the pop() method defined
        in the LinkedList class except an argument of zero is
        necessary.

        Examples:
            - dequeue(): 6 -> 3 -> 5 ===> 3 -> 5
            - dequeue(): True -> 25 ===> 25
        '''

        return LinkedList.pop(self, 0)

    def isEmpty(self):
        '''
        return -> bool

        Returns a boolean indicating whether the queue is empty.
        The functionality is same as the isEmpty() method of the
        linked list.

        Examples:
            - isEmpty(): Empty Queue ===> True
            - isEmpty(): 2 -> 15 ===> False
        '''

        return LinkedList.isEmpty(self)

    def size(self):
        '''
        return -> int

        Returns an integer representing the length of the queue.
        The functionality is the same as the size() method of the
        linked list.

        Examples:
            - size(): Empty Queue ===> 0
            - size(): 2 -> 3 -> 4 ===> 3
        '''

        return LinkedList.size(self)
