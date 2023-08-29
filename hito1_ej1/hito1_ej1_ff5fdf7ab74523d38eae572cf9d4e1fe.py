def promedio():
    PT=float(input("Nota tareas: "))
    PI=float(input("Nota interrogaciones: "))
    NE=float(input("Nota examen: "))
    PP=float(input("Nota presentacion: "))

    a=3*(PT)/10
    b=3*(PI)/10
    c=3*(NE)/10
    d=PP/10

    print( round(a+b+c+d,1))
promedio()