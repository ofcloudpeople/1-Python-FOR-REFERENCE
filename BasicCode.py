#CHECK IF A NUMBER IS EVEN:
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#CHECK IF IT’S AN INTEGER:
def is_int(n):
    if n == int(n):
        return True
    else:
        return False

#CHECK SUM OF A DIGIT:
def digit_sum(n):
    result = 0
    while n:
        result += n % 10
        n /= 10
    return result

#CHECK IF A FACTORIAL:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#CHECK IF A PRIME:
def is_prime(n):
    if n < 2:
        return False
    elif n == 2: 
        return True
    else:
        for num in range(2, n):
            if n % num == 0:
                return False
        return True

#REVERSE THE ORDER OF A WORD (WITHOUT REVERSE FUNCTION):
def reverse(text):
    result = ''
    for c in text:
        result = c + result
    return result

print reverse('Python!')

#LOOP TO REMOVE VOWELS USING REPLACE():
def anti_vowel(text):
    result = text
    for c in text:
        if c in "aeiouAEIOU":
            result = result.replace(c, '')
    return result

RETURN TOTAL SCRABBLE SCORE FROM LIBRARY
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total= 0
    for n in word.lower():
        total += score[n]
    return total

#REPLACE ASTERIKS WITH WORD CHOSEN
def censor(text, word):
    return text.replace(word, '*'*len(word))

#RETURN NUMBER OF TIMES THE ITEM OCCURS IN THE LIST
def count(sequence, item):
    result = 0
    for n in sequence:
        if n == item:
            result += 1
    return result

#REMOVE ODD NUMBERS FROM LIST
## Note: similar to keeping even numbers
def purify(list): 
    result = []
    for n in list:
        if n % 2 == 0:
            result.append(n)
    return result

#PRODUCT OF A LIST
def product(list):
    result = 1
    for n in list:
        result *= n
    return result

#REMOVE DUPLICATES FROM LIST
def remove_duplicates(list):
    result = []
    for n in list:
        if n not in result:
            result.append(n)
    return result

#FIND MEDIAN OF A LIST
def median(list):
    result = sorted(list)
    length = len(result)
    if not length % 2:
        return (result[length/2] + result[length/2-1]) / 2.0
    return result[length/2]
