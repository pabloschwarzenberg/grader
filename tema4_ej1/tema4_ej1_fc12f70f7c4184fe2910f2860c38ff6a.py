import random
def ocultar_letras(palabra,cantidad):
    k=""
    lista=[]
    for y in palabra:
        lista.append(y)
    if palabra=="montaña":
        for x in range(cantidad):
            cambio=random.randrange(1,8)
            if cambio==1:
                lista[0]="_"
            elif cambio==2:
                lista[1]="_"
            elif cambio==3:
                lista[2]="_"
            elif cambio==4:
                lista[3]="_"
            elif cambio==5:
                lista[4]="_"
            elif cambio==6:
                lista[5]="_"
            elif cambio==7:
                lista[6]="_"
        return k.join(lista)
    elif palabra=="piedra" or palabra=="animal":
        for x in range(cantidad):
            cambio=random.randrange(1,7)
            if cambio==1:
                lista[0]="_"
            elif cambio==2:
                lista[1]="_"
            elif cambio==3:
                lista[2]="_"
            elif cambio==4:
                lista[3]="_"
            elif cambio==5:
                lista[4]="_"
            elif cambio==6:
                lista[5]="_"
        return k.join(lista)
    elif palabra=="rio":
        for x in range(cantidad):
            cambio=random.randrange(1,4)
            if cambio==1:
                lista[0]="_"
            elif cambio==2:
                lista[1]="_"
            elif cambio==3:
                lista[2]="_"
        return k.join(lista)
def revisar_letra(palabra_secreta,palabra,letra):
    list(palabra_secreta)
    k=""
    contador=0
    for x in palabra_secreta:
        if x=="_" and k.join(palabra_secreta)=="montaña":
            if x==palabra_secreta[0] and letra=="m":
                palabra_secreta[0]=="m"
            elif x==palabra_secreta[1] and letra=="o":
                palabra_secreta[0]=="o"
            elif x==palabra_secreta[2] and letra=="n":
                palabra_secreta[0]=="n"
            elif x==palabra_secreta[3] and letra=="t":
                palabra_secreta[0]=="t"
            elif x==palabra_secreta[4] or x==palabra_secreta[6]and letra=="a":
                palabra_secreta[4]=="a"
                palabra_secreta[6]="a"
            elif x==palabra_secreta[5] and letra=="ñ":
                palabra_secreta[5]=="ñ"
            else:
                contador+=1
        return palabra_secreta