class node:
    def __init__(self,next=None,prev=None):
        self.data={}
        self.prev=prev
        self.next=next
       
class SMS(node):
    def __init__(self, next=None, prev=None):
        super().__init__(next, prev)
        self.studentId_list=[]
        self.roomList=[]

    def setDetails(self,cg=None):
        student=node()
        id=int(input("Enter your unique student-id:- "))
        if id in self.studentId_list:
            print(f'student with student id {id} already exists.')
            student.data["student-id"]=None
            return student
        else:
            self.studentId_list.append(id)
        student.data["student-id"]=id
        student.data["candidate"]=input("Enter candidate name:- ")
        student.data["course"]=input("course:- ")
        student.data["semester"]=int(input('semester(in number):- '))
        student.data["email"]=input("Email id:- ")
        student.data["contact"]=input("contact number: ")
        x=1
        while x:
            room=input('Allocate the room number:- ')
            # taking each room has 2 vacancy
            if self.roomList.count(room)==2:
                print(f'{room} is already occupied')
            else:
                self.roomList.append(room)
                student.data['room no.']=room
                x=0
        student.data["cgpa(previous sem)"]=cg
        return student
    
    def StudentAllocation(self,head,end):
        category=int(input("press 0 for new allocn 1 for contnuing student:- "))
        cg=None
        if category==1:
            cg=float(input('previous semester cgpa:- '))
            if cg<7.0:
                print("sorry,Hostel allocation denied!")
                return(head,end)
            else:
                category=2
                
        if category==0 or category==2:
            alloted=self.setDetails(cg=cg)
            if alloted.data['student-id'] is None:
                return head,end
            if head is None :
                head=end=alloted
            else:
                end.next=alloted
                alloted.prev=end
                end=alloted
        return head,end
    def Display_All_allocn(self,head):
        print('hostel allocation list:-\n')
        temp=head
        while temp:
            for k,v in temp.data.items():
                print(k,"-> ",v)
            print("\n")
            temp=temp.next

    def Display_particularAllocn(self,head,studentId):
        print('\nsearching for ',studentId)
        temp=head
        while temp and temp.data["student-id"]!=studentId:
            temp=temp.next
        if temp is None:
            print("no allocation with studentId ",studentId) 
        else:
            print('here are the details:-\n')
            for k,v in temp.data.items():
                print(k,"-> ",v)
            print()

    def deletingAllocation(self,head,end,studentId):
        temp=head
        while temp and temp.data["student-id"]!=studentId:
                temp=temp.next
        if temp is None:
            print("no allocation with studentId ",studentId)
            
            
        else:
            self.studentId_list.remove(studentId)
            self.roomList.remove(temp.data['room no.'])
            if head==end:
                head=end=None
            elif temp==head:
                head=head.next
                head.prev=None
            elif temp==end:
                end=end.prev
                end.next=None
            else:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev

            print('student with student-id ',studentId,' has been de-allocated.')
        return head,end
    def updateStudentDetails(self,head,studentId):
        temp=head
        while temp and temp.data['student-id']!=studentId:
            temp=temp.next
        if temp is None:
            print('sorry,there is no allocation with studentId ',studentId)
            return
        for k ,v in temp.data.items():
            if k=='student-id' or k=='cgpa(previous sem)':
                continue

            print(k,'-> ',v)
            update=input('press "y" to update this: ')
            if update.lower()=='y':
                n=input(f'enter new {k} :- ')
                if k =='room no.':
                    if n==v:
                        continue
                    if self.roomList.count(n)==2:
                        print('room no. ',n,' already occupied')
                        continue
                    self.roomList.remove(v)
                    self.roomList.append(n)
                
                if v is None:
                    temp.data[k]=float(n)   # for none type cgpa(new students)
                else:
                    temp.data[k]=type(v)(n)
        print('\n\t\tdetails mentioned are updated successfully')

    
        

    def total_Allocn(self):
        return len(self.studentId_list)
    

head = end = None
allocn = SMS()

while True:

    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("       HOSTEL MANAGEMENT SYSTEM")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("1. Student Allocation")
    print("2. Display All Allocations")
    print("3. Search Student Allocation")
    print("4. Update Student Details")
    print("5. Delete Student Allocation")
    print("6. Count of total no. of allocations")
    print("0. Exit")
    print("======================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        head, end = allocn.StudentAllocation(head, end)

    elif choice == 2:
        allocn.Display_All_allocn(head)

    elif choice == 3:
        studentId = int(input("Enter the student-id you are looking for: "))
        allocn.Display_particularAllocn(head, studentId)

    elif choice == 4:
        studentId = int(input("Enter the student-id whose details you want to update: "))
        allocn.updateStudentDetails(head, studentId)

    elif choice == 5:
        studentId = int(input("Enter the student-id for whom you want to de-allocate: "))
        head, end = allocn.deletingAllocation(head, end, studentId)

    elif choice==6:
        print('total no. of allocations yet: ',allocn.total_Allocn())
    elif choice == 0:
        print("\nExiting Hostel Management System...")
        break
    
    else:
        print("\nInvalid choice! Please enter a valid option.")

    