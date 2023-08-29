import math
# Declaración de las funciones
def area_triangulo(base,altura):
    art = (base*altura)/2
    return art

def area_rectangulo(base,altura):
    arc = base*altura
    return arc
    
def area_rombo(diagonal1,diagonal2):
    arm = diagonal1*diagonal2
    return arm
   
def area_circulo(radio):
    acir = math.pi * radio**2
    return acir
   
# Programa principal
op = "1"
while op!="5":
    # Presentar un menu de opciones
    print("\n\tCalculadora Geométrica")
    print("\t1. Área de Triángulo\n\t2. Área de Rectángulo\n\t3. Área de Rombo\n\t4. Área de Círculo\n\t5. Salir")
    op = input("\tOpción?: ")
    # Invocación de las funciones
    if op=="1":
     if __name__ == "__main__":
        bt = float(input("\tIngrese base del triángulo: "))
        At = float(input("\tIngrese altura del triángulo: "))
        print("\tÁrea del triángulo: ",round(area_triangulo(bt,At),2))
    elif op=="2":
     if __name__ == "__main__": 
        br = float(input("\tIngrese base del rectángulo: "))
        ar = float(input("\tIngrese altura del rectángulo: "))
        print("\tÁrea del rectángulo: ",round(area_rectangulo(br,ar),2))
    elif op=="3": 
     if __name__ == "__main__": 
        d1 = float(input("\tIngrese diagonal 1: "))
        d2 = float(input("\tIngrese diagonal 2: "))
        print("\tÁrea del rombo: ",round(area_rombo(d1,d2),2))
    elif op=="4":
    if __name__ == "__main__": 
        r = float(input("\tIngrese radio del circulo: "))
        print("\tÁrea del círculo: ",round(area_circulo(r),2))
    elif op=="5":
       print("\tPrograma terminado...")
           