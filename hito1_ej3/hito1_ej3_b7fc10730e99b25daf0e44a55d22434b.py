#Aprobación de créditos
ing=int(input("escriba su ingreso: "))
nac=int(input("escriba su año de nacimiento: "))
hij=int(input("escriba cuantos hijos tiene: "))
año=int(input("escriba cuantos años lleva en el banco: "))
est=input("escriba su estado civil con una S para soltero y C para casado: ")
res=input("escriba si vive en la ciudad con una U o con una R si vive en el campo: ")

S=1
C=2
U=3
R=4

if año >= 10 and hij >= 2:
    print("APROBADO")


elif est == 2 and hij >= 3 and nac > 1976 or nac < 1966:
    print("APROBADO")


elif ing >= 2500000 and est == 1 and res == 3:
    print("APROBADO")


elif ing >= 3500000 and año >= 5:
    print("APROBADO")


elif res == 4 and est == 2 and hij >= 2:
    print("APROBADO")

else:
    print("RECHAZADO")
