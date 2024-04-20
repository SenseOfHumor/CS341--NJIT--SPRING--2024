
"""
Swapnil Deb
sd2269
CS 341
Project 2
Section 006
Spring 2024
"""
## creating the function for PDA
##print(f"Present state: {state} \nCurrent input symbol under R-Head {i} \nStack top: {stack[-1]} \nSymbol popped from the stack: {stack.pop()} \nSymbol pushed into the stack: {push} \nNext state: {state} \n")

def isPDA269(string):
    stack = []
    state = 'q0'
    rejected = False
    reason = ""

    print("__________________________________________________________")
    print(f"\nThe string under processing is: {string}")
    print("The format is as: Current State, Current Input Symbol, Popped Symbol if any -> Next State, Pushed Symbol if any\n")
    print("Starting State: q0")

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
                
        elif state == 'q2' and i == ')':
            state = 'q9'
            print(f"q2, {i}, epsilon -> {state}, epsilon\n")

        ## for state q2
        elif state == 'q2' and i == '.':
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

        elif state == 'q2' and i.isalpha():
            state = 'q9'
            print(f"q2, {i}, epsilon -> {state}, epsilon\n")

        elif state == 'q2' and i == '+':
            state = 'q9'
            print(f"q2, {i}, epsilon -> {state}, epsilon\n")

        elif state == 'q2' and i == '*':
            state = 'q9'
            print(f"q2, {i}, epsilon -> {state}, epsilon\n")

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

        ## error handling for state q3
        elif state == 'q3' and i.isalpha():
            state = 'q9'
            print(f"q3, {i}, epsilon -> {state}, epsilon\n")

        elif state == 'q3' and i == '+':
            state = 'q9'
            print(f"q3, {i}, epsilon -> {state}, epsilon\n")

        elif state == 'q3' and i == '*':
            state = 'q9'
            print(f"q3, {i}, epsilon -> {state}, epsilon\n")



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

        elif state == 'q4' and i == ')':
            state = 'q9'
            print(f"q4, {i}, epsilon -> {state}, epsilon\n")

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

        ## for state q5 and i is '.'
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
            print(f"q5, {i},a -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        ## error handling for state q5
        elif state == 'q5' and i == 'a':
            state = 'q7'
            print(f"q5, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        elif state == 'q5' and i == '.':    
            state = 'q9'
            print(f"q5, {i}, epsilon -> {state}, epsilon\n")

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

        ## error handling for state q6
        elif state == 'q6' and i == 'a':
            state = 'q7'
            print(f"q6, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        elif state == 'q6' and i == ')':
            state = 'q6'
            print(f"q6, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        elif state == 'q6' and i.isnumeric():
            print(f"q6, {i}, epsilon -> {state}, epsilon\n")
            state = 'q9'

        elif state == 'q6' and i == '.':
            print(f"q6, {i}, epsilon -> {state}, epsilon\n")
            state = 'q9'

        

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
        ## error handling for state q7
        elif state == 'q7' and i == 'b':
            state = 'q8'
            print(f"q7, {i}, epsilon -> {state}, epsilon\n")
            if stack:
                print(f"Stack Top: {stack[-1]}\n\n")
            else:
                print("Stack Top: epsilon")

        elif state == 'q7' and i == 'b':
            state = 'q8'
            print(f"q7, {i}, epsilon -> {state}, epsilon\n")
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

        # elif i == 'b' or i == 'a' and state == 'q2':
        #     print("the string is not acceptable because such transition is not possible")

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
        

    ## if the stack is empty and the string is not rejected
    ## logic for accepting and rejecting the string
    if rejected:
        if state == 'q8':
            reason = "the stack is not empty"
        # elif state != 'q8':
        #     reason = f"the machine encountered an invalid transition at state {state} and input symbol {i}"
        elif stack and state == 'q8':
            reason = "the stack is not empty"
        elif not string and state != 'q8':
            reason = "the string ended before reaching the final state q8"
        elif not string and stack and state != 'q8':
            reason = "the stack is not empty"
        # elif i == 'a' and stack[-1] != 'a':
        #     reason = f"the stack top: {stack[-1]} does not match with the input symbol: {i}"
        elif i == ')' and stack[-1] != '(':
            reason = f"the stack top: {stack[-1]} does not match with the input symbol: {i}"
        elif i == 'b' and stack[-1] != 'b':
            reason = f"the stack top: {stack[-1]} does not match with the input symbol: {i}"
        elif i == 'a' and stack[-1] == 'b':
            reason = f"the stack top: {stack[-1]} does not match with the input symbol: {i}"
        elif not string and stack:
            reason = "the stack is not empty"
        # elif state != 'q8':
        #     reason = f"the machine encountered an invalid transition at state {state} and input symbol {i}"
        elif state == 'q2' and not string:
            reason = "the string ended before reaching the final state q8"
        elif state == 'q9':
            print("The string entered a trap state")
            reason = "such a transition is not possible"
        
        

        print("the machine crashed")
        return f"The string {string} is not acceptable by the given PDA because {reason} \n" #state and input symbol {i}\n {i} , {state}, {i}, {stack[-1]} -> {state}, {i}\n

    elif not stack:
        return f"\nThe string is accepted.\n"

## Program specitications
    
    ## the fwrites can be ignored because they are used to print the output to a document.
    ## the print statements are used to print the output to the console.
    ## everything is working as expected.
with open('output.txt', 'w') as f:
    f.write("\nProject 2 for CS 341\n")
    f.write("Section number: 006\n")
    f.write("Semester: Spring 2024\n")
    f.write("Written by: Swapnil Deb, sd2269\n")
    f.write("Instructor: Arashdeep Kaur, ak3257@njit.edu\n")

    ## asking user inputs
    index = int(input("Enter the number of strings you want to test (integer): "))
    f.write(f"Number of strings to test: {index}\n")
    for i in range(index):
        print("_"*50)
        inp_string = input(f"Enter string {i+1} of {index}: ")
        f.write(f"String {i+1}: {inp_string}\n")
        result = isPDA269(inp_string)
        f.write(f"Result: {result}\n")
        print(result)