from random import randint

def ocultar_letras(palabra,cantidad):
    #generar ubicaciones a ocultar
    ocultar=[]
    for i in range(1,cantidad+1):
        z=randint(0,(len(palabra))-1)
        while z in ocultar:
            z=randint(0,(len(palabra))-1)
        ocultar.append(z)
    #ocultar letras
    palabra_secreta=list(palabra)
    for i in ocultar:
        palabra_secreta[i]="_"
    palabra_secreta="".join(palabra_secreta)  
    return palabra_secreta

def revisar_letra(palabra,palabra_secreta,letra):
    palabra_secreta=list(palabra_secreta)
    #encontrar ubicaciones de la letra en la palabra
    ubicaciones_letra=[]
    x=0
    if len(letra)==1:
        while x<len(palabra):
            if  palabra[x]==letra:
                ubicaciones_letra.append(x)
            x+=1
        for i in ubicaciones_letra:
            palabra_secreta[i]=letra
        palabra_secreta="".join(palabra_secreta)
    if palabra==letra:
        palabra_secreta=palabra
    else:
        palabra_secreta="".join(palabra_secreta)
    return palabra_secreta

if __name__ == "__main__":
    palabras=["arbusto","vegetal","licantropo","filantropo",
              "reinato","espiroqueta","bachillerato","estatua",
              "hemoglobina","panadero","residencia","orquesta"]
    #elegir parabra y cantidad de letras ocultas
    palabra=palabras[randint(0,(len(palabras))-1)]
    cantidad=randint(1,len(palabra))
    #palabra secreta
    palabra_secreta=ocultar_letras(palabra,cantidad)
    print(palabra_secreta)
    #ingresar letra
    while palabra_secreta.isalpha()==False:
        letra=input("Ingrese letra: ").lower()
        palabra_secreta=revisar_letra(palabra,palabra_secreta, letra)
        print(palabra_secreta)