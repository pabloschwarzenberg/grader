#Cálculo del dígito verificador de un rut
rut = int(input("RUT: "))

list1 = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]

list2 =  [int(d) for d in str(rut)]
list2.reverse()

sum = 0
for i in range(0, len(list2)):
    sum = sum + list2[i]*list1[i]
#print(sum)

resto = sum%11

resta_resto = 11 - resto

dv = None
if resta_resto == 11:
    dv = 0
elif resta_resto == 10:
    dv = "K"
else:
    dv = resta_resto
    
print("dv=" + str(dv))