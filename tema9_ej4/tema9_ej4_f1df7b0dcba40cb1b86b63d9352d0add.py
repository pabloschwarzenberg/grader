class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if((7<len(password)<17)):
            if("A"in password)or("B"in password)or("C"in password)or("D"in password)or("E"in password)or("F"in password)or("G"in password)or("H"in password)or("I"in password)or("J"in password)or("K"in password)or("L"in password)or("M"in password)or("N"in password)or("Ñ"in password)or("O"in password)or("P"in password)or("Q"in password)or("R"in password)or("S"in password)or("T"in password)or("U"in password)or("V"in password)or("W"in password)or("X"in password)or("Y"in password)or("Z"in password)or(","in password)or(";"in password)or("."in password)or(":"in password)or("_"in password)or("-"in password):
                if("1"in password)or("2"in password)or("3"in password)or("4"in password)or("5"in password)or("6"in password)or("7"in password)or("8"in password)or("9"in password)or("0"in password):                   
                    if(("A"in password)or("B"in password)or("C"in password)or("D"in password)or("E"in password)or("F"in password)or("G"in password)or("H"in password)or("I"in password)or("J"in password)or("K"in password)or("L"in password)or("M"in password)or("N"in password)or("Ñ"in password)or("O"in password)or("P"in password)or("Q"in password)or("R"in password)or("S"in password)or("T"in password)or("U"in password)or("V"in password)or("W"in password)or("X"in password)or("Y"in password)or("Z"in password)or("a"in password)or("b"in password)or("c"in password)or("d"in password)or("e"in password)or("f"in password)or("g"in password)or("h"in password)or("i"in password)or("j"in password)or("k"in password)or("l"in password)or("m"in password)or("n"in password)or("ñ"in password)or("o"in password)or("p"in password)or("q"in password)or("r"in password)or("s"in password)or("t"in password)or("u"in password)or("v"in password)or("w"in password)or("x"in password)or("y"in password)or("z"in password)):
                        self.password=password
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def login(self,password):
        if(self.password==password):
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
           