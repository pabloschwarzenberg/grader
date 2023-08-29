PT = eval(input("Ingresa notas de tareas: "))
PI = eval(input("Ingrese notas de interrogaciones: "))
NE = eval(input("Ingrese notas de examenes: "))
PP = eval(input("Ingrese notas de presentacion: "))
problema = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
resultado = round(problema, 1)
print(resultado)
      