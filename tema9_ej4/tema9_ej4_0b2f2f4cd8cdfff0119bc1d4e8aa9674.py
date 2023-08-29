class Usuario:
	def __init__(self, nombre, email):
		self.nombre=nombre
		self.email=email
		self.clave=""

	def cambiar_password(self, password):
		if len(password)<8 or len(password)>16:
			return False

		mayusminus=False
		digitos=False
		especial=False

		for cara in password:
			if cara.isalpha() and cara.isupper():
				mayusminus=True
			elif cara.isdigit():
				digitos=True
			elif not cara.isalnum():
				especial=True

		if (mayusminus or especial) and digitos:
			self.clave=password
			return True
		else:
			return False

	def login(self, password):
		return self.clave==password

if __name__ == "__main__":

	usuario=Usuario("pablo","phschwarzenberg@uc.cl")
	print(usuario.cambiar_password("clave"))
	print(usuario.cambiar_password("clavesecreta1_"))
	print(usuario.cambiar_password("clavesecreta"))
	print(usuario.cambiar_password("clasesecreta1"))
	print(usuario.cambiar_password("claveSecreta1"))
	print(usuario.login("clavesecreta1_"))
	print(usuario.login("claveSecreta1"))
           