class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DLL:
    def __init__(self):
        self.head=None

    def traverse_forward(self):
        if self.head==None:
            print("List is Empty")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.next
    def traverse_backward(self):
        print()#for changing the line
        if self.head==None:
            print("List is Empty")
            return 
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            while n is not None:
                print(n.data,"-->",end="")
                n=n.prev
                
    #Insert at the begining of list when it is completely empty
    def insert_begining(self,data):
        if self.head is None:#if the list is empty or not
            new_node=node(data)
            self.head=new_node
        else:
            print("LL list is not completely empty")
            
    #Insertion at the begining
            
    def insert_at_first(self,data):
        new_node=node(data)
        if self.head is None:#if the list is empty or not,if it is empty new node will bw added as the first node
            self.head=new_node
        else:#The list is not empty and we have to insert the data at the begining of LL 
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def insert_at_last(self,data):
        new_node=node(data)
        n=self.head
        if self.head is None:#If LL is empty then add this node as first node
            self.head=new_node#it will give error if we write n=new_node because it is empty,that's why i have written self.head=new_node 
        else:
            while n.next!=None:
                n=n.next
            new_node.prev=n
            new_node.next=None
            n.next=new_node
    def insert_after_given(self,data_to_insert,data_after):
        if self.head is None:
            print("DLL is empty")
            return
        else:
            n=self.head
            while n is not None:#Checking for the data is present or not,this condition gets out of this while beacuse of 2 cases,1 if the data_after is not found or we found the node where we have to insert our data
                if n.data==data_after:
                    break
                n=n.next
            if n is None:
                print("Given data is not present in DLL")
                return 
            else:
                new_node=node(data_to_insert)
                new_node.next=n.next
                new_node.prev=n
                if n.next!=None:#To check if it is not the last node after which we are inserting the new node
                    n.next.prev=new_node#if we are inserting the the node after last node,we don't have to include these lines of code
                n.next=new_node  #we have to only write this line is we are inserting our node after last node

    def insert_before_given(self,data_to_insert,data_before):
        if self.head is None:
            print("DLL is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==data_before:
                    break
                n=n.next
            if n is None:
                print("Given data is not present in DLL")
                return
            else:
                new_node=node(data_to_insert)
                new_node.next=n
                new_node.prev=n.prev
                if n.prev is not None:
                    n.prev.next=new_node
                else:#if we are adding our node as first node then make it as the heaf of DLL
                    self.head=new_node
                n.prev=new_node
                
    def delete_first(self):
        if self.head==None:
            print("DLL is already empty")
            return
        elif self.head.next==None:#if the node have only one node,then after it our head should point to None
            self.head=None
            print("DLL is now empty after deleting the single node")
        else:
            self.head=self.head.next
            self.head.prev=None

    def delete_last(self):
        if self.head==None:
            print("DLL is already empty")
            return
        elif self.head.next==None:
            self.head=None
            print("DLL is now empty after deleting the single first node")
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            #n=last node 
            n.prev.next=n.next #or n.prev.next=None,beacause next of n also contains n 
    def delete_particular(self,data_todelete):
        if self.head==None:
            print("DLL is already empty")
            return 
        elif self.head.next==None:#if DLL has only one node
            if self.head.data==data_todelete:
                self.head=None
                print("DLL is now empty after deleting the single node")
                return
            else:
                print("Data is not present in DLL")
                return
        elif self.head.data==data_todelete:#if there is more than one node and we have to delete the first node
            self.head=self.head.next
            self.head.prev=None
            return
        n=self.head
        while n.next!=None:#to delete the middle of the DLL
            if data_todelete==n.data:
                break# we have found the node which we have to delete
            n=n.next
        if n.next!=None:
            n.next.prev=n.prev
            n.prev.next=n.next
        else:
            if n.data==data_todelete:
                n.prev.next=None
            else:
                print("Data is not present in DLL")
                    
            
dll=DLL()
dll.insert_begining(10)
dll.insert_at_first(11)
dll.delete_particular(10)
dll.traverse_forward()

            
