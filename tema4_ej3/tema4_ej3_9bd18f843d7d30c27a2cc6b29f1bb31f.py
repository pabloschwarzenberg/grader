def jerigonzo(string):
    new_string = ''
    consonante = ''
    for a in string:
        consonante += a
        if a in 'AaEeIiOoUu':
            new_string += consonante + 'p' + a
            consonante = ''
    return new_string

if __name__ == "__main__":
    string = input()
    print(jerigonzo(string))
    pass
         