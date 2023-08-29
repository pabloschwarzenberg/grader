#Nota final
F = float(input("ingrese su numero para TAREAS: "))
I = float(input("ingrese su segundo numero para INTERROGACIONES: "))
E = float(input("ingrese su tercer numero para EXAMEN: "))
O = float(input("ingrese su cuarto numero para PRESENTACION: "))

conclusion = 0.3*F + 0.3*I+ 0.3*E + 0.1*O

print("El promedio final redondeado a un decimal es: " , round(conclusion,1))