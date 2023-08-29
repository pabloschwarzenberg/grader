
#Insertamos un tablero vacío
def create_board():
    board= np.zeros((3,3))
    return board

board= create_board()

#Creamos una función para ingresar valores (1 para el primer jugador y 2 para el segundo 

def random_place(board,player):
    placement= possibilities(board)
    if len(placement)>0:
        placement = random.choice(placement)
        place(board, player, placement)
    return board

#Función para crear juegos completos de gato 
def play_game():
    board= create_board()
    for i in range(5):
        random_place(board,1) 
        random_place(board,2)
    print(board)

play_game()


#Creamos una función para evaluar quién gana por filas

def row_win(board,player):
    for i in range(len(board)):
        if np.all(board[i]==player):   
            return True
        else:
            return False

#Luego otra para evaluar quién gana por columnas

def col_win(board,player):
    for i in range(len(board)):
        if np.all(board[:,i]==1):   
            return True
        else:
            return False

#Finalmente, una para evaluar quién gana en diagonales

def diag_win(board, player):
    if np.all(np.diag(board)==player) or    np.all(np.diag(np.fliplr(board))==player):
        return True
    else:
        return False

#La función de evaluación que hasta ahora he construido

def evaluate(x):       
    if row_win(board,1) or col_win(board,1) or diag_win(board,1):
        return "Gana jugador 1"
    elif row_win(board,2) or col_win(board,2) or diag_win(board,2):
        return "Gana jugador 2"
    else:
        return "Nadie gana"
         