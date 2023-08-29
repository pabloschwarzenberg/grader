primeros = "abcdefghijklm"
ultimos = "nopqrstuvwxyz"
def rot13(palabra):
    nueva= ""
    for i in palabra:
        if i in primeros:
            nueva+= chr(ord(i)+13)
        elif i in ultimos:
            nueva+=chr(ord(i)-13)
        else:
            nueva+=i
    return nueva
        
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

           