# Task 1: Implementing Hash data structure from scratch

# Define a node class for the linked list
class Node:
    # Time = O(1) Space = O(1)
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    # Initialize the head and tail nodes (head node contains key and value)
    # Time = O(1) Space = O(1)
    def __init__(self, key, value):
        self.head = Node(key, value)
        self.tail = self.head

    def exists(self, key):
        # Time = O(n) (number of nodes in the list) Space = O(1)
        curr = self.head
        # Start from the head and traverse through the list
        while curr:
            if curr.key == key: # If a key is present (key exists)
                return True
            curr = curr.next
        # If the loop completes with no key
        return False

    def add(self, key, value):
        # Time = O(n) (number of nodes in the list) Space = O(1)

        # If the node doesn't exist add the node
        if not self.exists(key):
            new_node = Node(key, value) # New node with key and value
            # Append new node into the list and update the tail
            if self.tail:
                self.tail.next = new_node
                self.tail = new_node
            # If list is empty the new node will be both the head and tail of the linked list
            else:
                self.head = new_node
                self.tail = new_node


class HashTable:
    # Initialize the hash table
    # Time = O(1) Space = O(n) (n = size of the hash table)
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0 # Track the elements in the hash table

    def hash(self, key):
        # Time = O(len(k)) Space = O(1)
        index = 0
        found_alphanumeric = False

        # Ensure case insensitivity by converting the key to lower case
        for character in key.lower():
            if character.isalnum():  # Process both alphabetic and numeric characters
                found_alphanumeric = True
                if character.isalpha():
                    index += ord(character) - ord('a') + 1  # Alphabetic contribution (1 - 26)
                else:
                    index += ord(character) - ord('0') + 27  # Numeric contribution (numbers start from 27-36)

        # Return the hash value if valid alphanumeric characters are found
        return index % self.size if found_alphanumeric else None

    def insert(self, key, value):
        # Time = O(len(k) + n) Space = O(1)
        index = self.hash(key)
        if index is not None:
            if self.table[index] is None:
                self.table[index] = LinkedList(key, value)
                self.count += 1
            else:
                if not self.table[index].exists(key):  # Check for existing key before adding
                    self.table[index].add(key, value)
                    self.count += 1  # Increment when new key is added

    def print_hashtable(self):
        # Time = O(n + m) (table size plus number of nodes)
        # Space = O(1)
        # Iterate over each index and entry in the hash table
        for i, entry in enumerate(self.table):
            if entry is not None: # If entry present at index
                curr = entry.head
                # Traverse the linked list
                while curr:
                    # Print each node's key-value pair and current index
                    print(f"Index: {i}, Key: {curr.key}, Value: {curr.value}")
                    # Move pointer to the next node in the list
                    curr = curr.next

    def print_index(self, index):
        # Time = O(n) (number of nodes at the index)
        # Space = O(1)
        if index < len(self.table) and self.table[index] is not None:
            curr = self.table[index].head
            while curr:
                print(f"Index: {index}, Key: {curr.key}, Value: {curr.value}")
                curr = curr.next
        else:
            print(f"No entries at index {index}")

    def retrieve(self, key):
        # Time = O(len(k) + n) Space = O(1)
        index = self.hash(key)
        if index is None or self.table[index] is None:
            return None
        curr = self.table[index].head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def curr_size(self):
        # Time = O(1) Space = O(1)
        return self.count


# Task 1 Test Case
print('-------task 1--------')
hash_table = HashTable(10)

# Initialize an empty HashTable
print(f'Initialize an empty HashTable: {hash_table.curr_size()}')  # Output: 0

# Insert alpha keys into the HashTable
hash_table.insert("Ben", "99")
hash_table.insert("Kobbie", "7")
hash_table.insert("Timothy", "32")
hash_table.insert("Robert", "22")
hash_table.insert("Bander", "11")
hash_table.insert("Trent", "87")

hash_table.print_hashtable()

print(f'HashTable size after adding alphanumeric keys: {hash_table.curr_size()}')  # Output: 6

# Display that collisions are handled properly
print("\nContent at Index 4:")
hash_table.print_index(4)

# Insert non-alpha key (ignored by hash function)
hash_table.insert("@#?!", "Non-alphanumeric key value")
print(f'\nHashTable size after attempting to add Non-alphanumeric key: {hash_table.curr_size()}')  # Output: 6

# Prevent duplicate entries
hash_table.insert("Ben", "99")
print(f'HashTable size after attempting to add a duplicate: {hash_table.curr_size()}')  # Output: 6

# Retrieve values that are both present and not present in the list
print(f'\nRetrieve Ben: {hash_table.retrieve("Ben")}') # Value: 99
# Testing to retrieve a key that doesn't exist in the list
print(f'Retrieve non-existent key: {hash_table.retrieve("nonexistent")}')  # Output: None


# Task 2:
def parse_and_insert_anagram_roots(file_path, hash_table):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Replace non-alphanumeric characters with spaces , convert all letters to lowercase, and joins characters into single string
                processed_line = ''.join(char if char.isalnum() else ' ' for char in line.lower())
                # Split the processed string into a list of words
                cleaned_words = processed_line.split()

                for word in cleaned_words:
                    if word:  # Ignore empty strings
                        # Step 1: Sort the word to get its anagram root (key)
                        sorted_word = ''.join(sorted(word)) # join sorted words to single string
                        # Step 2: Insert the sorted word (anagram root) into the hash table if it does not exist
                        if not hash_table.retrieve(sorted_word):
                            hash_table.insert(sorted_word, True)  # True is a placeholder that tracks the sorted words in the hashtable

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return 0


# File path to 'pride-and-prejudice.txt'
file_path = 'pride-and-prejudice.txt'


hash_table = HashTable(size=10000)

# Parse the file and insert unique anagram roots
parse_and_insert_anagram_roots(file_path, hash_table)

# Count of unique anagram roots
unique_anagram_roots_count = hash_table.curr_size()

# Step 3: Results of the count of anagram root words
print('\n-------Task 2--------\n')
print(f"Number of unique anagram-root words: {unique_anagram_roots_count}")
