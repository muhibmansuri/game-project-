
# 50 Python and General Tech Questions

questions = [
    # Basic Python
    {"id": 1, "question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "12"], "answer": "8"},
    {"id": 2, "question": "Which keyword is used to define a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
    {"id": 3, "question": "What data type is the result of: 5 / 2?", "options": ["int", "float", "decimal", "double"], "answer": "float"},
    {"id": 4, "question": "How do you start a comment in Python?", "options": ["//", "/*", "#", "<!--"], "answer": "#"},
    {"id": 5, "question": "Which of these is NOT a core data type?", "options": ["List", "Dictionary", "Tuple", "Class"], "answer": "Class"},
    {"id": 6, "question": "What is len('hello')?", "options": ["4", "5", "6", "1"], "answer": "5"},
    {"id": 7, "question": "How do you check length of a list?", "options": ["size()", "length()", "len()", "count()"], "answer": "len()"},
    {"id": 8, "question": "Which operator is used for modulus?", "options": ["%", "/", "//", "*"], "answer": "%"},
    {"id": 9, "question": "What is the output of 'a' + 'b'?", "options": ["ab", "ba", "error", "9798"], "answer": "ab"},
    {"id": 10, "question": "Is Python interpreted or compiled?", "options": ["Interpreted", "Compiled", "Both", "None"], "answer": "Interpreted"},

    # Lists and Tuples
    {"id": 11, "question": "Are lists mutable?", "options": ["Yes", "No", "Sometimes", "Only with sudo"], "answer": "Yes"},
    {"id": 12, "question": "Are tuples mutable?", "options": ["Yes", "No", "Sometimes", "Only on Sundays"], "answer": "No"},
    {"id": 13, "question": "How to access the last element of a list?", "options": ["list[-1]", "list[last]", "list[0]", "list.end()"], "answer": "list[-1]"},
    {"id": 14, "question": "Method to add element to end of list?", "options": ["push()", "add()", "append()", "insert()"], "answer": "append()"},
    {"id": 15, "question": "How to remove an item by value?", "options": ["delete()", "remove()", "pop()", "kill()"], "answer": "remove()"},

    # Loops and Conditionals
    {"id": 16, "question": "Which loop is used when checking a condition?", "options": ["for", "while", "do-while", "foreach"], "answer": "while"},
    {"id": 17, "question": "How to stop a loop?", "options": ["stop", "break", "exit", "halt"], "answer": "break"},
    {"id": 18, "question": "How to skip the rest of the loop iteration?", "options": ["skip", "continue", "pass", "next"], "answer": "continue"},
    {"id": 19, "question": "What does 'pass' do?", "options": ["Stops program", "Skips iteration", "Nothing", "Passes variable"], "answer": "Nothing"},
    {"id": 20, "question": "How do you write an if statement?", "options": ["if x = 5", "if x == 5:", "if (x == 5)", "CHECK x IS 5"], "answer": "if x == 5:"},

    # Dictionaries
    {"id": 21, "question": "How are dictionaries defined?", "options": ["[]", "()", "{}", "<>"], "answer": "{}"},
    {"id": 22, "question": "How to get a list of keys?", "options": ["dict.keys()", "dict.values()", "dict.items()", "dict.all()"], "answer": "dict.keys()"},
    {"id": 23, "question": "Can dictionary keys be duplicates?", "options": ["Yes", "No", "Depends on Python version", "If using force=True"], "answer": "No"},
    {"id": 24, "question": "What happens if you access a missing key?", "options": ["Returns None", "KeyError", "Returns 0", "Creates the key"], "answer": "KeyError"},
    {"id": 25, "question": "Safe way to get a value?", "options": ["dict.get()", "dict.fetch()", "dict.grab()", "dict.safe()"], "answer": "dict.get()"},

    # Functions & Modules
    {"id": 26, "question": "Keyword to return a value?", "options": ["give", "return", "send", "result"], "answer": "return"},
    {"id": 27, "question": "Keyword to import variable from global scope?", "options": ["global", "extern", "super", "outer"], "answer": "global"},
    {"id": 28, "question": "Default return value of a function?", "options": ["0", "False", "None", "Undefined"], "answer": "None"},
    {"id": 29, "question": "How to import a module named math?", "options": ["import math", "include math", "require math", "use math"], "answer": "import math"},
    {"id": 30, "question": "What is __init__?", "options": ["A function", "A constructor", "A module", "A variable"], "answer": "A constructor"},

    # Advanced / Mixed
    {"id": 31, "question": "What is list comprehension?", "options": ["Compressing a list", "Creating list in one line", "Understanding a list", "Sorting a list"], "answer": "Creating list in one line"},
    {"id": 32, "question": "Output of bool([])?", "options": ["True", "False", "None", "Error"], "answer": "False"},
    {"id": 33, "question": "Output of bool([1])?", "options": ["True", "False", "None", "Error"], "answer": "True"},
    {"id": 34, "question": "What is a lambda function?", "options": ["Anonymous function", "Large function", "Main function", "Loop function"], "answer": "Anonymous function"},
    {"id": 35, "question": "Which is used for exception handling?", "options": ["try/except", "do/catch", "try/catch", "perform/rescue"], "answer": "try/except"},

    # Web & General
    {"id": 36, "question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Main Logic", "Hyper Tool Multi Level", "Home Tool Made Lite"], "answer": "Hyper Text Markup Language"},
    {"id": 37, "question": "What does CSS stand for?", "options": ["Computer Style Sheets", "Cascading Style Sheets", "Color Style System", "Creative Style Solutions"], "answer": "Cascading Style Sheets"},
    {"id": 38, "question": "Port for HTTP?", "options": ["21", "22", "80", "443"], "answer": "80"},
    {"id": 39, "question": "Port for HTTPS?", "options": ["80", "8080", "443", "3000"], "answer": "443"},
    {"id": 40, "question": "Library for web scraping?", "options": ["pandas", "numpy", "BeautifulSoup", "django"], "answer": "BeautifulSoup"},
    
    # More Python
    {"id": 41, "question": "What is pip?", "options": ["Package Installer", "Python Interpreter", "Performance Improver", "Program Interface"], "answer": "Package Installer"},
    {"id": 42, "question": "File extension for Python?", "options": [".python", ".py", ".pt", ".pi"], "answer": ".py"},
    {"id": 43, "question": "Variable name convention in Python?", "options": ["camelCase", "PascalCase", "snake_case", "kebab-case"], "answer": "snake_case"},
    {"id": 44, "question": "How to convert int to string?", "options": ["str()", "string()", "text()", "to_str()"], "answer": "str()"},
    {"id": 45, "question": "Operator for power?", "options": ["^", "**", "pow", "exp"], "answer": "**"},
    {"id": 46, "question": "What is slicing?", "options": ["Cutting strings/lists", "Deleting files", "Breaking loops", "Dividing numbers"], "answer": "Cutting strings/lists"},
    {"id": 47, "question": "Example of immutable type?", "options": ["List", "Set", "Tuple", "Dict"], "answer": "Tuple"},
    {"id": 48, "question": "Example of mutable type?", "options": ["Int", "Str", "Tuple", "List"], "answer": "List"},
    {"id": 49, "question": "Command to run python script?", "options": ["run app.py", "python app.py", "exec app.py", "start app.py"], "answer": "python app.py"},
    {"id": 50, "question": "Is Python case sensitive?", "options": ["Yes", "No", "Only for variables", "Only for functions"], "answer": "Yes"}
]

def get_quiz_data():
    # Return questions without correct answer for the frontend
    # But for simplicity in this app, we might check on backend.
    # We'll send the full list to a trusted frontend or strip answers.
    # Safe approach: Strip answers.
    safe_questions = []
    for q in questions:
        q_copy = q.copy()
        del q_copy['answer']
        safe_questions.append(q_copy)
    return safe_questions

def check_score(answers):
    # answers is a dict { "1": "8", "2": "def", ... }
    score = 0
    results = []
    for q in questions:
        qid = str(q['id'])
        user_ans = answers.get(qid)
        correct_ans = q['answer']
        is_correct = (user_ans == correct_ans)
        if is_correct:
            score += 1
        results.append({
            "id": q['id'],
            "question": q['question'],
            "user_answer": user_ans,
            "correct_answer": correct_ans,
            "is_correct": is_correct
        })
    return score, results
