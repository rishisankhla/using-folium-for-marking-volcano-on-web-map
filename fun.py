def acol(x):
    if x['properties']['POP2005']<10000000:
        return{'fillColor':'blue'}
    elif 10000000<= x['properties']['POP2005']<20000000:
        return{'fillColor':'orange'}
    else:
        return{'fillColor':'red'}
        
def col(e):
    if e<1000:
        return('green')
    elif 1000<= e <3000:
        return('orange')
    else:
        return('red')          

