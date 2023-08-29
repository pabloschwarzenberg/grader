def buscarTodas(a,b):
     i = 0
     lista = []
     for carac in a:
         if carac == b:
             lista.append(str(i))
         i = i + 1
     return " ".join(lista)


           