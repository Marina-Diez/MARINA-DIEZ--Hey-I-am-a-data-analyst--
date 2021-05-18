def regex(string):
    df.str.split("\(|\)", expand=True).iloc[:,[0,1]]

def cleaning(string):
    hoods = ["manhattan","brooklyn","bronx", "queens", "staten island"]
    for w in hoods:
        if w in str(string).lower(): 
            return w
    else:
         return "other"
