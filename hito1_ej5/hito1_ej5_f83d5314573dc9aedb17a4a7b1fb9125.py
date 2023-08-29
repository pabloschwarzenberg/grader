#Cálculo del dígito verificador de un rut
a1=int(input("Ingrese digito 1 del rut: "))
a2=int(input("Ingrese digito 2 del rut: "))
a3=int(input("Ingrese digito 3 del rut: "))
a4=int(input("Ingrese digito 4 del rut: "))
a5=int(input("Ingrese digito 5 del rut: "))
a6=int(input("Ingrese digito 6 del rut: "))
a7=int(input("Ingrese digito 7 del rut: "))
a8=int(input("Ingrese digito 8 del rut: "))

suma = (a8*2)+(a7*3)+(a6*4)+(a5*5)+(a4*6)+(a3*7)+(a2*2)+(a1*3)
resto = int(suma/11)
multi = resto*11
sustraccion = suma - multi
code = 11 - sustraccion
print(code)