PT=float(input("Ingresa promedio Tareas : "))
PI=float(input("Ingresa promedio Interrogaciones : "))
NE=float(input("Ingresa nota Exámen : "))
PP=float(input("Ingresa promedio Presentación : "))

promediofinal=((PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1))
print("El promedio final es:", (round(promediofinal,1)))