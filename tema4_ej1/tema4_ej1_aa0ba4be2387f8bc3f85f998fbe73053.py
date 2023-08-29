import random
def ocultar_letras(palabra,cantidad):
    j1=list(palabra)
    div=""
    for sort in range(cantidad):
        sort=sort
        j1[random.randint(1,len(j1))]="_"
    for h in range(len(j1)):
        div=div+j1[h]
    palabra_secreta=div
    return palabra_secreta

def revisar_letra(palabra_secreta,palabra,letra):
    div=""
    j4=list(palabra_secreta)

    for i in range(len(j4)):
      if(palabra[i]==letra):
        j4[i]=letra
    for h in range(len(j4)):
      div=div+j4[h]
    palabra_secreta=div
    return div
         