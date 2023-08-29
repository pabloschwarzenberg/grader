a = eval(input("Ingreso en pesos: "))
b = eval(input("Año de nacimiento: "))
c = eval(input("Número de hijos: "))
d = eval(input("Años de pertenencia al banco: "))
e = str(input("Estado civil (S: soltero, C, casado): "))
f = str(input("Si vive en campo o cuidad (U: urbano, R: rural): "))


if e=="c" and f=="r" and c>2:
    print("APROBADO")    
else:
    print("RECHAZADO")
    
    
if e=="c" and c>3 and b>1965 and b<1975:
    print("APROBADO")
else:
    print("RECHAZADO")    

if a>2500000 and e=="s" and f=="u":
    print("APROBADO")
else:
    print("RECHAZADO")


    

if a>3500000 and d>5:
    print("APROBADO")
else:
    print("RECHAZADO")

    

    
if d>10 and c>=2:
    print("APROBADO")
else:
    print("RECHAZADO")    
    
    
    