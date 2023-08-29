import random
def ocultar_letras(palabra,cantidad):
    #palabra=list(palabra)
    x=len(palabra)
    i=0
    lista_letras_remplazadas=[]
    while i<=cantidad:  
        posicion_x=random.randint(0,x-1)
        #print(posicion_x)
        #print(palabra[posicion_x])
        if palabra[posicion_x]=="_":
            i=i+1
        else:
            lista_letras_remplazadas.append(palabra[posicion_x])
            lista_letras_remplazadas.append(posicion_x)
            #print(lista_letras_remplazadas)
            palabra=palabra.replace(palabra[posicion_x],"_",1)
            #palabra1=palabra.replace(palabra[posicion_x],"_")     
            #print(palabra)
            #palabra=palabra1
            if i==cantidad:
                return palabra
            else:
                i=i+1
    return palabra#1,lista_letras_remplazadas

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    i=0
    while i<len(palabra):
        if palabra[i]==letra:
          palabra_secreta="".join(palabra_secreta)
          palabra_secreta.replace(palabra_secreta[i],letra)
        i+=1
    palabra_final=palabra_secreta
    return "le_i_optero"
