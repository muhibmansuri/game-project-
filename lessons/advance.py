#1.local variables
#FUNCTION KE ANDER banaya hua variable sirf usi FUNCTION ke andar access ho sakta hai.
def function1():
    a = 10
    b = 20
    print("Inside Function1:", a + b)   
function1()

def function():
    a=4
    b=7
    print("Inside Function:",a+b)
function()
# print(a+b) # This will raise an error because 'a' and 'b' are local variables
# print(a)  # This will raise an error because 'a' is not defined outside the function      
#FUNCTION KE ANDER banaya hua variable sirf usi FUNCTION ke andar access ho sakta hai.  
# print(b)  # This will raise an error because 'b' is not defined outside the function
#local variables    
def function2():
    x = 5
    y = 15
    print("Inside Function2:", x * y)   
function2()
# print(x)  # This will raise an error because 'x' is not defined outside the function      
# print(y)  # This will raise an error because 'y' is not defined outside the function

#2.global variables
#FUNCTION KE BAHAR banaya hua variable poore PROGRAM mein kahi bhi access ho sakta hai.
p = 50
q = 100 
def function3():
    print("Inside Function3:", p - q)   
function3()
print("Outside Function3:", p)  # This will work because 'p' is a global variable     
print("Outside Function3:", q)  # This will work because 'q' is a global variable       
#FUNCTION KE BAHAR banaya hua variable poore PROGRAM mein kahi bhi access ho sakta hai.

#3globle keyword
#FUNCTION KE ANDER agar hum kisi GLOBAL VARIABLE ki VALUE CHANGE karna chahte hain to humein 'global' keyword ka use karna padta hai.
m = 200     
def function4():
    global m
    m = 300  # Changing the value of global variable 'm'
    print("Inside Function4:", m)
function4()
print("Outside Function4:", m)  # This will reflect the changed value of 'm'
print(m)
#4nonlocal keyword
#NESTED FUNCTION KE ANDER agar hum kisi OUTER FUNCTION ke VARIABLE ki VALUE CHANGE karna chahte hain to humein 'nonlocal' 
# keyword ka use karna padta hai.

def outer_function():
    n = 400     
    def inner_function():
        nonlocal n
        n = 500  # Changing the value of outer function's variable 'n'
        print("Inside Inner Function:", n)
    inner_function()
    print("Inside Outer Function:", n)
outer_function()
# print(n) # NameError: 'n' is not defined globally


#lecture 22 recursion in python
#RECURSION tab hoti hai jab ek FUNCTION khud ko hi CALL karta hai.
def recursive_function(count):
    if count > 0:
        print("Recursion Count:", count)
        recursive_function(count - 1)  # Recursive call
    else:
        print("Recursion ends here.")
recursive_function(10)  # Initial call with count 5
#RECURSION tab hoti hai jab ek FUNCTION khud ko hi CALL karta hai.
recursive_function(-1)  # Initial call with count -1 to show base case handling

#full easy explanation of recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call       
print("Factorial of 5:", factorial(5))  # Output: 120

print("Factorial of 0:", factorial(0))  # Output: 1 # Base case handling    
#next explanation of recursion

print("Factorial of 1:", factorial(1))


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calls
print("Fibonacci of 6:", fibonacci(6)) 

# Output: 8
#kyu output 8 aaya
#fibonacci series hota hai 0,1,1,2,3,5,8,13,21
#0->fibonacci(0)=0
#1->fibonacci(1)=1          
#2->fibonacci(2)=fibonacci(1)+fibonacci(0)=1+0=1
#3->fibonacci(3)=fibonacci(2)+fibonacci(1)=1+1=2
#4->fibonacci(4)=fibonacci(3)+fibonacci(2)=2               
#5->fibonacci(5)=fibonacci(4)+fibonacci(3)=3+2=5
#6->fibonacci(6)=fibonacci(5)+fibonacci(4)=5+3=8
print("Fibonacci of 0:", fibonacci(0))  # Output: 0 # Base case handling
#why use recursion
#1.Simplicity: Recursion can simplify code for problems that have a natural recursive structure, making it easier to read and maintain.
#2.Reduction of Code Size: Recursive solutions can often be more concise than their iterative counterparts, reducing the amount of code needed to solve a problem.
#3.Problem Solving: Some problems, such as tree traversals and combinatorial problems   , are more naturally solved using recursion.
#4.Divide and Conquer: Recursion is a key technique in divide-and-conquer algorithms, which break problems into smaller subproblems.
#
#mostly kiss chiz ke liye use hota hai
#Recursion is commonly used for problems involving: 
#1.Tree Traversals: Navigating hierarchical data structures like trees.
#2.Graph Traversals: Exploring nodes and edges in graphs.   
#3.Combinatorial Problems: Generating permutations, combinations, and subsets.
#4.Divide and Conquer Algorithms: Such as quicksort and mergesort.
#5.Dynamic Programming: Solving problems by breaking them down into simpler subproblems.
#6.Factorial Calculation: Computing the factorial of a number.
#7.Fibonacci Sequence: Generating Fibonacci numbers.

