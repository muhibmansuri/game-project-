roadmaps = {
    "sentiment": {
        "title": "Sentiment AI",
        "subtitle": "Natural Language Processing (NLP) Step-by-Step Guide",
        "english": {
            "steps": [
                {"title": "Initialize Weights", "desc": "Create a dictionary of positive and negative words with assigned scores (e.g., 'happy': 5, 'sad': -5)."},
                {"title": "Pre-process Text", "desc": "Convert user input to lowercase and remove punctuation using Regex (<code>re.sub</code>)."},
                {"title": "Tokenization", "desc": "Split the sentence into individual words using the <code>split()</code> method."},
                {"title": "Scoring Engine", "desc": "Loop through words and sum up scores based on your dictionary. Decide the final sentiment label."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Dictionary Banayein", "desc": "Sabse pehle positive aur negative words ki list banayein aur har word ko ek value dein."},
                {"title": "Cleaning", "desc": "User ke input se फालतू characters hatayein aur lowercase mein convert karein."},
                {"title": "Words ko Alag Karein", "desc": "Poore sentence ko <code>split()</code> karke ek-ek word nikaalein."},
                {"title": "Magic Sum", "desc": "Loop chalayein aur total score calculate karein. Agar result > 0 hai toh 'Happy'!"}
            ]
        }
    },
    "predictor": {
        "title": "Grade Predictor",
        "subtitle": "Linear Regression Lab Roadmap",
        "english": {
            "steps": [
                {"title": "Data Setup", "desc": "Identify your independent variable (Study Hours) and dependent variable (Expected Grade)."},
                {"title": "The Slope", "desc": "Define a 'multiplier' (e.g., 5 marks per hour). This is your 'Coefficient'."},
                {"title": "The Intercept", "desc": "Define a base score (e.g., 20 marks) that a student gets even with 0 study hours."},
                {"title": "Final Equation", "desc": "Apply <code>Grade = Base + (Factor * Hours)</code>. Ensure result doesn't exceed 100."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Analysis", "desc": "Pehchaniye ki 'Study Hours' kitna asar daalte hain marks par."},
                {"title": "Multiplier", "desc": "Ek value decide karein ki har 1 ghante padhne se kitne marks badhenge (Coefficient)."},
                {"title": "Base Score", "desc": "Ek minimum score rakhein (Intercept) jo 0 padhai par milta hai."},
                {"title": "Equation Lagayein", "desc": "<code>Marks = Base + (Weight * Hours)</code> formula implement karein."}
            ]
        }
    },
    "spam": {
        "title": "Spam Detector",
        "subtitle": "Naive Bayes Classification Roadmap",
        "english": {
            "steps": [
                {"title": "Keyword Bank", "desc": "Create a 'Spam' list (Free, Prize, Claim) and a 'Safe' list (Meeting, Project, Lunch)."},
                {"title": "Text Analysis", "desc": "Clean the incoming email text and extract unique words."},
                {"title": "Frequency Check", "desc": "Count how many 'Spam' keywords are present vs 'Safe' keywords."},
                {"title": "Confidence Logic", "desc": "Use the Ratio of Spam keywords to Safe keywords to calculate a percentage confidence."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Keywords List", "desc": "Do list banayein - ek Spam words ki (Lottery, Win) aur ek Safe words ki (Hello, Regards)."},
                {"title": "Scan Karein", "desc": "Aane wale email ke words ko scan karein."},
                {"title": "Comparison", "desc": "Check karein ki kaunsi list ke words zyada match ho rahe hain."},
                {"title": "Decision", "desc": "Jiska score zyada hoga, email wahi label kiya jayega (Spam ya Safe)."}
            ]
        }
    },
    "digit": {
        "title": "Digit Recognizer",
        "subtitle": "Neural Network Visualizer Roadmap",
        "english": {
            "steps": [
                {"title": "Canvas Grid", "desc": "Set up a drawing area and capture the image as a 28x28 pixel grid."},
                {"title": "Normalization", "desc": "Convert pixel values (0-255) to a normalized range (0-1)."},
                {"title": "Template Matching", "desc": "Compare the user's grid with pre-defined mathematical 'Templates' for digits 0-9."},
                {"title": "Activation Visualization", "desc": "Display a grid of 'Neurons' that glow based on the average intensity of different regions."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Drawing Board", "desc": "Ek canvas banayein jahan user likh sake, fir use 28x28 chote pixels mein badal dein."},
                {"title": "Normalization", "desc": "Colours ko numbers (0 to 1) mein badal dein."},
                {"title": "Match Making", "desc": "User ki drawing ko 0-9 tak ke math patterns se match karein."},
                {"title": "Neurons", "desc": "Ek grid banayein jo glow kare jahan user ne line draw ki hai (Visualization layer)."}
            ]
        }
    },
    "house": {
        "title": "Price Estimator",
        "subtitle": "Multi-variable Regression Guide",
        "english": {
            "steps": [
                {"title": "Parameter Selection", "desc": "Identify multiple features: Area, Bedrooms, Location Rating, and Age."},
                {"title": "Weight Assignment", "desc": "Assign importance (weights) to each. E.g., Bedrooms +400k, Age -25k."},
                {"title": "The Regression Calc", "desc": "Implement <code>Total = Base + Sum(Feature * Weight)</code>."},
                {"title": "Result Breakdown", "desc": "Use Chart.js to show the user which factor contributed most to the final price."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Features Choose Karein", "desc": "Area, Rooms, aur Location ko input banayein."},
                {"title": "Weights Dein", "desc": "Tai karein ki 1 room kitna rate badhata hai aur purana ghar kitna girata hai."},
                {"title": "Calculation", "desc": "Sab values ko unke weights se multiply karke total price nikalein."},
                {"title": "Graphs", "desc": "Chart.js ka use karke user ko dikhayein ki result kaise aaya (Contribution analysis)."}
            ]
        }
    },
    "fraud": {
        "title": "Fraud Detector",
        "subtitle": "Anomaly Detection AI Guide",
        "english": {
            "steps": [
                {"title": "Define Normalcy", "desc": "Set thresholds for a normal transaction (e.g., Amount < $50,000)."},
                {"title": "Feature Flags", "desc": "Detect suspicious locations (Offshore islands) and high transaction frequency."},
                {"title": "Risk Aggregator", "desc": "Sum the severity of all violations into a single Risk Score (0-100)."},
                {"title": "HUD Alert System", "desc": "Display clear Green/Red signals based on the Risk Score threshold."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Normal Boundaries", "desc": "Banks ki normal limits decide karein (jaise amount aur time)."},
                {"title": "Outlier Detection", "desc": "Ajeeb (strange) locations ya bahut fast transactions ko pakdein."},
                {"title": "Risk Score", "desc": "Har mistake par score badhayein. Agar score high hai toh Fraud alert dein."},
                {"title": "Visual HUD", "desc": "Ek futuristic dashboard banayein jo status (Verified vs Fraud) dikhaye."}
            ]
        }
    },
    "blockchain": {
        "title": "Blockchain Sim",
        "subtitle": "Decentralized Ledger Guide",
        "english": {
            "steps": [
                {"title": "The Block Structure", "desc": "Define a block class containing: Index, Timestamp, Transactions, and PrevHash."},
                {"title": "SHA-256 Hashing", "desc": "Implement data hashing. Any tiny change in data must change the entire hash."},
                {"title": "Proof of Work (PoW)", "desc": "Create a 'Mining' loop that finds a 'Nonce' leading to a hash with enough zeros."},
                {"title": "Chain Integrity", "desc": "Ensure the 'PrevHash' of a block matches the actual hash of the previous block."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Block Banayein", "desc": "Ek container design karein jisme data, time aur purana hash ho."},
                {"title": "Hash Power", "desc": "SHA-256 function implement karein jo data ka unique ID (Hash) nikaale."},
                {"title": "Mining Logic", "desc": "Computer se 'Nonce' dhoondwayein jo mining puzzle solve kare."},
                {"title": "Security Check", "desc": "Ye confirm karein ki har naya block pichle block se connected (Chain) hai."}
            ]
        }
    },
    "tictactoe": {
        "title": "Tic Tac Toe",
        "subtitle": "Minimax Algorithm & Game Logic",
        "english": {
            "steps": [
                {"title": "Board Representation", "desc": "Use a 1D or 2D list to store X and O positions."},
                {"title": "Win Conditions", "desc": "Check rows, columns, and diagonals for 3 matching symbols."},
                {"title": "Player Turns", "desc": "Implement a toggle between 'X' and 'O' on every valid click."},
                {"title": "AI Opponent", "desc": "Use the Minimax algorithm to make the computer unbeatable."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Board Banayein", "desc": "Ek list banayein jise 3x3 grid ki tarah use karein."},
                {"title": "Jeetne Ke Rules", "desc": "Rows aur diagonals check karein matching signs ke liye."},
                {"title": "Turns", "desc": "Player aur AI ke beech switching logic banayein."},
                {"title": "Smart AI", "desc": "Minimax algorithm use karein taaki computer kabhi na haare."}
            ]
        }
    },
    "snake": {
        "title": "Snake Game",
        "subtitle": "Coordinate Math & Collision Guide",
        "english": {
            "steps": [
                {"title": "Movement Loop", "desc": "Update Snake's head coordinate based on direction Every X milliseconds."},
                {"title": "Body Growth", "desc": "Append new head position to a list and don't remove tail if food is eaten."},
                {"title": "Collision Detection", "desc": "Check if head coordinate matches walls or body coordinates."},
                {"title": "Food Spawning", "desc": "Generate random grid coordinates not occupied by the snake body."}
            ]
        },
        "hinglish": {
            "steps": [
                {"title": "Harkat (Movement)", "desc": "Snake ke sir (head) ki position loop mein update karein."},
                {"title": "Body badhayein", "desc": "Jab khaana (food) mile, toh tail ko delete mat karein aur body grow karein."},
                {"title": "Takkar (Collision)", "desc": "Check karein ki snake diwaar ya apni body se toh nahi takraya."},
                {"title": "Khaana (Food)", "desc": "Random jagah par khaana generate karein jahan snake na ho."}
            ]
        }
    },
    "quiz": {
        "title": "Quiz Portal",
        "subtitle": "Automated Exam System Roadmap",
        "english": {
            "steps": [
                {"title": "Database Schema", "desc": "Design a list of dictionaries to store questions, multiple-choice options, and the correct answer key."},
                {"title": "Session Management", "desc": "Initialize a user session to track the current question index, total score, and time remaining."},
                {"title": "Randomization", "desc": "Use <code>random.sample()</code> to pick a subset of unique questions for every new attempt."},
                {"title": "Stateful Navigation", "desc": "Build a 'Next' button logic that validates the selected answer and increments the score before loading the next question."},
                {"title": "Result Engine", "desc": "Calculate a percentage score and display a pass/fail summary based on a minimum threshold (e.g., 40%)."},
                {"title": "Performance Tuning", "desc": "Implement a countdown timer using JavaScript to auto-submit the exam when time expires."}
            ],
            "code": """
                <div class="code-block">
                    <pre># 1. Create quiz/data.py
questions = [
    {"id": 1, "question": "Python extension?", "options": [".c", ".py", ".js"], "answer": ".py"},
    {"id": 2, "question": "2+2?", "options": ["3", "4", "5"], "answer": "4"},
]</pre>
                </div>
                <div class="code-block">
                    <pre># 2. Main Logic in app.py
from flask import Flask, render_template, session
import random

@app.route('/quiz')
def start_quiz():
    # Pick 5 random questions
    session['quiz_data'] = random.sample(questions, 5)
    session['score'] = 0
    return render_template('quiz.html')</pre>
                </div>
            """,
            "details": """
                <h3>Project Blueprint</h3>
                <p>The system is divided into three main components:</p>
                <ul>
                    <li><b>Data Layer (quiz/data.py):</b> This file acts as a 'Mock Database'. We use a simple Python List because it's fast and easy to loop through. Each question is a <code>dict</code> for key-value access.</li>
                    <li><b>Business Logic (app.py):</b> The routes handle the 'Flow Control'. When you click 'Start', the server picks random questions to ensure no two students get the same exam.</li>
                    <li><b>User Interface (templates/quiz.html):</b> A clean UI that uses Jinja2 loops to render dynamic content sent from Python.</li>
                </ul>
                <h3>Why this code?</h3>
                <p>We use <code>session</code> because HTTP is 'stateless'. Without sessions, the server would forget your score as soon as you moved to Question 2. By using <code>session['score']</code>, we keep your data alive during the entire exam.</p>
            """
        },
        "hinglish": {
            "steps": [
                {"title": "Question Bank", "desc": "Ek list banayein jisme questions, options aur sahi answer (Key) save ho saken."},
                {"title": "User Session", "desc": "Session use karein taaki pata rahe user abhi kaunse sawal par hai aur uska score kya hai."},
                {"title": "Random Questions", "desc": "<code>random.sample()</code> library ka use karke har bar naye sawal shuffle karein."},
                {"title": "Logic Flow", "desc": "Agle sawal par jane se pehle check karein ki user ne sahi option select kiya ya nahi."},
                {"title": "Score Calculation", "desc": "End mein total marks dikhayein aur feedback dein (Pass/Fail status)."},
                {"title": "Timer Control", "desc": "JavaScript se ek countdown timer banayein jo automatic exam submit kar de."}
            ],
            "code": """
                <div class="code-block">
                    <pre># 1. quiz/data.py mein ye data rakhein
questions = [
    {"id": 1, "question": "Python file extension?", "options": [".c", ".py"], "answer": ".py"},
]</pre>
                </div>
                <div class="code-block">
                    <pre># 2. app.py ka logic (Backend)
@app.route('/quiz')
def start_quiz():
    # random.sample se sawal shuffle hote hain
    session['quiz_data'] = random.sample(questions, 5)
    return render_template('quiz.html')</pre>
                </div>
            """,
            "details": """
                <h3>Ye Kaise Bana? (The Planning)</h3>
                <p>Is project ko banane ke liye humne 3 cheezon par dhyan diya:</p>
                <ul>
                    <li><b>Data Storage (quiz/data.py):</b> Humne questions ko Database ki jagah ek Python file mein rakha taaki search fast ho. Har question ke sath ek 'answer' key di gayi hai matching ke liye.</li>
                    <li><b>Shuffle Logic:</b> Har bar exam naya lage, isliye <code>random.sample</code> use kiya jo questions ka order badal deta hai.</li>
                    <li><b>Live Timer:</b> Frontend par JavaScript ka use kiya gaya jo user ke browser par chalta hai aur fixed time khatam hote hi exam submit kar deta hai.</li>
                </ul>
                <h3>Important Techniques</h3>
                <p><b>Flask Sessions:</b> Sabse zaroori cheez session hai. Aapne dekha hoga ki Question 1 ke baad Question 2 par jane par bhi score save rehta hai. Ye session ki wajah se possible hai, jo server-side memory mein student ka data temporary save karke rakhta hai.</p>
            """
        }
    },
    "bank": {
        "title": "CodeAura Bank",
        "subtitle": "Persistent Banking System Roadmap",
        "english": {
            "steps": [
                {"title": "Initialize JSON Database", "desc": "Setup a <code>bank_data.json</code> file to act as your permanent storage."},
                {"title": "Core Bank Class", "desc": "Build a <code>BankSystem</code> class with methods for load/save and account management."},
                {"title": "Secure Sign-up", "desc": "Generate random 6-digit account numbers and store them with encrypted-style PINs."},
                {"title": "Transaction Engine", "desc": "Code the <code>deposit</code> and <code>withdraw</code> logic with strict balance checks."},
                {"title": "Audit Logs", "desc": "Create a history list to track every movement of money with timestamps."}
            ],
            "code": """
                <div class="code-block">
                    <pre># 1. bank/bms.py - The Architecture
import json, os, random

class BankSystem:
    def __init__(self):
        # Load existing data from JSON
        self.data_file = 'bank_data.json'
        self.accounts = self.load_data()

    def deposit(self, acc, amount):
        if amount > 0:
            self.accounts[acc]['balance'] += amount
            self.save_data()
            return True
        return False</pre>
                </div>
                <div class="code-block">
                    <pre># 2. Saving to Disk (The Secret Sauce)
def save_data(self):
    with open(self.data_file, 'w') as f:
        # indent=4 makes the file human-readable
        json.dump(self.accounts, f, indent=4)</pre>
                </div>
            """,
            "details": """
                <h3>Industrial Deep Dive</h3>
                <p><b>1. Persistence:</b> Real banks don't lose data when the power goes out. We simulate this using <code>JSON</code>. Every time a transaction happens, <code>json.dump()</code> writes the latest balance to the hard drive.</p>
                <p><b>2. Validation:</b> The code uses an 'if-gate' strategy. Before deducting money, it checks: <code>if balance >= amount</code>. This prevents the account from going into negative values.</p>
                <p><b>3. State Management:</b> By using a <code>class</code>, we keep all bank logic in one place. This is called Object-Oriented Programming (OOP) and is how professional software is built.</p>
            """
        },
        "hinglish": {
            "steps": [
                {"title": "JSON Database Setup", "desc": "Sabse pehle <code>bank_data.json</code> banayein jahan account details permanent save hongi."},
                {"title": "Bank Logic Class", "desc": "Ek <code>BankSystem</code> class banayein jo saare functions ko control kare."},
                {"title": "Sign-up Logic", "desc": "User ke liye random account numbers aur PIN save karne ka system banayein."},
                {"title": "Transaction Engine", "desc": "Paisa jama (Deposit) aur nikalne (Withdraw) ke rules code karein."},
                {"title": "Record Keeping", "desc": "Har transaction ka ek record (History) maintain karein date aur time ke sath."}
            ],
            "code": """
                <div class="code-block">
                    <pre># 1. bank/bms.py - Bank Ka Dimag
import json, random

class BankSystem:
    def __init__(self):
        # Database load karo
        self.accounts = self.load_from_json()

    def withdraw(self, acc, amount):
        # Check karo balance hai ya nahi
        if self.accounts[acc]['balance'] >= amount:
            self.accounts[acc]['balance'] -= amount
            self.save() # Foran save karein
            return "Success"
        return "Not Enough Money"</pre>
                </div>
                <div class="code-block">
                    <pre># 2. Permanent Storage (JSON Logic)
def save(self):
    # 'w' mode matlab file mein write karna
    with open('bank_data.json', 'w') as f:
        json.dump(self.accounts, f)</pre>
                </div>
            """,
            "details": """
                <h3>Bank Ka Blueprint (In-Depth)</h3>
                <p>Is project ko humne 3 parts mein samjha hai:</p>
                <ul>
                    <li><b>JSON Files:</b> Ye hamari 'External Memory' hai. Python jab band hota hai toh variables saaf ho jate hain, lekin JSON file disk par rehti hai. Isse aapka bank account hamesha raheyga.</li>
                    <li><b>Edge Case Handling:</b> Humne code mein check lagaya hai ki koi 0 se kam paisa na nikal sake aur na hi balance se zyada. Banks isi 'Edge Case' logic par chalte hain.</li>
                    <li><b>Audit Logs:</b> Transactions ko list mein save karna zaroori hai taaki 'Bank Statement' dikhaya ja sake. Student yahan list handling seekhte hain.</li>
                </ul>
                <p><b>Expert Tip:</b> Is code ko copy karke aap apna personal banking software bana sakte hain!</p>
            """
        }
    },
    "cryptopulse": {
        "title": "CryptoPulse AI",
        "subtitle": "Real-Time Market Data & Charting Roadmap",
        "english": {
            "steps": [
                {"title": "The Market Simulator", "desc": "Develop a simulation engine that generates random but realistic price fluctuations for coins like BTC, ETH, and SOL."},
                {"title": "Historical Buffer", "desc": "Implement a 'Moving Window' buffer (List) to store the last 30 price points for graph rendering."},
                {"title": "Flask API Endpoint", "desc": "Create a <code>/api/crypto/market</code> route that returns the latest prices as a JSON object for the frontend."},
                {"title": "Real-Time Charting", "desc": "Use <code>Chart.js</code> to draw line graphs on the frontend. Use <code>setInterval()</code> to fetch data every 2 seconds without refreshing the page."},
                {"title": "Visual Dynamics", "desc": "Apply conditional CSS to change colors (Green for up, Red for down) based on price movement."}
            ],
            "details": """
                <h3>The Pulse Engine Architecture</h3>
                <p>CryptoPulse demonstrates how <b>dynamic dashboards</b> work. Unlike standard websites, financial apps require data to move constantly.</p>
                <ul>
                    <li><b>Backend Simulation:</b> We use <code>random.uniform()</code> with a small volatility factor (0.2%) to mimic real market movements. Each tick updates a 'History' list which the frontend uses for the sparklines.</li>
                    <li><b>RESTful API:</b> The server acts as an 'Oracle' that provides data in JSON format. This separation of Backend (Python) and Frontend (JS) is how modern SPAs (Single Page Apps) are built.</li>
                    <li><b>Canvas Rendering:</b> Using <code>Chart.js</code> allows us to render high-performance graphics on a <code>&lt;canvas&gt;</code> element, which is much faster than standard HTML elements for live data.</li>
                </ul>
            """
        },
        "hinglish": {
            "steps": [
                {"title": "Market Engine", "desc": "Ek Python class banayein jo prices ko random lekin realistic tareeke se badalti rahe."},
                {"title": "Price History", "desc": "Har coin ke pichle 30 prices save karein (List buffer) taaki graph draw ho sake."},
                {"title": "API Banana", "desc": "Ek unique URL (API) banayein jo saara market data JSON format mein frontend ko bhej sake."},
                {"title": "Live Graphs", "desc": "<code>Chart.js</code> aur JavaScript ka use karke graphs ko bina page refresh kiye update karein."},
                {"title": "Dynamic Design", "desc": "Jab price badhe toh Hara (Green) aur gire toh Laal (Red) indicator dikhayen."}
            ],
            "details": """
                <h3>Live Dashboard Kaise Kaam Karta Hai?</h3>
                <p>CryptoPulse real-time financial tracking seekhne ke liye perfect project hai.</p>
                <ul>
                    <li><b>The Logic Loop:</b> Backend mein ek volatility factor (0.002) ka use kiya gaya hai. Iska matlab hai ki price har bar sirf 0.2% hi up-down hoyega, jo ek stable real market ki tarah lagta hai.</li>
                    <li><b>Async Data Fetching:</b> Humne <code>fetch()</code> API ka use kiya hai. Isse page ke 'market-grid' section pe data automatically update hota hai, user ko button dabane ki zaroorat nahi padti.</li>
                    <li><b>Glassmorphism Design:</b> Dashboard ko premium look dene ke liye <code>backdrop-filter: blur()</code> ka use kiya gaya hai, jo Apple aur Microsoft ke modern designs mein use hota hai.</li>
                </ul>
            """
        }
    },
    "skywatch": {
        "title": "SkyWatch AI",
        "subtitle": "Dynamic Weather Intelligence Roadmap",
        "english": {
            "steps": [
                {"title": "The Weather Oracle", "desc": "Build a simulation engine that maps cities to unique weather conditions (Rain, Snow, Sunny) and generates random temperatures."},
                {"title": "Dynamic Context API", "desc": "Create a Flask route that accepts a 'city' parameter and serves specifically tailored weather objects as JSON."},
                {"title": "Reactive UI Patterns", "desc": "Write JavaScript observers that detect condition changes and update the CSS background variables in real-time."},
                {"title": "Particle Systems", "desc": "Implement a 'Rain Generator' that creates and animates 50+ individual div 'droplets' using CSS Keyframes when conditions are wet."},
                {"title": "Visual Hierarchy", "desc": "Use Backdrop Filters and varying opacities to ensure readability against high-contrast, colorful backgrounds."}
            ],
            "details": """
                <h3>The Intelligence of UI</h3>
                <p>SkyWatch isn't just a weather app; it's an exploration of <b>Reactive Design</b>.</p>
                <ul>
                    <li><b>Data-Driven Styling:</b> The server sends a 'condition' string (e.g., 'Rain'). The frontend uses this as a key to swap out entire CSS variable sets for the background gradient.</li>
                    <li><b>Atmospheric Immersion:</b> By using the <code>&lt;div class='drop'&gt;</code> strategy, we create depth. Each droplet is randomly positioned and timed, creating a natural-looking rain effect without heavy libraries.</li>
                    <li><b>Fallback Logic:</b> The Python manager includes error handling to pick a random city if the requested one isn't in our database, ensuring the app never breaks for the user.</li>
                </ul>
            """
        },
        "hinglish": {
            "steps": [
                {"title": "Weather Data Engine", "desc": "Ek Python manager banayein jo alag-alag cities ke liye conditions (Sunny, Rain) aur temperature return kare."},
                {"title": "Smart API", "desc": "Flask API banayein jo query params se city name read kare aur accurate JSON bhej sake."},
                {"title": "Dynamic Backgrounds", "desc": "JavaScript logic likhein jo condition ke hisaab se CSS gradients (Themes) swap kare."},
                {"title": "Rain Animation", "desc": "CSS Keyframes ka use karke 'Raindrops' banayein jo screen par girte huye dikhein jab Condition 'Rain' ho."},
                {"title": "Premium Glassmorphism", "desc": "Translucent backgrounds aur blur effects use karein taaki data clear aur modern dikhe."}
            ],
            "details": """
                <h3>Reactive Architecture Kya Hai?</h3>
                <p>SkyWatch project dikhata hai ki kaise data UI ko control karta hai.</p>
                <ul>
                    <li><b>Theme Swapping:</b> Jaise hi user city badalta hai, JS function pehle purani animations clean karta hai aur fir condition ke hisaab se naya gradient apply karta hai.</li>
                    <li><b>Particle Logic:</b> Baarish (Rain) dikhane ke liye humne loop ka use kiya hai jo 50+ chote elements ko screen par random positions par bhejta hai, jisse lagta hai ki sach mein baarish ho rahi hai.</li>
                    <li><b>User Experience:</b> Modern apps user ke context (weather, time) ke hisaab se badalti hain. Ye project wahi seekhata hai.</li>
                </ul>
            """
        }
    }
}
