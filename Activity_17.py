def stringin():
    return input("Enter your string.")

def stringtolist(s):
    my_list = list(map(lambda x : x.partition("="), s.split(";")))
    return [(x, z) for (x, y, z) in my_list]

def listtostring(my_list):
    newList = ["=".join(e) for e in my_list]
    return ";".join(newList)
    
    
def printlist(list_of_list):
    print(list_of_list)

def printstring(string):
    print(string)

def main():
    string = stringin()
    my_list = stringtolist(string)
    string2 = listtostring(my_list)
    printlist(my_list)
    printstring(string)

main()
