import random
a=["lepidoptero"]
palabra_secreta=random.choice(a)
def ocultar_letras(palabra_secreta,cantidad):
    lista=list(palabra_secreta)
    contador_espacios=0
    while(contador_espacios!=cantidad):
        posicion=random.randint(0,10)
        lista[posicion]="_"
        contador_espacios=contador_espacios+1
        for letra in lista:
            if(lista[posicion]!="_"):
                lista[posicion]="_"
                contador_espacios=contador_espacios+1
            else:
                continue
    return "".join(lista)

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=list(palabra_secreta)
    palabra=list(palabra)
    for i in range (len(palabra_secreta)-1):
        if letra in palabra_secreta:
            if palabra_secreta[i]==letra and palabra[i]=="_":
                palabra[i]=letra
            elif letra=="o" and palabra[10]=="_":
                palabra[10]="o"
    return "".join(palabra)                
if __name__ == "__main__":
    cantidad=int(input())
    palabra=ocultar_letras(palabra_secreta,cantidad)
    print(palabra)
    letra=str(input())
    while palabra_secreta!=palabra:
      letra=str(input())
      palabra=revisar_letra(palabra_secreta,palabra,letra)
      print(palabra)
