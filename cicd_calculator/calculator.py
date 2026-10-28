def add(a , b):
    return a+b

def sub(a , b):
    return a - b

def mul(a , b):
    return a * b

def div(a , b):
    if b == 0 :
        raise ValueError("cannot divide by zero")
    return a / b

def main():
    a = 10 
    b = 5

    print("Python calculator :")
    print("First  number :" , a)
    print("Second  number :" , b)
    print("Addition  number :" ,add(a , b))
    print("Substraction  number :" ,sub(a , b))
    print("Multiplication number :" ,mul(a , b))
    print("Division  number :" ,div(a , b))

if __name__ == "__main__":
    main()