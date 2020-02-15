import random
import string

letters_of_password = int(input("How many letters do you want in your password?: "))
numbers_of_password = int(input("How many numbers do you want in your password?: "))
specialdigits_of_password = int(input("How many special digits do you want in your password?: "))

number_list = ''.join(random.choice(string.digits) for i in range(numbers_of_password))
letter_list = ''.join(random.choice(string.ascii_letters) for i in range(letters_of_password))
special_list = ''.join(random.choice(string.punctuation) for i in range(specialdigits_of_password))

syntax_list = letter_list + number_list + special_list
if len(syntax_list) < 6:
    print("Your password needs to be more than 6 characters long")
    exit()

result = random.sample(syntax_list, len(syntax_list))

password = ''.join(result)
print("Your password is {0}".format(password))