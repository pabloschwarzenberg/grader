def numero_perfecto(a):
    suma=0
    for i in range(1,a):
      if a%i==0:
        suma=suma+i
    if suma==a:
      return True
    elif suma!=a:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print("el numero es perfecto: ",numero_perfecto(a))
    n=int(input("Ingrese un numero: "))
n=9
suma2=0    
for i in range(1,n):
  if numero_perfecto(i)==True:
     suma2=suma2+i
if __name__=="__main__":
  print(suma2)
