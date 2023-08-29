#Descomponer un número
numero=input("Ingrese un numero: ")
variable=len(numero)
if variable==4:
    print(numero[0]+"M + "+numero[1]+"C + "+numero[2]+"D + "+numero[3]+"U")
elif variable==3:
    print(numero[0]+"C + "+numero[1]+"D + "+numero[2]+"U")
elif variable==2:
    print(numero[0]+"D + "+numero[1]+"U")
else:
    print(numero[0]+"U")     