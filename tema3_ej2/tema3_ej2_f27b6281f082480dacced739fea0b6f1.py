class Vector:

   def __init__(self, x, y, z):

       self.x = x

       self.y = y

       self.z = z

   

   def norma(self):

       return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

   

   def __add__(self, other):
   
       if isinstance(other, Vector):

           new_x = self.x + other.x

           new_y = self.y + other.y

           new_z = self.z + other.z

           return Vector(new_x, new_y, new_z)
           
       else:

           raise TypeError("Unsupported operand type. The operand must be a Vector.")

   

def suma_vectores(vector1, vector2):

   if isinstance(vector1, Vector) and isinstance(vector2, Vector):

       return vector1 + vector2

   else:

       raise TypeError("Unsupported operand types. The operands must be Vectors.")

 

# Ejemplo de uso

vector1 = Vector(1, 2, 3)

vector2 = Vector(4, 5, 6)

 

print("Norma del vector 1:", vector1.norma())

print("Norma del vector 2:", vector2.norma())

 

vector3 = suma_vectores(vector1, vector2)

print("Resultado de la suma:", vector3.x, vector3.y, vector3.z) 