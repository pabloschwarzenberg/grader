#Nota final
PT = float(input("ingrese su nota de tarea: "))
PI = float(input("ingrese su nota de interrogatorio: "))
NE = float(input("ingrese su nota de el examen: "))
PP = float(input("ingrese su nota de prsentacon: "))
PT = float(PT* 0.3)
PI = float(PI* 0.3)
NE = float(NE*0.3)
PP = float(PP* 0.1)
NotaFinal = PT + PI + NE + PP
print("Nota final:", NotaFinal)   