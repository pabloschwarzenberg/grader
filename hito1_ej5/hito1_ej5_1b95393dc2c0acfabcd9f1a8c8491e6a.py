#Cálculo del dígito verificador de un rut

#Algoritmo: escribir un programa que calcule el número verificador (el que viene después del guión) de los rut.

rut= int(input("Ingrese los nros de su rut que vienen antes del guión: "))
rut2= str(rut) #transformado a string.
largo_rut= len(rut2) #contar el número de dígitos del rut.

print("Cantidad de dígitos del rut: ",largo_rut)

if largo_rut== 8: #rut con 8 dígitos.
    n1= int(rut2[7])*2
    n2= int(rut2[6])*3
    n3= int(rut2[5])*4
    n4= int(rut2[4])*5
    n5= int(rut2[3])*6
    n6= int(rut2[2])*7
    n7= int(rut2[1])*2
    n8= int(rut2[0])*3

else: #rut con menos de 7 dígitos.
    n1= int(rut2[6])*2
    n2= int(rut2[5])*3
    n3= int(rut2[4])*4
    n4= int(rut2[3])*5
    n5= int(rut2[2])*6
    n6= int(rut2[1])*7
    n7= int(rut2[0])*2
    n8= 0

suma= n1+n2+n3+n4+n5+n6+n7+n8

#print("Resultado suma: ",suma)

r_division= suma//11

residuo= suma - (11*r_division)

n_verif= 11 - residuo

#print("Parte entera: ",r_division)
#print("Residuo de 11 menos la parte entera: ",residuo)

if n_verif== 11:
    print("dv= 0")
elif n_verif== 10:
        print("dv= k")
else:
    print("dv=",n_verif)