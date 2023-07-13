def calc():
    string = input('Enter your mathematical expression: ')
    sentence = ''.join(string.split())
    list2 = []
    currNum = 0
    operator = '+'
    for char in sentence + '+':
        if char.isdigit():
            currNum = (currNum * 10) + int(char)
        else:
            if operator == '+':
                list2.append(currNum)
            elif operator == '-':
                list2.append(int(f'-{currNum}'))
            elif operator == '*':
                list2.append(list2.pop() * currNum)
            elif char == '/':
                list2.append(int(list2.pop() / currNum))
            currNum = 0
            operator = char
    return sum(list2)

calc()