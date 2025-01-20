# Linked list built from scratch
class linked_list:
    def __init__(self):
        self.head = None

    # Time = O(n) Space = O(1)
    def add_node(self, node):
        if self.head is None:
            self.head = node # New node as head
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            current.next = node # Next pointer towards new node

    # Time = O(n) Space = O(1)
    def remove_node(self, user_id):
        current = self.head
        previous = None
        while current:
            # If current node has the specified user id to remove
            if current.id == user_id:
                if previous: # If not head of the list
                    previous.next = current.next
                else:
                    # If head update the head to the next node
                    self.head = current.next
                return True # Node removed
            previous = current
            current = current.next
        return False # Not found

    # Time = O(n) Space = O(1)
    def find_node(self, condition):
        current = self.head
        while current:
            # Condition to find node
            if condition(current):
                # Return first node that matches the condition
                return current
            current = current.next # Proceed
        return None

    # Time and Space = O(1)
    def is_empty(self):
        return self.head is None

    # Adding nodes in sorted order (sorted by id)
    def sorted_nodes(self, new_user):
        # If head is none or new user id is smaller than head id
        if self.head is None or self.head.id > new_user.id:
            # Point new user to head of the list
            new_user.next = self.head
            # Assign new user head of the list
            self.head = new_user
        else:
            # Start from head and traverse through the list to find place to insert new user
            current_node = self.head
            while current_node.next and current_node.next.id < new_user.id:
                current_node = current_node.next
            # link the new user to the next node
            new_user.next = current_node.next
            # Insert new user to next node (after current node)
            current_node.next = new_user

    # Time = O(n) Space = O(1)
    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # Time = O(n) Space = O(1)
    # Retrieve a node from particular index
    def get_node_at_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current # Return the node
            count += 1
            current = current.next
        return None


class AccountNode:
    # Initialize user details
    def __init__(self, user_id, name, address, ssn, funds):
        self.id = user_id
        self.name = name
        self.address = address
        self.ssn = ssn
        self.funds = funds
        self.next = None


