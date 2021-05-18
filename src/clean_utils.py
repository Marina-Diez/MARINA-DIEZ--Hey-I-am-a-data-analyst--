
def cleaning(string):
    hoods = ["manhattan","brooklyn","bronx", "queens", "staten island"]
    for w in hoods:
        if w in str(string).lower(): 
            return w
    else:
         return "other"