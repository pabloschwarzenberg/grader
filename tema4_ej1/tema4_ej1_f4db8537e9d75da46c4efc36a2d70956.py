import random
def ocultar_letras(palabra,cantidad):
    p=list(palabra)
    i=0
    while i<cantidad:
      l=["_"]
      j=random.randint(0,(len(p)-1))
      p[j]=l[0]
      i=i+1
      palabra="".join(p)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    p=list(palabra)
    s=list(palabra_secreta)
    l=list(letra)
    i=0
    while i<len(s):
      if s[i]==l[0]:
        p[i]=l[0]
      i=i+1
    palabra="".join(p)
    return palabra

if __name__ == "__main__":
    pass
         