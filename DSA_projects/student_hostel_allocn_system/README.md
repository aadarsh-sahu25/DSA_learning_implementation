# Hostel Management System

This project is a simple Python-based hostel allocation system that helps manage student records using a doubly linked list. It stores student information, checks room availability, searches records, updates details, deletes records, and counts the number of allocated students.

You can open the main program here: [management.py](management.py)

---

## 1. Project overview

The system is designed for a hostel office where a manager can:

- allocate a room to a new student
- continue allocation for an existing student
- view all student records
- search a student by student ID
- update student details
- remove a student when they leave or are de-allocated
- count the total number of students currently allocated

This is a real-world mini-project that combines:

- data structure logic
- menu-driven application design
- user validation
- room allocation rules
- record management

---

## 2. Why this project is useful

This project is helpful because it demonstrates how a real management system can be built using a data structure instead of a database. It is simple enough for beginners to understand, but it still uses important programming ideas such as:

- classes and objects
- linked list operations
- conditional logic
- loops and validation
- user interaction through input/output

In short, it teaches how software can reflect a real hostel office process.

---

## 3. Project structure and logic

The program uses a custom node structure and a doubly linked list.

### Node design

A `node` contains:

- `data` -> stores the student information in a dictionary
- `prev` -> pointer to the previous node
- `next` -> pointer to the next node

### SMS class

The `SMS` class is the main system class. It handles all major actions such as:

- adding a student
- checking if a student ID already exists
- allocating a room
- displaying all records
- searching a single record
- updating details
- deleting a record
- counting total allocations

---

## 4. Sequential workflow of the project

### Step 1: Start the program
When the program runs, it displays a menu:

1. Student Allocation
2. Display All Allocations
3. Search Student Allocation
4. Update Student Details
5. Delete Student Allocation
6. Count of total no. of allocations
0. Exit

### Step 2: User chooses an action
The user enters a number from the menu.

### Step 3: Allocation process
If the user selects allocation, the code asks:

- whether the student is new or continuing
- student ID
- candidate name
- course
- semester
- email
- contact number
- room number

If the student is continuing, the program checks their previous semester CGPA.

- if CGPA is below 7.0, allocation is denied
- if CGPA is 7.0 or above, the student is allowed

### Step 4: Room validation
Each room has a capacity of 2 students. The project checks room occupancy before assigning a room.

- if a room already has 2 students, it refuses the room
- otherwise, it assigns the room and stores it in the student record

### Step 5: Saving record in linked list
The student record is stored as a node and linked into the doubly linked list.

This allows the program to:

- move forward through records
- move backward through records
- insert new students at the end
- remove students easily
- search by ID efficiently

### Step 6: Search and display
The system can display:

- all allocated students
- a single student based on student ID

### Step 7: Update operation
The user can update details such as:

- candidate name
- course
- semester
- email
- contact number
- room number

The code prevents updates to protected fields like `student-id` and previous CGPA.

### Step 8: Deletion operation
When a student is removed:

- their ID is removed from the list
- their room is freed
- the linked list is adjusted to maintain proper node connections

### Step 9: Total count
The total number of allocations is counted using a list of student IDs.

---

## 5. Core logic explained simply

### Unique ID check
Every student has a unique ID. The program checks whether the ID already exists before adding a new student.

If the ID already exists, the program prints a message and rejects the duplicate entry.

### Room allocation logic
The code uses this idea:

- each room should not hold more than 2 students
- the room list stores all assigned room names
- if `count(room) == 2`, the room is full

This prevents over-booking.

### Search logic
To find a student, the program starts from the head of the linked list and moves node by node until it finds the target student ID.

If the ID is not found, it prints a message saying there is no allocation for that student.

### Update logic
The update function loops through the student details dictionary and asks whether the user wants to modify each field. If the user confirms, the value is replaced with the new value.

### Delete logic
The delete operation removes the selected node and reconnects the linked list so the remaining entries still stay in order.

---

## 6. Creativity and design ideas

This project is creative because it applies a data structure to a real-life problem. Instead of storing data in a simple list, it uses a doubly linked list, which is more realistic for dynamic management systems.

The creative elements include:

- using a student record dictionary to store multiple fields
- limiting room capacity rules
- validating CGPA for continuing students
- handle real-world hostel management operations
- keeping the interface menu-driven and beginner-friendly

This is a nice example of how DSA can be used in practical software.

---

## 7. Data flow in one simple cycle

The life cycle of one student record is:

1. User enters student information
2. Program validates ID and room capacity
3. Record is saved in a node
4. Node is linked in the doubly linked list
5. Data can be displayed, searched, updated, or deleted
6. Room and student records stay consistent throughout

This is the basic workflow of any management system.

---

## 8. How to run the project

First, make sure Python is installed. Then run:

```bash
python3 management.py
```

If you use Python 3 on your system, this command will start the menu-based hostel management system.

---

## 9. Example use case

A hostel manager might do the following:

- allocate 20 students in different rooms
- search a specific student by ID
- update contact information
- remove a student after check-out
- count how many students are currently staying

The system works as a lightweight hostel record manager.

---

## 10. Git pre-commit hook

A pre-commit hook helps prevent bad code from being committed. This project includes a simple hook that checks Python syntax before the commit is accepted.

The hook file is here: [.githooks/pre-commit](.githooks/pre-commit)

### Activate the hook

Run these commands in the terminal:

```bash
chmod +x .githooks/pre-commit
git config core.hooksPath .githooks
```

After that, every commit will run the hook automatically.

### What the hook does

It checks whether [management.py](management.py) can be compiled successfully:

```bash
python3 -m py_compile management.py
```

If there is a syntax error, the commit is blocked.

---

## 11. Useful links

- [Python official website](https://www.python.org/)
- [Git hooks documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [Doubly linked list concept](https://en.wikipedia.org/wiki/Doubly_linked_list)
- [Project file](management.py)

---

## 12. Future Improvements

- Add persistent file/database storage
- Add room-wise student listing
- Add hostel vacancy statistics
- Add authentication for hostel administrators
- Improve input validation