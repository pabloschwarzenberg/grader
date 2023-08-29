class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      if len(password) < 8 or len(password) > 16:
        return False
      mayusculas = 0
      minusculas = 0
      letras = 0
      numeros = 0
      especiales = 0
      for letra in password:
        if letra.isalpha():
          letras += 1
          if letra == letra.lower():
            minusculas += 1
          else:
            mayusculas += 1
        elif letra.isdigit():
          numeros += 1
        else:
          especiales += 1
      if (letras > 0 and numeros > 0) and (mayusculas > 0 or especiales > 0):
        self.password = password
        return True
        
      else:
        return False
      
      

    def login(self,password):
        if password == self.password:
          return True
        else:
          return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@unab.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           