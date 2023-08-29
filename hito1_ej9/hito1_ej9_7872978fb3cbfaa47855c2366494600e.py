#Sistema de Ecuaciones
def sis_ecu(x1,y1,r1,x2,y2,r2):

    deter = ((x1 * y2) - (y1*x2))

    if deter != 0 :

        x =  ((r1* y2)-(y1*r2))/deter
        y = ((x1*r2)-(r1*x2))/deter

        return x,y

    else:

        return None




x1= int(input("numero x1: "))
y1= int(input("numero y1: "))
r1= int(input("numero r1: "))
x2= int(input("numero x2: "))
y2= int(input("numero y2: "))
r2= int(input("numero r2: "))



lol = sis_ecu(x1,y1,r1,x2,y2,r2)

res_x = "x="+str(lol[0])
res_y = "y="+str(lol[1])


print(res_x)
print(res_y)
