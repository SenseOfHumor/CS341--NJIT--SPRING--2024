inp_string = "abba((14.252+(692.211*(.39+492.1))/49.235)abba"

## creating the function for PDA
##print(f"Present state: {state} \nCurrent input symbol under R-Head {i} \nStack top: {stack[-1]} \nSymbol popped from the stack: {stack.pop()} \nSymbol pushed into the stack: {push} \nNext state: {state} \n")

def isPDA(string):
    stack = []
    state = 'q0'
    rejected = False

    print("__________________________________________________________")
    print(f"\nThe string under processing is: {string}")
    print("The format is as: Current State, Current Input Symbol, Stack Top -> Next State, Pushed Symbol\n")

    for i in string:
        if state == 'q0' and i == 'a':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            push = stack.append('z0')
            state = 'q1'
            print(f"q0, {i}, epsilon -> {state}, z0\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")
            #print(stack)
        ## for state q1
        elif state == 'q1' and i == 'a':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.append(i)
            state = 'q2'
            print(f"q1, {i}, epsilon -> {state}, {i}\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")
            #print(stack)

        ## still for state q1
        elif state == 'q1' and i == 'b':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.append(i)
            state = 'q1'
            print(f"q1, {i}, epsilon -> {state}, {i}\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")
            #print(stack)

        ## for state q2
        elif state == 'q2' and i.isnumeric():
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q4'
            print(f"q2, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")
            #print(stack)

        ## for state q2
        elif state == 'q2' and i == '.':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q3'
            print(f"q2, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")
            #print(stack)

        ## for state q2
        elif state == 'q2' and i == '(':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q2'
            stack.append(i)
            print(f"q2, {i}, epsilon -> {state}, {i}\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q3
        elif state == 'q3' and i.isnumeric():
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q5'
            print(f"q3, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q4
        elif state == 'q4' and i == '.':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q5'
            print(f"q4, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q4
        elif state == 'q4' and i.isnumeric():
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q4'
            print(f"q4, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q5
        elif state == 'q5' and i.isnumeric():
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q5'
            print(f"q5, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q5
        elif state == 'q5' and i == ')' and stack[-1] == '(':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.pop()
            state = 'q6'
            print(f"q5, {i},( -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q5
        elif state == 'q5' and i == '+' or i == '-' or i == '*' or i == '/':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q2'
            print(f"q5, {i},epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q5
        elif state == 'q5' and i == 'a' and stack[-1] == 'a':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.pop()
            state = 'q7'
            print(f"q5, {i},a -> {stack}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q6
        elif state == 'q6' and i == '+' or i == '-' or i == '*' or i == '/':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            state = 'q2'
            print(f"q6, {i},epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q6
        elif state == 'q6' and i == ')' and stack[-1] == '(':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.pop()
            state = 'q6'
            print(f"q6, {i},( -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q6
        elif state == 'q6' and i == 'a' and stack[-1] == 'a':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.pop()
            state = 'q7'
            print(f"q6, {i},a -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q7
        elif state == 'q7' and i == 'b' and stack[-1] == 'b':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.pop()
            state = 'q7'
            print(f"q7, {i},b -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q7
        elif state == 'q7' and i == 'a' and stack[-1] == 'z0':
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            stack.pop()
            state = 'q8'
            print(f"q7, {i},z0 -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## for state q8
        elif state == 'q8' and not stack:
            # print(f"Current input symbol under R-Head: {i}")
            # print(f"Current state: {state}\n")
            print("Accepted\n\n")
            break
        else:
            #print(f"The string is rejected at {state} state and input symbol {i}")
            rejected = True
            break
        
    if rejected:
        print("The machine Crashed")
        return f"The string is rejected at {state}\n" #state and input symbol {i}\n {i} , {state}, {i}, {stack[-1]} -> {state}, {i}\n
    elif not stack:
        return f"\nThe string is accepted at {state}\n"

print(isPDA(inp_string))