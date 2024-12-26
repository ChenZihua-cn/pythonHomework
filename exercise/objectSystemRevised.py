class Kinds:
    pass
class goods(Kinds):
    def __init__(self,goodsName,goodsPrice,goodsKind,goodsLabel):
        
        self.name = goodsName
        self.price = goodsPrice
        self.kinds = goodsKind
        self.label = goodsLabel
    
    def greet(self):
        print(f"This goods valued {self.price}")

    def __str__(self):
        return f"goods({self.name},{self.price})"
    


ls_goodsName = []
ls_goodsPrice = []
goodsAttrib = {}
goodsInfo = set()

def main():
    while True:

        keyword = input("Please key in what you want to do in the system: \n\
            1.add goods\n\
            2.delete goods\n\
            3.revise info\n\
            4.exit\n")
        try:
            if int(keyword) == 1: # add goods
                addGoods()
                
            elif int(keyword) == 2:# delete goods
                deleteGoods()

            elif int(keyword) == 3:# revise goods
                reviseGoods()
            
            elif int(keyword) == 4:
                break
            else:
                print("please choose a number of function\n")
                continue
        except:
            pass
def addGoods():
    b =input("key in the goods name\n")
    a = float(input("what the goods cost?\n"))
    
    ls_goodsName.append(b)
    goodsInfo.add(zip(str(a),b))
    return 0

def deleteGoods():
    keyword = input("What kinds of goods do you want to delete?\n")
    print(ls_goodsName)
    try:
        ls_goodsName.remove(keyword)
    except ValueError:
        print("There is no goods named {}".format(keyword))
    return 0
    
def reviseGoods():
    keyword = input("What kinds of goods do you want to revise?\n")
    print(ls_goodsName)
    try:
        i = ls_goodsName.index(keyword)
        delGoods = ls_goodsName.pop(i)
        addgoods = input("what kinds of goods do you want to add in the list?\n")
        ls_goodsName.append(addgoods)
        print(f"The {delGoods} had already been replaced with the {addgoods}")
    except ValueError:
        print("There is no goods named {}".format(keyword))
    return 0



#    print("key in the 0 to break the loop")   
#    goodsKind = input("please key in the kind of goods")
#    goodsKind = input("please key in the kind of goods")
#    while True:
#        ls_goodsName.append(input("please key in the name of goods"))
#        ls_goodsPrice.append(input("please key in the price of goods"))
#        if "0" in ls_goodsName or ls_goodsPrice:
#            break
main()