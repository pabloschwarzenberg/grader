#aprobacion de creditos

ingreso=int(input("¿Cuál es tu ingreso en pesos?"))

nacimiento=int(input("¿Cuál es tu año de nacimiento?"))

hijos=int(input("¿Cuántos hijos tienes?"))

pertenencia=int(input("¿Cuántos años de pertenencia llevas en el banco?"))

estado=input("¿Cuál es tu estado civil?")

c="casado"

s="soltero"

vive=input("¿Vives en sector urbano o rural?")

u="urbano"

r="rural"

if(pertenencia>10 and hijos>=2):

 print("aprobado")

elif(estado==c and hijos>3 and nacimiento>1966 or nacimiento<1976):

 print("aprobado")

elif(ingreso>2500000 and estado==s and vive==u):

 print("aprobado")

elif(ingreso>3500000 and pertenencia>5):

 print("aprobado")

elif(vive==r and estado==c and hijos<2):

 print("aprobado")

else:

 print("rechazado")

