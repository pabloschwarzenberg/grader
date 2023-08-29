def area_triangulo(base,altura):
  A= (base*altura)/2
  return (A)
def area_rectangulo(base,altura):
  A=base*altura
  return(A)
def area_rombo(diagonal1,diagonal2):
  A= (diagonal1*diagonal2)/2
  return (A)
def area_circulo(radio):
  Pi=float(3.141592653589793)
  A=float(Pi*(radio**2))
  return(A)
if __name__ == "__main__":
    x=input("Ingrese la figura del area que desea calcular:")

    if x=="triangulo":
      base=float(input("Ingrese medida de la base:"))
      altura=float(input("Ingrese medida de la altura:"))
      print(area_triangulo(base,altura))
    if x=="rectangulo":
      base=float(input("Ingrese medida de la base:"))
      altura=float(input("Ingrese medida de la altura:"))
      print(area_rectangulo(base,altura))
    if x=="rombo":
      diagonal1=float(input("Ingrese medida de la primera diagonal:"))
      diagonal2=float(input("Ingrese medida de la segunda diagonal:"))
      print(area_rombo(diagonal1,diagonal2))
    if x=="circulo":
      radio=float(input("Ingrese medida del radio:"))
      print(area_circulo(radio))



           