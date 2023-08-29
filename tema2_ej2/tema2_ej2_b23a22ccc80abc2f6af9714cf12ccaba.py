# completa el código de la función
def main(a,b):  
  divisoresA=[]
  for i in range(1,a+1):
    if a%i==0:
      divisoresA.append(i)
      x=sum(divisoresA)-a   
  divisoresB=[]
  for j in range(1,b+1):
    if a%j==0:
      divisoresB.append(j)
      y=sum(divisoresB)-b
    
  if x==b and y==a:
    return True
  return False