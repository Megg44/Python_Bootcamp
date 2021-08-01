s = input()
my_list = list(map(int, s.split()))

sliced_list = my_list[0:3]
print(f"sliced list = {sliced_list}")
my_list[0], sliced_list[0], my_list[-1], sliced_list[-1] = 0, 0, 0, 0
print(f"replaced list-1 = {my_list}")
print(f"replaced list-1 = {sliced_list}")
