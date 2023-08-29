def tiene_letras(cocacola):
    cocacola=str(cocacola)
    abc="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    qwert=0
    for i in cocacola:

        if i in abc:
            qwert+=1
        else:
            pass
    if qwert==0:
        return False
    else:
        return True
def tiene_car_esp(cocacola):
    cocacola=str(cocacola)
    abc="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"

    qwert=0
    for i in cocacola:

        if i in abc:
            pass
        else:
            qwert+=1
    if qwert==0:
        return False
    else:
        return True
def tiene_numeros(cocacola):
    cocacola=str(cocacola)
    abc="0123456789"
    qwert=0
    for i in cocacola:

        if i in abc:
            qwert+=1
        else:
            pass
    if qwert==0:
        return False
    else:
        return True
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password=str(password)
        if len(password)>7 and len(password)<17 and ((password.lower()!=password)or(tiene_car_esp(password))) and tiene_letras(password) and tiene_numeros(password):
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