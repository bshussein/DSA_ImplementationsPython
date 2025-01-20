
class Node:
    def __init__(self, data):
        self.data = data # Node value
        self.left = None # Left child
        self.right = None # Right child


class BST:
    def __init__(self):
        self.root = None

    # Function to insert values into the BST
    def insert(self, num):
        if self.root is None:
            self.root = Node(num) # If empty assign the root to the new node
        else:
            self.__insert_recursive(self.root, num) # Recursive method to insert

    # Private method to insert values recursively
    def __insert_recursive(self, curr_node, num):
        if num <= curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(num)
            else:
                self.__insert_recursive(curr_node.left, num)
        else:
            if curr_node.right is None:
                curr_node.right = Node(num)
            else:
                self.__insert_recursive(curr_node.right, num)

    # in order traversal of the BST
    def in_order(self):
        nums = []
        self.__in_order_recursive(self.root, nums) # call recursive function
        return nums

    # Private function recursive for in order traversal
    def __in_order_recursive(self, node, nums):
        if node:
            self.__in_order_recursive(node.left, nums) # Recur (left subtree)
            nums.append(node.data) # Append current node
            self.__in_order_recursive(node.right, nums) # Recur (right subtree)

# Function to handle heap operations
class HeapBuilder:
    # Helper function to ensure the smallest element is the root
    def heapify_min(self, arr, n, i):
        smallest = i # Smallest value is the root
        left = 2 * i + 1 # To find left child index
        right = 2 * i + 2 # To find right child index

        # If left child is smaller update the smallest
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # If right child is smaller update the smallest
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # If the root is not the smallest recursively heapify
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify_min(arr, n, smallest)

    def heapify_max(self, arr, n, i):
        largest = i # initialize current node as largest
        left = 2 * i + 1 # calculate left child index
        right = 2 * i + 2 # calculate right child index

        # If left child is larger update the largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger update the largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the root is not the largest recursively heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # swap the current node and largest child
            self.heapify_max(arr, n, largest) # recursively heapify the subtree

    def build_min_heap(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1): # Start from last node (non leaf) and go upwards
            self.heapify_min(arr, n, i)
        return arr # heapify array

    def build_max_heap(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1): # Start from last node (non leaf) and go upwards
            self.heapify_max(arr, n, i)
        return arr

    # Convert to binary tree
    def heap_tree(self, nums):
        if not nums:
            return None
        root = Node(nums[0])
        queue = [root]
        i = 1

        while i < len(nums):
            curr_node = queue.pop(0) # dequeue
            if i < len(nums):
                left_child = Node(nums[i])
                curr_node.left = left_child # Assign current node as left child
                queue.append(left_child) # Append the left child
                i += 1

            if i < len(nums):
                right_child = Node(nums[i])
                curr_node.right = right_child
                queue.append(right_child)
                i += 1

        return root

    # Create min-heap tree from sorted list
    def min_heap(self, nums):
        if not nums:
            return None
        heapified = self.build_min_heap(nums[:]) # Heapify the list
        return self.heap_tree(heapified) # Convert to tree

    # Create max-heap tree from sorted list
    def max_heap(self, nums):
        if not nums:
            return None
        heapified = self.build_max_heap(nums[:])
        return self.heap_tree(heapified)

# Task 2: BST to heap transformer
class bst_to_heap:
    def __init__(self, bst_root):
        self.bst_root = bst_root

    def bst_to_min_heap(self):
        sorted_values = self.__in_order_traversal(self.bst_root)
        heap_builder = HeapBuilder()
        return heap_builder.min_heap(sorted_values) # Return built min heap

    def bst_to_max_heap(self):
        sorted_values = self.__in_order_traversal(self.bst_root)
        heap_builder = HeapBuilder()
        return heap_builder.max_heap(sorted_values) # Return built max heap

    def __in_order_traversal(self, node):
        if node is None:
            return []
        return self.__in_order_traversal(node.left) + [node.data] + self.__in_order_traversal(node.right)


if __name__ == "__main__":
    # Define the print function to visualize the heap as a tree
    def print_heap(root):
        if root is None:
            print("Heap is empty.")
            return
        queue = [root]
        while queue:
            curr = queue.pop(0)
            print(curr.data, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print()  # Newline for better readability


    # Test input
    A = [100, 60, 80, 77, 63]
    print("\nInput List:", A)
    print("-" * 75)

    # Task 1: Create Min-Heap and Max-Heap from the list of integers
    print("\nTask 1: Build Heaps from List:")

    # Create the HeapBuilder object
    heap_builder = HeapBuilder()

    # Build a Min-Heap and print the heap structure
    print("\nBuilding Min-Heap from list:")
    min_heap_root = heap_builder.min_heap(A)
    print("Min-Heap Tree Structure:")
    print_heap(min_heap_root)

    # Build a Max-Heap and print the heap structure
    print("\nBuilding Max-Heap from list:")
    max_heap_root = heap_builder.max_heap(A)
    print("Max-Heap Tree Structure:")
    print_heap(max_heap_root)

    # Task 2: Convert a BST to Min-Heap and Max-Heap
    print("-" * 75)
    print("\nTask 2: Convert BST to Heaps:")

    # Create a BST and insert values
    bst = BST()
    for value in A:
        bst.insert(value)

    # Print the BST's in-order traversal
    print("\nBST In-Order Traversal:", bst.in_order())

    # Create the bst_to_heap object for transformations
    transformer = bst_to_heap(bst.root)

    # Convert BST to Min-Heap and print the result
    print("\nConverting BST to Min-Heap:")
    min_heap_from_bst_root = transformer.bst_to_min_heap()
    print("Min-Heap Tree Structure from BST:")
    print_heap(min_heap_from_bst_root)

    # Convert BST to Max-Heap and print the result
    print("\nConverting BST to Max-Heap:")
    max_heap_from_bst_root = transformer.bst_to_max_heap()
    print("Max-Heap Tree Structure from BST:")
    print_heap(max_heap_from_bst_root)
