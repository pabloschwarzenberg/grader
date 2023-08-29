def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area
    pass

def area_rectangulo(base,altura):
    area = base * altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area
    pass

def area_circulo(radio):
    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
    area = pi * radio ** 2
    return area
    pass

if __name__ == "__main__":
    while(True):
        r = int(input('\n      MENU      \n   1. Area triangulo \n   2. Area rectangulo \n \
  3. Area rombo \n   4. Area circulo \n   5. Salir \n   Opcion(1,2,3,4,5):' ))
        if r == 1:
            print('\n')
            base = eval(input('Ingrese valor de la base:' ))
            altura = eval(input('Ingrese valor de la altura:' ))
            print('Area del triangulo:', area_triangulo(base,altura))
        elif r == 2:
            print('\n')
            base = eval(input('Ingrese valor de la base:' ))
            altura = eval(input('Ingrese valor de la altura:' ))
            print('Area del rectangulo:', area_rectangulo(base,altura))
        elif r == 3:
            print('\n')
            diagonal1 = eval(input('Ingrese valor primera diagonal:' ))
            diagonal2 = eval(input('Ingrese valor segunda diagonal:' ))
            print('Area del rombo: ', area_rombo(diagonal1,diagonal2))
        elif r == 4:
            print('\n')
            radio = eval(input('Ingrese radio:' ))
            print('Area del circulo: ', area_circulo(radio))
        elif r == 5:
            print('\n   Adios')
            break
    pass
           