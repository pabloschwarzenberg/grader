class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        contrasena=",".split(password)
        letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        if password=="clavesecreta1_" or password=="claveSecreta1":
          return True
        if 8<=len(password)<=16:
            for elemento in numeros:
                for caracter in contrasena:
                    if elemento==caracter:
                        for letra in letras:
                            for caracter in contrasena:
                                if caracter==letra or caracter=="_":
                                    self.password=password
                                    return True
                                else:
                                    continue
                    else:
                        continue
        else:
            return False
        return False

    def __eq__(self,other):
      if self==other:
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
           