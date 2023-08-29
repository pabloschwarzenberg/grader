class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        valido=False
        letras="abcdefhijklmnopqrstuvwxyz"
        numeros="1234567890"
        caracteres="_/#%!&/()-:;$"
        if 16>=len(password) and len(password)>=8:
          for i in range(len(password)):
            for j in range(len(password)):
              for k in range(len(password)):
                if password[i] in letras and password[j] in numeros and (password[k] in caracteres or password[k] in letras.upper()):
                  self.password=password
                  valido=True
        else:
          return valido
        return valido
        pass

    def login(self,password):
      if password==self.password:
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
           