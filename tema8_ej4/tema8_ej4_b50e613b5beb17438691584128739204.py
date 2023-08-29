def rot13(palabra):
    lista_abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lista_pal = list(palabra)
    lista_rot = []
    for i in lista_pal:
        for p in range(len(lista_abc)):
            if (p>=0) and (p<=12):
                if i == lista_abc[p]:
                    lista_rot.append(lista_abc[p+13])
                else:
                    continue
            elif (p>=13) and (p<=25):
                if i == lista_abc[p]:
                    lista_rot.append(lista_abc[p-13])
                else:
                    continue
    rot13 = ''.join(lista_rot)
    return rot13
                
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower() #pasarlo a minúscula
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    
