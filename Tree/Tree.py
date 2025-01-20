# Assignment 4: Tree

# Task 1: Build Binary Search Tree (BST) using tree input data

# Function to represent each student record as a node in the binary search tree
class StudentData:
    # Initialize student record
    def __init__(self, number, name, department, program, year):
        self.number = number.strip()
        self.name = name.strip()
        self.department = department.strip()
        self.program = program.strip()
        self.year = year.strip()

    def __repr__(self):
        return f"{self.number} - {self.name} - {self.department} - {self.program} - {self.year}"


class Node:
    # Initialize a node in the BST
    def __init__(self, record):
        self.record = record
        self.left = None
        self.right = None


# Function to build the Binary Search Tree (BST) (Time = O(log(n))
class BST:
    def __init__(self):
        self.root = None

    def insert(self, record):
        if not self.root:
            self.root = Node(record)  # if empty, new record becomes the root
        else:
            # Insert record in the tree
            self._insert_recursive(self.root, record)

    # Private function to place the record in the right place
    def _insert_recursive(self, node, record):
        # Normalize the comparison by converting names to lowercase
        current_name = node.record.name.lower()
        new_name = record.name.lower()

        if current_name > new_name:
            if node.left is None:
                node.left = Node(record)  # New record as the left child
            else:
                self._insert_recursive(node.left, record)  # Insert in left subtree
        elif current_name < new_name:
            if node.right is None:
                node.right = Node(record)  # New record as the right child
            else:
                self._insert_recursive(node.right, record)  # Insert in right subtree

    # Function to delete record by name from the binary search tree
    def delete(self, name):
        self.root = self._delete_recursive(self.root, name.strip().lower())

    # Private helper function to delete node by name (recursively)
    def _delete_recursive(self, node, name):
        if node is None:
            return node

        if name < node.record.name.lower():  # Delete left subtree
            node.left = self._delete_recursive(node.left, name)
        elif name > node.record.name.lower():  # Delete right subtree
            node.right = self._delete_recursive(node.right, name)
        else:
            if node.left is None and node.right is None:
                return None  # Return none if children node is not present
            elif node.left is None:
                return node.right  # Right child
            elif node.right is None:
                return node.left  # Left child
            else:
                # Node with 2 children
                smallest_node = self.min_node(node.right)  # Smallest node in the right subtree
                node.record = smallest_node.record
                node.right = self._delete_recursive(node.right,
                                                     smallest_node.record.name.lower())  # Delete the smallest node

        return node

    # Find the smallest node in a subtree
    def min_node(self, node):
        curr = node
        while curr.left is not None:  # Traverse the tree to the left
            curr = curr.left
        # Return the leftmost node as the smallest node value
        return curr

    # Task 2: Implement a depth-first (in-order tree traversal) and write file.
    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)  # Traverse the left subtree
        print(node.record)  # Print the entire record, including student number
        self.in_order(node.right)  # Traverse the right subtree

    # Function to write the in-order traversal of the BST to a file
    def write_in_order(self, node, file):
        with open(file, "w") as output_file:
            def write_in_order_recursive(n):
                if not n:
                    return
                write_in_order_recursive(n.left)  # Traverse left subtree
                output_file.write(f"{n.record}\n")  # Write to the file
                print(n.record)
                write_in_order_recursive(n.right)  # Traverse right subtree

            write_in_order_recursive(node)

    # Function to read student data from the file and insert into BST
    def read_data(self, file):
        with open(file, "r") as f:
            for line in f:
                # Parse each section of the line based on character positions
                operation = line[0]
                number = line[1:8].strip()
                name = line[8:33].strip()
                department = line[33:37].strip()
                program = line[37:41].strip()
                year = line[41:42].strip()

                if operation == 'I':
                    student = StudentData(number, name, department, program, year)
                    self.insert(student)  # Insert student record into the BST

                elif operation == 'D':
                    self.delete(name.strip())  # Delete student record from the BST

    # Task 3: Implement breadth-first traversal and write to file
    def breadth_first(self, file):
        if not self.root:
            return

        # Implementing the queue using a list
        queue = []  # Use a list as a queue
        queue.append(self.root)

        # Function to write the breadth first traversal of the BST to a file
        try:
            with open(file, "w") as level_file:
                level_file.write("Task 3:\n")
                while queue:
                    curr_node = queue.pop(0)  # Pop the first element
                    level_file.write(f"{curr_node.record}\n")
                    print(f"{curr_node.record}")

                    if curr_node.left:
                        queue.append(curr_node.left)  # Append left child

                    if curr_node.right:
                        queue.append(curr_node.right)  # Append right child
        except IOError as e:
            print(f"An exception occurred while writing to the file: {e}")

if __name__ == "__main__":
    bst = BST()
    bst.read_data("tree-input.txt")

    # Task 2: In-order traversal and write to file
    print("\n-------Task 2-------")
    bst.write_in_order(bst.root, "in_order_traversal.txt")


    # Task 3: Breadth-first traversal and write to file
    print("\n-------Task 3-------")
    bst.breadth_first("breadth_first.txt")
