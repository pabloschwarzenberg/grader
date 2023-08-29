def buscarTodas(a,b):
    poscisiones = ""
    numero = 0
    for i in a:
       if i == b:
         if poscisiones == "":
           numerostr = str(numero)
           poscisiones += numerostr
           numero += 1
         else:
            poscisiones += " "
            numerostr = str(numero)
            poscisiones += numerostr
            numero += 1
       else:
          numero += 1
    return poscisiones
           