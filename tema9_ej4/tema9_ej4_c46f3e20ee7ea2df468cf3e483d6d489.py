class Usuario:
    def init(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        char = False
        let = False
        if len(password) >= 8 and len(password) <=16 :
          for letra in password :
            if letra.isupper() or letra in special:
              char = True
            elif letra.isnumeric():
              let = True
          if char and let:
            self.password = str(password)
            return True
        return False
    def login(self,password):
        if password == self.password:
          return True
        return False

if name == "main":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiarpassword("clavesecreta1"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiarpassword("claveSecreta1"))
    print(usuario.login("clavesecreta1"))
    print(usuario.login("claveSecreta1"))