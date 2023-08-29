n1 = int(input('ingresa tres numeros enteros: '))
n2 = int(input('ingresa tres numeros enteros: '))
n3 = int(input('ingresa tres numeros enteros: '))

if(n1>=n2>=n3):
  print(n3, ',', n2, ',', n1)

if(n1>=n3>=n2):
  print(n2, ',', n3, ',', n1)
 
if(n2>=n1>=n3):
  print(n3, ',', n1, ',', n2)
  
if(n2>=n3>=n1):
  print(n1, ',', n3, ',', n2)
  
if(n3>=n1>=n2):
  print(n2, ',', n1, ',', n3)
  
if(n3>=n2>=n1):
  print(n1, ',', n2, ',', n3)
