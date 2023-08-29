secuencia=input("ingrese secuencia de ADN",)
largosecuencia=len(secuencia)
n=0
while n<largosecuencia:
    

    if secuencia[n]=="a":
        n=n+1
    elif secuencia[n]=="t":
        n=n+1
    elif secuencia[n]=="c":
        n=n+1
    elif secuencia[n]=="g":
        n=n+1
    else:
        print("secuencia incorrecta")
        break
print("secuencia correcta")