import random
import string

def recursive_function():
 letters_of_password = int(input("How many letters do you want in your password?: "))
 numbers_of_password = int(input("How many numbers do you want in your password?: "))
 specialdigits_of_password = int(input("How many special digits do you want in your password?: "))

 number_list = ''.join(random.choice(string.digits) for i in range(numbers_of_password))
 letter_list = ''.join(random.choice(string.ascii_letters) for i in range(letters_of_password))
 special_list = ''.join(random.choice(string.punctuation) for i in range(specialdigits_of_password))

 syntax_list = number_list + letter_list + special_list

 if len(syntax_list) < 6:
    print("Your password needs to be atleast six characters")
    return recursive_function()
 return syntax_list

syntax_list = recursive_function() 

result = random.sample(syntax_list, len(syntax_list))
password = ''.join(result)
print("Your password is {0}".format(password))

 




