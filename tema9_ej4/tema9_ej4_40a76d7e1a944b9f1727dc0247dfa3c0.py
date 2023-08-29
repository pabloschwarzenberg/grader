"""
Tiene un mínimo de 8 caracteres y un máximo de 16.
Contiene letras y números, y además contiene al menos una letra mayúscula o al menos un carácter especial 
(o sea un símbolo que no sea una letra, un #, por ejemplo)
Si la password del usuario cumple las regla, 
tu función debe actualizar el atributo password y retornar True. 
Si la password no cumple alguna de las reglas, tu función debe retornar False y no cambiar la clase.
"""

import string

class Usuario:
    
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,_password):
        largo=len(_password)

        mayuscula=string.ascii_uppercase
        numeros=string.digits
        caracter=string.punctuation
        minuscula=string.ascii_lowercase

        contador_min=0
        contador_may=0
        contador_num=0
        contador_car=0

        for i in _password:
            # if de los contadores
            if i in minuscula:
                contador_min=contador_min+1
            if i in numeros:
                contador_num=contador_num+1
            if i in mayuscula:
                contador_may=contador_may+1
            if i in caracter:
                contador_car=contador_car+1

        # VALIDACION
        if contador_min>0 and contador_num>0 and (contador_car>0 or contador_may>0) and (largo>=8 and largo<=16):
            self.password=_password
            return True
        else:
            return False

    def login(self,_password):
        if self.password==_password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("Valentina","valentina.daroch@gmail.com")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           