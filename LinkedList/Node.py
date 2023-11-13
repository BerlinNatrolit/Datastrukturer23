# A node that we use in the linked list
class Node:
    #next = None         # Är en Node

    def __init__(self, data, next=None, previous=None):
        self.next = next
        self.previous = previous
        self.data = data

    def __str__(self):
        return str(self.data)