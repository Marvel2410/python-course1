
class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output
    
    def __sub__(self, other):
        #height to inches
        self_total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches

        result_inches = self_total_inches - other_total_inches

        result_feet = result_inches // 12
        result_inches %= 12

        return Height(result_feet, result_inches)
    
height1 = Height(5, 10)
height2 = Height(3, 9)

result = height1 - height2

print("Result:", result)