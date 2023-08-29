#Aprobación de créditos
ing=int(input("Ingreso"))
ano=int(input("año"))
hij=int(input("hijos"))
an=int(input("años banco"))
ec=input("estado civil")
cc=input("zona")
if an>10 and hij>=2:
 print("APROBADO")
elif ec=="C" and hij>3 and 1962<ano<1975:
 print("APROBADO")
elif ing>2500000 and ec=="S" and cc=="U":
 print("APROBADO")
elif ing>3500000 and an>5:
 print("APROBADO")
elif cc=="R" and ec=="C" and hij<2:
 print("APROBADO")
else: print("datos invalidos")
