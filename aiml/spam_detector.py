import re

class SpamDetector:
    def __init__(self):
        # Educational dataset: Words commonly found in Spam vs Safe emails
        self.spam_keywords = {
            'free': 5, 'win': 5, 'prize': 5, 'claim': 4, 'urgent': 4,
            'money': 3, 'cash': 3, 'winner': 5, 'lottery': 5, 'offer': 3,
            'viagra': 5, 'click': 3, 'subscribe': 2, 'million': 4, 'dollars': 3,
            'bank': 2, 'account': 2, 'verify': 3, 'password': 3, 'investment': 4
        }
        
        self.safe_keywords = {
            'meeting': 5, 'lunch': 3, 'project': 4, 'update': 4, 'schedule': 3,
            'regards': 4, 'attached': 3, 'thanks': 4, 'hello': 2, 'dear': 2,
            'report': 4, 'presentation': 4, 'tomorrow': 3, 'discussion': 4, 'team': 3
        }

    def analyze(self, text):
        # Preprocessing
        clean_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        words = clean_text.split()
        
        if not words:
            return {"status": "Empty", "score": 0, "is_spam": False}

        spam_score = 0
        safe_score = 0
        matched_spam = []
        matched_safe = []

        for word in words:
            if word in self.spam_keywords:
                spam_score += self.spam_keywords[word]
                matched_spam.append(word)
            if word in self.safe_keywords:
                safe_score += self.safe_keywords[word]
                matched_safe.append(word)

        # Decide based on scores
        is_spam = spam_score > safe_score
        confidence = 0
        if (spam_score + safe_score) > 0:
            confidence = round((max(spam_score, safe_score) / (spam_score + safe_score)) * 100, 2)

        return {
            "is_spam": is_spam,
            "status": "🚨 SPAM" if is_spam else "✅ SAFE / HAM",
            "score": {"spam": spam_score, "safe": safe_score},
            "matched_spam": list(set(matched_spam)),
            "matched_safe": list(set(matched_safe)),
            "confidence": confidence,
            "advice": "Do not click links!" if is_spam else "Looks like a normal email."
        }

detector = SpamDetector()
