#Sistema de Ecuaciones
primeraletra = float(input("Numero a:"))
segundaletra = float(input("Numero b:"))
terceraletra = float(input("Numero c:"))
cuartaletra = float(input("Numero d:"))
quintaletra = float(input("Numero e:"))
sextaletra = float(input("Numero f:"))


x = (terceraletra * quintaletra - segundaletra * sextaletra) // (primeraletra * quintaletra - segundaletra * cuartaletra)
y = (primeraletra * sextaletra - terceraletra * cuartaletra) // (primeraletra * quintaletra - segundaletra * cuartaletra)

print("x=" +str(x) + "y="+str(y))