class Bank_of_Orange_County:
    def __init__(self):
        self.head = linked_list()
        self.freed_ids = linked_list()
        self.next_id = 1

    # A function to add a new user into the list
    def add_user(self, name, address, ssn, funds, user_id=None):
        # Check if user_id is provided or if there are any freed ids available
        if user_id is None:
            if not self.freed_ids.is_empty():
                # Get the smallest freed id
                smallest_id = self.freed_ids.head.id
                # Remove freed id since it is being reused
                self.freed_ids.remove_node(smallest_id)
                # Assign the smallest freed id to the new user
                user_id = smallest_id
            else:
                # If no freed ids are available, assign next available id
                user_id = self.next_id
                self.next_id += 1  # Increment for the next user

        # Create a new user with the assigned id
        new_user = AccountNode(user_id, name, address, ssn, funds)

        # Keep the linked list in sorted order after adding the user
        self.head.sorted_nodes(new_user)

    def delete_user(self, user_id):
        current_user = self.head.head
        previous_user = None

        # Traverse the user list to find the user to delete
        while current_user:
            if user_id == current_user.id:
                break
            previous_user = current_user
            current_user = current_user.next

        if current_user:
            # Remove the user from the bank
            if previous_user:
                previous_user.next = current_user.next
            else:
                self.head.head = current_user.next

                print(f'Added user {name} with ID {user_id}')  # Debug output

            # Check if user_id is already in freed_ids list
            freed_current = self.freed_ids.head
            found = False
            while freed_current:  # Traverse the freed_ids linked list
                if freed_current.id == user_id:  # Check for duplicate
                    found = True  # Duplicate found
                    break
                freed_current = freed_current.next

            # Add freed id if not found
            if not found:
                self.freed_ids.add_node(AccountNode(user_id, "", "", "", 0))

            return True

        return False

    def pay_user_to_user(self, payer_id, payee_id, amount):
        payer = self.find_user_by_id(payer_id)
        payee = self.find_user_by_id(payee_id)

        if payer and payee:
            if amount < 0:
                print("An error occurred: Unable to process a transaction with a negative amount.")
                return False

            if payer.funds >= amount:
                payer.funds -= amount
                payee.funds += amount
                print(f"An amount of ${amount} was transferred from user {payer_id} to user {payee_id} successfully.")
                return True
            else:
                print(f"Unable to complete the transfer due to insufficient funds for user {payer_id}.")
        else:
            print(f"Unable to complete the transfer. Either user {payer_id} or user {payee_id} was not found.")

    def find_user_by_id(self, user_id):
        current_user = self.head.head
        while current_user:
            if current_user.id == user_id:
                return current_user
            current_user = current_user.next
        return None

    def print_user_details(self):
        current = self.head.head  # Start from the head of the linked list
        print("User details (ID, Name):")
        while current:
            print(f"({current.id}, {current.name})")
            current = current.next  # Move to the next node


    # Get the median ID from the list of users
    def get_median_id(self):
        def sorted_insert(head, new_node):
            if head is None or head.id >= new_node.id:
                new_node.next = head
                head = new_node
            else:
                current = head
                while current.next is not None and current.next.id < new_node.id:
                    current = current.next
                new_node.next = current.next
                current.next = new_node
            return head

        def sort_linked_list(head):
            sorted_head = None
            current = head
            length = 0  # Initialize length to 0
            while current:
                next_node = current.next
                sorted_head = sorted_insert(sorted_head, current)
                current = next_node
                length += 1  # Increment length
            return sorted_head, length

        if self.head.is_empty():
            return None

        sorted_head, length = sort_linked_list(self.head.head)

        current = sorted_head

        # If the length is odd, find the middle element
        if length % 2 == 1:
            for _ in range(length // 2):
                current = current.next
            median = current.id

        # If the length is even, compute the average of the two middle elements
        else:
            for _ in range((length // 2) - 1):
                current = current.next
            left_middle = current
            right_middle = current.next
            median = (left_middle.id + right_middle.id) / 2

        return median

    def merge_accounts(self, id1, id2):
        account1 = self.find_user_by_id(id1)
        account2 = self.find_user_by_id(id2)

        if not account1:
            raise ValueError(f"Account with ID {id1} could not be located")
        if not account2:
            raise ValueError(f"Account with ID {id2} could not be located")

        if (account1.name == account2.name
                and account1.address == account2.address
                and account1.ssn == account2.ssn):
            account1.funds += account2.funds
            self.delete_user(account2.id)
            remaining_account_id = account1.id
        else:
            raise ValueError("The accounts are not duplicates")

        return remaining_account_id

    def print_users_in_sorted_order(self):
        sorted_users = linked_list()
        current = self.head.head

        while current:
            # Create a new account node to avoid modifying the original list
            new_node = AccountNode(current.id, current.name, current.address, current.ssn, current.funds)
            new_node.next = None  # Clear the next pointer to avoid linking to the old list
            sorted_users.sorted_nodes(new_node)
            current = current.next

        # Print users from the sorted linked list
        current = sorted_users.head
        print("Merged Bank User details (ID, Name):")
        while current:
            print((current.id, current.name))
            current = current.next

class Bank_of_Los_Angeles(Bank_of_Orange_County):
    pass

class Bank_of_Southern_California(Bank_of_Orange_County):
    @staticmethod
    def merge_banks(bank_oc, bank_la):
        merged_bank = Bank_of_Southern_California()

        current = bank_oc.head.head

        if current is None:
            merged_bank.head = bank_la.head
        else:
            while current.next:
                current = current.next
            current.next = bank_la.head.head

        merged_bank.head = bank_oc.head
        merged_bank.unique_ids()

        return merged_bank

    def unique_ids(self):
        current = self.head.head
        # Check for duplicates
        while current:
            # Initialize previous user to the head
            reference = self.head.head
            # Go through all previous users to find duplicates within the list
            while reference != current:
                # If duplicate found
                if reference.id == current.id:
                    current.id += 1 # Increment ID to avoid duplication
                    # Place previous user to the head of the list (reset and check again)
                    reference = self.head.head
                else:
                    reference = reference.next

            current = current.next


# Testing the addition of users sorted by IDs
def test_users_sorted_by_id():
    bank = Bank_of_Orange_County()

    bank.add_user("Makki", "240 Kearny Ln", "250-00-1234", 5000, 3)
    bank.add_user("John", "270 Oakwood St", "124-99-7576", 200, 2)
    bank.add_user("Jimmy", "120 Jamboree Rd", "999-11-2234", 1500, 1)
    bank.add_user("Ben", "459 Cedar Ln", "750-51-9254", 3000, 5)
    bank.add_user("Sara", "2300 Kearny Ct", "459-33-6560", 10000, 4)

    current = bank.head.head
    print("\n--- Task 1 ---\n")
    print("All users sorted by their ID in the linked list.\n")
    print("User details (ID, Name):")
    while current:
        print((current.id, current.name))
        current = current.next


test_users_sorted_by_id()

# Task 2: Add a new user with a unique ID that is either one more than the last ID or the first available ID.
def test_add_new_user():
    bank = Bank_of_Orange_County()

    bank.add_user("Makki", "240 Kearny Ln", "250-00-1234", 5000)
    bank.add_user("John", "270 Oakwood St", "124-99-7576", 200)
    bank.add_user("Jimmy", "120 Jamboree Rd", "999-11-2234", 1500)
    bank.add_user("Ben", "459 Cedar Ln", "750-51-9254", 3000, 4)

    # Delete user 2 to test ID assignment when adding a new user
    bank.delete_user(2)

    # Adding a new user to test if a new user will be added to user 2 spot (freed ID)
    bank.add_user("Sara", "2300 Cogenbury Ct", "459-33-6560", 10000)
    new_user = bank.find_user_by_id(2)

    # Add a new user that should be added to the end of the list (ID_5)
    bank.add_user("Jess", "120 Tysons Blvd", "750-88-8870", 200, 5)
    new_user_jess = bank.find_user_by_id(5)


    # Print new user details
    print("\n--- Task 2 and 3 ---\n")
    print(
        f"New user added with ID: {new_user.id} (Name: {new_user.name}, Address: {new_user.address}, SSN: {new_user.ssn}, Funds: ${new_user.funds})")
    print(
        f"New user added with ID: {new_user_jess.id} (Name: {new_user_jess.name}, Address: {new_user_jess.address}, SSN: {new_user_jess.ssn}, Funds: ${new_user_jess.funds})\n")

    bank.print_user_details()


test_add_new_user()


# Task 4: Testing the pay_user_to_user function by letting the payer be ID 1 and payee ID 3:
def test_pay_user_to_user():
    bank = Bank_of_Orange_County()

    bank.add_user("Makki", "240 Kearny Ln", "250-00-1234", 5000)
    bank.add_user("John", "270 Oakwood St", "124-99-7576", 200)
    bank.add_user("Jimmy", "120 Jamboree Rd", "999-11-2234", 1500)
    bank.add_user("Ben", "459 Cedar Ln", "750-51-9254", 3000)

    print("\n--- Task 4 ---\n")
    print("Payment Transaction:")
    payer_id = 1
    payee_id = 3
    amount = 500

    transaction_success = bank.pay_user_to_user(payer_id, payee_id, amount)
    payer = bank.find_user_by_id(payer_id)
    payee = bank.find_user_by_id(payee_id)

    if transaction_success:
        # Only assign and display payer and payee details if the transaction is successful
        payer = bank.find_user_by_id(payer_id)
        payee = bank.find_user_by_id(payee_id)

        if payer and payee:
            print("\nFunds of both users after the transaction:")

            print(f"User {payer_id} (Payer) funds after transaction: ${payer.funds}")
            print(f"User {payee_id} (Payee) funds after transaction: ${payee.funds}")

    else:
        print("Transaction failed.")


test_pay_user_to_user()


# Task 5: Testing median ID on both odd and even number of users
def test_get_median_id():
    bank = Bank_of_Orange_County()

    bank.add_user("Makki", "240 Kearny Ln", "250-00-1234", 5000)  # ID_1
    bank.add_user("John", "270 Oakwood St", "124-99-7576", 200)  # ID_2
    bank.add_user("Jimmy", "120 Jamboree Rd", "999-11-2234", 1500)  # ID_3
    bank.add_user("Ben", "459 Cedar Ln", "750-51-9254", 3000)  # ID_4
    bank.add_user("Sara", "2700 Cogenbury ct", "750-12-9876", 2500)  # ID_5

    median_id = bank.get_median_id()

    print("\n--- Task 5 ---\n")
    # Getting the median ID of odd count
    print(f"Median User ID (Odd): {median_id}")

    # Adding new user to get the median ID of even count
    bank.add_user("Rania", "4300 Skyline rd", "606-11-3489", 250)  # ID_6

    median_id = bank.get_median_id()
    print(f"Median User ID (Even): {median_id}")


test_get_median_id()


# Task 6: Merging two accounts into one
def test_merge_accounts():
    print("\n--- Task 6 ---\n")

    bank = Bank_of_Orange_County()

    bank.add_user("Makki", "240 Kearny Ln", "250-00-1234", 2500)
    bank.add_user("Makki", "240 Kearny Ln", "250-00-1234", 500)
    bank.add_user("John", "270 Oakwood St", "124-99-7576", 200)

    # Merging user 1 and 2
    merged_id = bank.merge_accounts(1, 2)

    merged_account = bank.find_user_by_id(merged_id)

    if merged_account:
        print(f"Merged Name:{merged_account.name}")
        print(f"Merged Account ID: {merged_id}")
        print(f"The funds of the now merged account ID {merged_id} are ${merged_account.funds}.")
        print("Test merge_accounts: Successful!")

    else:
        print("An error occurred: Merged account not found.")


test_merge_accounts()


# Task 7: Merge two banks into one
def test_merge_banks():
    print("\n--- Task 7 ---\n")

    # Creating two Banks
    bank_oc = Bank_of_Orange_County()
    bank_la = Bank_of_Los_Angeles()

    # Add users to the Bank of Orange County
    bank_oc.add_user("Makki", "240 Kearny Ln", "250-00-1234", 5000, 4)
    bank_oc.add_user("John", "270 Oakwood St", "124-99-7576", 200, 2)
    bank_oc.add_user("Neal", "231 Devian St", "098-99-7576", 1000, 1)

    # Add users to the Bank of Los Angeles
    bank_la.add_user("Jimmy", "120 Jamboree Rd", "999-11-2234", 1500, 2)
    bank_la.add_user("Ben", "459 Cedar Ln", "750-51-9254", 3000, 6)
    bank_la.add_user("Sara", "2300 Kearny Ct", "459-33-6560", 10000, 1)

    # Merge both banks into the Bank of Southern California
    merged_bank = Bank_of_Southern_California.merge_banks(bank_oc, bank_la)

    # Print the users in sorted order for Task 7
    merged_bank.print_users_in_sorted_order()


test_merge_banks()
