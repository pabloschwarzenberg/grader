def rot13(palabra):
    string=""
    for i in range(0,len(palabra)):
        letra=palabra[i:i+1]
        if ord(letra)+13>=123:
            x=ord(letra)+13-123
            uwu=chr(97+x)
            string+=uwu
        else:    
            uwu=chr(ord(letra)+13)
            string+=uwu
        
    return string

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
 

           