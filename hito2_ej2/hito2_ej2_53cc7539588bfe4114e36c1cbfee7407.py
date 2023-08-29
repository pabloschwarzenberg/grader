import sys
secuencia=str(input("Inserte secuencua : "))
secuencia=secuencia.lower()
secuencia_l=list(secuencia)
for n in range(0,len(secuencia_l)):
    print(secuencia_l[n])
    if secuencia_l[n]=="a" or secuencia_l[n]=="c" or secuencia_l[n]=="t" or secuencia_l[n]=="g":
        pass
    else:
        print("secuencia incorrecta")
print("secuencia correcta")