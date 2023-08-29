def rot13(palabra):
    palabra_nueva=""
    lista_palabra=list(palabra)
    abecedario1="abcdefghijklm"
    abecedario2="nopqrstuvwxyz"
    for i in palabra:
        n1=abecedario1.find(i)
        n2=abecedario2.find(i)
        if n1!=-1:
            palabra_nueva+=abecedario2[n1]
        else:
            palabra_nueva+=abecedario1[n2]


    return palabra_nueva
           