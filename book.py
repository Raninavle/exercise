class Book:
    count=0
    bid=1000
    def __init__(self,bname="newbook",pr=1000,ar="peter"):
        Book.count+=1
        Book.bid+=1
        self.bid=Book.bid
        self.bname=bname
        self.price=pr
        self.author=ar

    def showbook(self):
        print("------------------------------------------------")
        print("Book Id :",self.bid)
        print("Book Name:",self.bname)
        print("Book Price:",self.price)
        print("Book Author:",self.author)
        print("no.of object created:",Book.count)

    def __str__(self):
        data="\nBook Id:{0} ".format(self.bid)
        data+="\nBook Name:{0}".format(self.bname)
        data+="\nBook Price:{0}".format(self.price)
        data+="\nBook Author:{0}".format(self.author)
        data+="\nno.of object created:{0}".format(Book.count)
        return data
        
    def __del__(self):
        print("destructor called")


a1=Book('Math',500,"Bansal")
b1=Book("History",1500,"Ramchandra guha")
c1=Book("Beautiful things",2000,'Hunter Biden')
allobj=[a1,b1,c1]
for e in allobj:
    print(e)


