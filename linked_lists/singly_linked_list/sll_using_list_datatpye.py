# implementation of linked list using list datatype of python

class SLL:
    def __init__(self):
        self.lis=[]

    def insertion(self,data):
        self.lis.append(data)

    def insertionAt_beg(self,data):
        self.lis.insert(0,data)
    def insertionAt_index(self,index,data):
        if index>=0 and index<=len(self.lis):
            self.lis.insert(index,data)
        else:
            print('invalid index!')
    def insertionAfter_value(self,value,data):
        if value in self.lis:
            self.lis.insert(self.lis.index(value)+1,data)
        else:
            print(value,' is not present in the linked list')

    def deletionAtend(self):
        #self.lis.pop()     to return the deleted data
        if self.lis:
            del(self.lis[-1])
        else:
            print('list is empty')
    def deletionAt_beg(self):
        if self.lis:
            self.lis.pop(0)
            #del(self.lis[0])   to return the deleted data
        else:
            print('list is empty')
    def deletionAt_index(self,index):
        if index in range(len(self.lis)):
            del(self.lis[index])
        else:
            print('invalid index!')
    def deleteGiven_data(self,data):
        if data in self.lis:
            self.lis.remove(data)
        else:
            print(data,' not present in the linked list')
    def display(self):
        for i in self.lis:
            print(" -> ",i,end='')
        print()
    def count_element(self):
        return len(self.lis)

list2=SLL()
list2.insert(7)
list2.insert(8)
list2.insertionAt_beg(10)
list2.insertionAfter_value(8,18)
list2.insert(42)
list2.insertionAt_index(6,45)
list2.display()
print('total no. of elements in the list:- ',list2.count_element)
list2.deleteGiven_data(10)
list2.deletionAt_index(0)
list2.display()
'''
problem with linked list implementation is that user can perform unsual operations 
not valid for linked list but may be for list data type in python 
can prevent from overidding of the methods define for list but it's a hectic job to do.
'''
#list2.lis.extend()  (limitations)
