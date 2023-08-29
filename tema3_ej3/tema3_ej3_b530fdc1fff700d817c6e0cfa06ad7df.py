 def __init__(self, __dni,__nombre,__apellidos) -> None:
    self.set_dni(__dni)
    self.set_nombre(__nombre)
    self.set_apellidos(__apellidos)

def set_dni(self, dni):
    self.__dni = dni

def get_dni(self):
    return self.__dni

def set_nombre(self, nombre):
    self.__nombre = nombre

def get_nombre(self):
    return self.__nombre

def set_apellidos(self, apellidos):
    self.__apellidos = apellidos

def get_apellidos(self):
    return self.__apellidos

def __eq__(self, otro: object) -> bool:
    if type(self) != type(otro):
        return NotImplemented
    return self.__dni == otro.__dni   