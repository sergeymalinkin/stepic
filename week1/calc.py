a = float(input())
b = float(input())
what = input()

if what == '+':
    c = a + b
    print(str(c))
elif what == '-':
    c = a - b
    print(str(c))
elif what == '/':
    if b != 0:
        c = a / b
        print(str(c))
    else:
        print("Деление на 0!")
elif what == '*':
    c = a * b
    print(str(c))
elif what == 'mod':
    if b != 0:
        c = a % b
        print(str(c))
    else:
        print("Деление на 0!")
elif what == 'pow':
    if b != 0:
        c = a ** b
        print(str(c))
    else:
        print("Деление на 0!")
elif what == 'div':
    if b != 0:
        c = a // b
        print(str(int(c)))
    else:
        print("Деление на 0!")