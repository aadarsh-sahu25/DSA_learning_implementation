# circular linked list implementation

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    def __init__(self):
        self.head=None
        self.end=None
        self.count=0
    def insertion(self,data):
        newNode=node(data)
        self.count+=1
        newNode.next=self.head
        if self.head is None:
            self.head=self.end=newNode
            self.end.next=self.head
        else:
            self.end.next=newNode
            newNode.next=self.head
            self.end=newNode
    def insertionAt_beg(self,data):
        newNode=node(data)
        self.count+=1
        if self.head is None:
            self.head=self.end=newNode
            self.end.next=self.head
            return
        else:
            newNode.next=self.head
            self.end.next=newNode
            self.head=newNode

    def insertionAfter_value(self,value,data):
        if self.head is None:
            return
        temp=self.head
        while temp.next!=self.head and temp.data!=value:
            temp=temp.next
        if temp.data!=value:
            print(value,' is not in the list')
            return
        else:
            newNode=node(data)
            self.count+=1
            '''
            if temp==self.head:
                newNode.next=self.head.next
                self.head.next=newNode
                if self.head==self.end:
                    self.end=newNode
            else:
                newNode.next=temp.next
                temp.next=newNode
                if temp==self.end:
                    self.end=newNode
                '''
            newNode.next=temp.next
            temp.next=newNode
            if temp==self.end:
                self.end=newNode
            
    def delnAt_beg(self):
        if self.head is None:
            return
        else:
            self.count-=1
            if self.head==self.end:
                self.head=self.end=None
            else:
                self.head=self.head.next
                self.end.next=self.head

    def delnAt_end(self):
        if self.head is None:
            return
        self.count-=1
        temp=self.head
        while temp!=self.end:
            temp1=temp
            temp=temp.next
        if temp==self.head:
            self.head=self.end=None
        else:
            temp1.next=self.head
            self.end=temp1

    def delnGiven_value(self,data):
        if self.head is None:
            return 
        
        if self.head.data==data:
            self.count-=1
            if self.head==self.end:
                self.head=self.end=None
            else:
                self.head=self.head.next
                self.end.next=self.head
            return
        temp=self.head
        while temp.next!=self.head and temp.data!=data:
            temp1=temp
            temp=temp.next
        if temp.data!=data:
            print(data,' not present in the list')
            return
        else:
            self.count-=1
            temp1.next=temp.next
            if temp==self.end:
                self.end=temp1
    def display(self):
        if self.head is None:
            print('list is empty')
            return
        temp=self.head
        while temp.next!=self.head:
            print('->',temp.data,end='')
            temp=temp.next
        print('->',temp.data)
        

list4=CLL()
list4.insertion('s')
list4.insertion('h')
list4.insertion('a')
list4.insertion('i')
list4.insertionAfter_value('a','n')
list4.insertionAfter_value('s','u')
list4.display()
print('no. of elements in the list: ',list4.count)
list4.delnGiven_value('n')
list4.delnAt_end()
list4.display()
print('no. of elements in the list: ',list4.count)


            
            
            
