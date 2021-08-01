def input_number():
    return int(input("Enter an integer: "))

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
            break
    else:
        return 1
            
def display(number, flag):
    if flag:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    
def main():
    number = input_number()
    flag = prime(number)
    display(number, flag)

main()
