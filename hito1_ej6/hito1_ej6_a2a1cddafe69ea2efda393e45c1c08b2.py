#Ingresar los 3 numeros

a = int(input("Escriba el primer numero: "))
b = int(input("Escriba el segundo numero: "))
c = int(input("Escriba el tercer numero: "))

#Procedimiento

menor = min(a, b, c)
mayor = max(a, b, c)
medio = ( a + b + c ) - menor - mayor

#Resultado

print(" Los numeros ordenados de menor a mayor son: {} , {} , {}" .format(menor , medio , mayor ))
