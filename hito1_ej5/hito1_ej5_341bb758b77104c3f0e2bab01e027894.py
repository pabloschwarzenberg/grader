#Cálculo del dígito verificador de un rut
if __name__ == "__main__":
    print("Ingrese su RUT sin DV:")
n= int(input())
ret1 = n % 10
ret2 = n % 100
ret3 = n % 1000
ret4 = n % 10000
ret5 = n % 100000
ret6 = n % 1000000
ret7 = n % 10000000
ret8 = n % 100000000
P_1 = ret1 % 10
P_2 = (ret2-(ret2 % 10))//10
P_3 = (ret3-(ret3 % 100))//100
P_4 = (ret4-(ret4 % 1000))//1000
P_5 = (ret5-(ret5 % 10000))//10000
P_6 = (ret6-(ret6 % 100000))//100000
P_7 = (ret7-(ret7 % 1000000))//1000000
P_8 = (ret8-(ret8 % 10000000))//10000000
R_1 = 2
R_2 = 3
R_3 = 4
R_4 = 5
R_5 = 6
R_6 = 7
R_7 = 2
R_8 = 3
M1 = P_1 * R_1
M2 = P_2 * R_2
M3 = P_3 * R_3
M4 = P_4 * R_4
M5 = P_5 * R_5
M6 = P_6 * R_6
M7 = P_7 * R_7
M8 = P_8 * R_8
MT = (M1+M2+M3+M4+M5+M6+M7+M8)
MMT= (MT//11)
MNT= MT-(11*MMT)
CV = 11-MNT
if CV == 11:
    print("dv=0")
elif CV == 10:
    print("dv=K")
else:
    print("dv=", CV)      