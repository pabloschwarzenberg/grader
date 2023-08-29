# completa el código de la función
numero=int()
def suma_divisores(numero):
  for n in range(2,numero):
    if numero%n==0:
      divisores=[]
      divisores.append(n)
      suma=len(divisores)
      return suma
def primo(suma):
    if suma==1:
      return True
    elif suma!=1:
      return False
      
print(suma_divisores,primo)
    
    
  