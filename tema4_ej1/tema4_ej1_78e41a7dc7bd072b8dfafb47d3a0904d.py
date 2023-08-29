# Adivina la palabra
import random

diccionario=["sol","azul","fuego","cancha","diamante","comadreja","paralelepípedo","lepidoptero"]

# elegir la palabra
str_select=random.choice(diccionario)
long_str=len(str_select)
index_oculto=[]

def ocultar_letras(s, cant):
    long_str=len(s)
    str = ''.join(s)
    str = list(str)

    conta=0
    while conta < cant:
        if cant >= long_str:
            print("Error: numero fuera de indice")
            break
        index = random.randrange(0, long_str)
        index_oculto.append(index)
        str[index]="_"
        conta+=1

    # regresa el string modificado con los caracteres ocultos
    str=''.join(str)
    return str

def revisar_letra(s_select,s_show,input):
    # solo para recorrer
    s_show_index=list(s_show)
    input=input.lower()
    flag=True
    puntero=0
    contamin=0
    contamax=len(index_oculto)
    # comprueba si la palabra es identica a la almacenada
    if input == s_select:
        s_show=s_select
        flag=False
        return s_show
    # reemplaza letra en palabra
    while contamin < contamax and flag==True:
        puntero=index_oculto[contamin]
        # si la letra ingresada es igual a la palabra original, en la posicion faltante
        if input == s_select[puntero]:
            # reemplazar en palabra oculta
            s_show_index[puntero]=input
        contamin+=1
    # retorna el string con la letra añadida, si corresponde
    s_show=''.join(s_show_index)
    return s_show
    
if __name__ == "__main__":
    str_oculto=ocultar_letras(str_select, 2)
    print("La palabra oculta es:", str_oculto)
    entrada=input("Por favor ingrese la letra a comprobar dentro de la palabra: ")
    rev_str_show=''.join(revisar_letra(str_select, str_oculto, entrada))
    print("Resultado: ",rev_str_show)