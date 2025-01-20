# Task 1: Stack Implementation
class fifa_rating:
    def __init__(self, first_name, last_name, rating):
        # Initialize player details
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating

    # Provide a string representation of the player
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Rating: {self.rating}"


class Stack:
    def __init__(self):
        self.items = []  # List to store stack elements

    # Push an element onto the stack (Time = O(1) Space = O(1))
    def push(self, element):
        self.items.append(element)  # Append to the end of the list

    # Pop an element off the stack if the stack is not empty (Time = O(1) Space = O(1))
    def pop(self):
        if self.is_empty():
            print("Unable to pop from an empty stack.")
            return None
        return self.items.pop()  # Return and remove last element from stack (not empty)

    # Peek top item of the stack (without removing) (Time = O(1) Space = O(1))
    def peek(self):
        if not self.items:
            print("Unable to peek from an empty stack.")
            return None
        return self.items[-1]  # Returning the last element of the stack (not empty)

    # Size of the stack (Time = O(1) Space = O(1))
    def size(self):
        return len(self.items)

    # Check if stack is empty (Time = O(1) Space = O(1))
    def is_empty(self):
        return len(self.items) == 0


# Order of operations (placing */ in higher precedence than +-)
def precedence(op):
    # (Time = O(1) Space = O(1))
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def perform_operation(operands, operator):
    # (Time = O(1) Space = O(1))
    # Pop the top two operands from the stack
    right = operands.pop()
    left = operands.pop()

    # Check if either operand is non-numeric
    if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
        operands.push(float('nan'))
        return True

    # Perform the operation based on the operators below:
    if operator == '+':
        operands.push(left + right)
    elif operator == '-':
        operands.push(left - right)
    elif operator == '*':
        operands.push(left * right)
    elif operator == '/':
        if right == 0:
            return False  # Prevent division by zero
        operands.push(left / right)
    return True


# Time = O(n) (length of expression)
# Space = O(n) (maintaining operators and operands)
def evaluate(expression):
    # Function to handle numeric values
    def handle_number(expression, i, operands):
        val = 0
        is_float = False
        decimal_place = 0.1
        while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
            if expression[i] == '.':
                is_float = True
            elif is_float:
                val += int(expression[i]) * decimal_place
                decimal_place *= 0.1
            else:
                val = val * 10 + int(expression[i])
            i += 1
        operands.push(val)
        return i - 1

    def handle_operator(expression, i, operators, operands):
        while not operators.is_empty() and precedence(operators.peek()) >= precedence(expression[i]):
            op = operators.pop()
            if not perform_operation(operands, op):
                operands.push(float('nan'))  # Push NaN if operation fails
                return False
        operators.push(expression[i])
        return True

    def process_until_open_paren(operators, operands):
        while not operators.is_empty() and operators.peek() != '(':
            op = operators.pop()
            if not perform_operation(operands, op):
                operands.push(float('nan'))  # Push NaN if operation fails
                return False
        operators.pop()
        return True

    operators = Stack()
    operands = Stack()

    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue

        if expression[i].isdigit() or expression[i] == '.':
            i = handle_number(expression, i, operands)

        elif expression[i] == '(':
            operators.push(expression[i])

        elif expression[i] == ')':
            if not process_until_open_paren(operators, operands):
                return float('nan')

        elif expression[i].isalpha():
            operands.push(float('nan'))  # Push NaN if non-numeric character
            while i < len(expression) and expression[i].isalpha():
                i += 1
            i -= 1  # Ensure we don't skip characters

        else:
            if not handle_operator(expression, i, operators, operands):
                return float('nan')

        i += 1

    while not operators.is_empty():
        op = operators.pop()
        if not perform_operation(operands, op):
            return float('nan')

    result = operands.pop()
    return result if isinstance(result, (int, float)) else float('nan')


# Function to check if value is not a number
def is_nan(value):
    return value != value

# Test Case Task 1
def test_player_stack():
    stack = Stack()

    # Assigning/adding players into the stack
    print("\n------ TASK 1: Player Stack ------\n")
    player1 = fifa_rating("Marcus", "Rashford", 81)
    player2 = fifa_rating("Bobby", "Endrick", 80)
    player3 = fifa_rating("John", "Stones", 85)

    stack.push(player1)
    stack.push(player2)
    stack.push(player3)

    players = [player1, player2, player3]
    print("Stack of Player Ratings:")
    for player in players:
        print(player)
    print(f"Stack Size: {stack.size()}")

    print("\nPeeking at the Top Player:")
    top_player = stack.peek()
    print(f"Top Player: {top_player}")

    print("\nPop Players:")
    popped_player = stack.pop()
    print(f"Player Removed: {popped_player}")

    popped_player = stack.pop()
    print(f"Player Removed: {popped_player}")
    print(f"Stack Size: {stack.size()}")

    print("\nStack Status:")
    is_empty = stack.is_empty()
    print(f"Is Stack Empty? {is_empty}")

    print("\nPop Remaining Player:")
    popped_player = stack.pop()
    print(f"Popped Player: {popped_player}")
    print(f"Stack Size: {stack.size()}")

    print("\nCheck if stack is empty again:")
    is_empty = stack.is_empty()
    print(f"Is Stack Empty? {is_empty}")

    print("\nAttempt to pop from an empty stack:")
    popped_player = stack.pop()

    print("\nAttempt to peek at an empty stack:")
    top_player = stack.peek()


test_player_stack()

