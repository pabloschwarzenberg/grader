import random
palabrasSecretas=["rojo","verde","amarillo","azul"]
palabraSecreta=random.choice(palabrasSecretas)

mostrar=random.randint(0,len(palabraSecreta))
cantidad=len(palabraSecreta)-mostrar

def ocultar_letras(palabra,cantidad):
    pos_ocultar=[]
    while len(pos_ocultar)!=cantidad:
        p=len(palabra)-1
        oc=random.randint(0,p)
        if not oc in pos_ocultar:
            pos_ocultar.append(oc)
    oculta=""
    for i in range(len(palabra)):
        if i in pos_ocultar:
            oculta=oculta+"_"
        else:
            oculta=oculta+palabra[i]
    return oculta
            
palabra=ocultar_letras(palabraSecreta,cantidad)
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_resultante=""
    i=0
    while i <len(palabra_secreta):
        if palabra_secreta[i]==letra:
            palabra_resultante=palabra_resultante+palabra_secreta[i]
        else:
            palabra_resultante=palabra_resultante+palabra[i]
        i=i+1
    return palabra_resultante