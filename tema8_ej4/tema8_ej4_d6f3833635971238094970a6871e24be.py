def rot13(palabra):
    c = ""
    a = "abcdefghijklmnopqrstuvwxyz"
    for letra in palabra:
        x = a.find(letra)+ 13
        mod = int(x) % len(a)
        c = c + str(a[mod])
    return c
        
        
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           