# Exercise_31
def Captial():
    a = input("please Enter Your sentence:")
    a = a.lower()
    a_len = len(a)
    i = 0
    new_word = ""
    l = []
    if a == "end":
        exit(0)

    for val in a:

        if val == " ":
            ord_c = ord(new_word[0])
            if 96 < ord_c < 123:
                new_word = chr(ord_c - 32) + new_word[1:]
            l.append(new_word)
            new_word = ""
        else:
            new_word += val
        i += 1
        if i == a_len:
            ord_c = ord(new_word[0])
            if 96 < ord_c < 123:
                new_word = chr(ord_c - 32) + new_word[1:]
            l.append(new_word)

    sen = " ".join(l)
    print(sen)


    class WrongError(Exception):
        """WrongError Defualt class to
        raise wrong error
        when we have 'free' in sentnce"""
        pass

    free_word = 0
    for val in l:
        try:
            if val.lower() == "free":
                free_word += 1
                raise WrongError
        except WrongError as WR:
            print("-------------------------------")
            print("Wrong Word in sentece ")
            print("free")
    else:
        print(f"\"free\" word in sentence: {free_word} times!")