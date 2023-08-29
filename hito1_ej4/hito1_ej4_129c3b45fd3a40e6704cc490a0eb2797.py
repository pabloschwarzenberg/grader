#decimal a binario
n=eval(input("ingresa un numero: "))
contador= 0
#while n>0:
residuo= n%2 #el modulo es 0
print(residuo)
#n//2         #la division es 5
residuo1= (n//2)%2  # el modulo es 1
print(residuo1)
#(n/2)//2          #la divison es 2
residuo2= (n//4)%2  # el modulo es 0
print(residuo2)
#(n/4)//2          # la division es 1
residuo3= (n//8)%2  # el modulo es 1
print(residuo3)
residuo4= (n//16)%2
print(residuo4)
residuo5= (n//32)%2
print(residuo5)
residuo6= (n//64)%2
print(residuo6)
residuo7=(n//128)%2
print(residuo7)
if residuo6>residuo7:
 print("resultado = ",residuo6,residuo5,residuo4,residuo3,residuo2,residuo1,residuo)
if (residuo5>residuo6):
   print("resultado = ",residuo5,residuo4,residuo3,residuo2,residuo1,residuo)
if (residuo4>residuo5):
     print("resultado = ", residuo4,residuo3,residuo2,residuo1,residuo)
if (residuo3>residuo4):
        print("resultado = ", residuo3,residuo2,residuo1,residuo)