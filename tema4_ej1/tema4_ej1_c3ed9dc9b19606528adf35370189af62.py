from random import randint
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    p_s=palabra
    i=0
    k=[]
    pos_ocupadas=[]
    while i!=cantidad:
        k=randint(0,cantidad+1)        
        if p_s[k] == "_":
            pass
        else:
            p_s.pop(k)
            p_s.insert(k,"_")
            pos_ocupadas.append(k)
            i+=1
    p_s="".join(p_s)
    return p_s

def revisar_letra(palabra_secreta,palabra,letra):
    pos=[]
    p_s=list(palabra_secreta)
    palabra=list(palabra)
    for i in range(len(p_s)):
      if letra == p_s[i]:
        if p_s[i] == palabra[i]:
          pass
        else:
          palabra.pop(i)
          palabra.insert(i,letra)
    palabra="".join(palabra)
    return palabra