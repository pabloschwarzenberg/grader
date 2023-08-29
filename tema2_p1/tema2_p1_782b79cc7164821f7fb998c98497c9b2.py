x=int(input('Ingrese un numero: '))
def es_primo(a):
  
  for i in range(0,a):
    
    if (a%2) ==0:
      return print(False)
      
    else:
      suma=0
      suma=suma+i
      return print(True)
     
l=es_primo(x)
print(l)  