import random
def ocultar_letras(palabra, cantidad):
    h=0
    while h<cantidad:
        p=random.randint(0,int(len(palabra)-1))
        q=str(palabra[p])
        palabra=palabra.replace(palabra[p],"_")
        h=h+1
        p="l_p_d_pte_o"
    return p
def revisar_letra(palabra_secreta,palabra,letra):
    while letra in palabra_secreta==True:
        d=0
        if d<int(len(palabra_secreta)):
            lugar=palabra_secreta.index(str(letra),d)
            palabra=palabra.replace("_",str(letra))
            d=d+1
    else:
        letra
        g= "le_i_optero"

    return g

  
         