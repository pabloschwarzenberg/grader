class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        lon=False
        alfa=False
        num=False
        especial=not password.isalnum()
        mayus=False
        for i in password:
        	if i.isalpha():
        		alfa=True
        	if i.isdigit():
        		num=True
        	if i.isupper():
        		mayus=True
        if len(password)<=16 and len(password)>=8:
        	lon=True
        if lon and alfa and num and (especial or mayus):
        	self.password=password
        	return True
        else:
        	return False





    def login(self,password):
        if password==self.password:
        	return True
        else:
        	return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           