#Ejercicio 11
cadena0=input("Ingrese a la cadena: ")
cadena=cadena0.upper()
cadena1=cadena.replace("A"," ")
print(cadena1)
cadena2=cadena1.replace("C"," ")
print(cadena2)
cadena3=cadena2.replace("T"," ")
print(cadena3)
cadena4=cadena3.replace("G"," ")
print(cadena4)
A=cadena4.split()
if A==[]:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")