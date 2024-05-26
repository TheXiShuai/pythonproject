# fruits = {'guava', 'coconut', 'banana'}
# print(fruits)

# for fruit in fruits:
#     print(f"Fruit: {fruit}")



# ACCESS DICTIONARY ITEMS

# my_dict = { "name" : "Hector", "age": 36, "city": "Taipei"}

# name = my_dict["name"]
# age = my_dict["age"]
# city = my_dict["city"]

# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"City: {city}")



# # ACCESS TUPLE ITEMS

# artists = ("Anuel", "Rick", "Jhayco")

# first_artist = artists[0]

# print(first_artist)


# REMOVE AND ADD ITEMS LIST
# fruits = ['guava', 'coconut', 'banana']
# fruits.append("mango")
# fruits+= ["pineaple"]
# print(fruits)

# fruits.remove("coconut")
# print(fruits)
# del fruits[2]
# print(fruits)

# REMOVE AND ADD ITEMS DICTIONARY
# employee_info = {'name': 'Hector', 'position': 'engineer'}
# print(f"Original dictionary:", employee_info)

# employee_info['salary']= 500000
# employee_info['department'] = 'IT'
# print(employee_info)

# removed_info = employee_info.pop('position')
# print(employee_info)



# ADD REMOVE SET ITEMS
# fruits = {'guava', 'coconut', 'banana'}
# fruits.add("mango")
# print(fruits)

# fruits.discard("guava")
# print(fruits)



# ASSIGN MULTIPLE VALUES
# list=[1,2,3]
# a, b, c = list
# print(a, b, c)


# CHANGE UPDATE DICTIONARY

# employee_info = {'name': 'Hector', 'position': 'engineer'}
# print(f"Original dictionary:", employee_info)

# employee_info['position'] = "scientist"
# print(employee_info)


# CHANGE LIST ITEMS

# fruits = ['guava', 'coconut', 'banana']
# fruits[0] = 'apple'
# print(fruits)

# numbers = [1,2,3,4,5,6,7,8,9]
# numbers[2:6] = [20,30,40,50]
# print(numbers)

# DATA TYPES
# person = {"name": "Robert", "age" : 40 }
# profession =["engineer", "driver"]

# print(type(person))
# print(type(profession))


# CLASSES AND OBJECTS

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def bark(self):
#         print(f"{self.name} says woof!")

# my_dog = Dog(name="Rocky", age=3)
# print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
# my_dog.bark()



# ARGUMENTS AND PARAMETERS


# def display_info(name, age, **kwargs):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
    
#     for key, value in kwargs.items():
#         print(f"{key.capitalize()}: {value}")

# display_info(name="Thomas", age=56, occupation="engineer", city="Taipei")


# LOOP SETS
# fruits = ['guava', 'coconut', 'banana']

# for fruit in fruits:
#     print(f"fruit:{fruit}" )


# LOOP TUPLES

# this_tuple = ('guava', 'coconut', 'banana')

# for _ in range(len(this_tuple)):
#     print(this_tuple[_])
    
# i = 0

# while i < len(this_tuple):
#     print(this_tuple[i])
#     i = i + 1


# NESTED DICTIONARIES

# playstation_games = {
#     'The Last of Us Part II': {
#         'genre': 'Action-adventure',
#         'price': 59.99
#     },
#     'God of War': {
#         'genre': 'Action-adventure',
#         'price': 19.99
#     },
#     'Spider-Man: Miles Morales': {
#         'genre': 'Action',
#         'price': 49.99
#     }
# }

# genre_of_the_year = playstation_games['God of War']['genre']
# print(f"genre of the year: {genre_of_the_year}")


# REGULAR EXPRESSION to find THE POSITION AND MATCH OF WORDS

# import re
# text = "if you wanna be a fighter you gotta train like one"

# match_result = re.search(r"fighter", text)

# if match_result:
#     print(f"pattern 'fighter' found at text variable {match_result.start()}")
# else:
#     print("pattern 'fighter' not found")


# SET METHODS add and remove

# fruits = {'guava', 'coconut', 'banana'}

# fruits.add("durian")
# print(fruits)

# fruits.remove("guava")
# print(fruits)


#SLICING

# text = "if you wanna be a fighter you gotta train like one"
# substring = text[6:25]
# print(substring)

# reversed_phrase = text[::-1]
# print(reversed_phrase)

# text_length = len(text)
# print(text_length)


#REPLACE METHOD
# text = "if you wanna be a fighter you gotta train like one"
# modified_text = text.replace('fighter','player')
# splitted = text.split()
# print(text)
# print(modified_text)
# print(splitted)















    
    




