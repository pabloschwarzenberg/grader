class Vector:
          def __init__(self, _x, _y):
                    self.x = _x
                    self.y = _y

          def imprimir(self):
                    print("El valor de X es: " + str(self.x))
                    print("El valor de Y es: " + str(self.y))

          def __str__(self):
                    return "(" + str(self.x) + "#,#" + str(self.y) + ")"

          def son_iguales(self, c2):
                    if self.x == c2.x and self.y == c2.y:
                              return True
                    return False

          def suma_vector(self, c2):
                    a = self.x + c2.x
                    b = self.y + c2.y
                    return Vector(a,b)

nc1 = Vector(3,8)
nc2 = Vector(7,14)
print("Método Imprimir para nc1 nc2")
print("Para nc1")
r=nc1.imprimir()
print("Para nc2")
r=nc2.imprimir()
print("\nImprimir nc1 nc2 con método __str__ ")
print("Para nc1")
print(nc1)
print("Para nc2")
print(nc2)
print("\nMétodo son_iguales")
r = nc1.son_iguales(nc2)
print(r)
print("\nMétodo suma_vector")
r = nc1.suma_vector(nc2)
print(r)