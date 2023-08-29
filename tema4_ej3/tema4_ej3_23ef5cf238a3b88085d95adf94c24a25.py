def jerigonzo(string):
    string = list(string)
    for i in range(len(string)):
       if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
          string[i] = string[i] + "p" + string[i]    
    return "".join(string)

if __name__ == "__main__":
    string=input("Ingresar texto para traducir: ")
    string=string.lower()
    print(jerigonzo(string))
         