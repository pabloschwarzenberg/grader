n1=int(input("ingrese numero1:"))
n2=int(input("ingrese nuero2:"))
n3=int(input("ingrese numero3:"))

if(n1>=n2>=n3):
      print(n3,",",n2,",",n1)
elif(n1>=n3>=n2):
      print(n2,",",n3,",",n1)
elif(n2>=n1>=n3):
      print(n3,",",n1,",",n2)
elif(n2>=n3>=n1):
      print(n1,",",n3,",",n2)
elif(n3>=n1>=n2):
      print(n2,",",n1,",",n3)
elif(n3>=n2>=n3):
      print(n3,",",n2,",",n1)
