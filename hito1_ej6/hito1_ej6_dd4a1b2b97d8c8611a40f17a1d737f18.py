#Ordenar tres números
número1=int(input("a: "))
número2=int(input("b: "))
número3=int(input("c: "))

if número1>=número2>=número3:
    print(número3,",",número2,",",número1)
if número1>=número3>=número2:
    print(número2,",",número3,",",número1)
if número2>=número3>=número1:
    print(número1,",",número3,",",número2)
if número2>=número1>=número3:
    print(número3,",",número1,",",número2)
if número3>=número2>=número1:
    print(número1,",",número2,",",número3)
if número3>=número1>=número2:
    print(número2,",",número1,",",número3)
      