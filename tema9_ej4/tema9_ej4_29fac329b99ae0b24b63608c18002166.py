class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        pass_list = []
        letras_min = 0
        letras_may = 0
        numeros = 0
        car_especial = 0
        tiene_may_o_especial = False
        for letra in password:
            pass_list.append(letra)
        for i in range(len(pass_list)):
            if pass_list[i].isalpha() == True and pass_list[i].islower() == True:
                letras_min += 1
            elif pass_list[i].isalpha() == True and pass_list[i].isupper() == True:
                letras_may += 1
            elif pass_list[i].isnumeric() == True:
                numeros += 1
        if password.isalnum() == False:
            car_especial += 1
        if car_especial > 0 or letras_may > 0:
            tiene_may_o_especial = True
        if letras_min > 0 and numeros > 0 and tiene_may_o_especial == True:
            self.password = password
            return True
        else:
            return False

        pass

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
           