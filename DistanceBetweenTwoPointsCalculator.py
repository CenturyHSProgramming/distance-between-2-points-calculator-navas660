# DistanceBetweenPointsCalculator.py
# Your job is to write a function in DistanceBetweenPointsCalculator.py (call
# it **calculateDistanceBetween()** that calculates the distance between two points
# in 2D space (x1, y1) and (x2, y2)
# based on The Distance Formula
# mathwarehouse.com (http://www.mathwarehouse.com/algebra/distance_formula/index.php)

import math

# Define Function below
# be sure to return an integer
def calculateDistanceBetween(x1, y1, x2, y2):

    distance =(x2-x1)**2 + (y2-y1)**2
    distance = math.sqrt(distance)
    distance = round(distance, 2)
    return distance

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answer = calculateDistanceBetween(6, 8, 0, 0)
    print(answer)
    
