def numero_perfecto(a):
  global suma
  suma=0
  lista=[]
  n=int(a)
  for i in range(1,n):
    if n%i==0:
      lista.append(i)
    i+=1
  for numero in lista:
    suma+=numero
  if suma==n:
    return True
  else: 
    return False

if __name__=="__main__":
    print(numero_perfecto(a))
           