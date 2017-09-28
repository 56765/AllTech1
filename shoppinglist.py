
class SuperMarket:
    def __init__(self):
 
        self.Super_Market={}

    def addgrocery(self,item,price):
        self.Super_Market[item]=price
        

    def remnumber(self,name):
        if name in self.Phone_Book:

        
            
            del self.Phone_Book[name]
        else:
            print('no such number in the phone book')
    def show(self):
        print(self.Phone_Book)

    def find_number(self):
        x=input('whose number do you want to know?')
        if x in self.Phone_Book:
            
            print(self.Phone_Book[x])
        else:
            print('That phone number is not found')
        
phonebook=PhoneBook()

phonebook.addnumber(576031748,'a')
phonebook.show()
phonebook.addnumber(7892540275,'b')
phonebook.show()
phonebook.addnumber(7892540275,'d')
phonebook.show()
phonebook.remnumber('c')
phonebook.show()
phonebook.remnumber('b')
phonebook.show()
phonebook.find_number()









