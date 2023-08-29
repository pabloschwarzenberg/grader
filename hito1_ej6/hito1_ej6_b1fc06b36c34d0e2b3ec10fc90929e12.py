numero1 = int(input("ingrese numero1 :"))
numero2 = int(input("ingrese numero2 :"))
numero3 = int(input("ingrese numero3 :"))

a = min(numero1, numero2,numero3)
c = max(numero1, numero2,numero3)
b = (numero1+numero2+numero3) -a -c
print (a,",",b,",",c,",")