class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.clave=""
        self.email=email
    def cambiar_password(self,password):
        if 8<=len(password)<=16:
            abc="abcdefghijklmnñopqrstuvwxyz"
            l_num=[]
            l_letras=[]
            l=[]
            for i in password:
                if i.isdigit():
                    l_num.append(i)
                if i.isalpha():
                    l_letras.append(i)
                if i.isupper():
                    l.append(i)
                if abc.count(i)==0 and not i.isdigit():
                    l.append(i)
            if len(l_num)==0 or len(l_letras)==0 or len(l)==0:
                return False
            else:
                return True
        else:
            return  False

    def login(self,password):
        if password==self.clave:
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