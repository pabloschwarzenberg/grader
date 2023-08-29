num = int(input("Introduce el número: ")) 
def factor(num): 
  lista =[]
  for i in range(2,int(num)+1):
    if prime(i):
      if num%i==0:
        c =1
        while num%i**c==0:
          c +=1
        print(i)
    
  return(lista)
def prime(num):
  if num == 2:
    return True
    
  if num !=2 and num%2 == 0:
    return False
    
  for i in range(3,int(num**0.5)+1,2):
    if num%i==0:
      return False
      
  
  return True
x=(factor(num))
print((x))