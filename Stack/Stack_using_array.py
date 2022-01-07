stack = []
top = -1

def push():
    # global top
    element = int(input("Enter the number of elements: "))
    for i in range(element):
        # top += 1
        stack.append((input("Enter the element: ")))
    return stack


def pop():
    # global top
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element: ", stack.pop())
        # top -= 1
    return stack


def top():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element: ", stack[-1])
    return stack


def search(data):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        for i in stack:
            if i == data:
                return True
        return False


def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        for i in reversed(stack):
            print(i, end=" ")
    print()
    return stack


x = 0
while(x == 0):
    print("1. Push" + "\n" + "2. Pop" + "\n" + "3. Top" + "\n" + "4. Search" + "\n" + "5. Display" + "\n" + "6. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        stack = push()
    elif(choice == 2):
        stack = pop()
    elif(choice == 3):
        stack = top()
    elif(choice == 4):
        data = (input("Enter the element to peek: "))
        if search(data):
            print("Element found")
        else:
            print("Element not found")
    elif(choice == 5):
        stack = display()
    elif(choice == 6):
        print("Exiting...")
        x = 1
    else:
        print("Invalid choice")