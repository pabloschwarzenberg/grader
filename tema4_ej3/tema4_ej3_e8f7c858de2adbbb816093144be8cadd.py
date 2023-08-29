def jerigonzo(string):
  n_string = ""
  for c in string:
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
      n_string = n_string + c + "p" + c
    else:
      n_string = n_string + c
  return n_string

if __name__ == "__main__":
    s = input("Ingrese su mensaje: ")
    m_j = jerigonzo(s) 
    print(m_j)
    pass
         