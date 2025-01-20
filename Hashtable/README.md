# Hash Table Implementation and Anagram Analysis

This folder contains Python implementations for a custom-built **Hash Table** and its application to analyze anagrams in a large text file.

---

## Features

### **Task 1: Implement a Hash Table**
The custom Hash Table implementation includes the following functionalities:
- **Hash Function**: Converts a string into an integer index in the hash table. The hash function ensures case insensitivity and includes a collision-resolution mechanism using linked lists.
- **insert(key, value)**: Inserts a key-value pair into the hash table. Handles collisions by chaining.
- **retrieve(key)**: Retrieves the value associated with a given key.
- **curr_size()**: Returns the current number of keys in the hash table.
- **print_hashtable()**: Displays the entire hash table with all keys and values.

### **Task 2: Anagram Analysis**
This task reads the file `pride-and-prejudice.txt`, parses it line by line to avoid memory issues, and determines the number of unique anagram roots:
- An **Anagram Root** is a word sorted by its characters (e.g., "mango" -> "agmno").
- The process includes:
  1. Parsing each word from the file.
  2. Sorting the word to get its anagram root.
  3. Inserting the anagram root into the hash table (ignoring duplicates).
  4. Returning the total count of unique anagram roots.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bshussein/DSA_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd HashTable
   ```
3. Ensure the file `pride-and-prejudice.txt` is present in the appropriate directory.
   - Update the file path in the script if necessary.
4. Run the Python script:
   ```bash
   python HashTable.py
   ```

---

## Example Usage

### **Task 1: Hash Table Example**
```python
# Initialize the hash table
hash_table = HashTable(size=10)

# Insert key-value pairs
hash_table.insert("Ben", "99")
hash_table.insert("Timothy", "32")

# Retrieve values
print(hash_table.retrieve("Ben"))  # Output: 99
print(hash_table.curr_size())      # Output: 2

# Print the hash table
hash_table.print_hashtable()
```

### **Task 2: Anagram Analysis**
```python
# File path to pride-and-prejudice.txt
file_path = '/path/to/pride-and-prejudice.txt'

# Initialize a large hash table
hash_table = HashTable(size=10000)

# Parse file and count unique anagram roots
parse_and_insert_anagram_roots(file_path, hash_table)
print(f"Number of unique anagram-root words: {hash_table.curr_size()}")
```

---

## Test Cases

The following test cases are included to validate the implementation:

1. **Hash Table**:
   - Insert and retrieve keys and values.
   - Handle collisions using chaining with linked lists.
   - Prevent duplicate keys and handle non-alphanumeric keys.

2. **Anagram Analysis**:
   - Parse and process words from a large file.
   - Insert unique anagram roots into the hash table.
   - Verify the count of unique anagram roots.

---

This implementation demonstrates foundational skills in building hash tables, processing large datasets efficiently, and analyzing anagrams.
