s = input()
my_list = list(map(lambda x: int(x), s.split()))
sum = sum(my_list)

print(f"Sum of all the numbers is = {sum}") 
