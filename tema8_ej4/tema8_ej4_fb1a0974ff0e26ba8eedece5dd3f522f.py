def rot13(palabra):
    lista1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    l_palabra = []
    string = ""
    for letra in palabra:
        l_palabra.append(letra)
    print(l_palabra)
    print(len(l_palabra))
        
    for i in range(len(l_palabra)):
        print(i)
        if l_palabra[i] in lista1:
            a = lista1.index(l_palabra[i])
            l_palabra[i] = lista2[a]
            print(l_palabra[i],lista1[a],lista2[a])
            

        elif l_palabra[i] in lista2:
            a = lista2.index(l_palabra[i])
            l_palabra[i] = lista1[a]
            print(l_palabra[i],lista2[a],lista1[a])
            
    for letra in l_palabra:
        string = string + letra

    return string   

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)


           