#Aprobación de créditos
a=int(input("ingreso"))
b=int(input("añonacimiento"))
c=int(input("numerohijos"))
d=int(input("años_en_el_banco"))
e=input("Soltero_Casado")
f=input("Urbano_Rural")
if d>10 and c>=2:
    print("APROBADO")
elif e=="C" and c>3 and 1961<b<1971:
    print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and c<2:
    print("APROBADO")
else:
    print("RECHAZADO")
          