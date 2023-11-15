from LinkedList import LinkedList
from Node import Node

def is_palindrome(string):
    lista = LinkedList()
    
    for l in string:
        lista.append(Node(l))
        
    while len(lista) > 1:
        t = lista.remove_first()
        b = lista.remove_last()
        if not t == b:
            return False
    
    return True
        
    
    
if __name__ == "__main__":
    print(is_palindrome("tacocatten"))