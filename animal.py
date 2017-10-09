class Animals(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'Health: {} '.format(str(self.health))

animalFake = Animals('Wynnston', 100)
animalFake.walk()
animalFake.walk()
animalFake.walk()
animalFake.run()
animalFake.run()
animalFake.displayHealth()

class Dog(Animals):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150
        return self
    def pet(self):
        self.health += 5
        return self
dog1 = Dog('Max', 150)
dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.displayHealth()

class Dragon(Animals):
    def __init__(self):
        super(Dragon, self).__init__()
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self