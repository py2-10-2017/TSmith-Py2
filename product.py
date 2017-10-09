class Product(object):

    def __init__(self,price,name,weight,brand,cost,status='For Sale'):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = 'Sold'
        return self
    def add_tax(self,tax):
        self.price += (self.price)*tax
        return self
    def Return(self,reason):
        if reason == 'Broken':
            self.status = 'Broken'
            self.price = 0
        elif reason == 'Useable':
            self.status = "For Sale"
        elif reason == 'Open':
            self.status = 'Used'
            self.price -= (self.price)*0.2
        return self
    def display_info(self):
        print "Price is ${}".format(self.price)
        print "Product name is {}".format(self.name)
        print "Product weight is {}lb".format(self.weight)
        print "Product brand is {}".format(self.brand)
        print "Product cost is ${}".format(self.cost)
        print "Product Status is {}".format(self.status)

socks = Product(5,'socks',1,'Hanes',8)
socks.display_info()
socks.sell()
socks.add_tax(8.25)
