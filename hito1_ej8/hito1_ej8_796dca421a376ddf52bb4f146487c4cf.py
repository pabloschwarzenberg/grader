x= input("ingrse un numero de hasta cuatro cifras:")
if len(x) == 4:
 print(x[-4], "M+", x[-3],"C+", x[-2], "D+", x[-1],"U")
if len(x) == 3:
 print(x[-3],"C+", x[-2], "D+", x[-1],"U")
if len(x) == 2:
 print(x[-2], "D+", x[-1],"U")
if len(x) == 1:
 print(x[-1],"U")