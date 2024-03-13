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
    


    def __gt__(self, other):
      height_inches_A = self.feet * 12 + self.inches
      height_inches_B = other.feet * 12 + other.inches
      return height_inches_A > height_inches_B

    def __ge__(self, other):
      height_inches_A = self.feet * 12 + self.inches
      height_inches_B = other.feet * 12 + other.inches
      return height_inches_A >= height_inches_B

    def __ne__(self, other):
      height_inches_A = self.feet * 12 + self.inches
      height_inches_B = other.feet * 12 + other.inches
      return height_inches_A != height_inches_B

print(Height(4, 6) > Height(4, 5))    # True
print(Height(4, 5) >= Height(4, 5))   # True
print(Height(5, 9) != Height(5, 10))  # True

#extra tests
print(Height(4, 6) < Height(4, 5))    # False


