
# Binary Search Tree (BST) Implementation

This folder contains a Python implementation of a **Binary Search Tree (BST)** to process and manage student records from a given input file. The tasks include building the tree, performing depth-first and breadth-first traversals, and writing the results to output files.

---

## Features

### **Task 1: Build a Binary Search Tree**
- Build a BST using student records from the input file.
- Each student record is represented as a node in the tree.
- The tree is ordered by the student's last name (case-insensitive).
- Supports operations:
  - **Insertion**: Insert a student record into the BST.
  - **Deletion**: Remove a student record from the BST based on the last name.

### **Task 2: Depth-First (In-Order) Traversal**
- Traverse the BST recursively in ascending order (left-root-right).
- Print the nodes in logical order and write the results to a file (`in_order_traversal.txt`).

### **Task 3: Breadth-First Traversal**
- Traverse the BST level-by-level, starting from the root and proceeding downwards.
- Use a queue to implement the traversal and write the results to a file (`breadth_first.txt`).

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bshussein/DSA_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd Tree
   ```
3. Ensure the input file `tree-input.txt` is present in the same folder as the script.
   - Update the file path in the script if necessary.
4. Run the Python script:
   ```bash
   python Tree.py
   ```

---

## Example Usage

### **Building the BST**
```python
bst = BST()
bst.read_data("tree-input.txt")  # Read data from input file
```

### **Depth-First Traversal**
```python
# Write in-order traversal to a file
bst.write_in_order(bst.root, "in_order_traversal.txt")
```

### **Breadth-First Traversal**
```python
# Write breadth-first traversal to a file
bst.breadth_first("breadth_first.txt")
```

---

## Input File Format

The input file (`tree-input.txt`) contains an arbitrary number of student records in the following format:

```
Operation code: 1 character ('I' for insert, 'D' for delete)
Student number: 7 characters
Student last name: 25 characters
Home department: 4 characters
Program: 4 characters
Year: 1 character
```

### Example Input:
```
I1234567Smith                   COMPENGR3
I1234568Johnson                 MECHELEC4
D       Smith                   COMPENGR3
```

---

## Test Cases

The following test cases are included to validate the implementation:

1. **Insert Records**: Ensure records are inserted correctly based on last name.
2. **Delete Records**: Verify records are removed correctly while maintaining the BST structure.
3. **Depth-First Traversal**: Confirm in-order traversal outputs nodes in ascending logical order.
4. **Breadth-First Traversal**: Validate level-order traversal outputs nodes level-by-level.

---

This implementation demonstrates efficient management of hierarchical data using BST operations and traversal methods.
