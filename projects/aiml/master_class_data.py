master_projects = {
    "bank": {
        "title": "Mastery Course: Industrial Bank System",
        "logic_title": "From Scrap to Professional System",
        "desc": "Is roadmap mein hum aapko ek professional software engineer ki tarah project build karna sikhayenge. Zero mistakes, clean archiitecture.",
        "file_path": "bank/bms.py",
        "chapters": [
            {
                "title": "Module 0: Workspace Ki Taiyari",
                "content": "Professional coding mein folder structure sabse important hota hai.\n\n1. Apne main project folder `advance_python` ke andar jayye.\n2. Right click karke **'New Folder'** banayein.\n3. Folder ka naam rakhein `bank` (Ekdam lowercase, koi space nahi).\n\n**Visual Check:** Aapka rasta aisa dikhna chahiye: `.../advance_python/bank/`",
                "type": "setup",
                "icon": "📁"
            },
            {
                "title": "Module 1: Logic File Ka Janm",
                "content": "Ab aapne folder bana liya hai, ab humein 'Logic File' banani hai.\n\n1. `bank` folder ke **andar** ek nayi file banayein.\n2. Naam rakhein: `bms.py` (`Bank Management System`).\n3. File extension `.py` hona lazmi hai taaki computer ise Python file samajh sake.\n\n**Tip:** Naming mein kabhi bhi Capital letters ya Space mat dena, varna import karne mein error aayega!",
                "type": "setup",
                "icon": "📄"
            },
            {
                "title": "Module 2: Code Ka Pehla Hissa (The Tools)",
                "content": "Ab `bms.py` ko open karein. Sabse pehle humein wo modules chahiye jo file save karne aur random numbers banane mein madad karenge.\n\n**Line-by-Line Explanation:**\n- `import json`: Data ko file mein dhang se save karne ke liye.\n- `import os`: File ka rasta (Path) dhoondne ke liye.\n- `import random`: Unique Account number banane ke liye.",
                "code": "import json\nimport os\nimport random\nfrom datetime import datetime\n\n# Ye line computer ko batati hai ki database file 'bank' folder mein hi banani hai\nDATA_FILE = os.path.join(os.path.dirname(__file__), 'bank_data.json')",
                "type": "code",
                "icon": "🛠️"
            },
            {
                "title": "Module 3: Bank Ka Dimag (The Class)",
                "content": "Ab hum ek 'Class' banayenge. Socho ki ye ek Factory hai jo bank ke saare kaamo ko handle karegi.\n\n**Kyun?** Class use karne se code organized rehta hai aur errors kam aate hain.",
                "code": "class BankSystem:\n    def __init__(self):\n        # Jaise hi Bank system chalu ho, purana data load ho jaye\n        self.accounts = self.load_data()\n\n    def load_data(self):\n        # Agar bank_data.json file nahi hai, toh khali dictionary '{}' do\n        if not os.path.exists(DATA_FILE): return {}\n        with open(DATA_FILE, 'r') as f:\n            return json.load(f)\n\n    def save_data(self):\n        # Jab bhi koi transaction ho, use file mein lock (save) kardo\n        with open(DATA_FILE, 'w') as f:\n            json.dump(self.accounts, f, indent=4)",
                "type": "code",
                "icon": "🧠"
            },
            {
                "title": "Module 4: Account Creation Logic",
                "content": "Ab hum function likhenge jo naya account banayega. Isme hum user ka Name aur PIN lenge.",
                "code": "    def create_account(self, name, pin, initial):\n        # 1. 6-digit ka random account number generator\n        acc_num = str(random.randint(100000, 999999))\n        \n        # 2. Account ka poora data structure\n        self.accounts[acc_num] = {\n            'name': name,\n            'pin': pin,\n            'balance': float(initial),\n            'history': [] # Transactions ke liye khali list\n        }\n        \n        # 3. Save it to file!\n        self.save_data()\n        return acc_num",
                "type": "code",
                "icon": "➕"
            },
            {
                "title": "Module 5: Linking with app.py",
                "content": "Project tabhi chalega jab aap use apni main website file (`app.py`) se jodenge.\n\n1. `app.py` ke sabse upar ye line likhein:\n`from bank.bms import bank` \n(iska matlab: 'bank' folder ki 'bms' file se 'bank' object le aao).\n\n2. Niche ye Route (API) add karein:",
                "code": "@app.route('/api/bank/register', methods=['POST'])\ndef bank_register():\n    data = request.json\n    # Frontend se data lekar logic ko bhejo\n    acc_num = bank.create_account(data['name'], data['pin'], data['initial'])\n    return jsonify({'account_number': acc_num})",
                "type": "code",
                "icon": "🔌"
            }
        ],
        "final_project_url": "/bank",
        "final_project_name": "Test Your Bank Project 🏦"
    },
    "industry": {
        "title": "Mastery Course: Industry Standard Code",
        "logic_title": "Pro Dev Pipeline",
        "desc": "Industry level mein hum sirf 'code' nahi likhte, hum 'engineering' karte hain. Clean architecture, environment management aur security seekhein.",
        "file_path": "professional/industry.py",
        "chapters": [
            {
                "title": "Module 0: Professional Workspace",
                "content": "Sabse pehle professional workspace set karein.\n\n1. `.env` file banayein secrets ke liye.\n2. `requirements.txt` banayein dependencies ke liye.\n3. Virtual Environment (`venv`) activate karein.",
                "type": "setup",
                "icon": "📦"
            },
            {
                "title": "Module 1: Modular Architecture",
                "content": "Ek bade project ko chote-chote Blueprints mein divide karein taaki coding asaan ho jaye.",
                "code": "from flask import Blueprint\n\nauth = Blueprint('auth', __name__)\n\n@auth.route('/login')\ndef login():\n    return 'Login Page'",
                "type": "code",
                "icon": "🧩"
            },
            {
                "title": "Module 2: Error Handling & Logging",
                "content": "Professional apps kabhi crash nahi hoti, wo errors ko gracefully handle karti hain.",
                "code": "import logging\n\nlogging.basicConfig(level=logging.INFO)\n\ntry:\n    # code logic\n    pass\nexcept Exception as e:\n    logging.error(f'System Error: {e}')",
                "type": "code",
                "icon": "🛡️"
            }
        ],
        "final_project_url": "/industry",
        "final_project_name": "Explore Industry Standards 🚀"
    }
}

