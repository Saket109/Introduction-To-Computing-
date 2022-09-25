# creating a doubly linked list :

class Node:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.prev = None        # set the prev as none by default
        self.next = None        # set the next as none by default

class DLL:
    def __init__(self):
        self.head = None        # set the head as the None by default

    def addAtFirst(self,name,age):
        new_node = Node(name,age)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        # Don't forget to make newnode as the head of the DLL
        self.head = new_node
        
    def addAtLast(self,name,age):
        new_node = Node(name,age)
        new_node.next = None
        last = self.head            # make a last variable to store the tail of the DLL

        if self.head is None:       # if head is None then no need of the tail 
            new_node.prev = None
            self.head = new_node
            return

        while last.next is not None:        # traverse to get the tail of the Doubly linked list
            last = last.next

        last.next = new_node
        new_node.prev = last

    def deleteNode(self, dele):             # give the node as the parameter
         
        # Base Case
        if self.head is None or dele is None:
            return
         
        # If node to be deleted is head node
        if self.head == dele:               # if head has to be deleted then just change the head by head.next
            self.head = dele.next
 
        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev
     
        # Change prev only if node to be deleted is NOT
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        

    def printDLL(self):
        if self.head is None:               # if head is None then no need to print anything
            return 
        head = self.head                    # make a variable to traverse the whole linked list , so that head will remain the same
        while head is not None: 
            print(head.name,end=" , ")
            if head.next is not None:
                print(head.age ,end=" -> ")
            else:
                print(head.age,end="\n")
            head = head.next

    def printDLLReverse(self):
        if self.head is None:
            return
        last = self.head                        # use a variable to store the tail of the DLL
        while last.next is not None:  
            last = last.next

        while last is not None:                 # now traverse in the backward direction
            print(last.name,end=" , ")
            if last.prev is not None:
                print(last.age,end=" -> ")
            else:
                print(last.age,end="\n")
            last = last.prev


dllist = DLL()
dllist.addAtFirst("saket",18)
dllist.addAtLast("Kuldeep_singh",45)
dllist.addAtLast("Vandana",25)
dllist.addAtFirst(" Renu_Ahlawat",40)
dllist.addAtLast("Neha",21)
dllist.printDLL()
dllist.printDLLReverse()




# Bonus :
        # LINKING THE FAMILY MEMBERS :
    
        # 1.) if the relationship between nodes are given then we can link the family members. In this situation we have to give a extra variable to every nodes to store the relationship also.
            # this is not a good method as we have to give a lot of information in the input.
            
        # 2.) We can also relate the family members by their age gap and genders. This will not be very accurate in some cases but this is a good method as we have to store only one more 
            # information as gender.
            
