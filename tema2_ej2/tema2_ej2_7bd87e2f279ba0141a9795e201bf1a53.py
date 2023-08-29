def suma_divisores1(divisores1):
    sum=0
    for i in range(0,len(divisores1)):
        sum=sum+divisores1[i]
    return sum

def suma_divisores2(divisores2):
    sum=0
    for i in range(0,len(divisores2)):
        sum=sum+divisores2[i]
    return sum
a=0
b=0
if __name__ == "__main__":
 print("Veamos si tus numeros son amigos")
 num1= int(input("Ingresa el primer numero:"))
 num2= int(input("Ingresa el segundo numero:"))
a= a+num1
b= b+num2
def amigos(divisores1,divisores2):    
  divisores1=[]
  x=1  
  while x<a:
      a/x
      if a%x==0:
       divisores1.append(x)
      x= x+1
  suma1=int(suma_divisores1(divisores1))              

  divisores2=[]
  y=1
  while y<b:
       b/y
       if b%y==0:
        divisores2.append(y)
       y= y+1
  suma2=int(suma_divisores2(divisores2))
  if (a == suma2) and (b == suma1):
    return True
  else:
    return False
amigos(a,b) 