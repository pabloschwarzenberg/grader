secuencia=input("secuencia: ")
for i in range(0,len(secuencia)):
    a=secuencia[i]
    if a=="A" or a=="T" or a=="G" or a=="C":
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")