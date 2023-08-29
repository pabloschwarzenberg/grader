i = int(input("cuantos ingresos tiene en el banco?: $"))
a = int(input("\nen que año nacio?:"))
h = int(input("\ncuantos hijos tiene?:"))
b = int(input("\ncuantos años lleva perteneciendo al banco?:"))
e = input("\nes casado (C) o soleto (S)?:")
c = input("\nvive en campo (U) o ciudad (R)?:")
ñ = 2020 - a
    

if (b > 10 and h >=2 ):
    print ("\nAPROBADO")

elif (e == "C" and h >= 3 and 45 <= ñ <= 55):
    print ("\nAPROBADO")

elif (i > 2500000 and e == "S" and  c == "U"):
    print ("\nAPROBADO")

elif (i > 3500000 and b > 5):
    print ("\nAPROBADO")

elif (c == "R" and e == "C" and h < 2):
    print ("\nAPROBADO")

else:
    print ("\nRECHAZADO")
