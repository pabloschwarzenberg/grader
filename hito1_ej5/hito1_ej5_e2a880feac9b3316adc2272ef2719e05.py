#Cálculo del dígito verificador de un rut
rutsindigito = int(input("ingrese rut sin DV: "))

strnum = str (rutsindigito)[::-1]
print (strnum)

uno = int(strnum[0])*2
dos = int(strnum[1])*3
tres = int(strnum[2])*4
cua = int(strnum[3])*5
cin = int(strnum[4])*6
sei = int(strnum[5])*7
sie = int(strnum[6])*2
if (len(strnum)==8):
    och = int(strnum[7])*3
else:
    och = 0
suma = uno + dos + tres + cua + cin +  sei + sie + och
resto = suma %11
dv = 11 - resto

if (dv == 10):
    dv = "k"
if (dv == 11):
    dv = 0
print ("dv =",dv)
