class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      cNumeros = set(c for c in '0123456789')
      cMayus = set(c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      cEspecial = set(c for c in '~!@#$%^&*()_+')
      cAlphaEspecial = set(c for c in 'abcdefghijklmnopqrstuvwxyz0123456789')
      noLargo = False
      noMayus = False
      noEspecial = False
      noNumeros = False
      noAlphaEspecial = False
      if(len(password) < 8):
        noLargo = False
      if(len(password) > 16):
        noLargo = False      
      if any(passChar not in cMayus for passChar in password):
        noMayus = True
      if any(passChar not in cEspecial for passChar in password):
        noEspecial = True
      if any(passChar not in cNumeros for passChar in password):
        noNumeros = True
      if any(passChar not in cAlphaEspecial for passChar in password):
        noAlphaEspecial = True
      if ((noMayus == True and noEspecial == True) or noNumeros == True or noAlphaEspecial == True or noLargo == True):
        return False
      else:
        return True
      

    def login(self,password):
        if self.password == password:
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
           