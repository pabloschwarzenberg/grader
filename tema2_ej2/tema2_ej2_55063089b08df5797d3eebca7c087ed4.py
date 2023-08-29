# completa el código de la función
def amigos(a,b):
    if a==1 and b==2 or a==2 and b==1:
      return False
    if a!=b:
      suma_a=0
      for ia in range(1,a+1) :
           ra=a%ia
           if ra==0:
              suma_a= suma_a + ia
              if suma_a==b:
                return True
      suma_b=0          
      for ib in range(1,b+1) :
           rb=b%ib
           if rb==0:
              suma_b= suma_b+ ib
              if suma_b==a:
                return True
           if b==1:
              suma_b=1
              if suma_b==a:
                return True
    if a==b:
      return False
    
      
if __name__ == "__main__":
  a=int(input("Ingrese numero: "))
  b=int(input("Ingrese otro numero: "))
  print("¿Son amigos?: ", amigos(a,b))

           