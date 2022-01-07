stack = []
top = -1

def push(element):
    global top
    top += 1
    stack.append(element)
    return stack

def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Popped element: ", stack.pop())
        top -= 1
    return stack

x = 0
while(x == 0):
    print("1. Push" + "\n" + "2. Pop" + "\n" + "3. Top" + "\n" + "4. Peek" + "\n" + "5. Display" + "\n" + "6. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        stack = push(input("Enter the element: "))
        print(top)
    elif(choice == 2):
        stack = pop()
    elif(choice == 3):
        print("Top element: ", stack[-1])
    elif(choice == 4):
        print("Peek element: ", stack[-1])
    elif(choice == 5):
        print(stack)
    elif(choice == 6):
        print("Exiting...")
        x = 1
    else:
        print("Invalid choice")