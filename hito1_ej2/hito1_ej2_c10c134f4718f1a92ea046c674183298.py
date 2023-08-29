#Contestador de celular
N=str(input("Ingrese el numero telefonico:"))[0:8]
H=int(input("Ingrese la hora:"))
N[5:8]
N[0:3]
"""if N>[0,1,2,3,4,5,6,7]:
    print("numero invalido")"""
#ESTE IF SIRVE PARA VERIFICAR QUE EL USUARIO INGRESO UNA HORA EXISTENTE
if H>23:
    print("esta hora no existe")
# ESTE IF SIRVE PARA VERIFICAR SI LA LLAMADA SERA CONTESTADA
# O SI NO LO SERA

##CONDICION 1
if H >=0 and H<=7:
    print("Contestar")
    
##CONDICION 2
    #HORA ENTRE 7 Y 14
    #LOS ULTIMOS NUMEROS IGUAL A 909
if H>7 and H<14 and N[5:8]=='909':
    print("contestar")

    #HORA ENTRE 7 Y 14
    #LOS ULTIMOS NUMEROS DIFERENTE DE 909 
elif H>7 and H<14 and N[5:8]!='909':
        print("No contestar")
##CONDICION 3
    #HORA ENTRE 17 Y 19
    #PRIMEROS TRES NUMEROS IGUAL A 877
if H>=17 and H<=19 and N[0:3]=='877':
    print("no contestar")

    #HORA ENTRE 17 Y 19
elif H>=17 and H<=19:
    print("contestar")

if H>19:
    print("No contestar")