import math
def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
	return math.pi*radio**2
if __name__ == "__main__":
	x=input("Que operación desea realizar(1,2,3,4)? ")
	if x==1 or x==2:
		base=eval(input("Base?"))
		altura=eval(input("Altura"))
		if x==1:
			area_triangulo(base,altura)
		if x==2:
			area_rectangulo(base,altura)
	if x==3:
		diagonal1=eval(input("diagonal1"))
		diagonal2=eval(input("diagonal2"))
		area_rombo(diagonal1,diagonal2)
	if x==4:
		radio=eval(input("radio"))
		area_circulo(radio)