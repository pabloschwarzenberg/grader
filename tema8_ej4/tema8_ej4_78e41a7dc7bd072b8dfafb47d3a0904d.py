def rot13(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    tradu = abc[13:]+abc[:13]
    rot_str = lambda x: tradu[abc.find(x)] if abc.find(x)>-1 else x
    return ''.join( rot_str(x) for x in s )

if __name__=="__main__":
    entrada=input("Ingresa la palabra que deseas encriptar: ")
    entrada.lower()
    resul=rot13(entrada)
    print("El resultado es: ",resul)
