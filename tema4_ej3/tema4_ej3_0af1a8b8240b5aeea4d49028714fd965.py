def jerigonzo(x):
    v = ["a","e","i","o","u"]
    lis= list(x) 
    string = ""
    for i in lis:
        string = string + i
        for j in v:
            if i == j:
                string = string + "p" + i
    return string

if __name__ == "__main__":
    pass
    x=input("Ingrese su palabra: ")
    M= jerigonzo(x)