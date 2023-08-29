class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password = ""

    def cambiar_password(self,password):
        Intento = password
        letras = 'qwertyuiopasdfghjklñzxcvbnm'
        numeros = ['1','2','3','4','5','6','7','8','9','0']
        list(letras)
        intento = list(Intento)
        n = 0 # numbers
        l = 0 # letters
        e = 0 # especiales
        c = 0
        if len(intento) <= 16 and len(intento) >= 8:
          i = 0
          while i < len(intento):
            if isinstance(intento[i], str):
              if intento[i] in numeros:
                n += 1
                i += 1
              elif intento[i] not in letras:
                e += 1
                i += 1
              else:
                if intento[i].upper() == intento[i]:
                  l += 1
                  c += 1
                  i += 1
                else:
                  l += 1
                  i += 1
        else:
          return False
        if n != 0 and l != 0:
          if c != 0 and e != 0:
            return False
          elif c == 0 and e != 0:
            self.password = intento
            return True
          elif c != 0 and e == 0:
            self.password = intento
            return True
          else:
            return False
        else:
          return False

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
           