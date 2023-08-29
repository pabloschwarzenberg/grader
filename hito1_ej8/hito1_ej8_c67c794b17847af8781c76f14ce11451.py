#Descomponer un número
numero=int(input("ingrese un numero de 4 digitos: "))
while numero>9999:
    print("ingrese un numero valido.")

m= int((numero-(numero % 1000))/1000)
residuo1=numero % 1000
c=int((residuo1-(residuo1 % 100))/100)
residuo2=residuo1 % 100
d=int((residuo2-(residuo2%10))/10)
u=int(residuo2 % 10)
print(m,"M +",c,"C +",d,"D +",u,"U")
      