def rot13(palabra):
    palabra.lower()
    resultado= ''
    desplazamiento = 13
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for a in palabra:
        if a in abc:
            resultado += abc[(abc.index(a)+desplazamiento)%(len(abc))]
        else:
            resultado+=a
    return resultado
    pass
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    print("El resultado es: ",rot13(palabra))