class Shirt:
    sid=29
    small=1000
    medium=1200
    large=1400
    xl=1600

    def __init__(self,sname="Allen Solly Men's Solid Slim Fit ",type='formal',size='small'):
        Shirt.sid+=1
        self.sid=Shirt.sid
        self.sname=sname
        self.type=type
        self.size=size

    def display(self):
        print("-------------------------------------------------------")
        print("shirt id :{0}".format(Shirt.sid))
        print("shirt name :{0}".format(self.sname))
        print("shirt type :{0}".format(self.type))
        
        if(self.size=='small'):
            print("price of small size shirt:",Shirt.small)
        elif(self.size=='large'):
            print("price of large size shirt:",Shirt.large)
        elif(self.size=='medium'):
            print("price of medium size shirt:",Shirt.medium)
        else:
            print("price of XL size shirt:",Shirt.xl)

    def __del__(self):
            print("destructor called")



e=Shirt()
e.display()

e2=Shirt('stylish t-shirt','casual','medium')
e2.display()

