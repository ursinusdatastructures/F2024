class Node:
    def __init__(self, value):
        self.value = value
        self._next = None # Python's version of "null" is "None"
        self._prev = None
 
class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._N = 0
     
    def add_first(self, value):
        """
        Parameters
        ----------
        value: any
            Add a new node to the beginning with this value
        """
        ## TODO: Fill this in
        self._N += 1
     
    def add_last(self, value):
        ## TODO: Fill this in
        self._N += 1
     
    def remove_first(self):
        """
        Remove and return the first value from the linked list
        or do nothing and return None if it's already empty
        """
        ret = None
        ## TODO: Fill this in
        return ret

    def remove_last(self):
        """
        Remove and return the last value from the linked list
        or do nothing and return None if it's already empty
        """
        ret = None
        ## TODO: Fill this in
        return ret
         
    def __str__(self):
        # This is like the to-string method
        s = "DoublyLinkedList: "
        node = self._head
        while node: #As long as the node is not None
            s += "{} ==> ".format(node.value)
            node = node._next
        return s
     
    def __len__(self):
        # This allows us to use len() on our object to get its length!
        return self._N

if __name__ == '__main__':
    ## TODO: Update these tests
    L = DoublyLinkedList()
    L.add_first(10)
    L.add_first(4)
    L.add_first("chris")
    L.add_last("layla")
    L.add_last("theo")
    print(L)
    print(len(L))
    print(L.remove_first())
    print(L.remove_last())
    print(L)
    print(len(L))

