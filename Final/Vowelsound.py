#Exercise-13
#Vowels Sound
class allint(Exception):
    """if input will be integer
    raise this error!"""
def vowel():
    a = input("please enter your sentence: ")
    if a.lower() == "end":
        exit(0)
    b = c = d = e = f = 0
    for val in  a[0:]:
        if val in "Aa":
            b +=1
        if val in "Ee":
            c+=1
        if val in "Ii":
            d += 1
        if val in "Oo":
            e +=1
        if val in "Uu":
            f+=1

    else:
        return f"""a:{b}
e:{c}
i:{d}
o:{e}
u:{f}
"""


