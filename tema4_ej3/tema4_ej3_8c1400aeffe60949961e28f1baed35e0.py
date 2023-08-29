def jerigonzo(string):
    string_transformado=""
    for j in range(0,len(string)):
        if string[j]=="a":
            string_transformado += string[j] + "p"
        if string[j]=="e":
            string_transformado += string[j] + "p"
        if string[j]=="i":
            string_transformado += string[j] + "p"
        if string[j]=="o":
            string_transformado += string[j] + "p"            
        if string[j]=="u":
            string_transformado += string[j] + "p"
        else:
            string_transformado += string[j]

    return string_transformado

if __name__=="__main__":
    texto=input("ingrese el texto que desea transformar: ")
    resultado=jerigonzo(texto)
    print("el texto transformado es: ",resultado)