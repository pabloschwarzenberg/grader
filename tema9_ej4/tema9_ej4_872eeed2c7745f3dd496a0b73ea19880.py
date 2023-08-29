class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):

        a=len(password)

        #b->tiene numero
        #c->tiene letras
        #d->tiene símbolo

        lista_b=[]

        lista_c=[]

        lista_d=[]
        

        for letra in password:

            numero=ord(letra)
            
            if numero>47 and numero<58:

                b=True

                lista_b.append(b)

            elif numero>96 and numero<123:

                c=True

                lista_c.append(c)

            else:

                d=True

                lista_d.append(d)

        if (True in lista_b)==True:

            rb=True

        else:

            rb=False

        if (True in lista_c)==True:

            rc=True

        else:

            rc=False

        if (True in lista_d)==True:

            rd=True

        else:
            rd=False

        


        if ((a>=8 and a<=16) and (rb==True and rc==True)) and rd==True:

            self.password=password

            return True

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
           