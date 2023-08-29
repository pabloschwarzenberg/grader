__author__ = 'Domingo'
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        lista_password=[]
        salida_numeros=[]
        salida_minusculas=[]
        salida_mayusculas=[]
        salida_simbolos=[]
        suma_salida_numeros=0
        suma_salida_minusculas=0
        suma_salida_mayusculas=0
        suma_salida_simbolos=0
        for i in password:
            lista_password.append(i)
        if len(password)<8 or len(password)>16:
            return False
        else:
            abecedario='abcdefghijklmnopqrstuvwxyz'
            ABECEDARIO='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numeros='1234567890'
            simbolos='!@#$%^&*()-=_+][/<>'
            for i in lista_password:
                num=numeros.find(i)
                salida_numeros.append(num)
                minusculas=abecedario.find(i)
                salida_minusculas.append(minusculas)
                mayusculas=ABECEDARIO.find(i)
                salida_mayusculas.append(mayusculas)
                sim=simbolos.find(i)
                salida_simbolos.append(sim)
            for i in salida_numeros:
                suma_salida_numeros+=i
            for i in salida_minusculas:
                suma_salida_minusculas+=i
            for i in salida_mayusculas:
                suma_salida_mayusculas+=i
            for i in salida_simbolos:
                suma_salida_simbolos+=i
            if suma_salida_numeros==(-1)*len(salida_numeros):
                return False
            else:
                if (suma_salida_minusculas==(-1)*len(salida_minusculas)) and (suma_salida_mayusculas==(-1)*len(salida_mayusculas)):
                    return False
                else:
                    if (suma_salida_mayusculas==(-1)*len(salida_mayusculas)) and (suma_salida_simbolos==(-1)*len(salida_simbolos)):
                        return False
                    else:
                        self.password=password
                        return True

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