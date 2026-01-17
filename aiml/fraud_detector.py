import random

class FraudDetector:
    def __init__(self):
        # Educational Thresholds (Simplified Anomaly Detection)
        self.limit_velocity = 5        # Max transactions per hour before alert
        self.limit_amount = 50000     # Single transaction limit before alert
        self.suspicious_locations = ["Russia", "North Korea", "Offshore Island", "Unknown Proxy"]

    def analyze(self, amount, location, hour_freq, user_balance):
        """
        Anomaly Detection Logic:
        We calculate a 'Risk Score' based on several features.
        """
        risk_score = 0
        reasons = []

        # 1. Amount Check
        if amount > self.limit_amount:
            risk_score += 40
            reasons.append(f"High Amount: ${amount} exceeds normal patterns.")
        elif amount > user_balance:
            risk_score += 20
            reasons.append("Insufficient funds but attempted high value.")

        # 2. Location Check (Geospatial Anomaly)
        if location in self.suspicious_locations:
            risk_score += 50
            reasons.append(f"Geographic Anomaly: Transaction from {location}.")

        # 3. Velocity Check (Temporal Anomaly)
        if hour_freq > self.limit_velocity:
            risk_score += 30
            reasons.append(f"Velocity Alert: {hour_freq} transactions within 1 hour.")

        # Final Decision
        is_fraud = risk_score >= 60
        status = "⚠️ SUSPICIOUS" if (30 <= risk_score < 60) else ("🚨 FRAUD DETECTED" if is_fraud else "✅ VERIFIED")

        return {
            "risk_score": risk_score,
            "is_fraud": is_fraud,
            "status": status,
            "reasons": reasons if reasons else ["No anomalies detected."],
            "security_clearance": "DENIED" if is_fraud else ("MANUAL REVIEW" if risk_score >= 30 else "GRANTED"),
            "advice": "Contact cardholder immediately." if is_fraud else "Normal activity."
        }

detector = FraudDetector()
