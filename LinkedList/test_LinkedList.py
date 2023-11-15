from LinkedList import LinkedList
from Node import Node
import pytest


def test_create():
    llist = LinkedList()
    assert len(llist) == 0
    assert(llist.head == None)
    assert(llist.tail == None)
    
def test_append():
    llist = LinkedList()
    n = Node(5)
    llist.append(n)

    assert(llist.head == n)
    assert(llist.head == llist.tail)    
    assert(llist.head.previous == None)
    assert(llist.tail.next == None)

def test_remove_first_from_one():
    llist = LinkedList()
    n = Node(5)
    llist.append(n)
    nr = llist.remove_first()

    assert(llist.head == None)
    assert(llist.tail == None)    
    assert(n == nr)

def test_multiple_append():
    llist = LinkedList()
    n = Node(5)
    n1 = Node(2)
    n2 = Node(17)
    llist.append(n)
    llist.append(n1)
    llist.append(n2)

    assert(llist.head == n)
    assert(llist.tail == n2)
    assert(llist.head.next == n1)
    assert(llist.tail.previous == n1)
    assert(llist.head.previous == None)
    assert(llist.tail.next == None)
    assert(not llist.head == llist.tail)
    
def test_size():
    llist = LinkedList()
    assert(len(llist) == 0)
    
    n = Node(5)
    llist.append(n)
    assert(len(llist) == 1)
    
    n1 = Node(51)
    llist.append(n1)
    assert(len(llist) == 2)