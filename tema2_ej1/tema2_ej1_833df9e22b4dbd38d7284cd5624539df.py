def area_triangulo(base,altura):
        area_total=round(((base*altura)/2),2)
        return(area_total)
        
def area_rectangulo(base,altura):
        area_total=round((base*altura),2)
        return(area_total)
        
def area_rombo(diagonal1,diagonal2):
        area_total=round(((diagonal1*diagonal2)/2),2)
        return(area_total)
        
def area_circulo(radio):
        pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659
        area_total=(pi*(radio**2))
        return(area_total)