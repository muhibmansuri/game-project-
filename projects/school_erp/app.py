from flask import Flask, render_template, request, redirect, url_for, jsonify
from utils import load_data, save_data, STUDENTS_FILE, TEACHERS_FILE, init_files

app = Flask(__name__)

# Initialize Data
init_files()

@app.route('/')
def dashboard():
    students = load_data(STUDENTS_FILE)
    teachers = load_data(TEACHERS_FILE)
    stats = {
        'total_students': len(students),
        'total_teachers': len(teachers),
        'recent_admissions': students[-5:] if students else []
    }
    return render_template('dashboard.html', stats=stats)

# --- Student Management ---
@app.route('/students')
def student_list():
    students = load_data(STUDENTS_FILE)
    return render_template('students.html', students=students)

@app.route('/students/add', methods=['POST'])
def add_student():
    students = load_data(STUDENTS_FILE)
    new_student = {
        'id': len(students) + 101, # Simple ID generation
        'name': request.form['name'],
        'class': request.form['grade'],
        'contact': request.form['contact'],
        'fees_paid': False
    }
    students.append(new_student)
    save_data(STUDENTS_FILE, students)
    return redirect(url_for('student_list'))

@app.route('/students/delete/<int:id>')
def delete_student(id):
    students = load_data(STUDENTS_FILE)
    students = [s for s in students if s['id'] != id]
    save_data(STUDENTS_FILE, students)
    return redirect(url_for('student_list'))

# --- Teacher Management ---
@app.route('/teachers')
def teacher_list():
    teachers = load_data(TEACHERS_FILE)
    return render_template('teachers.html', teachers=teachers)

@app.route('/teachers/add', methods=['POST'])
def add_teacher():
    teachers = load_data(TEACHERS_FILE)
    new_teacher = {
        'id': len(teachers) + 1,
        'name': request.form['name'],
        'subject': request.form['subject'],
        'salary': request.form['salary']
    }
    teachers.append(new_teacher)
    save_data(TEACHERS_FILE, teachers)
    return redirect(url_for('teacher_list'))

if __name__ == '__main__':
    app.run(debug=True, port=8080) # Using port 8080 to avoid conflict with main app
