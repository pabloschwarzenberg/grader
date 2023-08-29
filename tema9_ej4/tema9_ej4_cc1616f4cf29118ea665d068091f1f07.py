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
        # Determinar si la cadena tiene la longitud válida
        if (8 <= len(password) <= 16):
            # Analizar la cadena caracter a caracter
            for car in password:
                # Si el caracter es una letra
                if car.isalpha():
                    tiene_letra = True
                    # Determinar si la letra es una letra mayúscula
                    caraux = car.upper()
                    if caraux == car:
                        tiene_mayuscula = True
                # Si el caracter es un número
                if car.isdigit():
                    tiene_num = True
                # Si el caracter es un caracter especial
                if not(car.isalpha()) and not(car.isdigit()):
                    tiene_car_esp = True
            # Devolver True si la cadena cumple como clave y False de lo contrario
            if tiene_letra and tiene_num and (tiene_mayuscula or tiene_car_esp):
                self.password = password
                return True
            else:
                return False
        else: # la cadena no tiene una longitud válida
            return False

    def login(self,password):
        if self.password == password:
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
           