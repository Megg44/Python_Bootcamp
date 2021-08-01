def input_number():
    s = input()
    return list(map(int, s.split()))

def greatest(my_list):
    if my_list[0] > my_list[1] & my_list[0] > my_list[2]:
        return my_list[0]
    elif my_list[1] > my_list[2]:
        return my_list[1]
    else:
        return my_list[2]
    
def display(my_list, greatest_num):
    print(f"{greatest_num} is the greatest number among {my_list[0]}, {my_list[1]} and {my_list[2]}.")
    
def main():
    my_list = input_number()
    greatest_num = greatest(my_list)
    display(my_list, greatest_num)

main()
