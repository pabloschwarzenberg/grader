cadena=input()
for i in cadena:
    if i.upper()!="A" and i.upper()!="C" and i.upper()!="G" and i.upper()!="T":
        valida=False
        break
    else:
        valida=True
if valida==False:
    print("secuencia incorrecta")
else:
    print("secuencia correcta")