#Contestador de celular
      
numero= int(input("Ingrese numero de telefono: "))
hora= int(input("ingresar hora del llamado: "))
n=str(numero)
f=int(n[5]+n[6]+n[7])
j=int(n[0]+n[1]+n[2])

if 0<= hora <=7 or (f==909 and hora <= 14) or (j!=877 and 17<=hora<=19):

    print("CONTESTAR")

else:
    print("NO CONTESTAR")