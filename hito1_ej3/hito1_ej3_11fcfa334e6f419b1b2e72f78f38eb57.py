#Aprobación de créditos
 ingreso = int(input("ingrese su ingreso: "))
fecha = int(input("ingrese su año de nacimiento: "))
while not (fecha >= 1900 and fecha <= 2020):
    fecha = input("error... ingrese año de nacimiento: ")
    
numh = int(input("ingrese numero de hijos: "))
añosbanco = int(input("ingrese numero de años en el banco: "))

ecivil = input("ingrese estado civil: soltero = s o casado = c")
while not(ecivil == "s" or ecivil == "c" ):
    ecivil = input("error... ingrese estado civil: soltero = s y casado = c")
    
vive = input("ingrese donde vive: rural = r ó urbano = u")
while not(vive == "r" or vive == "u"):
    vive = input("error... ingrese donde vive: ")
    
edad = 2020 - fecha

if(añosbanco>10 and numh == 2 or numh == 3):
    print("aprobado")

elif(ecivil == "c" and numh > 3 and edad >= 45 and edad <= 55):
    print("aprobado")

elif(ingreso>2500000 and ecivil == "s" and vive == "u"):
    print("aprobado")

elif(ingreso>3500000 and añosbanco>5):
    print("aprobado")

elif(vive == "r" and ecivil == "c" and numh<2):
    print("aprobado")

else:
    print("rechazado")     