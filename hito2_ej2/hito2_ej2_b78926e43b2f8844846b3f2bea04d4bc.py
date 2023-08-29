a=input("ingrese un genoma: ")
b="actg"



valido = True
for letra in a:
       if letra not in b and letra not in b.upper():
            valido= False
            break

if valido:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
