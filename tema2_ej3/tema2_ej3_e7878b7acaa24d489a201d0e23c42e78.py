def numero_perfecto(a):
  contador=1
  contador2=0
  divisores=[]
  suma=0
  while contador<a:
    if a%contador==0:
      divisores.append(contador)
    contador+=1 
  while contador2<len(divisores):
    suma=suma+divisores[contador2]
    contador2+=1
  if suma==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           