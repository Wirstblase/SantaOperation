import random
def colgen():

    a = ["my favorite colour","I prefer the colour",]
    b = ["red","green","blue","violet","gold","purple","cyan","turquoise","black","white","gold","silver","lillac","cactus green","sky blue","ocean blue"]
    i = random.randint(0,len(a)-1)
    j = random.randint(0,len(b)-1)

    col = a[i] + " " + b[j]

    return col  
