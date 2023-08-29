import random
palabras=["elefante","helipuerto","senpai","almohada","lala","noculpesalaluna"]
palabra=random.choice(palabras)

cantidad_lista=[]
for i in range(0,len(palabra)):
    cantidad_lista.append(i)   
cantidad=random.choice(cantidad_lista)
cantidad_oculta=len(palabra)-cantidad
    
def ocultar_letras(palabra,cantidad_oculta):
    palabranew=''
    listapalabra=list(palabra)
    listapos=range(0,len(palabra))
    
    for i in range(0,cantidad_oculta):
        a=random.choice(listapos)
        listapalabra[a]="_"
    palabranew=''.join(listapalabra)
    return palabranew


def revisar_letra(palabra,palabranew,letra):
    #letra=input('letra: ')
    #palabranew=ocultar_letras(palabra,cantidad)
    for i in range(0,len(palabra)):
        if palabra[i]==letra and palabranew[i]=='_':
            #palabrafinal=palabranew.replace('_',letra,i)
            palabranew_list=list(palabranew)
            palabranew_list[i]=letra
            palabranew=''.join(palabranew_list)

    return palabranew


if __name__ == "__main__":
    pass
         