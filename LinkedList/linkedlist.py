# A node in the linked list
class Node:
    #next = None         # Är en Node

    def __init__(self, data, next=None, previous=None):
        self.next = next
        self.previous = previous
        self.data = data

    def __str__(self):
        return str(self.data)


# Mainclass for linked list.
class LinkedList:
    head = None     # Är en Node
    tail = None
    count_of_nodes = 0

    # Count the number of items in the linked list
    # Instead of iterating through every single value
    # we are now just returning count. going from O(n) to O(1)
    def __len__(self):
        return self.count_of_nodes

    # Count the sum of all the items in the list
    def sum(self):
        n = self.head
        i = 0
        while n != None:
            i = i + n.data
            n = n.next
        return i

    # Add items to the back of the list.
    def append(self, new_node):
        if self.count_of_nodes == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail;   # By replacing the while loop with tail
            self.tail.next = new_node        # we can reduce the runtime of append from O(n) to O(1)
            self.tail = new_node

        self.count_of_nodes += 1
        
    def __str__(self):
        response = ""
        n = self.head
        i = 0
        while n != None:
            response = response + "index " + str(i) + ": " + str(n.data) + "\n"
            n = n.next
            i += 1
            
        return response
        


if __name__ == "__main__":
    n = Node(10)
    n2 = Node(15)
    n3 = Node(2)

    llist = LinkedList()
    llist.append(n)
    llist.append(n2)
    llist.append(n3)

    print("Head: " + str(llist.head))
    print("Count: " + str(len(llist)))
    print("Sum: " + str(llist.sum()))

    n8 = Node(8)
    llist.append(n8)
    print("Sum: " + str(llist.sum()))
    print(llist)

    """
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
    """
