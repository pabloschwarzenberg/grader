def rot13(palabra):
  Var_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  x = ""
  for i in palabra:
    Var_3 = Var_2.index(i)
    #print(Var_3)
    Var_3 += 13
    #print(Var_3)
    Var_4 = Var_2[Var_3]
    x += Var_4
  return x
 
if __name__ == "__main__":
  Var_1 = input("Ingresa la palabra que quieras encriptar: ")
  rot13(Var_1)
