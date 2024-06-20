# A recipe you are reading states how many grams you need for the ingredient. 
#Unfortunately, your store only sells items in ounces. 
#Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def to_ounces(grams):
    return grams * 28.3495231


# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
#The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def to_celcium(F):
     return 5/9*(F-32)


# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    # Equation 1: chickens + rabbits = numheads
    # Equation 2: 2 * chickens + 4 * rabbits = numlegs
    
    # Rewrite equation 1 to express chickens in terms of rabbits
    # chickens = numheads - rabbits
    # Substitute into equation 2
    # 2 * (numheads - rabbits) + 4 * rabbits = numlegs
    
    # Simplify and solve for rabbits
    # 2 * numheads - 2 * rabbits + 4 * rabbits = numlegs
    # 2 * numheads + 2 * rabbits = numlegs
    # 2 * rabbits = numlegs - 2 * numheads
    # rabbits = (numlegs - 2 * numheads) / 2
    
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    
    if rabbits >= 0 and chickens >= 0 and rabbits == int(rabbits) and chickens == int(chickens):
        return int(chickens), int(rabbits)
    else:
        return "No valid solution"


# You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):

    return list(filter(lambda x: is_prime(x), numbers))


# Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations

def print_permutations(s):
    perm = permutations(s)
    for permutaion in perm:
        print(''.join(permutaion))


# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(input_sentence)
print("Reversed sentence:", reversed_sentence)



# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
has_33([1, 3, 3]) #→ True
has_33([1, 3, 1, 3]) #→ False
has_33([3, 1, 3]) #→ False


def spy_game(nums):
    found_0 = False
    found_00 = False
    for num in nums:
        if num == 0 and not found_0:
            found_0 = True
        elif num == 0 and found_0 and not found_00:
            found_00 = True
        elif num == 7 and found_0 and found_00:
            return True
        
    return False

print(spy_game([1,2,4,0,0,7,5]))   # True
print(spy_game([1,0,2,4,0,5,7]))   # True
print(spy_game([1,7,2,0,4,5,0]))   # False

#Write a function that computes the volume of a sphere given its radius.

def volume(radius):
    return 4/3*3.14*radius**3

def unique_elements(input_list):
    unique_list = []
    
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    
    return 

def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]

def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])

import random

def guess_the_number():

    secret_number = random.randint(1, 20)
    guesses_taken = 0
    
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break  
    
    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")

guess_the_number()

#Create a python file and import some of the functions from the above 13 tasks and try to use them.








