# queue implementation using node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.__size=0

    def enqueue(self,data):

        newNode=node(data)
        self.__size+=1
        if self.front is None:
            self.front=self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode

    def dequeue(self):
        if self.front is None:
            print('queue is empty!')
            return None
        else:
            self.__size-=1
            temp=self.front.data
            self.front=self.front.next
            if not self.front:
                self.rear=self.front
            return temp

    def peek(self):
        if self.front:
            return self.front.data
        else:
            return None
        
    def IsEmpty(self):
        if self.front is None:
            return True
        return False
    def lengthOf_queue(self):
        return self.__size
    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end='<-')
            temp=temp.next
        print()

que1=queue()
que1.enqueue('MAHI')
que1.enqueue('THALA')
que1.enqueue('Captain Cool')
print('length of the queue :- ',que1.lengthOf_queue())
que1.enqueue('GOAT')
que1.enqueue('7781')
que1.display()
print(que1.dequeue())
print(que1.peek())
que1.display()
print('length of the queue :- ',que1.lengthOf_queue())
