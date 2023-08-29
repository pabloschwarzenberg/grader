import random
def ocultar_letras(palabra,cantidad): 
    p=list(palabra)
    cambiar=random.sample(p,cantidad)
    repetidas = []
    for i in p:
        if i in cambiar:
          if not i in repetidas:
            indice=p.index(i)
            p[indice]="_"
            repetidas.append(i)
    retorno=" ".join(p) 
    return retorno 


def revisar_letra(palabra_secreta,palabra,letra): 
    if letra in palabra_secreta:  
        pos=[]
        for i in range(0,len(palabra)):
            if palabra_secreta[i]==letra:
                pos.append(i)
        lista=list(palabra)
        for b in pos:
            lista[b]=letra
        pnueva="".join(lista)
        return pnueva
    else:
        nein="No esta"
        return nein 
        
if __name__ == "__main__":   
  l=["tenedor","calabaza","miercoles","malestar","mantequilla","calculadora"]
  palabraa=random.choice(l)
  largo_palabra=len(palabraa)
  cant=random.randint(1,largo_palabra-1)
  t=7
  while t>0: 
    le=input("Ingrese una letra o palabra") 
    guess=revisar_letra(palabraa,oculta,le)   
    if palabraa==guess: 
      print("Ganaste") 
    elif guess==nein:  
      print(nein)
      t=t-1  
    elif guess==ya_esta: 
      print(ya_esta) 
      t=t-1
  print("Perdiste")
  
     