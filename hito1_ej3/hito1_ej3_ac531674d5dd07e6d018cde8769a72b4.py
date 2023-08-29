ingreso=int(input("cuál es el ingreso?"))
anon=int(input("Ingrese su año de nacimiento"))
edad=2021-anon
nhijo=int(input("Cúantos hijos tiene?"))
anosb=int(input("cuántos años ha pertenecido a este banco?"))
ecivil=str(input("cuál es su estado civil"))
ecivil=ecivil.lower()
letras=ecivil.find("s")
#soltero=letras0
letrac=ecivil.find("c")
#casado=letrac0
uor=str(input("Usted vive en espacio urbano o rural?"))
uor=uor.lower()
letrau=uor.find("u")
#ciudad=letrad0
letrar=uor.find("r")
#rural=letraa0

if anosb>=10 and nhijo>=2:
    print("APROBADO")
elif letrac==0 and nhijo>3 and 45<=edad<=55:
    print("APROBADO")
elif ingreso>2500000 and letras==0 and letrau==0:
    print("APROBADO")
elif ingreso>3500000 and anosb>5:
    print("APROBADO")
elif letrar==0 and letrac==0 and nhijo<2:
    print("APROBADO")
else:
    print("RECHAZADO")