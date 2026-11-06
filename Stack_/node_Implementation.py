# creating a node in a way that could behave as top of the stack
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None

class Stack:    

    def __init__(self):
        self.top=None
        self.__size=0

    def push(self,data):
        newNode=node(data)
        self.__size+=1
        if self.top is None:
            self.top=newNode
        else:
            newNode.prev=self.top
            self.top=newNode

    def pop(self):
        self.__size-=1
        if self.top is None:
            return None
        else:
            temp=self.top.data
            self.top=self.top.prev
            return temp

    def seek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def display_stack(self):
        temp=self.top
        i=0
        while temp:
            i=1
            print(temp.data,end=' -> ')
            temp=temp.prev
        if(i==0):
            print('stack is empty!')
            return
        print()

    def IsEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    def size(self):
        return self.__size

stack1=Stack()
print(stack1.IsEmpty())
stack1.push(93)
stack1.push(81)
stack1.display_stack()

print(stack1.pop())
stack1.push(45)
stack1.push(33)
stack1.push(18)
print('size of the stack:- ',stack1.size())
stack1.push('7')
stack1.push('Mahi')
print(stack1.pop())
stack1.display_stack()
print('size of the stack:- ',stack1.size())

