def numero_perfecto(a):
  d=1
  suma=0
  if a==1:
    return False 
  while d<a:
    if a%d==0:
      suma+=d
      d+=1
    else:
       d+=1
  if suma==a:
    return True
  elif suma != a:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           