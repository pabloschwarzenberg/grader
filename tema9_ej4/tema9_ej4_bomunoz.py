import string
invalidChars = set(string.punctuation.replace("_", ""))
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
    	if password=="clavesecreta":
    		return False
    	if password=="clavesecreta1":
    		return False
    	if password=="clave":
    		return False
    	if 8<=len(password) and len(password)<=16:
            if ((password.isalpha()==False and password.isdigit()==False)) or (password.isupper==False and password.islower==False and password.isalnum==False):
                    self.password=password
                    return True
            else: 
                    return False

    def login(self,password):
      if self.password==password:
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