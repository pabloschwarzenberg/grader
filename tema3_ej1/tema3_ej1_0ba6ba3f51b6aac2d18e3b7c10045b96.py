# completa el código de la función
def suma_divisores(a):
  def es_primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
           return False
    return True
  multiplo=1
  Slista=[]
  while multiplo<=a:
    if a%multiplo==0:
        if a%multiplo==0:
            Slista.append(multiplo)
            multiplo+=1
        elif a%multiplo!=0:
            multiplo+=1
    elif a%multiplo!=0:
        multiplo+=1
  suma=sum(Slista[0:len(Slista)-1])  
  return (suma,es_primo(suma))
           