def rot13(palabra):
    palabra=str(palabra)
    palabra1=palabra
    lista_primeras_letras=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista_letras_restantes=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    string_primeras_letras="".join(lista_primeras_letras)
    string_letras_restantes="".join(lista_letras_restantes)
    for k in lista_primeras_letras:
        l=string_primeras_letras.find(k)
        l2=lista_letras_restantes[l]
        if k in palabra:
            palabra=palabra.replace(k,l2)
    lista_palabra=list(palabra)
    for j in lista_letras_restantes:
        n=-1
        if j in palabra1:
            m=palabra1.count(j)
            c=1
            n=-1
            p=[]
            while c<=m:
                n=palabra1.find(j,n+1)
                p.append(n)
                c=c+1
            l=string_letras_restantes.find(j)
            l2=lista_primeras_letras[l]
            for i in p:
                lista_palabra[i]=l2
    palabra="".join(lista_palabra)
    print(palabra)
    return palabra
                

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           