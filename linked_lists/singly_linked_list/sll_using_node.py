# linked list implemented with various operations using class and objects
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.end=None

    def insertion(self,data):
        newNode=node(data)
        if self.head is None:
            self.end=self.head=newNode
        else:
            self.end.next=newNode
            self.end=self.end.next

    def insertionAt_beg(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=self.end=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def insertionAfter_value(self,value,data):
        temp=self.head
        while temp and temp.data!=value:
            temp=temp.next
        if temp is None:
            print(value,' is not present in the list!')
            return
        else:
            newNode=node(data)
            newNode.next=temp.next
            if temp==self.end:
                self.end=newNode
            temp.next=newNode

    
    # if index> lenght of current linked list (then insert at end)
    def insertionAt_ith(self,index,data):  
        if index<1:
            print('invalid index')
            return
        newNode=node(data)
        if self.head is None:
            self.head=self.end=newNode
            return
        temp,i=self.head,1
        while temp and i<index:
            i+=1
            temp1=temp
            temp=temp.next
        if temp is None:
            temp1.next=newNode
            self.end=newNode
            return
        if temp==self.head:
            newNode.next=temp
            self.head=newNode
        else:
            temp1.next=newNode
            newNode.next=temp

    def delnAt_beg(self):
            if self.head is None:
                return
            elif self.head.next is None:
                self.head=self.end=None
                return
            else:
                self.head=self.head.next

    def delnAt_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=self.end=None
            return
        
        temp=self.head
        while temp.next!=self.end:
            temp=temp.next
        temp.next=None
        self.end=temp

    def deletingGiven_data(self,data):
        if self.head is None:
            return
        temp1=temp=self.head
        while temp and temp.data!=data:
            temp1=temp
            temp=temp.next
        if temp is None:
            return
        if temp==self.head:
            self.head=temp.next
            if temp.next is None:
                self.end=self.head
        else:
            temp1.next=temp.next
            if temp==self.end:
                self.end=temp1
    
    def deleting_ith_element(self,index):
        if index<1:
            print('invalid index!')
            return
        i=1
        temp=self.head
        while temp and i<index:
            i=i+1
            temp1=temp
            temp=temp.next
        if temp is None:
            return
        if temp==self.head:
            self.head=temp.next
            if temp.next is None:
                self.end=self.head
        else:
            temp1.next=temp.next
            if temp==self.end:
                self.end=temp1
        
    def count_Elements(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count


    def display(self):
        temp=self.head
        print('Elements of your linked list are:- ')
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print()

list1=SLL()
list1.insertion('T')
list1.insertion('H')
list1.insertionAfter_value('H','A')
list1.insertion('L')
list1.insertion('A')
list1.display()
list1.insertionAt_beg("Mahi")
list1.deleting_ith_element(5)
list1.display()
list1.insertionAfter_value('A',7)
list1.display()
    
