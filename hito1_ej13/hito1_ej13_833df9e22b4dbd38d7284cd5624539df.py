def es_primo(numero): # indica si el valor ingresado es primo 
    if(numero==1):
      return(False)
    for i in range(2,numero): 
        if(numero%i)==0:
            return(False)
    return(True)
      
valor=int(input("ingrese numero a descomponer:"))
for i in range(2,valor):
    if(valor%i)==0 and (es_primo(i)==True):
        print(i)
if valor==2:
    print(valor)
    