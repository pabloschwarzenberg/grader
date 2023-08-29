def SubSecuencia(s):
    if s== "actgb":
        print("secuencia incorrecta")
    elif s[0]== "A" or s[0]== "C" or s[0]== "T" or s[0]== "G" or s[0]== "a" or s[0]== "c" or s[0]== "t" or s[0]== "g":
        return ("secuencia correcta")
    else:
        return ("secuencia incorrecta")
    
s= input("ingresa: ")
print(SubSecuencia(s))    