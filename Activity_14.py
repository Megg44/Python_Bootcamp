import math
def input_dimensions():
    s = input("Enter length, breadth and height.")
    return list(map(float, s.split()))

def find_volume(my_list):
    return (my_list[2] ** 2)*(my_list[1] ** 2)/ math.sqrt((my_list[0] ** 2) + (my_list[1] ** 2) + (my_list[2] ** 2)) 

def find_radius(volume):
    return ((3 * volume) / (4 * math.pi)) ** (1/3)

def display_volume(volume):
    print(f"The volume of the tromboloid is {volume:.3f}")

def display_radius(volume, radius):
    print(f"The radius of the sphere with the volume {volume:.3f} would be {radius:.3f}.")

def main():
    my_list = input_dimensions()
    volume = find_volume(my_list)
    radius = find_radius(volume)
    display_volume(volume)
    display_radius(volume, radius)

main()
