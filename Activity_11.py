def input_number():
    num = int(input("Enter a number :"))
    return num

def add(a, b):
    return a+b

def display(num1, num2, summation):
    print(f"{num1} + {num2} = {summation}")
    
def main():
    a = input_number()
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)

main()
