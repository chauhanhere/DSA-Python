#n.next==n.next
#class to create a new node 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    #for traversing the LL
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        n=self.head #for our convenience
        while n!=None:
            print(n.data,"-->",end="")
            n=n.next

    #for adding the node as the first node
    def add_begin(self,data):
        new_node=node(data)#object of node class
        new_node.next=self.head
        self.head=new_node

    #for adding the node as the last node
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:#if LL is empty
            self.head=new_node
        else:#List is not empty
            n=self.head
            while n.next!=None:
                n=n.next
            n.next=new_node

    #for adding the node atfter the particular/given node
    def add_after_node(self,given_data,data_toinsert):
        n=self.head
        while n is not None:#if the node is not null then this while will execute
            if given_data==n.data:
                break
            n=n.next
        if n is None:
            print("Data is not int the list")
            return 
        else:
            new_node=node(data_toinsert)
            new_node.next=n.next#adding the next of the node n to the next of new_node because the new_node is going to be added after the n 
            n.next=new_node #adding the new_node after the valid given node
            
    #for adding the node before the particular/given node
    def add_before_node(self,given_data,data_toinsert):
        if self.head is None:
            print("Linked list is empty")
            return 
        if self.head.data==given_data:#This means add data as the first node
            new_node=node(data_toinsert)#object of node class
            new_node.next=self.head
            self.head=new_node
            return 
        n=self.head
        while n.next is not None:#if it is not NULL
            if n.next.data==data_toinsert():
                break #This is the node where to insert data
            n=n.next# go to next node
        if n.next is None:#node is not in the list where we have insert the data
            print("Node is not found")
            return 
        else:#same as else part of insert_after_node
            new_node=node(data_toinsert)
            new_node.next=n.next
            n.next=nuw_node

    def del_first_node(self):
        if self.head is None:
            print("Underflow/LL is already empty,so we cant delete node")
            return 
        self.head=self.head.next

    def del_last_node(self):
        if self.head is None:
            print("Linked List is already empty,so we cant delete node")
            return 
        else:#List is not empty
            n=self.head
            while n.next.next is not None:#checking for the second last node of the list
                n=n.next
            n.next=None #this condition will execute when while loop terminate while means we get the send last node then assign the None to the second last node
            
    def del_particular_node(self,data_to_delete):
        if self.head is None:
            print("Linked List is already,so we cant delete node")
            return
        if self.head.data==data_to_delete:#it is the first node which we want to delete
            self.head=self.head.next
        n=self.head
        while n.next is not None:
            if n.next.data==data_to_delete:
                break
            n=n.next
        if n.next==None:
            print("Data is not in the list which you want to delete")
            return 
        n.next=n.next.next#assigning the of the next of the node which we want to delete to the previous of the node,by this way we can delete a particular node             

LL1=LinkedList()
LL1.add_begin(20)
LL1.add_before_node(20,52)
LL1.print_LL()
LL1.del_particular_node(22)
LL1.print_LL()
                
    
