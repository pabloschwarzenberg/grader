def rot13(palabra):
    abc="abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    for i in range (0,len(palabra)):
        z=-1
        for c in abc:
            z=z+1
            if c==palabra[i]:
                palabra=palabra[:i]+abc[(z+13)%26]+palabra[i+1:]
                break
    return palabra
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           