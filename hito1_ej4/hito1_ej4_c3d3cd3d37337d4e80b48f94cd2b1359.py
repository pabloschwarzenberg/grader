#decimal a binario
n=eval(input("ingresa un numero: "))
contador= 0
#while n>0:
binario= n%2 #el modulo es 0
print(binario)
#n//2         
binario1= (n//2)%2  
print(binario1)
#(n/2)//2          
binario2= (n//4)%2  
print(binario2)
#(n/4)//2          
binario3= (n//8)%2  
print(binario3)
binario4= (n//16)%2
print(binario4)
binario5= (n//32)%2
print(binario5)
binario6= (n//64)%2
print(binario6)
binario7=(n//128)%2
print(binario7)
if binario6>binario7:
  print("resultado = ",binario6,binario5,binario4,binario3,binario2,binario1,binario)
if (binario5>binario6):
  print("resultado = ",binario5,binario4,binario3,binario2,binario1,binario)
if (binario4>binario5):
  print("resultado = ", binario4,binario3,binario2,binario1,binario)
if (binario3>binario4):
  print("resultado = ", binario3,binario2,binario1,binario)