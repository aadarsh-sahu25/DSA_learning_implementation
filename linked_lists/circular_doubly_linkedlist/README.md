# Circular Doubly Linked List (CDLL) 🔗

A Circular Doubly Linked List is a linked list in which each node contains three things:

- `data`: Stores the value.
- `next`: Points to the next node.
- `prev`: Points to the previous node.

Unlike a normal doubly linked list, the last node points back to the first node, and the first node points back to the last node. This creates a circular structure in both directions.

## Structure

Each node contains:

- `data`
- `next`
- `prev`

The list maintains three attributes:

- `head`: Points to the first node.
- `end`: Points to the last node.
- `length`: Keeps track of the total number of nodes.

The following conditions are maintained:

- `end.next` points to `head`.
- `head.prev` points to `end`.

## Operations Implemented

### 1. Insertion at the End

`insertion(data)`

Creates a new node and adds it after the current last node. The `end` pointer is updated, and the circular connections are maintained.

### 2. Insertion at the Beginning

`insertionAt_beg(data)`

Creates a new node before the current head and updates the `head` pointer. The new node is connected to the previous last node to maintain the circular structure.

### 3. Insertion at a Given Position

`insertionAt_ith(posn, data)`

Inserts a new node before the node at the specified 1-based position.

If the given position exceeds the current length, the node is inserted at the end. Positions less than 1 are treated as invalid.

### 4. Deletion at the Beginning

`delnAt_beg()`

Removes the first node and moves the `head` pointer to the next node. The circular connections are updated accordingly.

### 5. Deletion at the End

`delnAt_end()`

Removes the last node and updates the `end` pointer to the previous node.

### 6. Deletion at a Given Position

`delnOf_ith_value(posn)`

Traverses the list to locate the node at the specified 1-based position and removes it by updating the previous and next nodes' pointers.

Invalid positions are handled without modifying the list.

### 7. Display

`display()`

Traverses the list starting from `head` and prints each node's data until it reaches the last node.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Insertion at the end | O(1) |
| Insertion at the beginning | O(1) |
| Insertion at a given position | O(n) |
| Deletion at the beginning | O(1) |
| Deletion at the end | O(1) |
| Deletion at a given position | O(n) |
| Display | O(n) |

## Example

```python
list5 = CDLL()

list5.insertion("Dhoni")
list5.insertionAt_beg("Mahendra")
list5.insertionAt_ith(2, "Singh")

list5.display()
```

Output:

```text
Mahendra->Singh->Dhoni
```

The implementation maintains both forward and backward links while keeping track of the number of elements using `length`.
