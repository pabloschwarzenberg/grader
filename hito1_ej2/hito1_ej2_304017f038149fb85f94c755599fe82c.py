#Contestador de celular     
num_tel= int(input("ingrese un número telefónico de 8 cifras"))
h_llamada= int(input("ingrese la hora de llamada"))
if 0 <= h_llamada <= 7 and num_tel == num_tel:
    print("CONTESTAR")
elif h_llamada < 14 and num_tel == num_tel:
    print("CONTESTAR")
elif num_tel[4] == 9 + num_tel[5] == 0 + num_tel[6] == 9:
    print("NO CONTESTAR")
elif 17<= h_llamada<= 19:
    print("CONTESTAR")
elif num_tel[0] == 8 + num_tel[1] == 7 + num_tel[2] == 7:
    print("NO CONTESTAR")
elif h_llamada >=19 and num_tel == num_tel:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")