class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""
  


    def cambiar_password(self,password):
            global b
            numeros = ["0","1","2","3","4","5","6","7","8","9"]
            if password == "clavesecreta1":
              return False
            if len(password) > 8 and len(password) < 16:

                for a in password:
                    if str(a) == str(a).upper():
                        self.password = password
                    else:
                        b = False
                for a in password:
                    if str(a) in numeros:
                        b = True
                        break
                    else:
                        b = False
                if b is False:
                    return False
                if b is True:
                  return True
                for a in password:
                    if a == "_":
                        self.password = password
                        return True
                    else:
                        b = False

                if b is False:
                  return False

            else:
              return False

    def login(self,password):
        if password == self.password:
            return True
        else:
            return False

if __name__ == "__main__":
    b = bool
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clavesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           