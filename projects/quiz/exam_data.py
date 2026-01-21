
exam_questions = [
    # 1. Basics & Syntax
    {"id": 1, "question": "What is the correct file extension for Python files?", "options": [".python", ".py", ".pt", ".txt"], "answer": ".py"},
    {"id": 2, "question": "Which character is used to start a comment in Python?", "options": ["//", "/*", "#", "<!--"], "answer": "#"},
    {"id": 3, "question": "How do you output text to the console?", "options": ["echo()", "printf()", "print()", "log()"], "answer": "print()"},
    {"id": 4, "question": "Python relies on ____ to define scope (like blocks of code).", "options": ["Brackets {}", "Indentation", "Semicolons ;", "Parentheses ()"], "answer": "Indentation"},
    {"id": 5, "question": "Which statement is used to stop a loop?", "options": ["stop", "break", "exit", "return"], "answer": "break"},

    # 2. Variables & Data Types
    {"id": 6, "question": "How do you create a variable 'x' equal to 5?", "options": ["x = 5", "int x = 5;", "x == 5", "var x = 5"], "answer": "x = 5"},
    {"id": 7, "question": "What is the data type of: x = 5", "options": ["float", "int", "string", "double"], "answer": "int"},
    {"id": 8, "question": "What is the data type of: x = 'Hello'", "options": ["char", "str", "text", "string"], "answer": "str"},
    {"id": 9, "question": "What is the data type of: x = True", "options": ["bool", "boolean", "true", "bit"], "answer": "bool"},
    {"id": 10, "question": "What is the data type of: x = 5.5", "options": ["int", "long", "float", "decimal"], "answer": "float"},

    # 3. Operators
    {"id": 11, "question": "Which operator is used for multiplication?", "options": ["x", "*", "#", "%"], "answer": "*"},
    {"id": 12, "question": "What does the '%' operator do?", "options": ["Percentage", "Division", "Modulus (Remainder)", "Power"], "answer": "Modulus (Remainder)"},
    {"id": 13, "question": "Which operator is used for exponentiation (power)?", "options": ["^", "**", "pow", "exp"], "answer": "**"},
    {"id": 14, "question": "What is the result of 10 // 3?", "options": ["3.33", "3", "3.0", "1"], "answer": "3"},
    {"id": 15, "question": "Which operator checks for equality?", "options": ["=", "==", "===", "<>"], "answer": "=="},

    # 4. Strings
    {"id": 16, "question": "How do you get the first character of a string 'txt'?", "options": ["txt[1]", "txt(0)", "txt[0]", "txt.first()"], "answer": "txt[0]"},
    {"id": 17, "question": "Which method returns the length of a string?", "options": ["size()", "length()", "len()", "count()"], "answer": "len()"},
    {"id": 18, "question": "How do you convert a string to uppercase?", "options": [".upper()", ".toUpper()", ".caseUpper()", ".uppercase()"], "answer": ".upper()"},
    {"id": 19, "question": "How do you remove whitespace from the beginning/end?", "options": [".trim()", ".strip()", ".clean()", ".cut()"], "answer": ".strip()"},
    {"id": 20, "question": "What is the output of 'A' + 'B'?", "options": ["AB", "Error", "A B", "6566"], "answer": "AB"},

    # 5. Lists & Tuples
    {"id": 21, "question": "How do you create a list?", "options": ["{}", "()", "[]", "<>"], "answer": "[]"},
    {"id": 22, "question": "How do you create a tuple?", "options": ["{}", "()", "[]", "<>"], "answer": "()"},
    {"id": 23, "question": "Which collection is ordered and changeable?", "options": ["Tuple", "Set", "List", "Dictionary"], "answer": "List"},
    {"id": 24, "question": "Which collection is ordered and unchangeable?", "options": ["Tuple", "Set", "List", "Dictionary"], "answer": "Tuple"},
    {"id": 25, "question": "How do you add an item to the end of a list?", "options": [".push()", ".add()", ".append()", ".insert()"], "answer": ".append()"},

    # 6. Dictionaries & Sets
    {"id": 26, "question": "How do you create a dictionary?", "options": ["{}", "()", "[]", "dict[]"], "answer": "{}"},
    {"id": 27, "question": "How do you access the value of key 'model' in dict 'd'?", "options": ["d[model]", "d('model')", "d['model']", "d.model"], "answer": "d['model']"},
    {"id": 28, "question": "Which collection does not allow duplicate members?", "options": ["List", "Tuple", "Set", "Array"], "answer": "Set"},

    # 7. Conditionals & Loops
    {"id": 29, "question": "Which keyword starts a conditional statement?", "options": ["check", "test", "if", "when"], "answer": "if"},
    {"id": 30, "question": "How do you write a 'does not equal' comparison?", "options": ["<>", "!=", "not =", "=/="], "answer": "!="},
    {"id": 31, "question": "Which loop is used to iterate over a sequence?", "options": ["while", "loop", "for", "foreach"], "answer": "for"},
    {"id": 32, "question": "What does the 'range(5)' function return?", "options": ["1 to 5", "0 to 5", "0 to 4", "1 to 6"], "answer": "0 to 4"},
    {"id": 33, "question": "What keyword is used to skip the current iteration?", "options": ["break", "skip", "continue", "next"], "answer": "continue"},

    # 8. Functions
    {"id": 34, "question": "Which keyword defines a function?", "options": ["function", "def", "func", "define"], "answer": "def"},
    {"id": 35, "question": "How do you call a function named 'my_func'?", "options": ["call my_func", "my_func()", "run my_func", "def my_func"], "answer": "my_func()"},
    {"id": 36, "question": "What keyword is used to return a value?", "options": ["get", "return", "send", "result"], "answer": "return"},
    {"id": 37, "question": "Can a function call itself? (Recursion)", "options": ["Yes", "No", "Only in C++", "Errors out"], "answer": "Yes"},

    # 9. Miscellaneous
    {"id": 38, "question": "How do you accept user input?", "options": ["cin >>", "get()", "input()", "scan()"], "answer": "input()"},
    {"id": 39, "question": "How do you convert a number string '10' to an integer?", "options": ["int('10')", "str(10)", "parse('10')", "to_int(10)"], "answer": "int('10')"},
    {"id": 40, "question": "Which keyword imports a module?", "options": ["include", "import", "using", "require"], "answer": "import"}
]

def get_exam_questions():
    # Return questions without answer for security
    safe_data = []
    for q in exam_questions:
        c = q.copy()
        del c['answer']
        safe_data.append(c)
    return safe_data

def evaluate_exam(answers):
    # answers: dict { "1": "Option", "2": "Option" }
    score = 0
    results = []
    for q in exam_questions:
        qid = str(q['id'])
        user_ans = answers.get(qid)
        correct = q['answer']
        is_right = (user_ans == correct)
        if is_right:
            score += 1
        
        results.append({
            "id": q['id'],
            "question": q['question'],
            "user_answer": user_ans,
            "correct_answer": correct,
            "is_correct": is_right
        })
    return score, results
