  
#factorial
def fact (x,y=0):
    if y == 0:
        return"please enter 2 argument"
    elif x == y:
        return 1
    else:
        x+= 1
        return x * fact(x,y)
        