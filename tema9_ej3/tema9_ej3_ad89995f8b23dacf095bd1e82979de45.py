
         ##Decodificador
import json

def decodificar_numero_complejo(objeto):
    return complex(objeto['real'], objeto['imag'])


objeto = json.loads('{"real": 3, "imag": 6}', object_hook=decodificar_numero_complejo)

print(type(objeto))
print(objeto)
