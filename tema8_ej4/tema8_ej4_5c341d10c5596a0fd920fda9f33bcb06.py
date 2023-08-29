def rot13(palabra):
    string="abcdefghijklmnopqrstuvwxyz"
    lista=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista_palabra=[]
    listapalabrafinal=[]
    for letra in palabra:
        lista_palabra.append(letra)
    for i in lista_palabra:
        numero=string.find(i)
        nueva_letra=lista[numero]
        listapalabrafinal.append(nueva_letra)
    palabra_final="".join(str(e) for e in listapalabrafinal)
    return palabra_final
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
        
