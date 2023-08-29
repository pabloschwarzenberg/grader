class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        tiene_letra = False
        tiene_num = False
        tiene_mayuscula = False
        tiene_car_esp = False
        if (8 <= len(password) <= 16):
            for l in password:
                if l.isalpha():
                    tiene_letra = True
                if l.isdigit(): 
                    tiene_num = True
                if (65 <= ord(l) <= 90):
                    tiene_mayuscula = True
                if (33 <= ord(l) <= 47) or (58 <= ord(l) <= 64) or (91 <= ord(l) <= 96) or (123 <= ord(l) <= 126):
                    tiene_car_esp = True
            if tiene_letra and tiene_num and (tiene_mayuscula or tiene_car_esp):
                self.password = password
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
    print(usuario.cambiarpassword("clavesecreta1"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiarpassword("claveSecreta1"))
    print(usuario.login("clavesecreta1"))
    print(usuario.login("claveSecreta1"))
           