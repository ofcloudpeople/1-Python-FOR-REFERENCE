#CREATED Car CLASS AND ADDED pass IN THE BODY
class Car(object):
    pass

#ADDED A VARIABLE OF THE CLASS
class Car(object):
    pass

my_car = Car()

#REPLACED pass WITH A MEMBER VARIABLE
class Car(object):
    condition = "new"

my_car = Car()

#PRINTED RESULT
class Car(object):
    condition = "new"

my_car = Car()

print my_car.condition

#ADDED INITIALIZE METHOD WITH ARGUMENTS AND VARIABLES TO THE BODY
#ADDED my_car VARIABLE
#PRINTED CONDITION
class Car(object):
    condition = "new"
    define __init__(self, model, color, mpg):	#Added arguments
        self.model = model				#Added 3 variables
        self.color = color
        self.mpg = mpg

my_car = Car(model, color, mpg)		#Included the 3 variables
print my_car.condition

#ADDED SPECIFIC DATA IN my_car VARIABLE AND REPLACED PRINTED THOSE MEMBER VARIABLES 
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car('DeLorean', 'silver', 88)
print my_car.model
print my_car.color
print my_car.mpg

#ADDED display METHOD
#RETURNED STATEMENT TO STATE THE COLOR, MODEL AND MPG
#PRINTED DETAILS OF CAR
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a "+self.color+" "+self.model+" with "+str(self.mpg)+" MPG."

my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()

#ADDED drive_car METHOD WITH CONDITION
#PRINTED CONDITIONS “new” AND “used”
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a "+self.color+" "+self.model+" with "+str(self.mpg)+" MPG."
    def drive_car(self):
        self.condition = "used"
        return self.condition

my_car = Car("DeLorean", "silver", 88) 		#Add whatever prefered
print my_car.condition
print my_car.drive_car()

#ADDED drive_car METHOD TO ElectricCar CLASS
#PRINTED CONDITIONS “new” AND “like new”
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a "+self.color+" "+self.model+" with "+str(self.mpg)+" MPG."
    def drive_car(self):
        self.condition = "used"
        return self.condition
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type
    def display_car(self):
       return super(ElectricCar, self).display_car() + "It has a %s battery. " % (self.battery_type)
    def drive_car(self):
        condition = "like new"
        return condition
    
my_car = ElectricCar("Ford", "black", 30, "molten salt")
print my_car.condition
print my_car.drive_car()

#CREATED A CLASS, TWO METHODS AND A VARIABLE
#PRINTED THE VARIABLE
class PointsXYZ(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return str((self.x, self.y, self.z))
    
my_point = PointXYZ(1, 2, 3)
print my_point
