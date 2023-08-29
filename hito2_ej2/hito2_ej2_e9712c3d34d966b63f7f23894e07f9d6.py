genoma=input("Ingrese secuencia: ").lower()

for i in genoma:

    if i in "actg":
    
        valor=True
    else:
    
        valor=False
        break


if valor==True:

    print("Secuencia correcta")
    
else:
    print("Secuencia incorrecta") 