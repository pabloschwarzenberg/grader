#Variables incognitas
vI = []
count = 1
for i in range(6):
    print("Ingrese variable",count,":")
    vI.append(int(input()))
#Primera operacion
#Ecuacion 1 = Ax + By = C
#Ecuacion 2 = Dx + Ey = F

y = (vI[5] - ( (vI[3] * vI[2]) / vI[0] )) / ( ( (-1 * vI[3] * vI[1]) / vI[0])+ vI[4])
x = (vI[2] - (vI[1] * y )) / vI[0]


print("[x=","{0:.1f}".format(x) +", y=","{0:.1f}".format(y),"]")