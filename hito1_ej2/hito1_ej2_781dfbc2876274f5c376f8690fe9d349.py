#Contestador de celular
num_tel=str(input("Ingrese numero telefonico:"))
h=int(input("Ingrese hora de llamada:"))

num_fin = num_tel[5:8]
num_ini = num_tel[0:3]

if h>19 and h<=23:
    print("NO CONTESTAR")
elif h>0 and h<7:
    print("CONTESTAR")
else:
     if h>7 and h<14 and str(num_fin) == "909":
         print("CONTESTAR")
     elif h>7 and h<14 and str(num_fin)!= "909":
         print("NO CONTESTAR")
     else:
         if h>17 and h<19 and str(num_ini)== "877":
             print("NO CONTESTAR")
         elif h>17 and h<19 and str(num_ini) !="877":
             print("CONTESTAR")