class Node:
    '''
    this is a map to the nodes connected to each other
    '''
    def __init__(self, data):
        '''
        created a node by accepting an item and giving it a next value of none 
        '''
        self.data = data
        # store next data
        self.next = None
        return 
    
    # check if there is data in the node 
    def hasValue(self, value):
        if self.data == value:
            return True
        return False

# creating a linked list that accepst the nodes
class linkedList:
    '''
    appending nodes, finding nodes, counting nodes, deleting nodes
    '''
    def __init__(self):
        '''
        this is just to isntantiate the begining and end of the list
        '''
        self.head = None 
        self.tail = None 
        return

    def addNode(self, item):
        '''
        adding the nodes to the list

        # item is a datatype of type node
        '''
        # check if the item is a real node object 
        if not isinstance(item, Node):
            item = Node(item)

        # check if list is empty then append to it the item that has now been made a node
        if self.head is None :
            self.head = item 
        # if it's not empty connect to previous node 
        else:
            self.tail.next = item 
            # next is used to change the Node.next of the initial value from none to the current item

        # when the last element is added 
        self.tail = item 

        return 

    def listLength(self):
        '''
        counting the number of nodes in the list
        '''
        count = 0
        start = self.head 

        # if there are nodes ...
        while start is not None:
            count +=1

            # move to the  next node 
            start = start.next

        return count
    
    def currentNode(self):
        '''
        returns the nodes currently present in the list
        '''
        current = self.head

        # loop the list
        while current is not None:
            # calling the current node data
            print(current.data)

            current = current.next

        return

    def idofNode(self, value):
        '''
        this checks for the node in the list and returns its index
        '''
        node = self.head

        index = 1

        result = []

        while node is not None:
            # check if the node has the given value
            if node.hasValue(value):
                result.append(index)
                # replace node with the next node and increase its index 
                node = node.next
                index += 1
        return result
    
    # this is why python is the best :-0 :-) no garbage

    



a = linkedList()
b = [2, 4, 3]
for i in b:
    a.addNode(Node(i))
    print(f" the length is {a.listLength()}")

