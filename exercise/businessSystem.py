"""
here is the system that includes the goods name ,price and their category."""

# define a class of goods

class Goods:
    def __init__(self,name,price,kind):
        self.name = name
        self.price= price
        self.kind = kind

    def __str__(self):
        pass

ls_goods = []

# get the varible from the clients input
def loopGet():

    while True:
        print(" Please type the '#' to stop the loop!")

        try:
            Goods = (input("Please key in the name:\n"),input("Please key in the price:\n"))
            ls_goods.append(Goods)
        except:
            pass

        if "#" in ls_goods:
            break

# set a dictionary list of all the goods

