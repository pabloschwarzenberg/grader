#Contestador de celular
N=input("ingrese numero de telefono:")
H=int(input("ingrese hora de la llamada:"))
n1=N[0]
n2=N[1]
n3=N[2]
n4=N[3]
n5=N[4]
n6=N[5]
n7=N[6]
n8=N[7]

if H>0 and H<7:
    print("CONTESTAR")

elif H<14:
    if n6=="9" and n7=="0" and n8=="9":
        print("CONTESTAR")
    else:
         print("NO CONTESTAR")

elif H>17 and H<19:
    if n1=="8" and n2=="7" and n3=="7":
        print(" NO CONTESTAR")
    else:
         print("CONTESTAR")

elif H>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
    
    

      