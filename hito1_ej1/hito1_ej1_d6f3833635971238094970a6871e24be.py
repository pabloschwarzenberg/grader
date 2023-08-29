#Nota final
PT = eval(input("Ingrese la nota que obtuvo en sus tareas :"))
PI = eval(input("Ingrese la nota que obtuvo en sus interrogaciones :"))
NE = eval(input("Ingrese la nota que obtuvo en su exámen :"))
PP = eval(input("Ingrese la nota que obtuvo en su presentación :"))
valor1 = 0.3
valor2 = 0.1
valor3 = PT * valor1
valor4 = PI * valor1
valor5 = NE * valor1
valor6 = PP * valor2
valor7 = valor3 + valor4 + valor5 + valor6
print("Su promedio de notas es igual a :", "{0:.1f}".format(valor7))
      