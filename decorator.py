


def convert_upper(function):#hello_world
    def inner_fuction():
        func=function()
        return func.upper()
    return inner_fuction


def split_func(function):
    def inner_code():
        func=function()
        return func.split()
    return inner_code






#hello_world function start it go to the convert_upper,pass a output to the split_func as a input and than implimenting logic, it will give the final output
@split_func # collect return from the convert_upper function and than implement on that
@convert_upper # 1st exicute this 
def hello_world():
    return "hello to the world"

print(hello_world())