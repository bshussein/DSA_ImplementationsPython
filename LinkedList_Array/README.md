# LinkedList Implementation for Bank of Orange County

This implementation models the Bank of Orange County's user management system using a linked list. Each user's account is represented as a node in the list, and operations such as adding users, deleting users, merging accounts, and merging banks are implemented as methods in the system.

---

## Features

The linked list implementation supports the following tasks:

1. **Task 1: Model Users as a Linked List**
   - Each user account is stored as a node in a linked list, sorted by their unique ID.

2. **Task 2: Add User**
   - A method `addUser(user)` assigns a new unique ID to the user and adds them to the linked list.
   - The unique ID is either incremented from the last ID or reuses a free ID from a deleted account.

3. **Task 3: Delete User**
   - A method `deleteUser(ID)` removes a user from the linked list and frees up their unique ID for future use.

4. **Task 4: Pay User to User**
   - A method `payUserToUser(payerID, payeeID, amount)` transfers money from one user's account to another.

5. **Task 5: Get Median ID**
   - A method `getMedianID()` returns the median ID of all accounts:
     - If the number of accounts is odd, it returns the middle ID.
     - If the number is even, it returns the average of the middle two IDs or the first middle ID.

6. **Task 6: Merge Accounts**
   - A method `mergeAccounts(ID1, ID2)` merges two accounts owned by the same person (same name, address, and SSN).
   - The merged account retains the smaller unique ID, and the balances of both accounts are combined.

7. **Task 7: Merge Banks**
   - A method `mergeBanks(bankOfOrangeCounty, bankOfLosAngeles)` merges the linked lists of two banks into a new bank, `Bank of Southern California`.
   - Handles duplicate IDs by assigning new unique IDs while maintaining incremental properties.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bshussein/DSA_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd LinkedList_Array
   ```
3. Run the Python script:
   ```bash
   python LinkedList_Array.py
   ```

---

## Example Usage

Here’s an example of how to use the linked list implementation:

```python
# Initialize the bank
bank = BankOfOrangeCounty()

# Add users
bank.addUser({"name": "Alice", "address": "123 Orange St", "SSN": "111-22-3333", "deposit": 500})
bank.addUser({"name": "Bob", "address": "456 Peach Rd", "SSN": "222-33-4444", "deposit": 1000})

# Delete a user
bank.deleteUser(1)

# Pay from one user to another
bank.payUserToUser(2, 3, 200)

# Get median ID
print("Median ID:", bank.getMedianID())

# Merge accounts
bank.mergeAccounts(2, 4)

# Merge two banks
mergedBank = BankOfSouthernCalifornia.mergeBanks(bank1, bank2)
```

---

## Test Cases

Sample test cases to validate each method are included in the implementation.

1. Adding and deleting users.
2. Checking correct reassignment of IDs after deletion.
3. Performing payments between accounts and ensuring balances are updated.
4. Calculating the median ID for odd and even account counts.
5. Verifying correct merging of accounts with the same owner.
6. Ensuring proper handling of duplicate IDs during bank merging.
