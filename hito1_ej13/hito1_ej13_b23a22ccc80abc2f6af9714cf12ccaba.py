#Factores Primos
def main(a):  
  divisores=[]
  if a==2:
    e=2
    divisores.append(e) 
  for i in range(2,a):
    if a%i==0 and i<13:
      divisores.append(i)
  for divisor in divisores:
    print (divisor)         
  return divisor 
 
  
 