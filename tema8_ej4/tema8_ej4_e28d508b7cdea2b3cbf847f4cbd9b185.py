def rot13(palabra):
    palabra_list=list(palabra)
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra_final=[]
    for p in palabra_list:
        for i in range(0,len(letras)):
            if letras[i] == p:
                if i+14<=len(letras):
                    palabra_final.append(letras[(i+13)])
                elif i+14>len(letras):
                    s=(i+13)-len(letras)
                    palabra_final.append(letras[s])
    palabra="".join(palabra_final)
    return palabra
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           