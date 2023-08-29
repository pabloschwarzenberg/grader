#Conversión de Decimal a Binario
nmb=int(input("Ingresa un numero binario:"))
list = []

while nmb>0:
    rst=int(nmb%2)
    list.append(rst)
    nmb=(nmb-rst)/2
nmb_bin=""

print("Es: ",list[::-1])

for q in list[::-1]:
    nmb_bin= nmb_bin+str(q)

print("El resultado="+str(nmb_bin))      