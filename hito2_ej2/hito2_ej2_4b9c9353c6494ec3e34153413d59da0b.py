x = input("Ingrese : ").lower()
lista = list(x)
y = "actg"
for i in y:
   lista.remove(i)
if len(lista) == 0:
   print("secuencia correcta")
else:
   print("secuencia incorrecta")