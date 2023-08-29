def euclides(num1,num2):
  if num2 == 0:
   return num1
  return euclides(num2, num1 % num2)

print(euclides(2,10))

def mcm(num1,num2,num1num2):
   r=(num1*num2)/(euclides(num1,num2))
   return r