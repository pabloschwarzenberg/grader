class Usuario:
	def __init__(self,nombre,email):
		self.nombre=nombre
		self.email=email
		self.password=""

	def cambiar_password(self,password):
		if (password.isdigit() or password.isalpha() or password.isalnum()):
			for i in password:
				if (str(i).isupper()):
					self.password = password
					return True
			return(False)
		else:
			self.password = password
			return(True)
      
	def login(self,password):
		if password == self.password:
			return(True)
		else:
			return(False)

if __name__ == "__main__":
	usuario=Usuario("pablo","phschwarzenberg@uc.cl")
	print(usuario.cambiar_password("clave"))
	print(usuario.cambiar_password("clavesecreta1_"))
	print(usuario.cambiar_password("clavesecreta"))
	print(usuario.cambiar_password("clasesecreta1"))
	print(usuario.cambiar_password("claveSecreta1"))
	print(usuario.login("clavesecreta1_"))
	print(usuario.login("claveSecreta1"))