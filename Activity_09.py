import math
s = input("Enter length, breadth and height.")
my_list = list(map(float, s.split()))

volume = (my_list[2] ** 2)*(my_list[1] ** 2)/ math.sqrt((my_list[0] ** 2) + (my_list[1] ** 2) + (my_list[2] ** 2)) 

r = ((3 * volume) / (4 * math.pi)) ** (1/3)

print(f"The volume of the tromboloid is {volume:.3f} and the radius of the sphere with the same volume would be {r:.3f}.")
