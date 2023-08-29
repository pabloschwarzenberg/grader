#Contestador de celular
nTelefono = (input("Ingrese numero de telefonon de 8 cifras: "))
hora = int(input("Ingrese la hora de llamada: "))
lista= list(nTelefono)
lista13= lista[:2]
lista58= lista[5:]
acepta= ["9", "0", "9"]
noa = ["8", "0", "7"]

if 7>=hora>=0:
    print("CONTESTAR")
elif 14>=hora>7:
        if lista58.sort() == acepta.sort():
            print ("CONTESTAR") 
        else :
            print ("NO CONTESTAR")
elif 17>hora>14: 
        print("NO CONTESTAR")
elif 19>=hora>=17:
        if lista13.sort() == noa.sort():
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
elif 24>=hora>19:
        print("NO CONTESTAR")
