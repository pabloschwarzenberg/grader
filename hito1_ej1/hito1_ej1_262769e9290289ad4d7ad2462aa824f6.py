print("ingrese sus notas: Tareas, Interrogaciones, examen y presentacion")
tareas=float(input("tareas:"))
interrogaciones=float(input("interrogaciones:"))
examen=float(input("examen:"))
presentacion=float(input("presentacion:"))
formula= round((0.3*(tareas) + 0.3*(interrogaciones) + 0.3*(examen) + 0.1*(presentacion))**1,1)
print("el resultado final es:",(formula))