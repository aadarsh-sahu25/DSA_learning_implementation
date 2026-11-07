# Queue 🚶

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle, where the first element inserted is the first one to be removed.

## Operations

- **Enqueue:** Insert an element at the rear of the queue.
- **Dequeue:** Remove an element from the front of the queue.
- **Front / Peek:** Retrieve the front element without removing it.
- **isEmpty:** Check whether the queue is empty.
- **Size:** Return the number of elements in the queue.

## Implementation

- Queue using Python List
- Queue using Linked List
- Circular Queue 

## Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Enqueue | O(1)* |
| Dequeue | O(1)* |
| Front / Peek | O(1) |
| isEmpty | O(1) |
| Size | O(1) |

\*Assuming an efficient implementation, such as a linked list with front and rear pointers or Python's `collections.deque`.
