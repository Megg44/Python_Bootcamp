def stringin():
    return input("Enter your string.")

def stringtolist(s):
    my_list = list(map(lambda x : x.partition("="), s.split(";")))
    new_list = [(x, z) for (x, y, z) in my_list]
    return new_list
    
def printlist(list_of_list):
    print(list_of_tuples)

def main():
    string = stringin()
    my_list = stringtolist(string)
    print(my_list)

main()
