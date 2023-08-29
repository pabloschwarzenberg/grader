n = input("Ingrese numero telefonico: ")
n = int(n)
if n < 100000000 and n > 9999999:
                  h = input("Ingrese hora de la llamada: ")
                  h = int(h)
                  if h >= 0 and h <= 7:
                        print("Resultado: CONTESTAR" )
                  elif h > 7 and h < 14:
                        k = n%1000
                        k = int(k)
                        if k == 909:
                              print("Resultado: CONTESTAR" )
                        else:
                              print( "Resultado: NO CONTESTAR" )
                  elif h >= 14 and h < 17:
                        print( "Resultado: NO CONTESTAR" )
                  elif h >= 17 and h <=19:
                        if (n - n%100000) == 87700000:
                              print( "Resultado: NO CONTESTAR" )
                        else:
                              print("Resultado: CONTESTAR")
                  else:
                    print("Resultado: NO CONTESTAR")
              
else:
            print("NUMERO FUERA DE PARAMETROS")