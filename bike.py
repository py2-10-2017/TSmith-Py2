class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price: ${}'.format(str(self.price))
        print 'Top speed: {}'.format(str(self.max_speed))
        print 'Mileage: {}'.format(str(self.miles))

    def ride(self):
        print 'Riding'
        self.miles += self.miles + 10

    def reverse(self):
        print 'Reverse'
        if self.miles >= 5:
                self.miles -= 5

Bike1 = Bike(200, 40)
Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.reverse()
Bike1.displayInfo()







