class Fraccion:
	def __init__(self, numerador, denominador):
		self.num = numerador
		self.den = denominador

	def __mul__(self, other):
		r = Fraccion(0, 0)
		r.num = self.num * other.num
		r.den = self.den * other.den
		return r

	def __repr__(self):
		entero = self.num // self.den
		if entero > 0:
			resto = self.num % self.den
			if resto > 0:
				return "{0} {1}/{2}".format(entero, resto, self.den)
			else:
				return "{0}".format(entero)
		else:
			return "{0}/{1}".format(self.num, self.den)

	def __add__(self, other):
		if isinstance(other, Fraccion):
			num = self.num * other.den + other.num * self.den
			den = self.den * other.den
			return Fraccion(num, den)
		else:
			print("La operacion de suma solo es valida entre objetos de la clase Fraccion")

	def __sub__(self, other):
		if isinstance(other, Fraccion):
			num = self.num * other.den - other.num * self.den
			den = self.den * other.den
			return Fraccion(num, den)
		else:
			print("La operacion de resta solo es valida entre objetos de la clase Fraccion")

	def __truediv__(self, other):
		if isinstance(other, Fraccion):
			num = self.num * other.den
			den = self.den * other.num
			return Fraccion(num, den)
		else:
			print("La operacion de division solo es valida entre objetos de la clase Fraccion")

	def a_numero(self):
		return self.num / self.den


if __name__=="__main__":
	f = input("Ingresa la primera fraccion [a/b]: ")
	f = f.split("/")
	f1 = Fraccion(int(f[0]), int(f[1]))
	f = input("Ingresa la segunda fraccion [c/d]: ")
	f = f.split("/")
	f2 = Fraccion(int(f[0]), int(f[1]))
	print("La suma es", f1 + f2)
	print("La resta es", f1 - f2)
	print("La multiplicacion es", f1 * f2)
	print("La divisiun es", f1 / f2)
         