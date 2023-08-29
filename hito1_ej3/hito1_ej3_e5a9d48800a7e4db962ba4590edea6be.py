#Aprobación de créditos
ingreso=input()
nac=input()
hijos=input("")
pertenencia=input()
estadocivil=input()
dondevive=input()
if pertenencia>="10" and hijos>"2" :
    print("APROBADO")
elif estadocivil=="C"and hijos>"3" and nac>="1972" and nac<="1962":
     print("APROBADO")
elif ingreso>"200000" and estadocivil=="S" and dondevive=="U":
     print("APROBADO")
elif ingreso>"3500000" and pertenencia>"5":
     print("APROBADO")
elif dondevive=="R" and estadocivil=="C" and hijos<"2":
    print("APROBADO")
else:
    print("RECHAZADO")