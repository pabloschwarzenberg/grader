#Nota final
      pt = float(input("nota de tareas: ") or "0")
      pi = float(input("nota de interrogaciones: ") or "0")
      ne = float(input("nota de examen: ") or "0")
      pp = float(input("nota de presentacion: ") or "0")
      promedio_final = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
      print(round(promedio_final,1))