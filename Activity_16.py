def stringin():
    return input("Enter your string.")

def stringtolist(s):
    my_list = list(map(lambda x : x.partition("="), s.split(";")))
    new_list = []
    for e in my_list:
        x, y, z = e
        temp = (x, z)
        new_list.append(temp)
    return new_list
    
def printlist(list_of_list):
    print(list_of_tuples)

def main():
    string = stringin()
    my_list = stringtolist(string)
    print(my_list)

main()