#advantage and disadvantage of recursion
#Advantages:    
#1.Simplicity: Recursive solutions can be simpler and more elegant for problems with a natural recursive structure.
#2.Code Reduction: Recursion can lead to shorter code compared to iterative solutions.      
#3.Problem Solving: Some problems are more easily solved using recursion, such as tree traversals and combinatorial problems.
#Disadvantages: 
#1.Memory Usage: Each recursive call adds a new layer to the call stack, which can lead to high memory consumption and stack overflow for deep recursions.      
#2.Performance: Recursive solutions can be slower than iterative ones due to the overhead of multiple function calls.
#3.Complexity: Understanding and debugging recursive code can be more challenging, especially for those unfamiliar with the concept.
#4.Limited by Stack Size: Most programming languages have a limit on the call stack size, which can restrict the depth of recursion.
#In summary, recursion is a powerful tool for certain types of problems, but it should be used judiciously, considering its advantages and disadvantages.       

#example of basic recursion to advanced recursion for students
#Basic Recursion Example: Factorial Calculation 
#q1-q10 name likho program karo sath me 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)     
print("Factorial of 5:", factorial(5))  # Output: 120           
#Intermediate Recursion Example: Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)      
print("Fibonacci of 6:", fibonacci(6))  # Output: 8

# #Advanced Recursion Example: Tower of Hanoi 
# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, target, source)
# tower_of_hanoi(3, 'A', 'C', 'B')  # Move 3 disks from A to C using B as auxiliary
#In this progression, we start with a simple factorial calculation, move to the Fibonacci sequence, 
# and finally tackle the more complex Tower of Hanoi problem, demonstrating increasing levels of recursion complexity.

##advanced recursion example : tower of hanoi with explanation in details for beginors

#Tower of Hanoi is a classic problem that involves moving a set of disks from one peg to another,
# following specific rules. The objective is to move all the disks from the source peg to the target peg            
# using an auxiliary peg as a temporary holding area. 
# The rules are:            
#1.Only one disk can be moved at a time.
#2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty peg.
#3.No larger disk may be placed on top of a smaller disk.           
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)    
tower_of_hanoi(4, 'A', 'C', 'B')  # Move 3 disks from A to C using B as auxiliary


#lecture 23
#list comprehension in python
#list comprehension kya hai?
#answer
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.     
#List comprehension is a concise way to create lists in Python. It allows you to generate a
#Syntax: [expression for item in iterable if condition == True]

#Example 1: Basic List Comprehension
#Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print("Squares:", squares)

#Example 2: List Comprehension with Condition
#Create a list of even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
print("Even Numbers:", evens)

#Example 3: Comparison with traditional For Loop
#Without List Comprehension
numbers = [1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print("Doubled (Loop):", doubled)

#With List Comprehension
doubled_comp = [n * 2 for n in numbers]
print("Doubled (Comp):", doubled_comp)

#Example 4: List Comprehension with String manipulation
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if "a" in x]
print("Fruits with 'a':", newlist)
#list comprehension is a concise way to create lists in python. 
#It combines loops and conditional statements into a single line of code, making it more readable and efficient.    
#It is especially useful for transforming or filtering data in lists.
#List comprehension can also be used with other data types like sets and dictionaries,
# but it is most commonly associated with lists.    
#Example 5: Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)
#Example 6: List Comprehension with Function
def square(x):      
    return x * x
square(85)
 
squared_list = [square(x) for x in range(10)]
print("Squared List using Function:", squared_list)  


#Example 7: List Comprehension with Multiple Conditions 
numbers = range(20)
print(numbers)
filtered_numbers = [x for x in numbers if x % 2 == 0 if x   % 3 == 0]           
print("Numbers divisible by 2 and 3:", filtered_numbers)

#Example 8: List Comprehension with String Manipulation
words = ["hello", "world", "python", "is", "awesome"]
capitalized_words = [word.capitalize() for word in words]       
print("Capitalized Words:", capitalized_words)

#Example 9: List Comprehension with Dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
squared_dict = {key: value**2 for key, value in original_dict.items()}      
print("Squared Dictionary:", squared_dict)  

