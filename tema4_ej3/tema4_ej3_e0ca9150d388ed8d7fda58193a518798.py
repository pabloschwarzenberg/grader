def jerigonzo(string):
    pos = 0
    while pos < len(string):
        char = string[pos]
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            string = string[:pos+1] + 'p' + char + string[pos+1:]
            pos = pos + 2
        pos = pos + 1
    return string

      