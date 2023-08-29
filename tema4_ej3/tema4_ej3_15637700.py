def jerigonzo(string):
    string = list(string)
    s = string[:]
    A = s.count("a")
    c = 0
    i = 0
    while i<A:
        x = s.index("a")
        string.insert(x+c+1, "pa") 
        s.remove("a")
        c += 2
        i += 1
    E = s.count("e")
    s = string[:]
    c = 0
    i = 0
    while i<E:
        x = s.index("e")
        string.insert(x+c+1, "pe") 
        s.remove("e")
        c += 2
        i += 1
    I = s.count("i")
    s = string[:]
    c = 0
    i = 0
    while i<I:
        x = s.index("i")
        string.insert(x+c+1, "pi") 
        s.remove("i")
        c += 2
        i += 1
    O = s.count("o")
    s = string[:]
    c = 0
    i = 0
    while i<O:
        x = s.index("o")
        string.insert(x+c+1, "po") 
        s.remove("o")
        c += 2
        i += 1
    U = s.count("u")
    s = string[:]
    c = 0
    i = 0
    while i<U:
        x = s.index("u")
        string.insert(x+c+1, "pu") 
        s.remove("u")
        c += 2
        i += 1
    stri = ""
    for i in range(len(string)):
        stri += string[i]
    string = stri
    print(string)    
    return string

if __name__ == "__main__":
    string=input("Ingresar string: ")                  
    jerigonzo(string)
