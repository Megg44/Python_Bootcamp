def stringin():
    return input("Enter your string.")

def stringtodict(s):
    my_list = list(map(lambda x : x.partition("="), s.split(";")))
    return {x:z for (x, y, z) in my_list}

def printdict(dictionary):
    print(dictionary)

def main():
    string = stringin()
    dictionary = stringtodict(string)
    printdict(dictionary)

main()
