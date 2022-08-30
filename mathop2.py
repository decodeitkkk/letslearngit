a = 0
while a != 1:
    print("""1. Addition\n2. Subtraction\n3. Multiplication\n4. Division""")

    try:
        n1 = int(input("Enter Num 1:-"))
        n2 = int(input("Enter Num 2:-"))
        sum = n1 + n2
        print(f"This is your sum:-{sum}")
        a += 1
    except Exception as e:
        print(e)

print('You ran this successfully')

