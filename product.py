class Product:
    pid=100
    def __init__(self,pn="Ac",pr=35000,qty=1) :
        Product.pid+=1
        self.pname=pn
        self.price=pr
        self.quantity=qty
        
    def displayproduct(self):
        print("-----------------------------------------------------------")
        print("product id:{0}".format(Product.pid))
        print("product Name:{0}".format(self.pname))
        print("product Price:{0}".format(self.price))
        print("product Quantity:{0}".format(self.quantity))

    def __str__(self):
        data="\nproduct id:{0}".format(Product.pid)
        data+="\nproduct Name:{0}".format(self.pname)
        data+="\nproduct Price:{0}".format(self.price)
        data+="\nproduct Quantity:{0}".format(self.quantity)
        return data

    def __del__(self):
        print("destructor called")


s1=Product()
print(s1)

s2=Product('Fan',2000,2)
s2.displayproduct()

