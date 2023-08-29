#Contestador de celular
numero = int(input("ingrese numero telefonico:"))
hora = int (input("ingrese hora de la llamada:"))

n = numero
h = hora

#numero fin 909


o = str(n)
p = o[5:8]
q = int(p)

#numero inicia 877

j = str(n)
k = j[0:3]
l = int(k)

#casos especiales

if h in range (8,14) and q == 909:

    print ("contestar")
    
elif h in range (17,20) and l == 877:

    print ("no contestar")

#por hora


elif h in range (0, 8):

    print ("contestar")

elif h in range (8,14):

    print ("no contesta")

elif h in range (14,17):

    print ("no contesta")
    
elif h in range (17,20):

    print("contestar")

elif h in range (20,24):

    print("no contestar")
