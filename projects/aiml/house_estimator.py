class HousePriceEstimator:
    def __init__(self):
        # Educational Weights (Simulated Multi-variable Regression coefficients)
        self.base_price = 1500000  # Base price for any house (e.g., in PKR/INR)
        self.w_area = 4500         # Price per Square Feet
        self.w_bed = 400000        # Price per Bedroom
        self.w_location = 600000   # Multiplier per Location Rating (1-10)
        self.w_age = -25000        # Depreciation per year of age

    def estimate(self, area, bedrooms, location_rating, age):
        """
        Formula: Price = Base + (Area * w1) + (Beds * w2) + (Location * w3) + (Age * w4)
        """
        price = (self.base_price + 
                 (area * self.w_area) + 
                 (bedrooms * self.w_bed) + 
                 (location_rating * self.w_location) + 
                 (age * self.w_age))
        
        # Breakdown for educational visualizer
        breakdown = {
            "base": self.base_price,
            "area_contribution": area * self.w_area,
            "bedroom_contribution": bedrooms * self.w_bed,
            "location_contribution": location_rating * self.w_location,
            "age_depreciation": age * self.w_age
        }
        
        return {
            "estimated_price": max(1000000, round(price, 2)), # Minimum 1M
            "breakdown": breakdown,
            "formatted_price": f"{round(price/1000000, 2)} Million",
            "equation": "Price = Base + (Area * 4.5k) + (Beds * 400k) + (Loc * 600k) - (Age * 25k)"
        }

estimator = HousePriceEstimator()
