class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password) < 8 or len(password) > 16:
          return False
        else:
          letras = 0
          numeros = 0
          simbolos = 0
          for i in password:
            if i.isalpha():
                letras += 1
            elif i.isdigit():
                numeros += 1
            else:
                simbolos += 1
          if letras == 0 or numeros == 0:
            return False
          elif not any(c.isupper() for c in password) and simbolos == 0:
            return False
          else:
            self.clave = password
            return True
        pass

    def login(self,password):
      if self.clave == password:
        return True
      else:
        return False
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           