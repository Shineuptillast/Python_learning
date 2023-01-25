data = {    #dictionary of data
    
    "name":"Naman",
    "course":["ML","Dl","Stats","Python","CV"],
    "message":"This is my class"
}


def get_course():
       return data["course"]

def msg():
    return data["message"]

def get_name():
    return data["name"]
