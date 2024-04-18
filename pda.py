inp_string = "abba+6.5abba"

## creating the function for PDA
##print(f"Present state: {state} \nCurrent input symbol under R-Head {i} \nStack top: {stack[-1]} \nSymbol popped from the stack: {stack.pop()} \nSymbol pushed into the stack: {push} \nNext state: {state} \n")

def isPDA(string):
    stack = []
    state = 'q0'
    rejected = False

    for i in string:
        if state == 'q0' and i == 'a':
            push = stack.append('z0')
            state = 'q1'
            print(f"{i},epsilon -> z0")
            #print(stack)
        ## for state q1
        elif state == 'q1' and i == 'a':
            stack.append(i)
            state = 'q2'
            print(f"{i},epsilon -> {i}")
            #print(stack)

        ## still for state q1
        elif state == 'q1' and i == 'b':
            stack.append(i)
            state = 'q1'
            print(f"{i},epsilon -> {i}")
            #print(stack)

        ## for state q2
        elif state == 'q2' and i.isnumeric():
            state = 'q4'
            print(f"{i},epsilon -> epsilon")
            #print(stack)

        ## for state q2
        elif state == 'q2' and i == '.':
            state = 'q3'
            print(f"{i},epsilon -> epsilon")
            #print(stack)

        ## for state q2
        elif state == 'q2' and i == '(':
            state = 'q2'
            stack.append(i)
            print(f"{i},epsilon -> {i}")

        ## for state q3
        elif state == 'q3' and i.isnumeric():
            state = 'q5'
            print(f"{i},epsilon -> epsilon")

        ## for state q4
        elif state == 'q4' and i == '.':
            state = 'q5'
            print(f"{i},epsilon -> epsilon")

        ## for state q4
        elif state == 'q4' and i.isnumeric():
            state = 'q4'
            print(f"{i},epsilon -> epsilon")

        ## for state q5
        elif state == 'q5' and i.isnumeric():
            state = 'q5'
            print(f"{i},epsilon -> epsilon")

        ## for state q5
        elif state == 'q5' and i == ')' and stack[-1] == '(':
            stack.pop()
            state = 'q6'
            print(f"{i},( -> epsilon")

        ## for state q5
        elif state == 'q5' and i == '+' or i == '-' or i == '*' or i == '/':
            state = 'q2'
            print(f"{i},epsilon -> epsilon")

        ## for state q5
        elif state == 'q5' and i == 'a' and stack[-1] == 'a':
            stack.pop()
            state = 'q7'
            print(f"{i},a -> epsilon")

        ## for state q6
        elif state == 'q6' and i == '+' or i == '-' or i == '*' or i == '/':
            state = 'q2'
            print(f"{i},epsilon -> epsilon")

        ## for state q6
        elif state == 'q6' and i == ')' and stack[-1] == '(':
            stack.pop()
            state = 'q6'
            print(f"{i},( -> epsilon")

        ## for state q6
        elif state == 'q6' and i == 'a' and stack[-1] == 'a':
            stack.pop()
            state = 'q7'
            print(f"{i},a -> epsilon")

        ## for state q7
        elif state == 'q7' and i == 'b' and stack[-1] == 'b':
            stack.pop()
            state = 'q7'
            print(f"{i},b -> epsilon")

        ## for state q7
        elif state == 'q7' and i == 'a' and stack[-1] == 'z0':
            stack.pop()
            state = 'q8'
            print(f"{i},z0 -> epsilon")

        ## for state q8
        elif state == 'q8' and not stack:
            print("Accepted")
            break
        else:
            #print(f"The string is rejected at {state} state and input symbol {i}")
            rejected = True
            break
        
    if rejected:
        return f"\nThe string is rejected at {state} state and input symbol {i}\n"
    elif not stack:
        return "\nThe string is Accepted\n"

print(isPDA(inp_string))