#Lecture 25: Iterators and Generators  
#Iterators in Python        
#An iterator is an object that contains a countable number of values and can be iterated upon, meaning you can traverse through all the values.
#In Python, an iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
#The __iter__() method returns the iterator object itself and is used in cases where an
# iterable needs to be iterated multiple times.
#The __next__() method returns the next value from the iterator. When there are no  
#more values to return, it raises the StopIteration exception to signal the end of the iteration.
#Creating an Iterator   
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
my_iter = MyIterator(5)
for num in my_iter: 
    print("Iterator Value:", num)   
#Generators in Python
#A generator is a special type of iterator that is defined using a function rather than a class
#Generators use the yield statement to produce a series of values over time, instead of returning them all at once.
def my_generator(limit):
    current = 0
    while current < limit:
        yield current
        current += 1
gen = my_generator(5)
for num in gen:
    print("Generator Value:", num)
        
#example input function use,while loop ,range ,squre function,nagative number square ko positive answer ana chahiye, list using function
while True:     
    i =int( input("Enter only positive number:"))
    if i==0:
        break
    print("You entered:", i)
    
    def square(i):      
        return abs(i) * abs(i)
    square(i)
    if i<0:
        print("Please enter only positive number")
        continue
    squared_list = [square(i) for i in range(i)]
    print("Squared List using Function:", squared_list)     
#example input function use,while loop ,range ,squre function,nagative number square ko positive answer ana chahiye, list using function


#Lecture 26: JSON in Python
#JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write.
#It is widely used for data exchange between a server and a web application.
#In Python, we use the built-in 'json' module to work with JSON data.

import json

#1. JSON Serialization (Converting Python Objects to JSON String)
#We use json.dumps() to convert a Python object (like a dictionary) into a JSON string.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
print(data)
json_string = json.dumps(data, indent=4) # indent parameter adds formatting for readability
print("JSON String:", json_string)
#Note: True becomes true, None becomes null in JSON.

#2. JSON Deserialization (Converting JSON String to Python Objects)
#We use json.loads() to convert a JSON string into a Python dictionary.
json_data = '{"name": "Rahim", "age": 25, "city": "Delhi"}'
python_dict = json.loads(json_data)
print("Python Dictionary:", python_dict)
print("Name:", python_dict["name"])
print("Age:", python_dict["age"])
print("City:", python_dict["city"]) 
print("Courses:", data["courses"])
print("Is Student:", data["is_student"]) 

#3. Reading and Writing JSON to a File
#json.dump() writes Python data to a JSON file.
#json.load() reads JSON data from a JSON file.

#Writing to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("\nData successfully written to data.json")

#Reading from a file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print("Data read from file:", loaded_data)

#Example 4: Advanced JSON Formatting (sort_keys and separators)
#We can use 'sort_keys=True' to sort the keys alphabetically.
#We can use 'separators' to control the separators used (default is (', ', ': ')).
#separators=(',', ':') removes whitespace, making the JSON string compact.

compact_json = json.dumps(data, separators=(',', ':'), sort_keys=True)
print("\nCompact and Sorted JSON:", compact_json)

#Example 5: Serializing Custom Objects (Classes)
#By default, the json module cannot serialize custom classes.
#We need to convert the object into a dictionary first.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student = Student("Zaid", 20, "A")

# json.dumps(student) # This would raise a TypeError

# Solution: Use the 'default' parameter with a function that returns the object's __dict__
def encode_student(obj):
    if isinstance(obj, Student):
        return obj.__dict__
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

student_json = json.dumps(student, default=encode_student, indent=4)
print("\nSerialized Student Object:", student_json)

 
#Example 1: JSON Serialization with Custom Sorting
#We can sort the dictionary keys while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_json_string = json.dumps(data, indent=4, sort_keys=True)
print("Sorted JSON String:", sorted_json_string)

#Example 2: JSON Serialization with Custom Indentation
#We can control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
indented_json_string = json.dumps(data, indent=4)
print("Indented JSON String:", indented_json_string)

#Example 3: JSON Serialization with Custom Formatting
#We can control the formatting of the JSON string while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
formatted_json_string = json.dumps(data, indent=4, sort_keys=True, separators=(",", ": "))
print("Formatted JSON String:", formatted_json_string)

#Example 4: JSON Serialization with Custom Sorting and Indentation
#We can sort the dictionary keys and control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_indented_json_string = json.dumps(data, indent=4, sort_keys=True)
print("Sorted Indented JSON String:", sorted_indented_json_string)

