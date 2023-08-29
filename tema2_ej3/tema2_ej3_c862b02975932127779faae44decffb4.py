def numero_perfecto(a):
  posibles_divisoresa=1
  sum_divisoresa=0  
 
  while posibles_divisoresa<a:
      if a%posibles_divisoresa==0:
          sum_divisoresa+=posibles_divisoresa
      posibles_divisoresa+=1     
          
  if sum_divisoresa==a:       
    return True
  else:
     return False
  i=1 
  sum_np=0  
  while i<a:
      if numero_perfecto(i)==True:
          sum_np+=i
      i+=1
  return sum_np
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           