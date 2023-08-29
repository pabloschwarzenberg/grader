def rot13(palabra):
    string=''
    lista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in palabra:
        if x in lista:
            c=0
            p=1
            while p:
                if lista[c]==x:
                    string+=lista[c+13]
                    p=0
                c+=1
    return string

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           