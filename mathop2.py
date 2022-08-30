a = 0
while a != 1:
    print("""1. Addition\n2. Subtraction\n3. Multiplication\n4. Division""")
    op = int(input("Enter your choice:-"))
    if op == 1:
        try:
            n1 = int(input("Enter Num 1:-"))
            n2 = int(input("Enter Num 2:-"))
            sum = n1 + n2
            print(f"This is your sum:-{sum}")
            a += 1
        except Exception as e:
            print(e)
    elif op == 2:
        try:
            n1 = int(input("Enter Num 1:-"))
            n2 = int(input("Enter Num 2:-"))
            sum = n1 - n2
            print(f"This is your sum:-{sum}")
            a += 1
        except Exception as e:
            print(e)