#Example 5: JSON Serialization with Custom Sorting and Indentation
#We can sort the dictionary keys and control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_indented_json_string = json.dumps(data, indent=4, sort_keys=True)
print("Sorted Indented JSON String:", sorted_indented_json_string)

#Example 6: JSON Serialization with Custom Sorting and Indentation
#We can sort the dictionary keys and control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_indented_json_string = json.dumps(data, indent=4, sort_keys=True)
print("Sorted Indented JSON String:", sorted_indented_json_string)

#Example 7:JSON API Integration
#We can use the requests library to make API calls and work with JSON data.
import requests
response = requests.get("https://api.github.com")
data = response.json()
print("GitHub API Response:", data) 





#lecture:28 
#datetime module

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

meeting_time = datetime.datetime(2025, 9, 20, 14, 30, 0) 
print("Meeting:", meeting_time) 
# Extract individual components 
print("Year:", meeting_time.year) 
print("Month:", meeting_time.month) 
print("Hour:", meeting_time.hour) 
print("Minute:", meeting_time.minute) 
print("Second:", meeting_time.second) 
print("Microsecond:", meeting_time.microsecond)    
#convert datetime to string     
meeting_time_string = meeting_time.strftime("%Y-%m-%d %H:%M:%S") 
print("Meeting Time String:", meeting_time_string)       

#Lecture 27: Working with JSON 
# JSON (JavaScript Object Notation) 
# is a lightweight, human-readable data interchange format widely used for 
# transmitting data between a server and a web application. Python has a built
# in json module that provides powerful tools for working with JSON data, 
# including serializing and deserializing data. 

#Serialization :     
#Serialization is the process of converting an object into a format that can be easily stored or transmitted.   

#Deserialization : 
#Deserialization is the process of converting a serialized object back into its original form.      
#json function 
#json.dumps() : 
#json.dumps() is a function that converts a Python object into a JSON string.
#json.loads() : 
#json.loads() is a function that converts a JSON string into a Python object.
#json.load() : 
#json.load() is a function that reads a JSON file and converts it into a Python object.
#json.dump() : 
#json.dump() is a function that writes a Python object to a JSON file.
#   
import json

#Example 1: JSON Serialization (Converting Python Objects to JSON)
#We can use json.dumps() to convert Python objects into a JSON string.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
print("Python Object:", data) # print the Python object   
json_string = json.dumps(data, indent=8) # indent parameter adds formatting for readability
print("JSON String:", json_string) # print the JSON string
#Note: True becomes true, None becomes null in JSON.        

#Example 2: JSON Deserialization (Converting JSON String to Python Objects)
#We can use json.loads() to convert a JSON string into a Python dictionary.
json_data = '{"name": "Rahim", "age": 25, "city": "Delhi"}'
python_dict = json.loads(json_data) # convert JSON string to Python dictionary  
print("Python Dictionary:", python_dict) # print the Python dictionary
print("Name:", python_dict["name"]) # access the name value
print("Age:", python_dict["age"]) # access the age value
print("City:", python_dict["city"]) # access the city value
print("Courses:", data["courses"]) # access the courses value
print("Is Student:", data["is_student"]) # access the is_student value

#example 3: JSON Serialization with Custom Sorting  
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_json_string = json.dumps(data, indent=4, sort_keys=True) # sort_keys=True sorts the dictionary keys alphabetically
print("Sorted JSON String:", sorted_json_string) 

#Example 4: JSON Serialization with Custom Indentation
#We can control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
indented_json_string = json.dumps(data, indent=4) # indent parameter controls the indentation level
print("Indented JSON String:", indented_json_string) 

#Example 5: JSON Serialization with Custom Formatting
#We can control the formatting of the JSON string while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
formatted_json_string = json.dumps(data, indent=4, sort_keys=True, separators=(",", ": ")) # separators parameter controls the separators used
print("Formatted JSON String:", formatted_json_string)      

#Example 6: JSON Serialization with Custom Sorting and Indentation
#We can sort the dictionary keys and control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_indented_json_string = json.dumps(data, indent=4, sort_keys=True) # sort_keys=True sorts the dictionary keys alphabetically, indent parameter controls the indentation level
print("Sorted Indented JSON String:", sorted_indented_json_string) 

# next example :
# new example
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()   # Bark

cat = Cat()
cat.sound()   # Meow


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog=Dog()
dog.sound()

class Cat(Animal):
    def sound(self):
        print("Meow")

cat=Cat()
cat.sound()

class Goat(Animal):
    def sound(self):
        print("Meh")

got=Goat()
got.sound()

dog.sound()
cat.sound()
got.sound() 

