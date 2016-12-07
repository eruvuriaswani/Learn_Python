
# login module
class login():
    pass
    
    def logme(username):
        result, data = restapi.call(login)
        if(result):
            print(data)
        else:
            asset(result)