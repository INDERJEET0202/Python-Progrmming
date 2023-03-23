stack = []
top = -1
max_size = int(input("Enter the size of the stack: "))

def push(element):
    global top
    if top == max_size - 1:
        print("Stack is full")
    else:
        stack.append(element)
        top += 1
    return stack

def pop():
    global top
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element: ", stack.pop())
        top -= 1
    return stack

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        for i in reversed(stack):
            print(i, end=" ")
    print()

def stack_top():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element: ", stack[top])
    return stack

x = 0
while(x == 0):
    print("1. Push" + "\n" + "2. Pop" + "\n" + "3. Top" + "\n" + "4. Peek" + "\n" + "5. Display" + "\n" + "6. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        stack = push(input("Enter the element: "))
        # print(top)
    elif(choice == 2):
        stack = pop()
    elif(choice == 3):
        stack = stack_top()
    elif(choice == 4):
        print("Peek element: ", stack[-1])
    elif(choice == 5):
        display()
    elif(choice == 6):
        print("Exiting...")
        x = 1
    else:
        print("Invalid choice")