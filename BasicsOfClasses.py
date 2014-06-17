#ADDED Animal CLASS AND ADDED ‘pass’ IN THE BODY
class Animal(object):
    pass

#DEFINED INITIALIZE METHOD IN Animal CLASS
#ADDED pass TO THE BODY
class Animal(object):
    def __init__(self):
        pass

#ADDED name AS SECOND PARAMETER TO Animal CLASS
#ADDED BODY TO METHOD
class Animal(object):
    def __init__(self, name):
        self.name = name

#ADDED zebra VARIABLE EQUAL TO Animal(“Jeffrey”) AND PRINTED
class Animal(object):
    def __init__(self, name):
        self.name = name
        
zebra = Animal("Jeffrey")

print zebra.name

#ADDED is_hungry VARIABLE
class Animal(object):
    """Makes cute animals."""
    def __init__(self, name, age, is_hungry):	#Added is_hungry
        self.name = name
        self.age = age
        self.is_hungry = is_hungry			#Added line item

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

#ADDED is_alive VARIABLE
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age, is_alive):		#Added is_alive
        self.name = name
        self.age = age
        self.is_alive = is_alive 			#Added this line item

zebra = Animal("Jeffrey", 2, True)		#Added True
giraffe = Animal("Bruce", 1, True)		#Added True
panda = Animal("Chad", 7, True)		# Added True

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

#ADDED description METHOD
#PRINTED name AND age
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):		# Added section
        print self.name
        print self.age

#ADDED health VARIABLE EQUAL TO “good”
#ADDED ANIMALS sloth AND ocelot
#PRINTED health OF hippo, sloth, AND ocelot
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age

hippo = Animal("Beau", 5) 	#Added code from here onward
sloth = Animal("Tom", 2) 	
ocelot = Animal("Henry", 3)	

print hippo.health 		
print sloth.health 		
print ocelot.health 		

#ADDED my_cart VARIABLE EQUAL TO ShoppingCart CLASS
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Tom") 	#Added line item
my_cart.add_item("Bread", 5)

#ADDED Triangle CLASS AND INHERITED IT FROM Shape
#ADDED ARGUMENTS side1, side2, side3 AND THE BODY
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):			#Added section
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

#ADDED PartTimeEmployee CLASS THAT INHERITS FROM Employee
#ADDED calculate_wage METHOD
#OVERRODE Employee ARGUMENTS WITH self AND hours
#RETURNED hours WORKED MULTIPLIED by 12.00
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):		#Added section
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

#ADDED PartTimeEmployee CLASS CALLED milton
#PRINTED RESULT OF full_time_wage
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")		#Added code from here onward
print milton.full_time_wage(10)

#CREATED Triangle CLASS WITH INITIALIZE METHOD WITH ARGUMENTS angle1, angle2, AND angle3 AND ADDED BODY
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

#ADDED number_of_sides VARIABLE
#ADDED METHOD check_angles AND SUMMED ALL THE ANGLES AND RETURN CONDITION TRUE OR FALSE
class Triangle(object):
    number_of_sides = 3		#Added line
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
def check_angles(self):		#Added section
    if angle1 + angle2 + angle3 == 180:
        return True
    else:
        return False

#ADDED INITIALIZE METHOD WITH (3) ANGLES AS ARGUMENTS
#ADDED number_of_sides VARIABLE
#ADDED check_angles VARIABLE TO SUM ALL (3) ANGLES AND RETURN CONDTION TRUE OR FALSE
class Triangle(object):
    def __init__(self, angle1, angle2, angle3): 	#Added code from here onward
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3
    
    def check_angles(self):
        if angle1 + angle2 + angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(60, 60, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles

#ADDED Equilateral CLASS THAT INHERITS FROM Triangle
#ADDED angle VARIABLE EQUAL TO 60
#ADDED INITIALIZE METHOD
#ADDED self.angle VARIABLE EQUAL TO self.angle1, self.angle2, AND self.angle3
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3
    
    def check_angles(self):
        if angle1 + angle2 + angle3 == 180:
            return True
        else:
            return False

class Equilateral(Triangle): 		#Added code from here onward
    angle = 60
    def __init__(self):
        self.angle = self.angle1, self.angle2, self.angle3

my_triangle = Triangle(60, 60, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles
