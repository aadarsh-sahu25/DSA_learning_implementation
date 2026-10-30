# circular doubly linked list implementation with its features
class node:
    def __init__(self,data=None):
        self.data=data
        self.prev=None
        self.next=None

class CDLL:
    def __init__(self):
        self.head=None
        self.end=None
        self.length=0

    def insertion(self,data):
        newNode=node(data)
        self.length+=1
        if self.head is None:
            self.head=self.end=newNode
            
        else:
            self.end.next=newNode
            self.end=newNode
        
        self.end.next=self.head
        self.head.prev=self.end

    def insertionAt_beg(self,data):
        newNode=node(data)
        self.length+=1
        if self.head is None:
            self.head=self.end=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

        self.head.prev=self.end
        self.end.next=self.head

    def insertionAt_ith(self,posn,data):
        if posn<1:
            print('invalid position!')
            return
        newNode=node(data)
        
        if self.head is None:
            self.length+=1
            self.head=self.end=newNode
            self.head.prev=self.end
            self.end.next=self.head
            return
        if posn>self.length:
            self.end.next=newNode
            newNode.prev=self.end
            newNode.next=self.head
            self.head.prev=newNode
            self.end=newNode

            self.length+=1
            return
        else:
            self.length+=1
            temp,i=self.head,1
            while i!=posn:
                i+=1
                temp=temp.next

            newNode.next=temp
            if temp!=self.head:
                temp.prev.next=newNode
                newNode.prev=temp.prev
                temp.prev=newNode

            else:
                temp.prev=newNode
                self.head=newNode
                self.head.prev=self.end
                self.end.next=self.head



    def delnAt_beg(self):
        if self.head is None:
            return
        else:
            self.length-=1
            if self.head==self.end:
                self.head=self.end=None
            else:
                self.head=self.head.next
                self.head.prev=self.end
                self.end.next=self.head

    def delnAt_end(self):
        if self.head is None:
            return
        else:
            self.length-=1
            if self.head==self.end:
                self.head=self.end=None
            else:
                self.end=self.end.prev
                self.end.next=self.head
                self.head.prev=self.end

    def delnOf_ith_value(self,posn):
        if self.head is None:
            return
        if posn<1 or posn>self.length:
            print('invalid position!')
            return
        temp,i=self.head,1
        self.length-=1
        while i!=posn:
            i+=1
            temp=temp.next

        if temp==self.head:
            if self.head==self.end:
                self.head=self.end=None
            else:
                self.head=self.head.next
                self.head.prev=self.end
                self.end.next=self.head
        else:
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            if temp==self.end:
                self.end=temp.prev

    def display(self):
        temp=self.head
        while temp!=self.end:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
        
list5=CDLL()
list5.insertion("Dhoni")
list5.insertionAt_beg("Mahendra")
list5.insertionAt_ith(2,"Singh")
list5.display()
print('total no. of elements in the linked-list:- ',list5.length)
list5.delnAt_beg()
list5.insertionAt_ith(1,'Mahi')
list5.delnOf_ith_value(2)
list5.delnAt_end()
list5.insertionAt_ith(5,'maar')
list5.insertionAt_ith(7,'rha hai')
list5.display()
print('total no. of elements in the linked-list:- ',list5.length)

    
