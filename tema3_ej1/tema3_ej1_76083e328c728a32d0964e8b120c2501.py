# completa el código de la función
def suma_divisores(a):
  div_a =[i for i in range(1,a) if a %i==0]
  sumadiv_a = 0
  for j in div_a:
    sumadiv_a= sumadiv_a + j

  if sumadiv_a==1:
    return sumadiv_a,True
  else:
    return sumadiv_a,False

if __name__ == "__main__":
  a=int(input("numero: "))
  print (suma_divisores(a))
           