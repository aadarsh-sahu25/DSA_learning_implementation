# Circular Linked List 🔄

This folder contains my implementation of a Circular Singly Linked List in Python using nodes.

Unlike a normal singly linked list, the last node of a circular linked list points back to the first node instead of pointing to `None`.

## Operations Implemented

- Insertion at the beginning
- Insertion at the end
- Insertion after a given value
- Deletion from the beginning
- Deletion from the end
- Deletion of a given value
- Displaying the list
- Counting the number of nodes

## How It Works

The implementation uses three variables:

- `head` – points to the first node.
- `end` – points to the last node.
- `count` – keeps track of the total number of nodes.

The main thing to remember in a circular linked list is that the last node always points back to the head.

```python
end.next = head
```

This connection needs to be maintained whenever nodes are inserted or deleted.

## Time Complexity

| Operation | Complexity |
|---|---|
| Insertion at the beginning | O(1) |
| Insertion at the end | O(1) |
| Insertion after a given value | O(n) |
| Deletion from the beginning | O(1) |
| Deletion from the end | O(n) |
| Deletion of a given value | O(n) |
| Display | O(n) |
| Getting the node count | O(1) |

## CLL vs SLL vs DLL

| Feature | SLL | DLL | CLL |
|---|---|---|---|
| Pointers in each node | One | Two | One |
| Last node points to | `None` | `None` | `head` |
| Forward traversal | Yes | Yes | Yes |
| Backward traversal | No | Yes | No |
| Insertion at the beginning | O(1) | O(1) | O(1) |
| Insertion at the end | O(1)* | O(1)* | O(1) |
| Deletion from the end | O(n) | O(1)* | O(n) |

*Assumes the list maintains a tail pointer; DLL deletion from the end is O(1) when the tail's `prev` pointer is available.*

## What I Learned

While implementing a circular linked list, I practised working with node pointers, handling different insertion and deletion cases, and maintaining the circular connection between the last and first nodes.

I also learned how CLL differs from SLL and DLL and how to analyse the time complexity of different operations.

**Language:** Python
