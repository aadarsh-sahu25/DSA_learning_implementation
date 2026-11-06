# Approach:-  linked list with just insertion at beg and deletion at beg option (i.e Last IN First OUT)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.__length=0

    def push(self,data):    # insertion at beg
        newNode=node(data)
        self.__length+=1
        if self.top is None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode

    def pop(self):
        if self.top is None:
            return None
        self.__length-=1
        temp=self.top.data
        self.top=self.top.next
        return temp

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data
    def display_stack(self):
        if self.top is None:
            print('stack is empty!')
            return
        
        temp=self.top
        while temp:
            i=1
            print(temp.data,end='->')
            temp=temp.next
        print()


    def IsEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    
    def size(self):
        return self.__length

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

