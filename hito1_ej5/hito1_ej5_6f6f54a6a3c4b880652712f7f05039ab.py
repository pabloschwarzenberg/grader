#Cálculo del dígito verificador de un rut
RUT = input("Ingresar rut sin puntos: ")

if(len(RUT) == 8):
    
    n1 = int(int(RUT[7]) * 2)
    n2 = int(int(RUT[6]) * 3)
    n3 = int(int(RUT[5]) * 4)
    n4 = int(int(RUT[4]) * 5)
    n5 = int(int(RUT[3]) * 6)
    n6 = int(int(RUT[2]) * 7)
    n7 = int(int(RUT[1]) * 2)
    n8 = int(int(RUT[0]) * 3)
    
    tot = n1+n2+n3+n4+n5+n6+n7+n8

if(len(RUT) == 7):

    n1 = int(int(RUT[6]) * 2)
    n2 = int(int(RUT[5]) * 3)
    n3 = int(int(RUT[4]) * 4)
    n4 = int(int(RUT[3]) * 5)
    n5 = int(int(RUT[2]) * 6)
    n6 = int(int(RUT[1]) * 7)
    n7 = int(int(RUT[0]) * 2)

    tot = n1 + n2 + n3 + n4 + n5 + n6 + n7



mod = int(tot/11)

er = tot-(11*mod)

res = 11-er
if(res == 10):
    res = "k"
    print("dv=",res)
elif(res == 11):
    res = "0"
    print("dv=",res)
else:
    print("dv=",res)