from fpdf import FPDF
import datetime

class ExamReport(FPDF):
    def header(self):
        # Logo or Title
        self.set_font('Arial', 'B', 20)
        self.set_text_color(56, 189, 248) # #38bdf8 Accent Blue
        self.cell(0, 10, 'CodeAura Certification Exam', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_exam_pdf(name, score, total_questions, details, time_taken):
    pdf = ExamReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- Student Details ---
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(255, 255, 255)
    
    # Draw a header box
    pdf.set_fill_color(30, 41, 59) # Dark background
    pdf.rect(10, 25, 190, 40, 'F')
    
    pdf.set_y(30)
    pdf.set_x(15)
    pdf.cell(100, 10, f"Student Name: {name}", 0, 1, 'L', fill=False)
    
    pdf.set_x(15)
    pdf.cell(100, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", 0, 1, 'L', fill=False)
    
    pdf.set_x(15)
    pdf.cell(100, 10, f"Time Taken: {time_taken}", 0, 1, 'L', fill=False)

    # Score Box
    percentage = (score / total_questions) * 100
    color = (74, 222, 128) if percentage >= 70 else (244, 63, 94) # Green or Red
    
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(*color)
    pdf.set_xy(140, 35)
    pdf.cell(50, 10, "SCORE", 0, 1, 'C')
    pdf.set_font('Arial', 'B', 24)
    pdf.set_xy(140, 45)
    pdf.cell(50, 10, f"{percentage:.1f}%", 0, 1, 'C')
    
    pdf.ln(25)

    # --- Detailed Results Table ---
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    
    # Table Header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(10, 10, "No", 1, 0, 'C', 1)
    pdf.cell(110, 10, "Question", 1, 0, 'L', 1)
    pdf.cell(35, 10, "Your Answer", 1, 0, 'L', 1)
    pdf.cell(35, 10, "Status", 1, 1, 'C', 1)

    pdf.set_font('Arial', '', 9)
    
    for i, item in enumerate(details, 1):
        # Question text might be long, so we use MultiCell logic or truncate
        # For simplicity in this table, let's truncate nicely or handle wrapping slightly
        q_text = item['question']
        if len(q_text) > 60:
            q_text = q_text[:57] + "..."
            
        user_ans = str(item['user_answer']) if item['user_answer'] else "Skipped"
        status = "Correct" if item['is_correct'] else "Wrong"
        
        # Color for status
        if item['is_correct']:
            pdf.set_text_color(0, 150, 0)
        else:
            pdf.set_text_color(200, 0, 0)

        pdf.cell(10, 10, str(i), 1, 0, 'C')
        pdf.set_text_color(0)
        pdf.cell(110, 10, q_text, 1, 0, 'L')
        pdf.cell(35, 10, user_ans, 1, 0, 'L')
        
        if item['is_correct']:
            pdf.set_text_color(0, 150, 0)
        else:
            pdf.set_text_color(200, 0, 0)
            
        pdf.cell(35, 10, status, 1, 1, 'C')
        
        # If wrong, show correct answer in a small sub-row
        if not item['is_correct']:
            pdf.set_font('Arial', 'I', 8)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(10, 6, "", 1, 0)
            pdf.cell(180, 6, f"   Correct Answer: {item['correct_answer']}", 1, 1, 'L')
            pdf.set_font('Arial', '', 9)
            pdf.set_text_color(0)

    filename = f"Exam_Result_{name.replace(' ', '_')}.pdf"
    filepath = f"temp_{filename}" # Save temporarily
    pdf.output(filepath)
    return filepath
