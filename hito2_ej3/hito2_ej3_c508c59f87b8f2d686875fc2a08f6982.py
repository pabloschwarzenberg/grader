string=input("Secuencia: ")
entero=int(input("Subgrupos: "))
indice=0
lista=[]
valido=""
while indice<len(string):
    letra=string[indice]
    sub_lista=list(string[indice:entero])
    for i in sub_lista:
        cantidad=sub_lista.count(i)
        if cantidad>1:
            valido="False"
            break
        else:
            valido="True"
    if valido=="True":
        lista=lista+sub_lista
    entero+=1
    indice+=1
if lista==[]:
    print("Ninguna")
else:
    for i in lista:
        print (i)