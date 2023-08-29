def rot13(palabra):
    abc_1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    abc_2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    msg_rot = []
    for letra in palabra:
        if letra in abc_1:
            index = abc_1.index(letra)
            nueva_lera = abc_2[index]   
            msg_rot.append(nueva_lera)
        else:
            index = abc_2.index(letra)
            nueva_lera = abc_1[index]
            msg_rot.append(nueva_lera)
    print("".join(msg_rot))
    return "".join(msg_rot)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           