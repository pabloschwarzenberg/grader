hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
    frase_list=list(frase)
    numero_palabras=frase.split(" ")
    num_pal=0 
    num_pal=len(numero_palabras)
    num_let=0
    num_pun=0
    num_esp=0
    num_back=0
    num_back_2=0
    i=0
    for i in range(len(frase_list)):
        if frase_list[i]==".":
            num_pun+=1       
    for j in range(len(frase_list)):
        if frase_list[j]==" " :
            num_esp+=1
        elif frase_list[j]=="\n":
            num_back+=1
            if frase_list[j+1].isupper():
                num_back_2+=1
        else:
            num_let+=1

    print(num_back)
    num_pal=num_pal+num_back-num_back_2
    num_let=num_let+num_esp+num_back
    promedio=(num_let-num_esp-num_pun-num_back)/num_pal
    promedio=round(promedio,2)
    return num_pal, num_let, promedio, num_esp, num_pun
            
if __name__ == "__main__":
    pass
    print(estadisticas_frase(hombre_imaginario))