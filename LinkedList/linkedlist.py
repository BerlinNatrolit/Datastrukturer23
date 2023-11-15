from Node import Node

# Mainclass for linked list.
class LinkedList:
    head = None     	# Är en Node, first node of the linked list
    tail = None			# Last Node of the linked list.
    count_of_nodes = 0	# Keeps track of how many nodes/length of the list.

    # Count the number of items in the linked list
    # Instead of iterating through every single value
    # we are now just returning count. going from O(n) to O(1)
    def __len__(self):
        return self.count_of_nodes

    # Count the sum of all the items in the list
    # O(n)
    def sum(self):
        ans = 0
        for n in self:			# We are now using our own __iter__ generator/method/function
            ans += n.data
        return ans

    # Add items to the back of the list.
    # O(1)
    def append(self, new_node):
        if self.count_of_nodes == 0:		# When adding the first node to the list it is a bit of a special case.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail    # By replacing the while loop with tail
            self.tail.next = new_node        # we can reduce the runtime of append from O(n) to O(1)
            self.tail = new_node

        self.count_of_nodes += 1			# And lets not forget to increase the node counter so we can use it

    # removes the first element/node from the linked list.
    # O(1)
    def remove_first(self):
        temp = self.head
        
        if self.count_of_nodes == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next      # move the head to the new head.
            self.head.previous = None       # remove the link between head and the new first element.
            temp.next = None                # remove the last reference from the temp element, so that it is "flowing" freely in the eather.

        self.count_of_nodes -= 1
        if self.count_of_nodes < 0:
            self.count_of_nodes == 0
        return temp                     # return the element that we removed.

    # removes the last element/node from the linked list.
    # i am lazy here, please have a look at the comments for remove first. It works the same way. :)
    # O(1)
    def remove_last(self):
        temp = self.tail
        
        if self.count_of_nodes == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous  # move the tail to the new tail
            self.tail.next = None
            temp.previous = None

        self.count_of_nodes -= 1
        if self.count_of_nodes < 0:
            self.count_of_nodes == 0
        return temp
    
    # Generates a string representation of the linked list when print(LinkedList)
    # O(n)
    def __str__(self):						# Dunderfunktion for creating a string representation of the linked list.
        response = ""
        n = self.head
        i = 0
        while n != None:
            response = response + "index " + str(i) + ": " + str(n.data) + "\n"
            n = n.next
            i += 1
            
        return response
    
    # Method that enables us to write node in LinkedList
    # O(n)
    def __contains__(self, c):				# Does a specific node exist in the linked list.
        n = self.head						# This function is for us to be able to write "n in list".
        while n != None:
            if c == n:
                return True
            n = n.next
        return False
    
    # Generator for enabling us to write a for each over the LinkedList.
    # I.e. it makes the LinkedList iterable
    # Inspiration/reference: if you want to know a bit more and how to modify iterables, you can look at the library "itertools". Although this is not part of the course.
    # O(n)      (I verkligheten O(1) eftersom det är en generator)
    def __iter__(self):						# Iter enables us to write a for each loop over the linked list.
        n = self.head						# when yield-ing a value the method is called a generator.
        while n != None:
            yield n
            n = n.next
        


if __name__ == "__main__":
    # Lets create a bunch of nodes.
    n = Node(10)
    n2 = Node(15)
    n3 = Node(2)

    # And att them to the LinkedList llist.
    llist = LinkedList()
    llist.append(n)
    llist.append(n2)
    llist.append(n3)

    # Lets check whats in the different places, and what happens.
    print("Head: " + str(llist.head))
    print("Count: " + str(len(llist)))
    print("Sum: " + str(llist.sum()))

    # Create another node.
    n8 = Node(8)
    
    # is it in llist, we are not using the __contains__ method.
    if n8 in llist:
        print("N8 exists in llist")
    else:
        print("N8 does not exists in llist")
    llist.append(n8)	# Add it to the list.
    if n8 in llist:								# check again (with __contains__)
        print("N8 exists in llist")
    else:
        print("N8 does not exists in llist")
        
    # Iterate over the LinkedList with a foreachloop. Using __iter__
    print("Nu är vi i foreachloopen:")
    for node in llist:
        print(node)
    
    
    print("Sum: " + str(llist.sum()))
    print(llist)						# Print the entire LinkedList (thanks to __str__)

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
