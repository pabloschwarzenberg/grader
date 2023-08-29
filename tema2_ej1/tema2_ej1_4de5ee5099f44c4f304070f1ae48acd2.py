print("defina que area desea calcular:")
print("1.rectangulo  2.triangulo  3.rombo  4.circulo  5.salir")
dato=0
while dato==0:
    opcion=int(input("ingrese la opcion que desea:"))
    if opcion==1:
        print("DESEA CALCULAR EL AREA DE UN RECTANGULO")
        base_rec=int(input("ingrese su base:"))
        altura_rec=int(input("ingrese su altura:"))
        area_rec=base_rec*altura_rec
        print("El area del rectangulo es:",area_rec)
    if opcion==2:
        print("DESEA CALCULAR EL AREA DE UN TRIANGULO")
        base_tri=int(input("ingrese la base:"))
        altura_tri=int(input("ingrese la altura:"))
        area_tri=base_tri*altura_tri/2
        print("El area del triangulo es:",area_tri)
    if opcion==3:
        print("DESEA CALCULAR EL AREA DE UN ROMBO")
        diagonal_mayor=int(input("ingrese el valor de su primer diagonal:"))
        diagonal_menor=int(input("ingrese el valor de su segundo diagonal:"))
        area_rom=diagonal_mayor*diagonal_menor/2
        print("El area del rombo es:",area_rom)
    if opcion==4:
        print("DESEA CALCULAR EL AREA DE UN CIRCULO")
        pi=3.14
        radio=int(input("ingrese el radio del circulo:"))
        area_cir=pi*radio**2
        print("El area del circulo es:",area_cir)
    if opcion==5:
        print("BUENA SUERTE")
        dato=1