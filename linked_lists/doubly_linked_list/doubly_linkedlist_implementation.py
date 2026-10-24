#Doubly linked list implementation and understanding efficient use of prev and next pointer/reference
class node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DLL:
    def __init__(self):
        self.head=None
        self.end=None
        self.count=0
    def insertion(self,data):
        newNode=node(data)
        self.count=self.count+1
        if self.head is None:
            self.head=self.end=newNode
        else:
            self.end.next=newNode
            newNode.prev=self.end
            self.end=newNode
    def insertionAt_beg(self,data):
        newNode=node(data)
        self.count=self.count+1
        if self.head is None:
            self.head=self.end=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insertionAfter_value(self,value,data):
        if self.head is None:
            return
        temp=self.head
        while temp and temp.data!=value:
            temp=temp.next
        if temp is None:
            print(value,' is not present in the list')
            return
        else:

            newNode=node(data)
            self.count=self.count+1
            
            newNode.next=temp.next
            newNode.prev=temp
            if temp.next:
                temp.next.prev=newNode
            else:
                self.end=newNode
            temp.next=newNode

    def insertionAt_ith(self,posn,data):
        if posn<1:
            print('invalid position!')
            return
        newNode=node(data)
        self.count=self.count+1
        if self.head is None:
            self.head=self.end=newNode
            return
        temp=self.head
        i=1
        while temp and i<posn:
            i+=1
            temp=temp.next
        if temp is None:
            self.end.next=newNode
            newNode.prev=self.end
            self.end=newNode
        else:
            if temp==self.head:
                self.head.prev=newNode
                newNode.next=self.head
                self.head=newNode
            else:
                newNode.next=temp
                newNode.prev=temp.prev
                temp.prev.next=newNode
                temp.prev=newNode


    def delnAt_beg(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=self.end=None
        else:
            #self.head.next.prev=None
            #self.head=self.head.next
            self.head=self.head.next
            self.head.prev=None
        self.count=self.count-1

    def delnAt_end(self):
        if self.end is None:
            return
        if self.head.next is None:
            self.head=self.end=None
        else:
            self.end=self.end.prev
            self.end.next=None
        self.count=self.count-1
    def deleteGiven_data(self,data):
        temp=self.head
        while temp and temp.data!=data:
            temp=temp.next
        if temp is None:
            print(data,' is not present in the list')
            return
        else:
            self.count=self.count-1
            if temp==self.head:
                self.head=self.head.next
                if self.head:
                    self.head.prev=None
                else:
                    self.end=None
            else:
                temp.prev.next=temp.next
                if temp.next:
                    temp.next.prev=temp.prev
                else:
                    self.end=temp.prev

    def delnAt_posn(self,posn):
        if posn<1:
            print('invalid posn')
            return
        if self.head is None:
            return
        
        i,temp=1,self.head
        while temp and i<posn:
            i+=1
            temp=temp.next
        if temp is None:
            print('invalid posn')
            return
        self.count=self.count-1
        if temp==self.head:
            self.head=self.head.next
            if self.head:# more than one element
                self.head.prev=None
            else:# only one element
                self.end=self.head

        else:
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.prev
            else:
                self.end=temp.prev
    def display(self):
        temp=self.head
        while temp:
            print('->',temp.data,end='')
            temp=temp.next
        print()
    

list3=DLL()
list3.insertion(93)
list3.insertion(81)
list3.insertion('Devki')
list3.insertionAfter_value(93,33)
list3.insertionAt_beg(42)
list3.insertionAt_ith(3,63)
list3.display()
print('total elements in the list: ',list3.count)
list3.deleteGiven_data(81)
list3.display()
list3.delnAt_posn(3)
list3.display
print('total elements in the list: ',list3.count)
