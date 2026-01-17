# Q1. Student Grade Evaluation﻿

# Input: Marks in 5 subjects.﻿
# Conditions:﻿

# 1. Check if all subjects are passed (>=33).﻿


# 2. Calculate total percentage.﻿


# 3. If ≥90 → Grade A+﻿


# 4. If 80–89 → A﻿


# 5. If 70–79 → B﻿


# 6. If 60–69 → C﻿


# 7. If 50–59 → D﻿


# 8. Else → Fail﻿

marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)      
if all(mark >= 33 for mark in marks):   
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    print(f"Total Percentage: {percentage}%")
    
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'Fail'
    
    print(f"Grade: {grade}")        
else:
    print("Student has failed in one or more subjects.")   


#

# Q2. Online Shopping Discount﻿

# Input: Purchase amount & Membership type (Gold, Silver, Bronze, None).﻿
# Conditions:﻿

# 1. If amount > 5000 and Gold → 20% off﻿


# 2. If amount > 5000 and Silver → 15% off﻿


# 3. If amount > 3000 and Bronze → 10% off﻿


# 4. If amount > 2000 and None → 5% off﻿


# 5. Else → No discount﻿


# 6. If discount > 1000 → Free delivery﻿


# 7. Else delivery charge = 100﻿

amount = float(input("Enter purchase amount: "))
membership = input("Enter membership type (Gold/Silver/Bronze/None): ").strip().lower() 
print(membership)
discount = 0    
if amount > 5000:
    if membership == 'gold':
        discount = 0.20 * amount
    elif membership == 'silver':
        discount = 0.15 * amount            
elif membership == 'bronze':
    if amount > 3000:
        discount = 0.10 * amount                    
elif membership == 'none':  
    if amount > 2000:
        discount = 0.05 * amount                        +
final_amount = amount - discount
if discount > 1000:
    delivery_charge = 0             
else:               
    delivery_charge = 100               
final_amount += delivery_charge        
print("your total bill",amount,"your discount is:", discount, "and delivery charge is:", delivery_charge, "your final amount to be paid is:", final_amount)     

# Q3.Q3. Movie Ticket Booking﻿

# Input: Age, Time (Morning/Evening/Night), Member or Not.﻿
# Conditions:﻿

# 1. If Age < 5 → Free﻿


# 2. If Age between 5–12 → Child Ticket 50%﻿


# 3. If Age between 13–60 → Full Ticket﻿


# 4. If Age > 60 → Senior Discount 30%﻿


# 5. If Night show and not member → extra ₹50﻿


# 6. If member → additional 10% off﻿


# 7. If total < 100 → Minimum charge 100﻿


age = int(input("Enter your age: "))
time = input("Enter show time (Morning/Evening/Night): ").strip().lower()
is_member = input("Are you a member? (yes/no): ").strip().lower()   
ticket_price = 200    
if age < 5:
    ticket_price = 0            
elif 5 <= age <= 12:
    ticket_price *= 0.50    
elif 13 <= age <= 60:
    ticket_price = ticket_price 
elif age > 60:
    ticket_price *= 0.70
if time == 'night' and is_member == 'no':
    ticket_price += 50
if is_member == 'yes':
    ticket_price *= 0.90    
if ticket_price < 100:
    ticket_price = 100  
print(f"Total ticket price: ₹{ticket_price}")



#Q4