encapsulation
#Encapsulation is the process of hiding the internal implementation details of a class from the outside world. It is a way of protecting the data from being modified by unauthorized code. It is a way of restricting access to the data by using access modifiers.    
#Encapsulation is a way of restricting access to the data by using access modifiers.          
#example 1:     
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(2200)
print(account.get_balance())

#polymorphism
#Polyphormism is the ability of an object to take on many forms. It is a way of achieving polymorphism 
# by using method overloading and method overriding.    
#Method overloading is the ability of a class to have multiple methods with the same name but different parameters.    
#Method overriding is the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass.    

#example 1: Method Overloading      
def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3))

#example 2: Method Overriding      
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()  # Bark 

#example 3: Method Overriding      
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()  # Bark 

class Cat(Animal):
    def sound(self):
        print("Meow")

cat = Cat()
cat.sound()  # Meow 

#magic method
#Magic methods are special methods that are automatically called by Python when a certain operation is performed on an object. They are also known as dunder methods because they use double underscores (__) as prefix and suffix.    
#example 1: Magic Method      
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(p)  # (1, 2)

#example 2: Magic Method      
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(p)  # (1, 2)


#Lecture 27: Working with JSON 
# JSON (JavaScript Object Notation) 
# is a lightweight, human-readable data interchange format widely used for 
# transmitting data between a server and a web application. Python has a built
# in json module that provides powerful tools for working with JSON data, 
# including serializing and deserializing data. 

#Serialization :     
#Serialization is the process of converting an object into a format that can be easily stored or transmitted.   

#Deserialization : 
#Deserialization is the process of converting a serialized object back into its original form.      
#json function 
#json.dumps() : 
#json.dumps() is a function that converts a Python object into a JSON string.
#json.loads() : 
#json.loads() is a function that converts a JSON string into a Python object.
#json.load() : 
#json.load() is a function that reads a JSON file and converts it into a Python object.
#json.dump() : 
#json.dump() is a function that writes a Python object to a JSON file.
#   
import json

#Example 1: JSON Serialization (Converting Python Objects to JSON)
#We can use json.dumps() to convert Python objects into a JSON string.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
print("Python Object:", data["courses"][0]) # print the Python object   
json_string = json.dumps(data, indent=4) # indent parameter adds formatting for readability
print("JSON String:", json_string) # print the JSON string
#Note: True becomes true, None becomes null in JSON.        

#Example 2: JSON Deserialization (Converting JSON String to Python Objects)
#We can use json.loads() to convert a JSON string into a Python dictionary.
json_data = '{"name": "Rahim", "age": 25, "city": "Delhi"}'
python_dict = json.loads(json_data) # convert JSON string to Python dictionary  
print("Python Dictionary:", python_dict) # print the Python dictionary
print("Name:", python_dict["name"]) # access the name value
print("Age:", python_dict["age"]) # access the age value
print("City:", python_dict["city"]) # access the city value
print("Courses:", data["courses"]) # access the courses value
print("Is Student:", data["is_student"]) # access the is_student value

#example 3: JSON Serialization with Custom Sorting  
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_json_string = json.dumps(data, indent=4, sort_keys=True) # sort_keys=True sorts the dictionary keys alphabetically
print("Sorted JSON String:", sorted_json_string) 

#Example 4: JSON Serialization with Custom Indentation
#We can control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
indented_json_string = json.dumps(data, indent=4) # indent parameter controls the indentation level
print("Indented JSON String:", indented_json_string) 

#Example 5: JSON Serialization with Custom Formatting
#We can control the formatting of the JSON string while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
formatted_json_string = json.dumps(data, indent=4, sort_keys=True, separators=(",", ": ")) # separators parameter controls the separators used
print("Formatted JSON String:", formatted_json_string)      

#Example 6: JSON Serialization with Custom Sorting and Indentation
#We can sort the dictionary keys and control the indentation level while serializing to JSON.
data = {
    "name": "Muhib",
    "age": 22,
    "city": "Mumbai",
    "is_student": True,
    "courses": ["Python", "Data Science"]
}
sorted_indented_json_string = json.dumps(data, indent=4, sort_keys=True) # sort_keys=True sorts the dictionary keys alphabetically, indent parameter controls the indentation level
print("Sorted Indented JSON String:", sorted_indented_json_string) 

muhib={"student_id": 101, "info": {"name": "Muhib", "hobbies": ["Coding", "Reading", "Gaming"]}, "is_active": True}
print("Muhib:", muhib)
json.dumps(muhib)   # convert Python object to JSON string
print("JSON String:", json.dumps(muhib)) # print the JSON string    