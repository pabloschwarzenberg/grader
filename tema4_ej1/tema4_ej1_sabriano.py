import random
def ocultar_letras(palabra,cantidad):
   palabra_1=list(palabra)
   for i in range(0,cantidad):
       n=random.randint(0,len(palabra)-1)
       while palabra_1[n]==" _ ":
           n=random.randint(0,len(palabra)-1)
       del palabra_1[n]
       palabra_1.insert(n," _ ")
   palabra="".join(palabra_1)
   return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta1=list(palabra_secreta)
    palabra1=list(palabra)
    for i in range(0,len(palabra1)):
        print(i)
        if letra==palabra_secreta1[i]:
            del palabra1[i]
            palabra1.insert(i,letra)
        palabra="".join(palabra1)
    return palabra
if __name__ == "__main__":
    pass
         