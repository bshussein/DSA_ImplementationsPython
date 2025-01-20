
# Heap Implementation and BST to Heap Transformation

This folder contains Python implementations for **Heap** operations and transformation of a **Binary Search Tree (BST)** into Min-Heap and Max-Heap.

---

## Features

### **Task 1: Build a Heap from a List**
- Implement both Min-Heap and Max-Heap using a binary tree structure.
- Supports the following operations:
  - **Build Min-Heap**: Rearranges a list into a Min-Heap.
  - **Build Max-Heap**: Rearranges a list into a Max-Heap.
  - **Heap Tree Construction**: Converts a list into a binary tree representation of the heap.

### **Task 2: BST to Heap Transformation**
- Transform a given BST into a Min-Heap and Max-Heap.
- The transformation leverages in-order traversal of the BST to ensure the heap property.
- Supports the following operations:
  - **BST to Min-Heap**: Converts the BST into a Min-Heap.
  - **BST to Max-Heap**: Converts the BST into a Max-Heap.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bshussein/DSA_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd Heap
   ```
3. Run the Python script:
   ```bash
   python Heap.py
   ```

---

## Example Usage

### **Building Heaps from a List**
```python
heap_builder = HeapBuilder()
nums = [100, 60, 80, 77, 63]

# Build and print Min-Heap
min_heap_root = heap_builder.min_heap(nums)
print_heap(min_heap_root)

# Build and print Max-Heap
max_heap_root = heap_builder.max_heap(nums)
print_heap(max_heap_root)
```

### **Transforming BST to Heap**
```python
bst = BST()
nums = [100, 60, 80, 77, 63]
for num in nums:
    bst.insert(num)

# Transform BST to Min-Heap
transformer = bst_to_heap(bst.root)
min_heap_from_bst = transformer.bst_to_min_heap()
print_heap(min_heap_from_bst)

# Transform BST to Max-Heap
max_heap_from_bst = transformer.bst_to_max_heap()
print_heap(max_heap_from_bst)
```

---

## Input and Output Details

### **Input List**
A list of integers is provided as input for heap operations. For example:
```python
nums = [100, 60, 80, 77, 63]
```

### **Heap Output**
The heaps (Min-Heap or Max-Heap) are displayed as binary tree structures.

---

## Test Cases

The following test cases are included to validate the implementation:

1. **Heap Operations**:
   - Build Min-Heap and Max-Heap from a given list of integers.
   - Verify the heap property for both Min-Heap and Max-Heap.

2. **BST to Heap Transformation**:
   - Convert a BST to a Min-Heap and verify the structure.
   - Convert a BST to a Max-Heap and verify the structure.

---

This implementation demonstrates efficient heap operations and transformations between binary trees and heaps, showcasing key data structure concepts.
