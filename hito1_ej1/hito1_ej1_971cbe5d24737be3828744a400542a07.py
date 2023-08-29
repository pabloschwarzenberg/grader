print("ingrese notas")
npt = eval(input("nota tareas: "))
npi = eval(input("nota interrogaciones: "))
nne = eval(input("nota examen: "))
npp = eval(input("nota presetacion: "))

p = round(npt*0.3 + npi*0.3 + nne*0.3 + npp*0.1, 1)
print("el promedio es: ", p)   