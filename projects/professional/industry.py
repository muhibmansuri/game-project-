import os

class IndustryStandardGuide:
    def __init__(self):
        self.standards = {
            "folder_structure": {
                "title": "1. MVC & Clean Architecture",
                "desc": "Instead of putting everything in one file, divide your code into specific folders.",
                "steps": [
                    "Root/ -> Main Config",
                    "Root/api/ -> Routes & Endpoints",
                    "Root/models/ -> Database Structure",
                    "Root/services/ -> Business Logic",
                    "Root/templates/ -> Frontend UI"
                ],
                "icon": "🏗️"
            },
            "environment": {
                "title": "2. Environment & Dependencies",
                "desc": "Never hardcode passwords or API keys. Use .env files and requirements.txt.",
                "steps": [
                    "Create a .env file for secrets.",
                    "Use pip freeze > requirements.txt for tracking versions.",
                    "Always use a Virtual Environment (venv)."
                ],
                "icon": "🌐"
            },
            "security": {
                "title": "3. Professional Security",
                "desc": "Protect user data with hashing and tokenization.",
                "steps": [
                    "Use Bcrypt for password hashing.",
                    "Use JWT (JSON Web Tokens) for session management.",
                    "Enable CORS and Rate Limiting for APIs."
                ],
                "icon": "🔒"
            },
            "modularity": {
                "title": "4. Flask Blueprints",
                "desc": "Split your Flask app into modules so multiple developers can work together.",
                "steps": [
                    "Each feature (auth, shop, chat) gets its own Blueprint.",
                    "Easier to debug and test individual parts.",
                    "Scalable architecture for massive apps."
                ],
                "icon": "🧩"
            }
        }

    def get_all_standards(self):
        return self.standards

industry_guide = IndustryStandardGuide()
