ADN=input("Base nitrogenadas:")
ADN=ADN.upper()
ADN_REAL="ACGT"
for i in ADN_REAL:
    ADN=ADN.replace(i,"")
if len(ADN)==0:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
    