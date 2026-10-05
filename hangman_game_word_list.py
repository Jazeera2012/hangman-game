# Python Dictionary Game
# Python Terms Database


python_terms = {

    # =========================
    # BASICS
    # =========================

    "variable": {
        "definition": "A name used to store or refer to a value.",
        "example": "name = 'Jazeera'",
        "category": "Basics",
        "difficulty": "Easy"
    },

    "operator": {
        "definition": "A symbol used to perform an operation on values.",
        "example": "5 + 3",
        "category": "Basics",
        "difficulty": "Easy"
    },

    "comparison operator": {
        "definition": "An operator used to compare two values.",
        "example": "5 > 3",
        "category": "Basics",
        "difficulty": "Easy"
    },

    "logical operator": {
        "definition": "An operator used to combine or modify conditions.",
        "example": "age > 18 and has_id",
        "category": "Basics",
        "difficulty": "Medium"
    },

    "modulo": {
        "definition": "An operator that returns the remainder after division.",
        "example": "10 % 3",
        "category": "Basics",
        "difficulty": "Easy"
    },


    # =========================
    # DATA TYPES
    # =========================

    "string": {
        "definition": "A sequence of characters surrounded by quotation marks.",
        "example": "name = 'Jazeera'",
        "category": "Data Types",
        "difficulty": "Easy"
    },

    "integer": {
        "definition": "A whole number without a decimal point.",
        "example": "age = 16",
        "category": "Data Types",
        "difficulty": "Easy"
    },

    "float": {
        "definition": "A number that contains a decimal point.",
        "example": "price = 19.99",
        "category": "Data Types",
        "difficulty": "Easy"
    },

    "boolean": {
        "definition": "A data type that has only True or False values.",
        "example": "is_student = True",
        "category": "Data Types",
        "difficulty": "Easy"
    },


    # =========================
    # DATA STRUCTURES
    # =========================

    "list": {
        "definition": "An ordered collection that can store multiple values.",
        "example": "fruits = ['apple', 'banana']",
        "category": "Data Structures",
        "difficulty": "Easy"
    },

    "tuple": {
        "definition": "An ordered collection that cannot be changed after creation.",
        "example": "coordinates = (10, 20)",
        "category": "Data Structures",
        "difficulty": "Medium"
    },

    "dictionary": {
        "definition": "A collection that stores data in key-value pairs.",
        "example": "student = {'name': 'Jazeera'}",
        "category": "Data Structures",
        "difficulty": "Easy"
    },

    "set": {
        "definition": "An unordered collection that stores unique values.",
        "example": "numbers = {1, 2, 3}",
        "category": "Data Structures",
        "difficulty": "Medium"
    },


    # =========================
    # CONDITIONS
    # =========================

    "if": {
        "definition": "A statement used to execute code when a condition is true.",
        "example": "if age >= 18:",
        "category": "Conditions",
        "difficulty": "Easy"
    },

    "elif": {
        "definition": "A statement used to check another condition if the previous condition was false.",
        "example": "elif age >= 13:",
        "category": "Conditions",
        "difficulty": "Easy"
    },

    "else": {
        "definition": "A statement used when all previous conditions are false.",
        "example": "else:",
        "category": "Conditions",
        "difficulty": "Easy"
    },

    "condition": {
        "definition": "An expression that evaluates to True or False.",
        "example": "age >= 18",
        "category": "Conditions",
        "difficulty": "Easy"
    },


    # =========================
    # LOOPS
    # =========================

    "for loop": {
        "definition": "A loop used to repeat code for each item in a sequence.",
        "example": "for item in items:",
        "category": "Loops",
        "difficulty": "Easy"
    },

    "while loop": {
        "definition": "A loop that continues running while a condition is true.",
        "example": "while score < 100:",
        "category": "Loops",
        "difficulty": "Easy"
    },

    "break": {
        "definition": "A statement used to immediately stop a loop.",
        "example": "if number == 5: break",
        "category": "Loops",
        "difficulty": "Easy"
    },

    "continue": {
        "definition": "A statement used to skip the current iteration of a loop.",
        "example": "if number == 5: continue",
        "category": "Loops",
        "difficulty": "Medium"
    },

    "range": {
        "definition": "A function used to generate a sequence of numbers.",
        "example": "range(5)",
        "category": "Loops",
        "difficulty": "Easy"
    },


    # =========================
    # FUNCTIONS
    # =========================

    "function": {
        "definition": "A reusable block of code designed to perform a specific task.",
        "example": "def greet():",
        "category": "Functions",
        "difficulty": "Easy"
    },

    "parameter": {
        "definition": "A variable listed in a function definition.",
        "example": "def greet(name):",
        "category": "Functions",
        "difficulty": "Medium"
    },

    "argument": {
        "definition": "A value passed to a function when the function is called.",
        "example": "greet('Jazeera')",
        "category": "Functions",
        "difficulty": "Medium"
    },

    "return": {
        "definition": "A statement used to send a value back from a function.",
        "example": "return total",
        "category": "Functions",
        "difficulty": "Easy"
    },

    "default parameter": {
        "definition": "A parameter that already has a value if no argument is provided.",
        "example": "def greet(name='User'):",
        "category": "Functions",
        "difficulty": "Medium"
    },


    # =========================
    # INPUT / OUTPUT
    # =========================

    "input": {
        "definition": "A function used to receive text entered by the user.",
        "example": "name = input('Name: ')",
        "category": "Input / Output",
        "difficulty": "Easy"
    },

    "print": {
        "definition": "A function used to display information in the console.",
        "example": "print('Hello')",
        "category": "Input / Output",
        "difficulty": "Easy"
    },

    "f-string": {
        "definition": "A string format that allows expressions to be placed inside curly brackets.",
        "example": "f'Hello {name}'",
        "category": "Input / Output",
        "difficulty": "Medium"
    },

    "type conversion": {
        "definition": "The process of changing a value from one data type to another.",
        "example": "int('25')",
        "category": "Input / Output",
        "difficulty": "Medium"
    },


    # =========================
    # LIST METHODS
    # =========================

    "append": {
        "definition": "A list method used to add an item to the end of a list.",
        "example": "numbers.append(5)",
        "category": "Lists",
        "difficulty": "Easy"
    },

    "insert": {
        "definition": "A list method used to add an item at a specific position.",
        "example": "numbers.insert(0, 5)",
        "category": "Lists",
        "difficulty": "Medium"
    },

    "remove": {
        "definition": "A list method used to remove the first matching value.",
        "example": "numbers.remove(5)",
        "category": "Lists",
        "difficulty": "Easy"
    },

    "pop": {
        "definition": "A list method used to remove and return an item from a list.",
        "example": "numbers.pop()",
        "category": "Lists",
        "difficulty": "Medium"
    },

    "sort": {
        "definition": "A list method used to arrange items in order.",
        "example": "numbers.sort()",
        "category": "Lists",
        "difficulty": "Easy"
    },

    "reverse": {
        "definition": "A list method used to reverse the order of items.",
        "example": "numbers.reverse()",
        "category": "Lists",
        "difficulty": "Easy"
    },

    "index": {
        "definition": "A method used to find the position of a value in a sequence.",
        "example": "numbers.index(5)",
        "category": "Lists",
        "difficulty": "Medium"
    },

    "count": {
        "definition": "A method used to count how many times a value appears.",
        "example": "numbers.count(5)",
        "category": "Lists",
        "difficulty": "Easy"
    },


    # =========================
    # STRINGS
    # =========================

    "lower": {
        "definition": "A string method that converts letters to lowercase.",
        "example": "'HELLO'.lower()",
        "category": "Strings",
        "difficulty": "Easy"
    },

    "upper": {
        "definition": "A string method that converts letters to uppercase.",
        "example": "'hello'.upper()",
        "category": "Strings",
        "difficulty": "Easy"
    },

    "strip": {
        "definition": "A string method that removes whitespace from the beginning and end.",
        "example": "' hello '.strip()",
        "category": "Strings",
        "difficulty": "Easy"
    },

    "replace": {
        "definition": "A string method used to replace one part of a string with another.",
        "example": "'hello'.replace('h', 'H')",
        "category": "Strings",
        "difficulty": "Easy"
    },

    "split": {
        "definition": "A string method that divides a string into a list.",
        "example": "'a,b,c'.split(',')",
        "category": "Strings",
        "difficulty": "Medium"
    },

    "join": {
        "definition": "A string method used to combine multiple strings into one string.",
        "example": "','.join(words)",
        "category": "Strings",
        "difficulty": "Medium"
    },

    "startswith": {
        "definition": "A string method that checks whether a string begins with specific characters.",
        "example": "'Python'.startswith('Py')",
        "category": "Strings",
        "difficulty": "Medium"
    },

    "endswith": {
        "definition": "A string method that checks whether a string ends with specific characters.",
        "example": "'Python'.endswith('on')",
        "category": "Strings",
        "difficulty": "Medium"
    },


    # =========================
    # DICTIONARIES
    # =========================

    "key": {
        "definition": "A unique identifier used to access a value in a dictionary.",
        "example": "student['name']",
        "category": "Dictionaries",
        "difficulty": "Easy"
    },

    "value": {
        "definition": "The data stored and associated with a key in a dictionary.",
        "example": "'Jazeera' in {'name': 'Jazeera'}",
        "category": "Dictionaries",
        "difficulty": "Easy"
    },

    "items": {
        "definition": "A dictionary method that returns its key-value pairs.",
        "example": "student.items()",
        "category": "Dictionaries",
        "difficulty": "Medium"
    },

    "keys": {
        "definition": "A dictionary method that returns all keys.",
        "example": "student.keys()",
        "category": "Dictionaries",
        "difficulty": "Easy"
    },

    "values": {
        "definition": "A dictionary method that returns all values.",
        "example": "student.values()",
        "category": "Dictionaries",
        "difficulty": "Easy"
    },

    "get": {
        "definition": "A dictionary method used to safely retrieve a value using a key.",
        "example": "student.get('name')",
        "category": "Dictionaries",
        "difficulty": "Medium"
    },


    # =========================
    # BUILT-IN FUNCTIONS
    # =========================

    "len": {
        "definition": "A function that returns the number of items in an object.",
        "example": "len('Python')",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "type": {
        "definition": "A function that returns the data type of a value.",
        "example": "type(10)",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "int": {
        "definition": "A function used to convert a value into an integer.",
        "example": "int('25')",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "float()": {
        "definition": "A function used to convert a value into a floating-point number.",
        "example": "float('3.14')",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "str": {
        "definition": "A function used to convert a value into a string.",
        "example": "str(100)",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "sum": {
        "definition": "A function that calculates the total of numeric values.",
        "example": "sum([1, 2, 3])",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "max": {
        "definition": "A function that returns the largest value.",
        "example": "max(10, 20, 5)",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "min": {
        "definition": "A function that returns the smallest value.",
        "example": "min(10, 20, 5)",
        "category": "Built-in Functions",
        "difficulty": "Easy"
    },

    "abs": {
        "definition": "A function that returns the absolute value of a number.",
        "example": "abs(-10)",
        "category": "Built-in Functions",
        "difficulty": "Medium"
    },

    "round": {
        "definition": "A function used to round a number to a specified number of digits.",
        "example": "round(3.14159, 2)",
        "category": "Built-in Functions",
        "difficulty": "Medium"
    },


    # =========================
    # ERROR HANDLING
    # =========================

    "try": {
        "definition": "A block used to test code that may cause an error.",
        "example": "try: number = int(input())",
        "category": "Error Handling",
        "difficulty": "Medium"
    },

    "except": {
        "definition": "A block used to handle an error that occurs inside a try block.",
        "example": "except ValueError:",
        "category": "Error Handling",
        "difficulty": "Medium"
    },

    "exception": {
        "definition": "An event that interrupts the normal execution of a program because of an error.",
        "example": "ValueError is an exception.",
        "category": "Error Handling",
        "difficulty": "Medium"
    },

    "ValueError": {
        "definition": "An exception that occurs when a value has an inappropriate type or format.",
        "example": "int('hello')",
        "category": "Error Handling",
        "difficulty": "Hard"
    },


    # =========================
    # MODULES
    # =========================

    "module": {
        "definition": "A Python file containing code that can be imported and reused.",
        "example": "import random",
        "category": "Modules",
        "difficulty": "Medium"
    },

    "import": {
        "definition": "A keyword used to bring code from another module into a program.",
        "example": "import random",
        "category": "Modules",
        "difficulty": "Easy"
    },

    "random": {
        "definition": "A Python module used to generate random values and make random choices.",
        "example": "import random",
        "category": "Modules",
        "difficulty": "Easy"
    },

    "random.choice": {
        "definition": "A function that randomly selects one item from a sequence.",
        "example": "random.choice(numbers)",
        "category": "Modules",
        "difficulty": "Medium"
    },

    "random.randint": {
        "definition": "A function that returns a random integer between two specified values.",
        "example": "random.randint(1, 10)",
        "category": "Modules",
        "difficulty": "Medium"
    },


    # =========================
    # FILES
    # =========================

    "open": {
        "definition": "A function used to open a file for reading or writing.",
        "example": "open('data.txt', 'r')",
        "category": "Files",
        "difficulty": "Medium"
    },

    "read": {
        "definition": "A method used to read the contents of a file.",
        "example": "file.read()",
        "category": "Files",
        "difficulty": "Medium"
    },

    "write": {
        "definition": "A method used to write text into a file.",
        "example": "file.write('Hello')",
        "category": "Files",
        "difficulty": "Medium"
    },


    # =========================
    # ADVANCED
    # =========================

    "lambda": {
        "definition": "A small anonymous function written in a single expression.",
        "example": "square = lambda x: x * x",
        "category": "Advanced",
        "difficulty": "Hard"
    },

    "list comprehension": {
        "definition": "A compact way to create a list using an expression and a loop.",
        "example": "[x * 2 for x in numbers]",
        "category": "Advanced",
        "difficulty": "Hard"
    },

    "generator": {
        "definition": "An object that produces values one at a time instead of storing them all at once.",
        "example": "(x * 2 for x in numbers)",
        "category": "Advanced",
        "difficulty": "Hard"
    },

    "class": {
        "definition": "A blueprint used to create objects in object-oriented programming.",
        "example": "class Student:",
        "category": "OOP",
        "difficulty": "Hard"
    },

    "object": {
        "definition": "An instance created from a class.",
        "example": "student = Student()",
        "category": "OOP",
        "difficulty": "Hard"
    },

    "method": {
        "definition": "A function defined inside a class.",
        "example": "def greet(self):",
        "category": "OOP",
        "difficulty": "Hard"
    },

    "inheritance": {
        "definition": "A feature where one class receives attributes and methods from another class.",
        "example": "class Dog(Animal):",
        "category": "OOP",
        "difficulty": "Hard"
    }
}