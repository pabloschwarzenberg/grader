raton='O'
gato='X'
underscore_=''
Ta=[["_","_","_"],["_","_","_"],["_","_","_"]]

def revisar_horizontal(Ta,fila):
      if Ta[fila][0]=="X" and Ta[fila][1]=="X" and Ta[fila][2]=="X":
            print("gato gana")
            return -1
      elif Ta[fila][0]=="O" and Ta[fila][1]=="O" and Ta[fila][2]=="O":
            print("raton gana")
            return 1
      else:
            print("no hay ganador")
            return 0

def revisar_vertical(Ta,columna):
      if  Ta[0][columna]=="X" and Ta[1][columna]=="X" and Ta[2][columna]=="X":
            print("gato gana")
            return -1
      elif Ta[0][columna]=="O" and Ta[1][columna]=="O" and Ta[2][columna]=="O":
            print("raton gana")
            return 1
      else:
            print("no hay ganador")
            return 0

def revisar_diagonal_derecha(Ta):
      if Ta[0][0]=="X" and Ta[1][1]=="X" and Ta[2][2]=="X":
            print("gato gana")
            return -1
      elif Ta[0][0]=="O" and Ta[1][1]=="O" and Ta[2][2]=="O":
            print("raton gana")
            return 1
      else:
            print("no hay ganador")
            return 0

def revisar_diagonal_izquierda(Ta):
      if Ta[0][2]=="X" and Ta[1][1]=="X" and Ta[2][0]=="X":            
            print("gato gana")
            return -1
      elif Ta[0][2]=="O" and Ta[1][1]=="O" and Ta[2][0]=="O":
            print("raton gana")
            return 1
      else:
            print("no hay ganador")
            return 0