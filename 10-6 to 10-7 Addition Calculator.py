
session_active = True
while session_active:
    try :
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        answer = num1 + num2
        print(answer)
        session_active = False

    except ValueError:
        print("Please enter numeric values")

