#Contestador de celular
n=int(input("Ingrese número de teléfono: "))
h=int(input("Ingrese hora de la llamada: "))
m=n%1000
if 0<=h<=7:
    print("Contestar")
elif 7<h<14 and m==909:
    print("Contestar")
elif 14<=h<17:
    print("No Contestar")
elif 17<=h<=19 and n<87700000 and 87799999<n:
    print("Contestar")
elif 19<h<23:
    print("No Contestar")
else:
    print("No Contestar")