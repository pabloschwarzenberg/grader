class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password="" 

    def cambiar_password(self,password):
        lista_abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        lista_num = ['0','1','2','3','4','5','6','7','8','9']
        lista_may = []
        for i in lista_abc:
            lista_may.append(i.upper())
        l = list(password)
        r = []
        letra = []
        num = []
        may = []
        for i in range(len(l)):
            if l[i] in lista_abc:
                letra.append(l[i])
            elif l[i] in lista_num:
                num.append(l[i])
            elif l[i] in lista_may:
                may.append(l[i])
            elif (l[i] not in lista_abc) and (l[i] not in lista_num):
                r.append(l[i])

        largo = len(password)
        if (largo >= 8) and (largo <= 16):
            if ((len(r)!=0) and (len(letra)!=0) and (len(num)!=0)) or ((len(may)!=0) and (len(letra)!=0) and (len(num)!=0)):
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
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

           