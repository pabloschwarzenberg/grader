#Ordenar tres números
a1 =int(input("Ingrese un numero natural"))
a2 =int(input("Ingrese un numero natural"))
a3 =int(input("Ingrese un numero natural"))
if a1>=a2>=a3 :
       N1=a3,a2,a1
       print(N1)
if a1>=a3>=a2 :
       N2=a2,a3,a1
       print(N2)
if a2>=a1>=a3 :
       N3=a3,a1,a2
       print(N3)
if a2>=a3>=a1 :
       N4=a1,a3,a2
       print(N4)
if a3>=a2>=a1 :
       N5=a1,a2,a3
       print(N5)
if a3>=a1>=a2 :
       N6=a2,a1,a3
       print(N6)
