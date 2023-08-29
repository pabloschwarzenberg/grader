class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        abc="qwertyuiopasdfghjklzxcvbnm"
        ABC=abc.upper()
        nums="1234567890"
        sym='|°"#$%&/()=.:,;-_'
        condicion1=False
        condicion2=False
        condicion3=False
        condicion4=False
        for minuscula in abc:
            if minuscula in password:
                condicion1=True
        for mayuscula in ABC:
            if mayuscula in password:
                condicion2=True
        for numero in nums:
            if numero in password:
                condicion3=True
        for simbolo in sym:
            if simbolo in password:
                condicion4=True
        condiciones=condicion1 and condicion3 and (condicion2 or condicion4)
        if 8<=len(password)<=16 and condiciones:
            self.password=password
        return condiciones
    def login(self,password):
        if password==self.password:
            return True
        else:
            return False

if __name__=="__main__":
    usuario=Usuario("Pablo Schwarzenberg","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))