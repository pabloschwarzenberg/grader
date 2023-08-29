def rot13(palabra):
    postWord = []
    for i in range(len(palabra)):
        if ord(palabra[i])>=110:
            post = palabra.replace(palabra[i],chr(ord(palabra[i])-13))
            postWord.append(post[i])
        elif ord(palabra[i])<110: 
            post = palabra.replace(palabra[i],chr(ord(palabra[i])+13))       
            postWord.append(post[i])        
    return ''.join(postWord)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
