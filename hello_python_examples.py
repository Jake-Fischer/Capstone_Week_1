print('Hello World!')

#variables
#Lowercase, joined with underscores

school = 'MCTC'
gpa = 3.7
students = 22

#if statements
if gpa == 4:
    print("Wow!")
else:
    print('Cool!')

#if-elif-else

#lists
schools = ['MCTC', "DCTC", "NDSU"]

schools.sort()
print(schools)

schools.append('Century College')

schools.reverse()
print(schools)

#in operator
if 'MCTC' in schools:
    print("MCTC is a school in the list!")

#strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split())

if 'Capstone' in class_name:
    print("This must be the capstone.")

#loops for loops over range
for x in range(10):
    print(x)

#loops for over sequence
for s in schools:
    print(s.upper())

for letter in school:
    print(letter)

for letter in school:
    print(letter * 10)

#while loops

# name = input('Enter your name:')

# while not name:
#     print('Please enter at least one character')
#     name = input('Enter your name')

#True and False and None
start_of_semester = True
winter = False

if winter:
    print('brrrr')
else:
    print('its not winter.')

#Dictionaries

class_codes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)

#String formatting
for code, name in class_codes.items():
    print(f'The class code is {code} and the name is {name}')

#Slicing strings, lists

schools = ['MCTC', "DCTC", "NDSU"]
first_two = schools[:2]
print(first_two)

last_school = schools[-1]
print(last_school)

last_two = schools[-2:]
print(last_two)

school_name = 'Minneapolis Comunity and Technical College'
city = school_name[:11]
print(city)

#file IO
#Read
with open('data.txt') as f:
    print(f.read())
#Write
with open('data.txt', 'w') as f:
   f.writelines(schools)

#functions

def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is: ')
    return name

name = get_name()