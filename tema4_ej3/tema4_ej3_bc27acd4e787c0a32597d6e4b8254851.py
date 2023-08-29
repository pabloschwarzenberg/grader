def jerigonzo(string):
    string=string.lower()
    string=list(string)
    i=0
    while i<len(string):
        if string[i]=="a" or string[i]=="e" or string[i]=="i" or  string[i]=="o" or string[i]=="u":
            string.insert(i+1,"p")
            string.insert(i+2,string[i])
            i=i+3
        else:
            i=i+1
    strin=''.join(string)
    return strin

if __name__ == "__main__":
    a=str(input("Ingrese la palabra a traducir "))
    a=jerigonzo(a)
    print(a)
         