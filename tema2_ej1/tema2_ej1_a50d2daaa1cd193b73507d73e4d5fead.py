def area_triangulo(base,altura):
    res=(float(base)*float(altura))/2
    return res
    pass

def area_rectangulo(base,altura):
    res=float(base)*float(altura)
    return res
    pass

def area_rombo(diagonal1,diagonal2):
    res=(float(diagonal1)*float(diagonal2))/2
    return res
    pass

def area_circulo(radio):
    pi=float(3.141592653589793)
    # CON PI probé de todo, estaba que ponía una libreria de math que nisiquiera cacho como usar
    # alfin me lo puso bien porque le faltaban como 10 mas al lado del punto
    # de hecho ni el pi de google sirvió, lo tube que buscar en una wea de física cuántica
    # https://www.stechies.com/pi-python/
    res=((float(radio)**2)*pi)
    return res
    pass

if __name__ == "__main__":
    pass