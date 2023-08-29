class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=None
    def cambiar_password(self,password):
        letras="abcdefghijklmnopqrstuvwxyz"
        numeros="1234567890"
        criterios_aprobados=[]
        if len(password)>=8 and len(password)<=16:
            criterios_aprobados.append("criterio largo")
        for numero in numeros:
            if numero in password:
                if len(criterios_aprobados)==1:
                    criterios_aprobados.append("criterio numero")
        criterio_raro=[]           
        for x in password:
            if x in letras:
                criterio_raro.append(x)
            elif x in numeros:
                criterio_raro.append(x)
        if len(criterio_raro)!=len(password):
            criterios_aprobados.append("criterio raro")
        if len(criterios_aprobados)==3:
            self.password=password
            return True
        else:
            return False
    

    def login(self,password):
        if password==self.password:
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
           