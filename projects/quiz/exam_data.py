
import json
import os

# Get path to questions.json in the same directory as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, "questions.json")

def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_exam_questions():
    questions = load_questions()
    # Return questions without answer for security
    safe_data = []
    for q in questions:
        c = q.copy()
        if 'answer' in c:
            del c['answer']
        safe_data.append(c)
    return safe_data

def evaluate_exam(answers):
    # answers: dict { "1": "Option", "2": "Option" }
    questions = load_questions()
    score = 0
    results = []
    for q in questions:
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
