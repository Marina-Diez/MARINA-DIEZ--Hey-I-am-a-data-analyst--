
def cleaning(string):
    hoods = ["Manhattan","Brooklyn","Bronx","State Island","Queens"]

    for w in hoods:
        if w in str(string): 
            return w
    else:
         return "other"

