secuencia=input("Secuencia: ")

secuencia=secuencia.upper()

lista_secuencia=list(secuencia)
a=True

for i in lista_secuencia:
    if i=="A" or i=="C" or i=="T" or i=="G":
        a=True
    else:
        a=False
        break

if a==True:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")