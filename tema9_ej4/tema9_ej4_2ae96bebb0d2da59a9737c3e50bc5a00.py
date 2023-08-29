class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        cont_abc = 0
        cont_n = 0
        cont_simbol = 0
        for letra in password:
          if letra.isalpha() == False and letra.isdigit() == True:
            cont_n += 1
          if letra.isalpha().isupper() == False and letra.isdigit() == False:
            cont_simbol += 1
          if letra.isalpha().isupper() == True and letra.isdigit() = False:
            cont_simbol += 1
          if letra.isalpha() == True:
            cont_abc += 1
          
        if (cont_abc != 0) and (cont_n != 0) and (cont_simbol != 0) and (len(password) >= 16) and (len(password) <= 8):
          self.password = password
          return True
            
    def login(self,password):
        if password == self.password:
          return True

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           