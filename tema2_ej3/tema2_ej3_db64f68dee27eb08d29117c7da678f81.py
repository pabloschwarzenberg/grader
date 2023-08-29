def numero_perfecto(a):
    i=1
    suma=0
    while i<a:
        if a%i==0:
            suma=suma+i
        i=i+1
    if suma==a:
      return True
    else:
      return False
if __name__ == "__main__": 
  n=int(input("Ingrese n:"))
  u=2
  suma=0
  while u<n:
      if numero_perfecto(u):
          suma=suma+u
      u=u+1
  print(suma)
  
           