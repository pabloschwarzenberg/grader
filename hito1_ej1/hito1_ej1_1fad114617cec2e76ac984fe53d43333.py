PT=float(input("Tareas"))
PI=float(input("Interrogaciones"))
NE=float(input("Examen"))
PP=float(input("Presentacion"))
Promfinal=0.3*PT+0.3*PI+0.3*NE+0.1*PP
R=Promfinal*100
if R%10>=5:
    R=R+10-R%10
    print(R/100)
elif R%10<5:
    R=R-R%10
    print(R/100)


      