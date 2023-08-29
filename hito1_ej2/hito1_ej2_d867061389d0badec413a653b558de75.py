#Contestador de celular
nro=int(input("Ingrese número de teléfono: "))
hro=int(input("Ingrese la hora: "))
if 0<=hro<=7 :
        print("Contestar")
elif hro<=14 and ((nro-909)%100)!=0:
        print("No contestar")
elif hro<=14 and (nro-909)%100==0:
        print("Contestar")
elif 17<=hro<=19 and nro//87700000!=1:
        print("Contestar")
elif 17<=hro<=19 and nro//87700000==1:
        print("No contestar")
else :
        print("No contestar")

