#CREATED TO OPEN A FILE
#ADDED ARGUMENT SO FILE ALLOWS TO READ AND WRITE IT
my_file = open("output.txt", "r+")

#ADDED REITERATION /LOOP TO WRITE EA VALUE
#WITH STR SO WRITE FUNCTION ACCEPTS IT
#WITH \n SO RESULTS ARE ON NEW LINE
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for item in my_list: 			#Added this section
    my_file.write(str(item) + "\n")
my_file.close()

#CREATED IN ORDER TO READ OUTPUT TEXT
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

#CREATED TO READ FROM A FILE LINE BY LINE
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

#BUFFERED DATA
read_file = open("text.txt", "r")
write_file = open("text.txt", "w")
write_file.write("Not closing files is VERY BAD.")
write_file.close()		#Added line item
print read_file.read()
read_file.close()			#Added line item

#CREATED JUST AS AN EXAMPLE OF USING with AND as
with open("text.txt", "w") as f:
    f.write("Hi")

#CHECKED TO SEE IF FILE WAS CLOSED
with open("text.txt", "w") as my_file:
    my_file.write("Hi")

if my_file.closed == False:	#Added code from here below
    my_file.close()

print my_file.closed
