# completa el código de la función
def suma_divisores(a):
  d=[]
  for i in range(1,a):
    if a%i==0:
      d.append(i)
      
  if sum(d)==1:
    return(sum(d),True)
  else:
    return(sum(d),False)
 
if __name__ == "__main__":
  a=int(input("ingrese numero: "))
  print(suma_divisores(a))