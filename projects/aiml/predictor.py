class GradePredictor:
    def __init__(self):
        # We'll use a simple Linear Regression concept: y = mx + c
        # For simplicity in this student project, we calculate the trend 
        # based on the input tests to project the final score.
        pass

    def predict(self, scores):
        """
        scores: list of 3 integers (Test 1, Test 2, Test 3)
        Returns: predicted final score and trend data
        """
        # Linear Regression Math (Simple version for students):
        # x = [1, 2, 3] (Test numbers)
        # y = scores 
        
        n = len(scores)
        x = [1, 2, 3]
        y = scores
        
        # Calculate means
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        
        # Calculate Slope (m) = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean)^2)
        numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean)**2 for i in range(n))
        
        if denominator == 0:
            m = 0
        else:
            m = numerator / denominator
            
        # Calculate Intercept (c) = y_mean - m * x_mean
        c = y_mean - m * x_mean
        
        # Predict Final Exam (x = 4)
        prediction = m * 4 + c
        
        # Clamp prediction between 0 and 100
        prediction = max(0, min(100, prediction))
        
        # Generate trend points for graph
        trend_line = [m * i + c for i in [1, 2, 3, 4]]
        
        return {
            "prediction": round(prediction, 2),
            "slope": round(m, 2),
            "intercept": round(c, 2),
            "trend_line": [round(val, 2) for val in trend_line],
            "status": "Improving" if m > 0 else ("Declining" if m < 0 else "Stable")
        }

# Global instance
predictor = GradePredictor()
