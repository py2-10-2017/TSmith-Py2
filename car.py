class Car(object):
    def __init__(self, price, speed, mileage, fuel):
        self.price = price
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel

        if self.price > 10000:
            self.tax = .15
        
        else:
            self.tax = .12

    def display_all(self):
        print 'Price {}'.format(str(self.price))
        print 'Speed {} mph'.format(str(self.speed))
        print 'Mileage {} mpg'.format(str(self.mileage))
        print 'Fuel {}'.format(str(self.fuel))
        print 'Tax {}'.format(str(self.tax))

Car1=Car(2000, 45, 25, 'full')

Car1.display_all()

        
    


