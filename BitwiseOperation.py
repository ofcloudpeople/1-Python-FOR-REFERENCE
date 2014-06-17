#USED AS REFERENCE
#2**0 = 1
#2**1 = 2
#2**2 = 4
#2**3 = 8
#2**4 = 16
#2**5 = 32
#2**6 = 64
#2**7 = 128
#2**8 = 256
#2**9 = 512
#2**10 = 1024

#I KNOW WHAT THE BINARIES OF 1 THROUGH 12 ARE
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#HERE IS HOW TO PRINT BINARY OF 1 THROUGH 5
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

#HERE IS THE PRINTED DECIMAL EQUIVALENT OF BINARY 11001001
print int(bin(201),2)

#1) SHIFT VARIABLE 2 TO THE RIGHT
#2) SHIFT VARIABLE 2 TO THE LEFT
shift_right = 0b1100
shift_left = 0b1

# Answer is here
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

#FOR EVERY GIVEN BIT OF A ‘AND’ B, THIS IS TRUE
#0 & 0 = 0
#0 & 1 = 0
#1 & 0 = 0
#1 & 1 = 1

#HERE IS HOW TO PRINT BINARY OF 0b1110 ‘AND’ 0b101 
print bin(0b1110 & 0b101)

#FOR EVERY GIVEN BIT IN A ‘OR’ B, THIS IS TRUE
#0 | 1 = 1 
#1 | 0 = 1
#1 | 1 = 1

#HERE IS HOW TO PRINT BINARY OF 0b1110 ‘OR’ 0b101
print bin(0b1110 | 0b101)

#HERE IS HOW TO PRINT BINARY TO SHOW WHERE BITS ARE 1S IN BOTH A ‘AND’ B
print bin(0b1110 ^ 0b101)

#HERE IS HOW TO PRINT THE NOT OPERATOR ~ OF 1, 2, 3, 42, 123
#EQUIVALENT TO ADDING ONE TO NUMBER, THEN MAKING IT NEGATIVE
print ~1		#-2
print ~2		#-3
print ~3		#-4
print ~42	#-43
print ~123	#-124

#CHECKED IF 4TH BIT TO THE RIGHT IS TURNED ON
def check_bit4(input):
    if input & 0b1000:
        return "on"
    else:
        return "off"

check_bit4(0b00101010) #Example

#CHANGED AND PRINTED SO 3RD BIT IN a FROM RIGHT IS TURNED ON
a = 0b10111011
mask = 0b10111111
print bin(a | mask)

#CHANGED AND PRINTED SO ALL BITS IN a ARE TURNED ON
a = 0b11101110
mask = 0b11111111 
print bin(a ^ mask)

#WITH 1s BIT BEING 1ST BIT, FLIPPED THE n BIT AND RETURNED RESULT
def flip_bit(number, n):
    mask = (0b1 << (n-1))
    result = number ^ mask
    return bin(result)

print flip_bit(0b10000, 4)
