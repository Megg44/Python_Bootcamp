def input_strings():
    s = input()
    my_list = s.split('.')
    my_list.pop()
    return my_list
           
def sort_1(my_list):
    return sorted(my_list)

def sort_2(my_list):
    my_list.sort()

def display(my_list):
    print(s)
    
def main():
    my_list = input_strings()
    print(my_list)
    new_list = sort_1(my_list)
    sort_2(my_list)
    print(f"sorted() output = {new_list}")
    print(f"sort() output = {my_list}")
    
main()
