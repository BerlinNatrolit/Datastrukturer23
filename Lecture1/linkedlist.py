# A node in the linked list
class Node:
    #next = None         # Är en Node

    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)


# Mainclass for linked list.
class LinkedList:
    head = None     # Är en Node

    # Count the number of items in the linked list
    def count(self):
        n = self.head
        i = 0
        while n != None:
            n = n.next
            i = i+1
        return i

    # Count the sum of all the items in the list
    def sum(self):
        n = self.head
        i = 0
        while n != None:
            i = i + n.data
            n = n.next
        return i

    # Add items to the back of the list.
    def append(self, node):
        n = self.head
        while n.next != None:
            n = n.next
        n.next = node


if __name__ == "__main__":
    n = Node(10)
    n2 = Node(15)
    n3 = Node(2)

    llist = LinkedList()
    llist.head = n
    llist.head.next = n2
    llist.head.next.next = n3;

    print(llist.head)
    print(llist.head.next)
    print(llist.head.next.next)
    print(llist.head.next.next.next)

    print(llist.count())
    print(llist.sum())

    n8 = Node(8)
    llist.append(n8)
    print(llist.sum())
