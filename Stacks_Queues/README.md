# Stacks and Queues Implementation

This folder contains Python implementations for **Stacks** and **Queues** from scratch, along with their respective use cases. These implementations avoid using built-in Stack or Queue APIs, relying instead on lists or custom-built data structures.

---

## Features

### **Task 1: Stack Implementation**
The stack is implemented from scratch with the following functionalities:
- `push(element)`: Pushes an element onto the stack.
- `pop()`: Removes and returns the latest (top) element from the stack.
- `peek()`: Returns the latest (top) element without removing it.
- `size()`: Returns the size of the stack.
- **Validation Test**: Includes a FIFA player stack example that pushes, pops, and peeks players.

### **Task 2: Evaluate Arithmetic Expression**
A function `evaluate(expression)` evaluates arithmetic expressions using the custom stack implementation:
- Supports operators: `+`, `-`, `*`, `/`.
- Handles parentheses and ignores whitespace.
- Returns `NaN` for invalid expressions or division by zero.
- **Validation Test**: Includes test cases for valid, invalid, and edge-case expressions.

### **Task 3: Queue Implementation**
The queue is implemented from scratch with the following functionalities:
- `enqueue(element)`: Adds an element to the queue.
- `dequeue()`: Removes and returns the earliest (front) element from the queue.
- `poll()`: Returns the earliest (front) element without removing it.
- `size()`: Returns the size of the queue.
- **Validation Test**: Includes a FIFA player queue example for enqueue, dequeue, and poll operations.

### **Task 4: Stack Using Two Queues**
A stack is implemented using two instances of the custom queue class:
- `push(element)`: Pushes an element onto the stack.
- `pop()`: Removes and returns the latest (top) element from the stack.
- `peek()`: Returns the latest (top) element without removing it.
- `size()`: Returns the size of the stack.
- **Validation Test**: Includes test cases for edge scenarios like peeking and popping from an empty stack.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bshussein/DSA_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd Stacks_Queues
   ```
3. Run the Python script:
   ```bash
   python Stacks_Queues.py
   ```

---

## Example Usage

### **Task 1: Stack Example**
```python
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30
print(stack.pop())   # Output: 30
print(stack.size())  # Output: 2
```

### **Task 2: Evaluate Arithmetic Expression**
```python
expression = "(2 + 3) * (4 - 1)"
result = evaluate(expression)
print(result)  # Output: 15
```

### **Task 3: Queue Example**
```python
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.poll())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.size())  # Output: 2
```

### **Task 4: Stack Using Two Queues**
```python
stack = StackWithTwoQs()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30
print(stack.pop())   # Output: 30
print(stack.size())  # Output: 2
```

---

## Test Cases

The following test cases are included to validate the implementation:
1. Stack operations (`push`, `pop`, `peek`, `size`) with various data types.
2. Expression evaluation with valid, invalid, and edge cases.
3. Queue operations (`enqueue`, `dequeue`, `poll`, `size`) with data integrity checks.
4. Edge scenarios for stack using two queues, including empty stack operations.

---

This implementation demonstrates foundational programming skills by building these structures from scratch and validating their correctness with real-world-inspired test cases.
