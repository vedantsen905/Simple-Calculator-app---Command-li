def add_number(a,b):
    return a+b

def subtract_number(a,b):
    return a-b

def multiply_number(a,b):
    return a*b

def divide_number(a,b):
    return a/b

def square_number(a):
    return a**a





def main():
    while True :

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Exit")

        choice = input("Enter your choice  ")

        if choice == '1':
            name = float(input("Write First Number "))
            name = float(input("Write Second Number "))
            print(add_number(name,name))
        

        if choice == '2':
            name = float(input("write your first number "))
            name = float(input("write your second number "))
            print(subtract_number(name,name))

        if choice == '3':
            name = float(input("write your first number "))
            name = float(input("write your second number "))
            print(multiply_number(name,name))

        if choice == '4':
            name = float(input("write your first number "))
            name = float(input("write your second number "))
            print(divide_number(name,name))

        if choice == '5':
            name = float(input("write your number "))
            print(square_number(name))
        

        if choice == '6':   
            break


main()