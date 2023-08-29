# Jerigonzo
def jerigonzo(s_1):
    s_2 = ""
    
    for i in range(len(s_1)):
        if((s_1[i] == 'a' or s_1[i] == 'A') or (s_1[i] == 'e' or s_1[i] == 'E') or (s_1[i] == 'i' or s_1[i] == 'I') or (s_1[i] == 'o' or s_1[i] == 'O') or (s_1[i] == 'u' or s_1[i] == 'U')):
            s_2 = s_2 + s_1[i] + 'p' + s_1[i]
        else:
            s_2 = s_2 + s_1[i]
    
    return s_2

if __name__ == "__main__":
    palabra_1 = input("Ingrese una palabra: ")
    
    palabra_2 = jerigonzo(palabra_1)
    
    print("\nLa palabra traducida a jerigonzo es:", palabra_2)