def input_fun(idx):
    try:
        my_list=[1,2,3]
        print(my_list[idx])
    except Exception as e:
        print(e)
        return -1
    
def main():
    val1=2
    val2=4
    if val1>3:
        raise Exception ("the var value more than 3.{} value provided".format(val1))
        #Asseration error
    assert (val2 > 3), "the var value more than 3"
    try:
        assert (val2 > 3), "the var value more than 3"
    except AssertionError as ae:
        print("catch error:",ae)
    except ZeroDivisionError as ze:
        print("catch arror:",ze)
    else:
        print("reach here bcoz there no error")
        try:
            a=4
            b=5
            c=a+b
        except Exception as e:
            print(e)

main()
