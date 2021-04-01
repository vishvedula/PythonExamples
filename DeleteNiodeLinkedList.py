'''
To delete a node from linkedlist
'''

class Node: #define the class
    def __init__(self,data): #define the constructor
        self.data = data
        self.next = None
    
class LinkedList: #define the parent class
    def __init__(self): #define the constructor
        self.head = None # define the head of the LinkedList
    
    def push(self, data): # define normal function for adding elements to LL
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next # 4, 3
            
    def deleteNode(self,deleteNode):        
        current = self.head
       # base condition, if 1st node itself is to be removed
        if current is not None:
            if current.data == deleteNode:
                self.head = current.next
                current  = None
                return
            # if the node belongs somewhere in between    
            while current is not None:
                if current.data == deleteNode:
                    break
                prev = current
                current = current.next
            
            prev.next = current.next
        else:
            print(f'No elements in the linkedlist')
           
            
        
    
LL = LinkedList()
LL.push(3)
LL.push(4)
LL.push(5)
LL.push(6)
print(f'the elements in the linkedlist are')
LL.printList()
LL.deleteNode(4)
print(f'Elements after deletion')
LL.printList()
         
    
        
