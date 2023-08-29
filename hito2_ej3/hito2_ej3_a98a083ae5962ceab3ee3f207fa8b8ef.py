def adn(palabra,n):
    i=0
    lista=[]
    nadie=0
    while i<len(palabra)-2:
        substr=palabra[i:(i+n)]
        lista.append(substr)
        i+=1

    for x in lista:
        if lista.count(x)==1:
            nadie+=1
            print(x)
    if nadie==0:
        print("ninguna")

palabra2=input("ingrese substr")
numero2=int(input("ingrese numero"))
adn(palabra2,numero2)