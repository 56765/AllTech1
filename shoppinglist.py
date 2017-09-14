
class ShoppingList:
    def __init__(self,money):
        self.money=money
        self.Shopping_List={}

    def additem(self,item,price):
        self.Shopping_List[item]=price
        self.money=self.money-price
        

    def remitem(self,item):
        self.money=self.money+ShoppingList[item]
        del self.Shopping_List[item]
    def show(self):
        print(self.money,self.Shopping_List)
        
shop=ShoppingList(100)
shop.additem('grapes',10)
shop.show()
shop.additem('oranges',10)
shop.show()
shop.additem('bananas',10)
shop.show()
shop.additem('apples',10)
shop.show()
shop.additem('lemons',10)
shop.show()
shop.remitem('grapes')
shop.show()









