def numero_perfecto(a):
  global suma
  global lista
  suma=0
  lista=[]
  for i in range(1,a):
    if a%i==0:
      lista.append(i)
  for i in lista:
     suma= suma + i
  if suma==a:
    return(True)
  else:
    return(False)
      
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           