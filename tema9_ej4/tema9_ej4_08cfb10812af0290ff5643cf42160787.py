class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        contador_numeros=0
        contador_letras=0
        contador_mayuscula=0
        contador_signos=0
        for i in password:
            if i.isdigit()==True:
                contador_numeros=contador_numeros+1
            if i.isalpha()==True:
                contador_letras=contador_letras+1
            if i.isupper()==True:
                contador_mayuscula=contador_mayuscula+1
            if i.isalpha()==False and i.isdigit()==False:
                contador_signos=contador_signos+1
        if 8<=len(password)<=16 and contador_numeros!=0 and contador_letras!=0 and (contador_mayuscula!=0 or contador_signos!=0):
            self.password=password
            return True
        else:
            return False

    def login(self,password):
        if password == self.password:
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