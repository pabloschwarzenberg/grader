a = input("Enter cells: ")
lista = list(a)

def matrix():
    p = 9 * "-"
    print(p)
    print("|", lista[0], lista[1], lista[2], "|")
    print("|", lista[3], lista[4], lista[5], "|")
    print("|", lista[6], lista[7], lista[8], "|")
    print(p)

matrix()

def who_wins():
    
    while True:
        
        if lista[0] == lista[1] == lista[2] != " " and not lista[3] == lista[4] == lista[5] and not lista[6] == lista[7] == lista[8]:
            print(lista[0], "wins")
            break
        elif lista[3] == lista[4] == lista[5] != " " and not lista[0] == lista[1] == lista[2] and not lista[6] == lista[7] == lista[8]:
            print(lista[3], "wins")
            break
        elif lista[6] == lista[7] == lista[8] != " " and not lista[0] == lista[1] == lista[2] and not lista[3] == lista[4] == lista[5]:
            print(lista[6], "wins")
            break
        elif lista[0] == lista[3] == lista[6] != " " and not lista[1] == lista[4] == lista[7] and not lista[2] == lista[5] == lista[8]:
            print(lista[0], "wins")
            break
        elif lista[1] == lista[4] == lista[7] != " " and not lista[0] == lista[3] == lista[6] and not lista[2] == lista[5] == lista[8]:
            print(lista[1], "wins")
            break
        elif lista[2] == lista[5] == lista[8] != " " and not lista[0] == lista[3] == lista[6] and not lista[1] == lista[4] == lista[7]:
            print(lista[2], "wins")
            break
        elif lista[0] == lista[4] == lista[8] != " ":
            print(lista[0], "wins")
            break
        elif lista[2] == lista[4] == lista[6] != " ":
            print(lista[2], "wins")
            break
        elif " " in lista:
            continue #??????????!!!!!!!!!!!
        else:
            print("Draw")
            break

def change_player():
    pass

while True:

    n = input("Enter the coordinates: ").split()

    if (n[0].isnumeric() and n[1].isnumeric()) != True:
        print("You should enter numbers!")
        continue
    elif int(n[0]) > 3 or int(n[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif lista[(int(n[0])-1)*3 + (int(n[1])-1)] in ["X", "O"]:
        print("This cell is occupied! Choose another one!")
        continue
    else:
        lista[(int(n[0])-1)*3 + (int(n[1])-1)] = "X"
        matrix()
        who_wins()
    break