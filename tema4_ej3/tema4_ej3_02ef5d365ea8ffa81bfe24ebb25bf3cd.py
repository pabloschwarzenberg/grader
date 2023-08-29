def jerigonzo(string):
    list1 = list(string)
    counter = 0
    while counter < len(list1):
        if list1[counter] == 'a' or list1[counter] == 'e' or list1[counter] == 'i' or list1[counter] == 'o' or list1[counter] == 'u':
            list1.insert(counter+1, 'p' + list1[counter])
            counter +=1
        counter += 1
    string = ''.join(list1)
    return string




if __name__ == "__main__":
    pass
         