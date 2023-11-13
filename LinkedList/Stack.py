from Node import Node
from LinkedList import LinkedList

class Stack:
    # Create an empty list that is used in the stack.
    def __init__(self):
        self.llist = LinkedList()

    # Lets add a value in the last position of the list
    # append is doing this for us.
    def push(self, item):
        self.llist.append(item)

    # remove and return the last element that was added.
    def pop(self):
        return self.llist.remove_last()

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
    stack = Stack()

    n1 = Node(1)
    n2 = Node(2)

    print("is empty: " + str(stack.is_empty()))

    stack.push(n1)
    stack.push(n2)

    print("is empty: " + str(stack.is_empty()))
    print("Stack.peek: " + str(stack.peek()))

    print("Stack.pop:" + str(stack.pop()))
    print("Stack.peek: " + str(stack.peek()))