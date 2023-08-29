# Función buscarTodas
def buscarTodas(s_a, s_b):
    c, s_c = 0, ""
    
    for i in range(len(s_a)):
        if s_a[i] == s_b:
            if c == 0:
                c, s_c = c + 1, s_c + str(i)
            elif (c > 0) and (c < ((len(s_a)) - 1)):
                c, s_c = c + 1, s_c + " " + str(i)
            elif c == ((len(s_a)) - 1):
                s_c = s_c + str(i)
                
                return s_c
        else:
            if c == int((len(s_a)) - 1):
                return s_c
            
            c += 1

if __name__ == "__main__":
    str_a = input("Ingrese string a: ")
    str_b = input("Ingrese string b: ")
    str_c = buscarTodas(str_a, str_b)
    
    print("\n" + str_c)