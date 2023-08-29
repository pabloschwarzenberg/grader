#Aprobación de créditos
ing=str(input("¿Cuántos son tus ingresos?: $"))
añodn=int(input("¿En cuál año naciste?: "))
ndhijos=int(input("¿Cuántos hij@s tienes?: "))
añosenbanco=int(input("¿Cuántos años llevas en el banco?: "))
ecivil=str(input("¿Cuál es su estado civil? Escriba 'S' si es solter@ o 'C' si es casado@: "))
lvive=str(input("¿Dónde vive? Escriba 'U' si es urbado o 'R' si es rural: "))

if añosenbanco>10 and ndhijos>=2:
    print("APROBADO")
elif ecivil=="C" and 1963<añodn<1973:
    print("APROBADO")
elif ing>2500000 and ecivil=="S" and lvive=="C":
    print("APROBADO")
elif ing>3500000 and añodn>5:
    print("APROBADO")
elif lvive=="R" and ecivil=="C" and ndhijos<2:
    print("APROBADO")
    