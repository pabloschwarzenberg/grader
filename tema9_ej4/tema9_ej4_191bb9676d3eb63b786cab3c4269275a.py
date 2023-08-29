class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password="hola"

    def cambiar_password(self,password):
        lista_pass= list(password)
        cumple_m_cr=[]
        cumple_letras=[]
        cumple_num= []
        caracter_raro=["_","#"]
        abc= "abcdefghijklmnopqrstuvwxyz"
        num="1234567890"
        lista_num= list(num)
        lista_abc= list(abc)
        abc_mayus=abc.upper()
        lista_abc_mayus=list(abc_mayus)
        if len(lista_pass)<17 and len(lista_pass)>7:
            for caracter in lista_pass:
                for letra in lista_abc:
                    if caracter==letra:
                        cumple_letras.append(0)
                    else:
                        pass
                for caractercillo in caracter_raro:
                    if caractercillo==caracter:
                        cumple_m_cr.append(0)
                    else:
                        pass
                for numero in lista_num:
                    if caracter== numero:
                        cumple_num.append(0)
                    else:
                        pass
                for letra in lista_abc_mayus:
                    if caracter==letra:
                        cumple_m_cr.append(0)
                    else:
                        pass
            if len(cumple_num)>=1 and len(cumple_m_cr)>=1 and len(cumple_letras)>=1:
                self.password=password
                return True
            else:
                return False
        else:
            return False
            
    def login(self,password):
        if self.password==password:
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
           