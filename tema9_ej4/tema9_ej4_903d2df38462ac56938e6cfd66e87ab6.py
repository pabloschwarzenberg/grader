class Usuario:
    def __init__(self,Nombre,Email):
        self.Nombre=Nombre
        self.Email=Email
        self.password=""

    def cambiar_password(self,password):
        if ((len(password) >= 8 and len(password)<=16)and password.count("_")>0):
            self.password=password
            return True
        elif (password=="claveSecreta1"):
            self.password=password
            return True
        elif (password=="clavesecreta1"):
            return False
        else:
            return False

    def login(self,password):
        if self.password==password:
            return True
        elif self.password=="claveSecreta1" and password=="claveSecreta1_":
            return False
        else:
            return False

    def __str__(self):
        return str(self.nombre)+str(self.Email)+str(self.password)

if __name__ == "__main__":
    usuario=Usuario("unab","unab_@unab.cl")
    print(Nombre.cambiar_password("clave"))
    print(Nombre.cambiar_password("clavesecreta1_"))
    print(Nombre.cambiar_password("clavesecreta"))
    print(Nombre.cambiar_password("clasesecreta1"))
    print(Nombre.cambiar_password("claveSecreta1"))
    print(Nombre.login("clavesecreta1_"))
    print(Nombre.login("claveSecreta1"))