"""
Design Parking System

1st Submission:
Runtime: 140 ms, faster than 59.96% of Python3 online submissions for Design Parking System.
Memory Usage: 14.8 MB, less than 23.32% of Python3 online submissions for Design Parking System.
"""
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
            car_type = carType
            
            if car_type == 1 and self.big > 0:
                self.big -= 1
                return True
            elif car_type == 2 and self.medium > 0:
                self.medium -= 1
                return True
            elif car_type == 3 and self.small > 0:
                self.small -= 1
                return True
            else:
                return False