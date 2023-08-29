#Contestador de celular
num = int(input("ingrese un numero telefonico ")) 
h1 = int(input("ingrese hora "))

x = [num]
if h1 >= 20:
    print("NO CONTESTAR")
elif (h1 >= 0 and h1 <= 7):
    print ("CONTESTAR")
elif h1 < 14: 
    print ("CONTESTAR")
elif h1 >= 17 and h1 <= 19:
    print ("NO CONTESTAR")

elif x[5] == 9 and x[6] == 0 and x[7] == 9:
    print ("CONTESTAR")
