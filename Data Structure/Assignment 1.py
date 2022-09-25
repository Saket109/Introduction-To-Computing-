# creating a doubly linked list :

class Node:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

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

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def deleteNode(self, dele):
         
        # Base Case
        if self.head is None or dele is None:
            return
         
        # If node to be deleted is head node
        if self.head == dele:
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
        if self.head is None:
            return 
        head = self.head
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
        last = self.head
        while last.next is not None:
            last = last.next

        while last is not None:
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
