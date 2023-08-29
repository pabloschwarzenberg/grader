#Nota final
print("PT = Tareas\nPI = Interrogaciones\nNE = Examen\nPP = Presentación\n")
nota1= float(input("ingrese nota PT: "))
nota2= float(input("ingrese nota PI: "))
nota3= float(input("ingrese nota NE: "))
nota4= float(input("ingrese nota PP: "))
promedio = (0.3*nota1)+(0.3*nota2)+(0.3*nota3)+(0.1*nota4)
print(f"El promedio final es: {round(promedio, 1)}")      