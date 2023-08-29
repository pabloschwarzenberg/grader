#Aprobación de créditos
print ("Para pedir un crédito debe ingresar los siguientes datos:")
ingreso = float(input("Su ingreso en pesos: "))
año = int(input("Su año de nacimiento: "))
num_hijos = int(input("Su número de hiijos: "))
años_ban = int(input("Años que lleva en el banco: "))
estado = input("Estado civil con S si es soltero y C si es casado: ")
s = estado
soltero = s
c = estado
casado = c
años = (2020 - año)
vive = input("Si vive en ciudad escriba U y si vive en campo escriba R: ")
u = vive
urbano = u
r = vive
campo = r
###########################################################################

if años_ban >= 10:
    if num_hijos >= 2:
        print("APROBADO")
    else:
        print("RECHAZADO")
#####################################################

if estado == c:
    if num_hijos >= 3:
        if  45 >= años <= 55:
            print ("APROBADO")
    else:
        print ("RECHAZADO")
###########################################################
if ingreso >= 25000000:
    if estado == s:
        if vive == u:
            print ("APROBADO")
    else:
        print ("RECHAZADO")
###############################################################
if ingreso >= 3500000:
    if años_ban >= 5:
        print ("APROBADO")
    else:
        print("RECHAZADO")
#######################################################
if vive == r:
    if estado == c:
        if num_hijos < 2:
            print ("APROBADO")
    else:
        print ("RECHAZADO")
              