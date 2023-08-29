trabajos=["la tareas","la interrogacion","el examen","la presentacion"]
notas=[]
ponderaciones=[]
semi=[]
pre=0
total=0
if __name__ == "__main__":
    for i in trabajos:
      nota=input(f"ingrese su nota obtenida en {trabajos[trabajos.index(i)]} :\n")
    ponderacion=input(f"ingrese ponderacion:\n ")
    notas.append(float(nota))
    ponderaciones.append(float(ponderacion))
  for x in range(3):
    pre=float(notas[x])*float(ponderaciones[x])
    total=total+pre
  print("Su nota final ponderada es: "+str(total))