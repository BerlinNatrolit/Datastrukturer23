from Node import Node
from LinkedList import LinkedList

class Queue:
    # Create an empty list that is used in the queue.
    def __init__(self):
        self.llist = LinkedList()
    
    # add an element to the queue.
    def enqueue(self, item):
        self.llist.append(item)

    # remove and return the last element that was added.
    def dequeue(self):
        return self.llist.remove_first()

    # Check if the queue is empty. (if llist is 0, it is by definition empty)
    def is_empty(self):
        return len(self.llist) == 0

    # The tail of llist is the last element, and therefore it is enough to
    # look at this element for peek.
    def peek(self):
        return self.llist.tail

    # len of llist is giving the number of items in the list,
    # so we can just return this.
    def size(self):
        return len(self.llist)


if __name__ == "__main__":
    queue = Queue()

    n1 = Node(1)
    n2 = Node(2)

    print("is empty: " + str(queue.is_empty()))

    queue.enqueue(n1)
    queue.enqueue(n2)

    print("is empty: " + str(queue.is_empty()))
    print("Queue.peek: " + str(queue.peek()))

    print("Queue.pop:" + str(queue.dequeue()))
    print("Queue.peek: " + str(queue.peek()))