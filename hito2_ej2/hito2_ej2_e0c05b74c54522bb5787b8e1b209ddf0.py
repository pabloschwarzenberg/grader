def secuencia(string):  
    string=str(string)
    string=string.lower()
    contador_1=0
    while contador_1<=len(string)-1:
        if string[contador_1]=="a" or string[contador_1]=="c" or string[contador_1]=="t" or string[contador_1]=="g":
          contador_1=contador_1+1
        else:
          return "secuencia incorrecta"
          break
    return "secuencia correcta"
string=str(input())
print(secuencia(string))



