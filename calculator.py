import math

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

# Nuevas funciones científicas
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def main():
    print("Scientific Calculator")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin (degrees)")
    print("8. Cos (degrees)")
    
    choice = input("Enter choice (1-8): ")
    
    if choice in ['1', '2', '3', '4', '5']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {sum(a, b)}")
        elif choice == '2':
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            print(f"Result: {power(a, b)}")
    else:
        a = float(input("Enter number: "))
        if choice == '6':
            print(f"Result: {square_root(a)}")
        elif choice == '7':
            print(f"Result: {sin(a)}")
        elif choice == '8':
            print(f"Result: {cos(a)}")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()