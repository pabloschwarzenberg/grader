N1 = int(input("Ingrese primer Número: "))
N2 = int(input("Ingrese segundo Número: "))
N3 = int(input("Ingrese tercer Número: "))
sp = ","
if N1 <= N2 and N1 <= N3:
   if N2 <= N3:
      print(N1,sp,N2,sp,N3)
   else:
       print(N1,sp,N3,sp,N2)
if N2 <= N1 and N2 <= N3:
    if N1 <= N3:
        print(N2,sp,N1,sp,N3)
    else:
        print(N2,sp,N3,sp,N1)
if N3 <= N1 and N3 <= N2:
    if N1 <= N2:
        print(N3,sp,N1,sp,N2)
    else:
        print(N3,sp,N2,sp,N1)