# Test case Task 2
def test_evaluate():
    print("\n-------- TASK 2: Evaluate Expression --------\n")
    test_cases = [
        ("2 * 2 - 5", -1),
        ("5 - 3", 2),
        ("5 * 2", 10),
        ("8 / 2", 4),
        ("3 + 2 * 3", 9),
        ("(2 + 2) * 3", 12),
        ("10 - 5 + 2 * 2", 9),
        ("100 / 10 + 2 * 5", 20),
        ("5 + 6 * (3 - 1)", 17),
        ("(2 + 3) * (4 - 1)", 15),
        ("foo / 2", float('nan')),
        ("10/0", float('nan')),
    ]

    for expression, expected in test_cases:
        result = evaluate(expression)
        result_text = "Correct" if result == expected or (isinstance(result, float) and is_nan(result)) else "Fail"
        print(f"Expression: {expression}\nOutput: {result}\nExpected: {expected}\nResult: {result_text}")
        print("-" * 25)


test_evaluate()

# Task 3: Implementing a queue from scratch
class Node:
    def __init__(self, player=None):
        self.player = player
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, player):
        new_node = Node(player)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1 # Increment size of the queue

    def dequeue(self):
        if self.is_empty():
            print("Unable to dequeue from an empty queue.")
            return None
        dequeued_player = self.head.player
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1 # decrement size of the queue
        return dequeued_player

    def poll(self):
        if self.is_empty():
            print("Unable to poll from an empty queue.")
            return None
        # Return the head node (player information)
        return self.head.player

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

# Test Case for Task 3
def test_queue():
    queue = Queue()

    print("\n------- TASK 3: Queue Implementation -------\n")

    player1 = fifa_rating("Kobbie", "Mainoo", 78)
    player2 = fifa_rating("Cole", "Palmer", 85)
    player3 = fifa_rating("Ben", "Blanco", 95)

    print("Enqueued Players and Queue Size:\n")
    queue.enqueue(player1)
    print(f"Enqueued: {player1}")
    print(f"Queue Size: {queue.get_size()}")

    queue.enqueue(player2)
    print(f"Enqueued: {player2}")
    print(f"Queue Size: {queue.get_size()}")

    queue.enqueue(player3)
    print(f"Enqueued: {player3}")
    print(f"Queue Size: {queue.get_size()}")

    print("\nPolling first Player:\n")
    first_player = queue.poll()
    print(f"Polled Player: {first_player}")

    print("\nDequeued Player:\n")
    dequeued_player = queue.dequeue()
    print(f"Dequeued: {dequeued_player}")
    print(f"Queue Size: {queue.get_size()}")

    top_player = queue.poll()
    print(f"\nPolled Player: {top_player}\n")

    print("Queue Status:")
    is_empty = queue.is_empty()
    print(f"Is Queue Empty? {is_empty}")
    print(f"Queue Size: {queue.get_size()}\n")

    queue.dequeue()
    queue.dequeue()

    print(f"Dequeued: {dequeued_player}")
    print(f"Dequeued: {dequeued_player}")
    print(f"Queue Size: {queue.get_size()}")

    is_empty = queue.is_empty()
    print("\nQueue Status While Queue is Empty:")
    print(f"Queue Empty? {is_empty}")

    print("\nDequeue from an empty queue:")
    queue.dequeue()

    print("\nPolling from an empty queue:")
    top_player = queue.poll()
    print(f"Polled Player: {top_player}")


test_queue()

# Task 4: Stack Implementation Using Two Queues
class StackWithTwoQs:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, element):
        self.queue1.enqueue(element)

    def pop(self):
        if self.queue1.is_empty():
            print("Unable to pop from an empty stack.")
            return None
        # Transfer elements from queue1 to queue2 until one element remains in queue1
        while self.queue1.get_size() > 1:
            item = self.queue1.dequeue()
            self.queue2.enqueue(item)
        # Last Element in queue1 = top of stack
        popped_item = self.queue1.dequeue()
        # Swap queue1 and queue2 ensure all stack operations work in correct order
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_item

    def peek(self):
        if self.queue1.is_empty():
            print("Unable to peek from empty stack")
            return None
        while self.queue1.get_size() > 1:
            item = self.queue1.dequeue()
            self.queue2.enqueue(item)
        top_item = self.queue1.poll()
        self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_item

    def size(self):
        return self.queue1.get_size()


def test_stack_with_two_qs():
    stack = StackWithTwoQs()

    player1 = fifa_rating("Ben", "Blanco", 95)
    player2 = fifa_rating("Marcus", "Rashford", 81)
    player3 = fifa_rating("Bobby", "Endrick", 80)

    print("\n------- TASK 4: Stack Implementation Using Two Queues -------\n")

    print("-----Push and Check Size-----")
    stack.push(player1)
    print(f"Pushed: {(player1)}")
    stack.push(player2)
    print(f"Pushed: {(player2)}")
    stack.push(player3)
    print(f"Pushed: {(player3)}")
    print(f"Stack Size: {stack.size()}")


    print("\n---Peek Operations---\n")
    print(f"Peek: {stack.peek()}")
    print(f"Stack Size after peek: {stack.size()}")

    print("\n---Pop Operations---\n")
    print(f"Pop 1: {stack.pop()}")
    print(f"Pop 2: {stack.pop()}")
    print(f"Pop 3: {stack.pop()}")
    print(f"Pop on empty stack: {stack.pop()}")
    print(f"Stack Size after pops: {stack.size()}")

    print("\n---Edge Case Testing---\n")
    print(f"Peek on empty stack: {stack.peek()}\n")
    stack.push(77)
    print(f"Pushed: {(77)}")
    print(f"Peek after pushing one element: {stack.peek()}")
    print(f"Pop after pushing one element: {stack.pop()}")
    print(f"Stack Size after popping the last element: {stack.size()}")



test_stack_with_two_qs()
