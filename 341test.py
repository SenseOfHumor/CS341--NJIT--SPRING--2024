str = "njit@njithbwbgiwbiugwbu.gov.fsgd"
state = 0

for i in range(len(str)):
    char = str[i]
    print(state)
    if state == 0:
        if char.isalpha():
            state = 1
        else:
            print("Invalid String")
            break
    elif state == 1:
        if char.isalpha():
            state = 1
        elif char == '@':
            state = 2
        else:
            print("Invalid String")
            break
    elif state == 2:
        if char.isalpha():
            state = 3
        else:
            print("Invalid String")
            break
    elif state == 3:
        if char.isalpha():
            state = 3
        elif char == '.':
            state = 4
        else:
            print("Invalid String")
            break
    elif state == 4:
        if char == 'g':
            state = 5
        else:
            print("Invalid String")
            break
    elif state == 5:
        if char == 'o':
            state = 6
        else:
            print("Invalid String")
            break
    elif state == 6:
        if char == 'v':
            print("Valid String")
        else:
            print("Invalid String")
            break
