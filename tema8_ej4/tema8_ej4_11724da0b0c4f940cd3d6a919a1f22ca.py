def rot13(palabra):
    alfb = "abcdefghijklmnopqrstuvwxyz"
    T = (alfb[13:]) + (alfb[:13])
    rot_alfb = lambda x: T[alfb.find(x)] if alfb.find(x)>-1 else x
    return ''.join(rot_alfb(x) for x in palabra) 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           