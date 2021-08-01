s = input()
my_list = list(map(int, s.split()))

sum = sum(my_list)
print(f"{my_list[0]} + {my_list[1]} = {sum}")
