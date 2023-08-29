#Contestador de celular
n=input("Ingrese numero telefonico: ")
h=int(input("Ingrese hora de llamada: "))
if 0<h<7:
    print("CONTESTAR")
elif 7<=h<14 and n[5:8]=="909":
    print("CONTESTAR")
elif 7<=h<14:
    print("NO CONTESTAR")
elif 17<h<19 and n[0:3]=="877":
    print("NO CONTESTAR")
elif 17<h<19:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")