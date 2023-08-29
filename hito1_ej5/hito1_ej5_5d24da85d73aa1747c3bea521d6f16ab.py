#Cálculo del dígito verificador de un rut
n=str(input())
suma = 0
i=0
x= [ 2, 3, 4, 5, 6, 7]
y = 0
for i in range(1, len(n) + 1):
    suma += int(n[-i]) * x[y]
    #print(int(n[-i]), x[y])
    y += 1
    if y == 6:
        y -= 6
     
dv=(11-(suma%11))
if 1<dv<9:
    print("dv=",dv)
elif dv==10:
    print("dv=k")
elif dv==11:
    print("dv=0")

