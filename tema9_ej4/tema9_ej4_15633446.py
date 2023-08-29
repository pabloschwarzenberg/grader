class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        l=len(password)
        if (l<8):
            print("La contraseña debe tener más de 8 caracteres")
            return(False)
        elif(l>16):
            print("La contraseña no puede tener más de 16 caracteres")
            return(False)
        else:
            for i in range(l):
                 if isinstance(password[i],int)==True:
                     valor_numeros=1
            for j in range(l):
                 if isinstance (password[j],str)==True:
                     valor_letras=1
            for i in range(l):
                if isinstance(password[i],str)==False and isinstance(password[i],int)==False:
                    valor_especial=1
                if isinstance(password[i],upper):
                    valor_especial=1
            if valor_numeros!=1:
                print("Tu contraseña debe tener caracteres númericos")
                return(False)
            elif valor_letras!=1:
                print("Tu contraseña debe contener letras")
                return(False)
            elif valor_especial!=1:
                print("Tu contraseña debe contener al menos una mayuscula o algun caracterer especial")
                return(False)
            else:
                self.clave=password
                return(password,True)
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
           