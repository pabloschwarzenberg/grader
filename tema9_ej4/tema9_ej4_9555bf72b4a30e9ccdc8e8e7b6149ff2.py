class Usuario:
      def __init__(self,nombre,email):
        if isinstance(nombre,str)==True and isinstance(email,str)==True:
            self.nombre=nombre
            self.clave=""
            self.email=email

      def cambiar_password(self,password):
            if isinstance(password,str)==True:
                especial=False
                for c in password:
                    if c.lower()!=c or c.isalnum()==False:
                        especial=True
                if 7<len(password)<17 and especial==True:
                    self.clave=password
                    return True
            return False

      def login(self,password):
            if password==self.clave:
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