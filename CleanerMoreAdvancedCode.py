#PRINT LIST EVEN NUMBERS TO 50
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#PRINT LIST THE SQUARE OF EVEN NUMBERS TO 11
even_squares = [i**2 for i in range(1,11) if i % 2 == 0]
print even_squares

#PRINT LIST THE CUBE OF NUMBERS TO 11 DIVISIBLE BY 4
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]
print cubes_by_four

#PRINT LIST OF ODD ELEMENT TO 11
my_list = range(1, 11)
print my_list[::2]

#RETURN REVERSED LIST VERSION BY 1s
my_list = range(1, 11)
backwards = my_list[::-1]

#RETURN REVERSED LIST VERSION BY 10s
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

##SIMPLE EXERCISES
to_21 = range(1, 22)
odds = to_21[::2] #created odd numbers list
middle_third = to_21[7:14:1] #created list of middle numbers

#USE LAMBDA TO ONLY LIST “PYTHON”
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

#PRINT SQUARES BETWEEN 30 AND 70
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

#ITERATING OVER A DICTIORNARY - PRINT ITEMS IN DICT
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

#LIST NUMBERS 1 THROUGH 15 DIVISIBLE BY 3 OR 5
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

#RETURN REVERSE OF LIST AND ONLY EVERY OTHER LETTER
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
reverse = garbled[::-1]
message = reverse[::2]

#FILTER OUT  Xs
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
