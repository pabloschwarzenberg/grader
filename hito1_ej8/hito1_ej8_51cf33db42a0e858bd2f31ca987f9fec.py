#Descomponer un número
num= int(input("ingrese numero de 4 dijitos: "))
if not num<1000 and num>9999:
    print("error")
else:
    M=num//1000
    C=num//100-M*10
    D=num//10-M*100-C*10
    U=num%10
    numn=str(num)
    if len(numn)==4:
        print(M,"M + ",C,"C + ",D,"D + ",U,"U")
    if len(numn)==3:
        print(C, "C + ", D, "D + ", U, "U")
    if len(numn)==2:
        print(D, "D + ", U, "U")
    if len(numn)==1:
        print(U, "U")