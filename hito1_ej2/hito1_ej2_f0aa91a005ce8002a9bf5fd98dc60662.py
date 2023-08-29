#Contestador de celular
numero=[]
numero.append(input(" "))
hora=input("la hora: ")
hora=int(hora)
if 0<=hora<=7:
 print("CONTESTAR")
elif 8<=hora<=14:
 print("CONTESTAR")
elif 17<=hora<=19 and numero[0]==8 and numero[1]==7 and numero[2]==7:
 print("NO CONTESTAR")
elif 17<=hora<=19:
 print("NO CONTESTAR")
else:
 print("NO CONTESTAR")
