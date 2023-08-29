#nota final
tareas=float(input( "Inserte su nota de tareas: "))
interrogaciones=float(input( "Inserte su nota de interrogaciones: "))
examenes=float(input( "Inserte su nota de examenes: "))
presentacion=float(input( "Inserte su nota de presentacion: "))
Resultadopromedio= (tareas*30/100)+(interrogaciones*30/100)+(examenes*30/100)+(presentacion*10/100)
print (str(round(Resultadopromedio, 1)))