def area_triangulo(base,altura):
    art = (base+altura)/2
    return art

def area_rectangulo(base,altura):
    arc = base*altura
    return arc

def area_rombo(diagonal1,diagonal2):
    arm = diagonal1*diagonal2
    return arm
    
def area_circulo(radio):
    acir = 3.1416 * radio **2 
    return acir

op = "1"
while op!="5": 
    print("Calculadora geometrica")
    print("\t1. Area de triangulo\n\t2. Area de rectangulo\n\t3. Area de rombo\n\t4. Area de circulo\n\t5.Salir")
    op = input("\tOpcion?: ")

    if op=="1":
        bt=float(input("\tIngrese la base del traingulo: "))
        at=float(input("\tIngrese la altura del traingulo: "))
        area_trian = area_triangulo(bt,at)
        print("\tArea del triangulo: ",area_trian)
    elif op=="2":
        br=float(input("\tINgrese la base del rectangulo: "))
        ar=float(input("\tINgrese la altura del rectangulo: "))
        are_rec = area_rectangulo(br,ar)
        print("\tArea de rectangulo :",are_rec)
    elif op=="3":
        d1=float(input("\tIngrese diagonal 1: "))
        d2=float(input("\tIngrese diagonal 2: "))
        area_rom = area_rombo(d1,d2)
        print("\tArea del rombo: ",area_rom)
    elif op=="4":
        r =float(input("\tIngrese el radio del circulo: "))
        area_cir = area_circulo(r)
        print("\t Area del circulo: ",round(area_cir,2))
    elif op =="5":
        print("\t Programa terminado...")