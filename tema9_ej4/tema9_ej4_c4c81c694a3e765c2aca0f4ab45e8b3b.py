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

        # determino si la longitud de la cadena es la requerida

        if (8 <= len(password) <= 16):

            # Análisis de cada caracter de la cadena

            for letra in password: # para cada letra de la cadena password

                # si el caracter guardado en letra es alfabético

                if letra.isalpha():

                    tiene_letra = True

                    c = letra.upper() # convierte a mayúsculas

                    if (c == letra): # el caracter es una mayúscula

                        tiene_mayuscula = True

                # si el caracter guardado en letra es numérico

                if letra.isdigit():

                    tiene_num = True

                # si el caracter es un caracter especial

                if (not(letra.isalpha()) and not(letra.isdigit())):

                    tiene_car_esp = True

            # decidir si la cadena password cumple con todos los criterios

            if tiene_letra and tiene_num and (tiene_mayuscula or tiene_car_esp):

                self.password = password

                return True

            else:

                return False

        else: # no cumple con la longitud requerida

            return False

        

    def login(self,password):

        if (self.password == password):

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