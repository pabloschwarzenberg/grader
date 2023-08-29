import random
def ocultar_letras(palabra_secreta,cantidad):
    x=list(palabra_secreta)
    for i in range(1,cantidad+1):
      pocicion=random.randint(0,len(palabra_secreta)-1)
      x[pocicion]="_"
    palabra_secreta="".join(x)  
    return palabra_secreta
def revisar_letra(palabra_secreta,palabra,letra):
    x=list(palabra)
    y=list(palabra_secreta)
    for i in range(0,len(y)):
        if y[i]==letra:
            x[i]=letra
    return "".join(x)

         