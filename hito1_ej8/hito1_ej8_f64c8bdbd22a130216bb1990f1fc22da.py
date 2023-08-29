#Descomponer un número
valor = int(input("Ingrese un numero de hasta 4 digitos: "))
a1 = int(valor/1000)
b1 = a1%10
a2 = int(valor/100)
b2 = int(a2%10)
a3 = valor%100
b3 = int(a3/10)
b4 = valor%10
b1 = str(b1)
c1 = (b1+"M")
b2 = str(b2)
c2 = (b2+"C")
b3 = str(b3)
c3 = (b3+"D")
b4 = str(b4)
c4 = (b4+"U")
print(c1,"+",c2,"+",c3,"+",c4)
      