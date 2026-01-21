import re

class SentimentAnalyzer:
    def __init__(self):
        # Basic word-list based approach for students to understand scoring
        self.positive_words = {
            'love', 'great', 'awesome', 'amazing', 'good', 'happy', 'excellent',
            'wonderful', 'best', 'fantastic', 'creative', 'cool', 'nice', 'beautiful',
            'proud', 'excited', 'success', 'brilliant', 'perfect'
        }
        self.negative_words = {
            'hate', 'bad', 'awful', 'terrible', 'horrible', 'sad', 'angry',
            'fail', 'failure', 'worst', 'boring', 'noisy', 'ugly', 'disgusting',
            'error', 'problem', 'waste', 'rude', 'poor', 'useless'
        }

    def analyze(self, text):
        # Convert to lowercase and remove non-alphabetic chars
        clean_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        words = clean_text.split()
        
        if not words:
            return "neutral", 0, "No valid words found"

        score = 0
        positive_found = []
        negative_found = []

        for word in words:
            if word in self.positive_words:
                score += 1
                positive_found.append(word)
            elif word in self.negative_words:
                score -= 1
                negative_found.append(word)

        # Determine sentiment
        if score > 0:
            sentiment = "positive"
            emoji = "😊"
        elif score < 0:
            sentiment = "negative"
            emoji = "😞"
        else:
            sentiment = "neutral"
            emoji = "😐"

        return {
            "sentiment": sentiment,
            "score": score,
            "emoji": emoji,
            "positive_matches": list(set(positive_found)),
            "negative_matches": list(set(negative_found))
        }

# Global instance
analyzer = SentimentAnalyzer()
