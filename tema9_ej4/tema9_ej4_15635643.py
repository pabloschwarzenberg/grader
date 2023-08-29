class Usuario:
    def __init__(self,nombre,mail):
        self.nombre=nombre
        self.email=mail
        self.password=""
    def cambiar_password(self,password):
        if len(password) in range(8,16):
            nums=False
            may=False
            esp=False
            for car in password:
                try:
                    c=int(car)
                    nums=True
                except ValueError:
                    if type(car)==int:
                        nums=True
                    if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        may=True
                    elif car.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        esp=True
            if nums and (may or esp):
                self.password=password
                return True
            else:
                return False
        else:
            return False
    def login(self,passw):
        if passw==self.password:
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
           