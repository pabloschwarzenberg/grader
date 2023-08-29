def rot13(palabra):
    nig = "abcdefghijklmnopqrstuvwxyz"
    abc = list(nig)
    nik = len(palabra)
    loko = []

    for i in range(nik):
        if(abc.index(palabra[i])<12):

            rr = abc.index(palabra[i])+13
            loko.insert(i,abc[rr])

        else:

            rr = abc.index(palabra[i])+13
            x = rr-26
            loko.insert(i,abc[x])


    m = ''.join(loko)
    
    return m


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           