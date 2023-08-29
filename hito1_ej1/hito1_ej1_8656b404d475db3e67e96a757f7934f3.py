#Nota final
S1=float(input("ingrese nota de solemne1: "))
S2=float(input("ingrese nota de solemne2: "))
TATT=float(input("ingrese nota final de servidor EDX: "))
MIC=float(input("ingrese la nota de actividad Microsoft: "))
T1=float(input("ingrese nota de tarea 1: "))
T2=float(input("ingrese nota de tarea 2: "))
T3=float(input("ingrese nota de tarea 3: "))
T4=float(input("ingrese nota de tarea 4: "))
NF=0.7*NPE + 0.3*NOTA_EXAMEN

          NF_v2 = round(NF,1)

          print("tu nota final corresponde a: ",NF_v2)

          if NF>=4.0:

                    print("has aprobado")

          else:

                    print("REP")

--

